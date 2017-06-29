# Propane Configuration

Welcome to the documentation for the propane_config.ini file.

The propane_config.ini file is extremely easy to use and hopefully this documentation will make that apparent.


TARGETS are servers/computers/boxes/machines/PCs/whateveryouwannacallthem that are being scored by the Propane platform.

Simply put, the propane_config.ini file is a configuration file for the Propane KoTH game. It is a dynamically editable file and is used to specify template setup paths, TARGETS, and scoring intervals.

The configuration file is broken down as such:

## [General]
Upon first cloning the Propane project your configuration file under [General] will look like this:
```
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
```

Below is a description of each of these settings:

**outfile** is the directory and file name of the scoreboard. It should be an HTML file, but can be named anything you want.
It is reccommend you write this to your root web server directory as the index.html so that users can view the scoreboard more easily, but feel free to do whatever makes you happy.

**outdir** is the directory where the rest of the template files will be copied to. The default template included in Propane is a bootstrap template and has lots of files to be copied over during the setup phase of the script. This directory is usually the same directory specified in **outfile** but if you change the template it'll be whatever the **outfile** you specified is pointing to.

**sleeptime** the interval at which the scoreboard scores TARGETS in SECONDS. Default is 60 but feel free to set this to whatever value you want.


## [Targets]
Upon first cloning the Propane project your configuration file under [Targets] will look like this:
```
linux = http://192.168.1.13/index.html
windoos = http://192.168.1.13/test.html
```

These are placeholder values and should be replaced with whatever TARGETS you have set up and the IP/location of the HTML file that is being scored by the scoreboard. We reccommend keeping it simple and pointing to an INDEX file just in case things get rowdy and a web server's settings are cleared or crucial files are deleted during the heat of battle. This will allow competitors to write to whatever the INDEX file is and move on. If you wanna make it challenging and require users to keep up with a specific file however, you can absolutely do that. The syntax for the above format shown is as follows:

**[TARGET NAME]** = **[TARGET IP and path to HTML file]**

Example:

**metasploitable** =  **http://192.168.1.20/index.html**



## Adding TARGETS/Changing Settings Dynamically

Previously it was stated that the propane_config.ini can be edited dynamically while the game is running. This means you can add servers or change the location of the scoreboard output "on the fly". So if you see things going to smoothly and wish to trip up competitors by adding a new machine, go for it!

Simply edit the file like you would normally and change the values you desire to change.

This includes adding new TARGETs. To add a new TARGET simply follow the previous instructions for adding a TARGET, and you can add them as the game is running.

After you make changes, on the next interval specified by the timer your settings should update. You can even change the timer interval if you want to speed up scoring!
