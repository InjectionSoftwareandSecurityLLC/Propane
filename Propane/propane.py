#!/usr/local/bin/python

"""
Libraries:

urllib and urllib2: Used for scanning and reading HTML pages from TARGET Servers
re: Regex library used for searching for data in a particular format. Namely searching HTML pages for <team> tags
ConfigParser: Parser library used for parsing scores and configuration data.
time: Time used for delaying score updates at a set interval.
distutils.dir_util (copy_tree): Used to load templates. Automatically creates and copies a
                                directory set in the propane_config file
os: Currently only used for removing uneeded template files generated on initialization.
    Used to make general OS calls as needed.

"""
import urllib2
import urllib
import re
import ConfigParser
import time
from distutils.dir_util import copy_tree
import os


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
sleeptTime: Initialize global that will store the delay interval that is parsed from propane_config.
            (Initialized as string, but will be used as a number)
outfile: Initialize global string that will store the desired location and name of the main scoreboard output file.
         (usually /var/www/html/index.html or /var/www/index.html in Apache)
outdir: Initialize the global string thaht will store the desired output location of the template.
        This is usally the same directory as outfile, but without the outfile name (e.g. /var/www/).
gameSetup: Initialize the global boolean that is used to test if this is the initial start up.
            This is used so that any set up is done only on the first iteration, but currently is
            only needed to load in the initial template.
'''
config = ConfigParser.RawConfigParser()
scores = ConfigParser.RawConfigParser()
configFile =""
serversToCheck = ""
sleepTime = ""
outfile = ""
outdir = ""
gameSetup = True


'''
loadConfig():
    Loads and parses the propane_config file.
    Loads the globals "configFile, serversToCheck, sleepTime, outfile, outdir" from the config file to use later on.
'''


def loadConfig():
        print bcolors.CYAN + bcolors.BOLD + "Loading Configurations" + bcolors.ENDC
        global configFile, serversToCheck, sleepTime, outfile, outdir
        configFile = config.read("propane_config.ini")
        serversToCheck = config.items("Targets")
        sleepTime = config.getint("General", "sleepTime")
        outfile = config.get("General", "outfile")
        outdir = config.get("General", "outdir")

'''
score():
    Loads and parses the propane_scores file.
    Iterates through the servers testing for a connection.
    If a connection is found the team tag is parsed and the appropriate team (first tag found) is awarded a point/added
    to the scoreboard.
    Writes the new score data to the propane_scores file.
    If server is not found, and error message displays in console.
    If no one owns the box scanned, then no points are awarded.
'''

def score():
        scoresfile = scores.read("propane_scores.txt")
        for server in serversToCheck:
            try:
                print bcolors.GREEN + bcolors.BOLD + "Checking Server: " + bcolors.RED + server[0] + bcolors.ENDC + " @ " + bcolors.BOLD + server[1] + bcolors.ENDC
                url = urllib2.urlopen(server[1],None,10)
                #url = urllib2.urlopen(server[1])
                html = url.read()
                team = re.search('<team>(.*)</team>', html, re.IGNORECASE).group(1).strip().replace("=","").replace("<","").replace(">","")
                print bcolors.BOLD + "Server " + server[0] + bcolors.ENDC + " pwned by " + bcolors.RED + team + bcolors.ENDC
                serverscoressection = server[0]+"Scores"
                if not scores.has_option("TotalScores", team):
                    scores.set("TotalScores", team, 0)
                currentscore = scores.getint( "TotalScores",team)
                scores.set( "TotalScores", team, currentscore+1)
                if not scores.has_option(serverscoressection, team):
                    scores.set(serverscoressection, team, 0)
                currentscore = scores.getint( serverscoressection,team)
                scores.set( serverscoressection, team, currentscore+1)
            except IOError:
                print bcolors.FAIL + bcolors.BOLD + server[0] + bcolors.ENDC + " @ " + bcolors.FAIL + bcolors.BOLD + server[1] + bcolors.ENDC + " might be down, skipping it"
            except AttributeError:
                print bcolors.BOLD + "Server " + bcolors.RED + server[0] + bcolors.ENDC + " might not be " + bcolors.RED + "pwned " + bcolors.ENDC + "yet"
        with open("propane_scores.txt", 'wb') as scoresfile:
                scores.write(scoresfile)

'''
initScoreFile():
    Reads the propane_scores file and adds appropriate sections to the score file if they do not exist.
    (Initializes the score file)
'''



def initScoreFile():
        scoresfile = scores.read("propane_scores.txt")
        if not scores.has_section("TotalScores"):
                scores.add_section("TotalScores")

        for server in serversToCheck:
                serverscoressection = server[0]+"Scores"
                if not scores.has_section(serverscoressection):
                        scores.add_section(serverscoressection)


'''
reloadScoreBoard():
    Fetches the score data from the the server list and formats it into an HTML table.
    The table is returned to be used elsewhere.

    If a section is missing an error is displayed in the console.
'''


def reloadScoreBoard(server):
        print bcolors.BLUE + bcolors.BOLD + "Reloading Scoreboard for: " + bcolors.ENDC + bcolors.BOLD + server[0] + bcolors.ENDC
        try:
            serverscoressection = server[0]+"Scores"
            serverscores = scores.items(serverscoressection)
            tableresults = "<div class=\"table-responsive\" id=\"" + server[0] + "\">"
            tableresults = tableresults + "<table class=\"table\" border=\"2\">\n<tr>"
            tableresults = tableresults + "<td colspan=\"2\"><center><h3>" +(server[0]).title() + "</h3><br>"
            if((server[0]).title() != "Total"):
                    tableresults = tableresults + "<hr style=\"border-top: 1px solid #000;\"/><h4>Server: <a href=\"" + server[1] + "\">" + server[1]  +"</a></h4>"
            tableresults = tableresults + "</center></td></tr>\n"
            serverscores.sort(key=lambda score: -int(score[1]))
            toptagstart="<div class=\"topscore\">"
            toptagend="</div>"
            for team in serverscores:
                tableresults = tableresults + "<tr><td>" + toptagstart + team[0].title() + toptagend + "</td><td>" + toptagstart + str(team[1]) +  toptagend  + "</td></tr>\n"
                toptagstart="<div class=\"otherscore\">"
                toptagend="</div>"
            tableresults = tableresults + "</table></div>"
            return tableresults
        except:
            print bcolors.FAIL + bcolors.BOLD + "No section for " + server[0] + " (check your template for errors)" + bcolors.ENDC

'''
main():
    Propane main function. Runs the loadConfig(), initScoreFile() functions and then setups up the scoreboard web pages
    by writing them and copying the templates to the directories specified in the propane_config.

    This is an endless loop that constantly scores users, reloads the scoreboard, and error corrects itself as needed in
    some cases (e.g. initScoreFile())

    By placing the loadConfig(), initScoreFile(), and score() functions in the loop to run everytime, an administrator can
    live edit the config, and score files as needed.

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
                # Do some scoring!
                score()

                # Do one-time set up stuff on start of the game
                if(gameSetup):
                        print bcolors.CYAN + bcolors.BOLD + "Game Setup: " + bcolors.ENDC + " copying template files"
                        copy_tree("template", outdir)
                        os.remove(outdir + "template.html")
                        gameSetup = False

                # Update Server Scores on Scoreboard
                for server in serversToCheck:
                    thistable = reloadScoreBoard(server)
                    serverlabeltag=("<" + server[0] + ">").upper()
                    print bcolors.GREEN + bcolors.BOLD + "Updating " + bcolors.ENDC + bcolors.BOLD + serverlabeltag + bcolors.ENDC + " tag in the template"
                    scorePage = scorePage.replace(serverlabeltag,thistable)
                # Update Total Scores on Scoreboard
                thistable = reloadScoreBoard(["Total",""])
                serverlabeltag=("<TOTAL>").upper()
                print bcolors.GREEN + bcolors.BOLD + "Updating " + bcolors.ENDC + bcolors.BOLD + serverlabeltag + bcolors.ENDC + " tag in the template"
                scorePage = scorePage.replace(serverlabeltag,thistable)
                # Write out the updates made to the Scoreboard and get ready for next interval
                print bcolors.BLUE + bcolors.BOLD + "Updating Scoreboard " + bcolors.ENDC + bcolors.BOLD + outfile + bcolors.ENDC
                outfilehandle = open(outfile, 'w')
                outfilehandle.write(scorePage)
                outfilehandle.close()
                print bcolors.CYAN + bcolors.BOLD + "Next update in: " + bcolors.ENDC + str(sleepTime) + bcolors.BOLD + " second(s)" + bcolors.ENDC
                time.sleep(sleepTime)


#Execute main()

if __name__ == "__main__":
    main()
