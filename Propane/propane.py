#!/usr/bin/python3

"""
Libraries:

urllib: Used for scanning and reading HTML pages from TARGET Servers
re: Regex library used for searching for data in a particular format. Namely searching HTML pages for <team> tags
configparser Parser library used for parsing scores and configuration data.
time: Time used for delaying score updates at a set interval.
distutils.dir_util (copy_tree): Used to load templates. Automatically creates and copies a
                                directory set in the propane_config file
os: Currently only used for removing uneeded template files generated on initialization.
    Used to make general OS calls as needed.
csv: used for parsing comma delimited lists for the White and Black Lists.
imp: used for importing plugins (Propane Accessories)

"""
import urllib.request
import re
import configparser
import time
from distutils.dir_util import copy_tree
import os
import csv
import imp
from datetime import datetime
from threading import Timer


# Colors for terminal output. Makes things pretty.
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'




'''
Globals:

config: Initialize the parser that will be used to parse the propane_config file.
scores: Initialize the parser that will be used to parse the propane_scores file.
configFile: Initialize global string where the path to the propane_config will be stored.
serversToCheck: Initialize global where the parsed data about the Servers from the propane_config will be stored.
                (Initialized as string, but will be used as a list)
whiteListInit: Initialize the white list global value that will be used to store the users option from the WhiteList section.
blackListInit: Initialize the black list global value that will be used to store the users option from the BlackList section.
sleeptTime: Initialize global that will store the delay interval that is parsed from propane_config.
            (Initialized as string, but will be used as a number)
outfile: Initialize global string that will store the desired location and name of the main scoreboard output file.
         (usually /var/www/html/index.html or /var/www/index.html in Apache)
outdir: Initialize the global string thaht will store the desired output location of the template.
        This is usally the same directory as outfile, but without the outfile name (e.g. /var/www/).
gameSetup: Initialize the global boolean that is used to test if this is the initial start up.
            This is used so that any set up is done only on the first iteration, but currently is
            only needed to load in the initial template.
PropAccDir: Initialize the main directory for plugins (Propane Accessories)
PropAccModule: Initialize the main module name for all plugins (Propane Accessories)
'''
config = configparser.RawConfigParser()
scores = configparser.RawConfigParser()
configFile = ""
serversToCheck = ""
whiteListInit = ""
blackListInit = ""
sleepTime = ""
outfile = ""
outdir = ""
startTime = ""
endTime = ""
gameSetup = True
PropAccDir = "./PropAcc"
PropAccModule = "__init__"

'''
loadConfig():
    Loads and parses the propane_config file.
    Loads the globals "configFile, serversToCheck, whiteListInit, blackListInit, sleepTime, outfile, outdir, whiteListIsOn, blackListIsOn" 
    from the config file to use later on.
'''


def loadConfig():
        print(bcolors.CYAN + bcolors.BOLD + "Loading Configurations" + bcolors.ENDC)
        global configFile, serversToCheck, whiteListInit, blackListInit, sleepTime, outfile, outdir, startTime, endTime, whiteListIsOn, blackListIsOn, enablePropAcc
        configFile = config.read("propane_config.ini")
        serversToCheck = config.items("Targets")
        whiteListInit = config.items("WhiteList")
        blackListInit = config.items("BlackList")
        sleepTime = config.getint("General", "sleepTime")
        outfile = config.get("General", "outfile")
        outdir = config.get("General", "outdir")
        startTime = config.get("General", "starttime")
        endTime = config.get("General", "endtime")
        whiteListIsOn = config.getboolean("General", "whiteListOn")
        blackListIsOn = config.getboolean("General", "blackListOn")
        enablePropAcc = config.getboolean("General", "EnablePropAcc")



'''
loadPropAcc():
    Imports all modules in the PropAcc Directory and returns a list of them to be initialized

'''
def loadPropAcc():
    
    propaccs = []
    possibleplugins = os.listdir(PropAccDir)
    for i in possibleplugins:
        location = os.path.join(PropAccDir, i)
        if not os.path.isdir(location) or not PropAccModule + ".py" in os.listdir(location):
            continue
        info = imp.find_module(PropAccModule, [location])
        propaccs.append({"name": i, "info": info})
    return propaccs


'''
initPropAcc():
    Accepts a Propane Accessory generated by the loadPropAcc function, and returns an initiliazed module
    that is imported and ready to be used.

'''
def initPropAcc(propacc):
    return imp.load_module(PropAccModule, *propacc["info"])


'''
score():
    Loads and parses the propane_scores file.
    Iterates through the servers testing for a connection.
    If a connection is found the team tag is parsed and the appropriate team (first tag found) is awarded a point/added
    to the scoreboard.
    Writes the new score data to the propane_scores file.
    If server is not found, and error message displays in console.
    If no one owns the box scanned, then no points are awarded.
    If black list feature is on, then users in the black list are flagged in the output and no score is awarded.
    If white list is feature is on, then users not in the white list are flagged in the output and no score is awarded.
'''

def score(whiteList, blackList):
        scoresFile = scores.read("propane_scores.txt")
        for server in serversToCheck:
            try:
                print(bcolors.GREEN + bcolors.BOLD + "Checking Server: " + bcolors.RED + server[0] + bcolors.ENDC + " @ " + bcolors.BOLD + server[1] + bcolors.ENDC)
                url = urllib.request.urlopen(server[1],None,10)
                #url = urllib2.urlopen(server[1])
                html = url.read()
                team = re.search('<team>(.*)</team>', str(html), re.IGNORECASE).group(1).strip().replace("=","").replace("<","").replace(">","")
                print(bcolors.BOLD + "Server " + server[0] + bcolors.ENDC + " pwned by " + bcolors.RED + team + bcolors.ENDC)
                serverScoresection = server[0]+"Scores"

                if whiteListIsOn and not blackListIsOn:
                    if team in whiteList:
                        if not scores.has_option("TotalScores", team):
                            scores.set("TotalScores", team, 0)
                        currentScore = scores.getint( "TotalScores",team)
                        scores.set( "TotalScores", team, currentScore+1)
                        if not scores.has_option(serverScoresection, team):
                            scores.set(serverScoresection, team, 0)
                        currentScore = scores.getint( serverScoresection,team)
                        scores.set( serverScoresection, team, currentScore+1)
                    else:
                        print(bcolors.FAIL + bcolors.BOLD + "User: " + team + " not in the white list! Score was not updated." + bcolors.ENDC)
                elif blackListIsOn and not whiteListIsOn:
                    if team in blackList:
                         print(bcolors.FAIL + bcolors.BOLD + "User: " + team + " is in the black list! Score was not updated." + bcolors.ENDC)
                    else:
                        if not scores.has_option("TotalScores", team):
                            scores.set("TotalScores", team, 0)
                        currentScore = scores.getint( "TotalScores",team)
                        scores.set( "TotalScores", team, currentScore+1)
                        if not scores.has_option(serverScoresection, team):
                            scores.set(serverScoresection, team, 0)
                        currentScore = scores.getint( serverScoresection,team)
                        scores.set( serverScoresection, team, currentScore+1)
                elif whiteListIsOn and blackListIsOn:
                    if team in blackList:
                         print(bcolors.FAIL + bcolors.BOLD + "User: " + team + " is in the black list! Score was not updated." + bcolors.ENDC)
                    elif team in whiteList:
                        if not scores.has_option("TotalScores", team):
                            scores.set("TotalScores", team, 0)
                        currentScore = scores.getint( "TotalScores",team)
                        scores.set( "TotalScores", team, currentScore+1)
                        if not scores.has_option(serverScoresection, team):
                            scores.set(serverScoresection, team, 0)
                        currentScore = scores.getint( serverScoresection,team)
                        scores.set( serverScoresection, team, currentScore+1)
                    else:
                         print(bcolors.FAIL + bcolors.BOLD + "User: " + team + " not in the white list! Score was not updated." + bcolors.ENDC)
                else:
                    if not scores.has_option("TotalScores", team):
                        scores.set("TotalScores", team, 0)
                    currentScore = scores.getint( "TotalScores",team)
                    scores.set( "TotalScores", team, currentScore+1)
                    if not scores.has_option(serverScoresection, team):
                        scores.set(serverScoresection, team, 0)
                    currentScore = scores.getint( serverScoresection,team)
                    scores.set( serverScoresection, team, currentScore+1)
            except IOError:
                print(bcolors.FAIL + bcolors.BOLD + server[0] + bcolors.ENDC + " @ " + bcolors.FAIL + bcolors.BOLD + server[1] + bcolors.ENDC + " might be down, skipping it")
            except AttributeError:
                print(bcolors.BOLD + "Server " + bcolors.RED + server[0] + bcolors.ENDC + " might not be " + bcolors.RED + "pwned " + bcolors.ENDC + "yet")
        with open("propane_scores.txt", 'w') as scoresFile:
                scores.write(scoresFile)

'''
initScoreFile():
    Reads the propane_scores file and adds appropriate sections to the score file if they do not exist.
    (Initializes the score file)
'''



def initScoreFile():
        scoresFile = scores.read("propane_scores.txt")
        if not scores.has_section("TotalScores"):
                scores.add_section("TotalScores")

        for server in serversToCheck:
                serverScoresection = server[0]+"Scores"
                if not scores.has_section(serverScoresection):
                        scores.add_section(serverScoresection)


'''
reloadScoreBoard():
    Fetches the score data from the the server list and formats it into an HTML table.
    The table is returned to be used elsewhere.

    If a section is missing an error is displayed in the console.
'''


def reloadScoreBoard(server):
        print(bcolors.BLUE + bcolors.BOLD + "Reloading Scoreboard for: " + bcolors.ENDC + bcolors.BOLD + server[0] + bcolors.ENDC)
        try:

            serverScoresection = server[0]+"Scores"
            serverScores = scores.items(serverScoresection)

            tableResults = "<div class=\"col-md-12\" id=\"" + server[0] + "\">"
            tableResults = tableResults + "<table class=\"table\" border=\"2\">\n<tr>"
            tableResults = tableResults + "<td colspan=\"2\"><center><h3>" +(server[0]).title() + "</h3><br>"
            if((server[0]).title() != "Total"):
                    tableResults = tableResults + "<hr style=\"border-top: 1px solid #000;\"/><h4>Server: <a href=\"" + server[1] + "\">" + server[1]  +"</a></h4>"
            tableResults = tableResults + "</center></td></tr>\n"
            serverScores.sort(key=lambda score: -int(score[1]))
            topTagStart="<div class=\"topscore\">"
            topTagEnd="</div>"
            for team in serverScores:
                tableResults = tableResults + "<tr><td>" + topTagStart + team[0].title() + topTagEnd + "</td><td>" + topTagStart + str(team[1]) +  topTagEnd  + "</td></tr>\n"
                topTagStart="<div class=\"otherscore\">"
                topTagEnd="</div>"
            tableResults = tableResults + "</table></div>"
            return tableResults
        except:
            print(bcolors.FAIL + bcolors.BOLD + "No section for " + server[0] + " (check your template for errors)" + bcolors.ENDC)


def endGame():

    print(bcolors.YELLOW + bcolors.BOLD + "Propane has ended at: " + str(datetime.now()) + bcolors.ENDC)

    os._exit(0)


'''
main():
    Propane main function. Runs the loadConfig(), initScoreFile() functions and then setups up the scoreboard web pages
    by writing them and copying the templates to the directories specified in the propane_config.

    This is an endless loop that constantly scores users, reloads the scoreboard, parses white and black lists, and error corrects itself as needed in
    some cases (e.g. initScoreFile())

    By placing the loadConfig(), initScoreFile(), and score() functions in the loop to run everytime, an administrator can
    live edit the config, and score files as needed.

    Plugins (Propane Accessories) are loaded in a for loop which initializes and runs the main function of every plugin.

    The core functionality of the main is to run the entire scoreboard and connect all the pieces, and write them out to the
    scoreboard file that is specified by the outfile variable.

    The delay interval set by the time value loaded into the time global variable determines how often the scoreboard executes
    its operations.
'''

def main():

        global gameSetup


        while True:

                # Load Conifgurations
                loadConfig()
                # Init Score File
                initScoreFile()
                # Open template file
                templateFile = open("template/template.html", 'r')
                # Read in template file
                scorePage = templateFile.read()
         
                # Load up the white list
                whiteList = ""

                for user in whiteListInit:
                    parseWhiteList = csv.reader([user[1]])
                    for user in parseWhiteList:
                        whiteList = user
                
                blackList = ""

                for user in blackListInit:
                    parseBlackList = csv.reader([user[1]])
                    for user in parseBlackList:
                        blackList = user

               

                # Do one-time set up stuff on start of the game
                if(gameSetup):
                        print(bcolors.CYAN + bcolors.BOLD + "Game Setup: " + bcolors.ENDC + " copying template files")
                        copy_tree("template", outdir)
                        os.remove(outdir + "template.html")

                        if startTime:
                            currentTime = datetime.now()

                            startHour = int(startTime.split(":")[0])
                            startMinute = int(startTime.split(":")[1])
                        
                            formattedStartTime = currentTime.replace(day=currentTime.day, hour=startHour, minute=startMinute, microsecond=currentTime.microsecond)

                            timeDelta = formattedStartTime - currentTime

                            print(bcolors.GREEN + bcolors.BOLD + "Propane will start at: " + str(formattedStartTime) + bcolors.ENDC)
                            time.sleep(timeDelta.seconds)

                        if endTime:
                            currentTime = datetime.now()

                            endHour = int(endTime.split(":")[0])
                            endMinute = int(endTime.split(":")[1])

                            formattedEndTime = currentTime.replace(day=currentTime.day, hour=endHour, minute=endMinute, microsecond=currentTime.microsecond)

                            timeDelta = formattedEndTime - currentTime

                            endTimer = Timer(timeDelta.seconds, endGame)

                            print(bcolors.YELLOW + bcolors.BOLD + "Propane will end at: " + str(formattedEndTime) + bcolors.ENDC)

                            endTimer.start()

                        gameSetup = False
                        
                # Do some scoring!
                score(whiteList, blackList)

                #Load Propane Accessories and run their start() function
                if enablePropAcc:
                    for i in loadPropAcc():
                        print(bcolors.CYAN + bcolors.BOLD + "Loading Propane Accessory: " + bcolors.ENDC + bcolors.BOLD + i["name"] + bcolors.ENDC)
                        propacc = initPropAcc(i)
                        propacc.start()

                # Update Server Scores on Scoreboard
               
                for server in serversToCheck:
                    thisTable = reloadScoreBoard(server)
                    serverLabelTag=("<" + server[0] + ">").upper()
                    print(bcolors.GREEN + bcolors.BOLD + "Updating " + bcolors.ENDC + bcolors.BOLD + serverLabelTag + bcolors.ENDC + " tag in the template")
                    scorePage = scorePage.replace(serverLabelTag,thisTable)
                # Update Total Scores on Scoreboard
                thisTable = reloadScoreBoard(["Total",""])
                serverLabelTag=("<TOTAL>").upper()
                print(bcolors.GREEN + bcolors.BOLD + "Updating " + bcolors.ENDC + bcolors.BOLD + serverLabelTag + bcolors.ENDC + " tag in the template")
                scorePage = scorePage.replace(serverLabelTag,thisTable)
                # Write out the updates made to the Scoreboard and get ready for next interval
                print(bcolors.BLUE + bcolors.BOLD + "Updating Scoreboard " + bcolors.ENDC + bcolors.BOLD + outfile + bcolors.ENDC)
                outFileHandler = open(outfile, 'w')
                outFileHandler.write(scorePage)
                outFileHandler.close()
                print(bcolors.CYAN + bcolors.BOLD + "Next update in: " + bcolors.ENDC + str(sleepTime) + bcolors.BOLD + " second(s)" + bcolors.ENDC)
                time.sleep(sleepTime)


#Execute main()

if __name__ == "__main__":
    main()
