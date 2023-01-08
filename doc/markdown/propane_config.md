# Propane Configuration

Welcome to the documentation for the propane_config.ini file.

The propane_config.ini file is extremely easy to use and hopefully this documentation will make that apparent.


TARGETS are servers/computers/boxes/machines/PCs/whateveryouwannacallthem that are being scored by the Propane platform.

Simply put, the propane_config.ini file is a configuration file for the Propane KoTH game. It is a dynamically editable file and is used to specify template setup paths, TARGETS, and scoring intervals.

The configuration file is broken down as such:

## [General]
Upon first cloning the Propane project your configuration file under [General] will look like this:
```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
enablePropAcc = false# Propane

<p align="center">
<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/propane-logo.png" width=450px height=350px/>
</p>


## VERSION 1.1

An Open Source KoTH Platform based on [NetKotH](https://github.com/NetKotH/netkoth-python)

## Live Scoreboard:
[https://propane.injecti0n.org/](https://propane.injecti0n.org/)

## Documentation:
[Propane Documentation](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/)



## How to use Propane:
[Propane Setup Guide](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_setup.md)

## Current Features:
1. Propane Accessories! (Plugins)
2. White/Black Lists
3. Timed Events
4. Templates
1. Improved Server Status Checks/Scoreboard Server Status
2. Target IP Scoreboard Toggle
3. Scoreboard backups

## TODO:
1. Improve logging functionality to help be more "service" friendly
2. Contribute a bare bones officially supported docker image to make setup a breeze
3. ?Potential frontend and templating rewrite maybe?

Special thanks to [clamsec](https://github.com/ClamSec) and [myntal](https://github.com/Myntal) for their contributions!

## Screenshots:

### Scoreboard

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/scoreboard_screenshot.png">

### Rules

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/rules_screenshot.png">

showTargetIP = true
enableCustomPorts = false
enableBackUp = false
starttime = # Propane

<p align="center">
<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/propane-logo.png" width=450px height=350px/>
</p>


## VERSION 1.1

An Open Source KoTH Platform based on [NetKotH](https://github.com/NetKotH/netkoth-python)

## Live Scoreboard:
[https://propane.injecti0n.org/](https://propane.injecti0n.org/)

## Documentation:
[Propane Documentation](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/)



## How to use Propane:
[Propane Setup Guide](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_setup.md)

## Current Features:
1. Propane Accessories! (Plugins)
2. White/Black Lists
3. Timed Events
4. Templates
1. Improved Server Status Checks/Scoreboard Server Status
2. Target IP Scoreboard Toggle
3. Scoreboard backups

## TODO:
1. Improve logging functionality to help be more "service" friendly
2. Contribute a bare bones officially supported docker image to make setup a breeze
3. ?Potential frontend and templating rewrite maybe?

Special thanks to [clamsec](https://github.com/ClamSec) and [myntal](https://github.com/Myntal) for their contributions!

## Screenshots:

### Scoreboard

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/scoreboard_screenshot.png">

### Rules

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/rules_screenshot.png">

Below is a description of each of these settings:

**outfile** is the directory and file name of the scoreboard. It should be an HTML file, but can be named anything you want.
It is reccommend you write this to your root web server directory as the index.html so that users can view the scoreboard more easily, but feel free to do whatever makes you happy.

**outdir** is the directory where the rest of the template files will be copied to. The default template included in Propane is a bootstrap template and has lots of files to be copied over during the setup phase of the script. This directory is usually the same directory specified in **outfile** but if you change the template it'll be whatever the **outfile** you specified is pointing to.

**sleeptime** the interval at which the scoreboard scores TARGETS in SECONDS. Default is 60 but feel free to set this to whatever value you want.


**whiteListOn** is a boolean value that enables or disables the "White List" feature that only allows specified users in the list to earn points when a box is scored. The actual list for this feature is set as a comma delimited list under the [WhiteList] section of the configuration file.

**balckListOn** is a boolean value that enables or disables the "Black List" feature that bans specified users in the list from earning points when a box is scored. The actual list for this feature is set as a comma delimited list under the [BlackList] section of the configuration file.

**enablePropAcc** is a boolean that tells Propane whether or not to execute PropAccs that are in the PropAcc directory.

**showTargetIP** is a boolean that simply toggles the visibility of the Target IPs on the scoreboard.

**enableBackUp** is a boolean that toggles the scoreboard back up feature. If you enable this feature Propane will create time stamped back up of the scores file on every scoring interval.

**starttime** is a 24 hour formatted time at which a game of Propane will begin. If this is set, when Propane is executed it will not begin scoring until the specified time is reached.

**endtime** is a 24 hour formatted time at which a game of Propane will end. If this is set, the Propane scoreboard will display a countdown timer and the game will cease all scoring and end itself once this end time is reached.


## [Targets]
Upon first cloning the Propane project your configuration file under [Targets] will look like this:
```
[Targets]
linux = 192.168.2.51
windoos =  192.168.2.52
ms3 =  192.168.2.54
webserver =  192.168.2.60
```

These are placeholder values and should be replaced with whatever TARGETS you have set up. By default Propane searches for an index.html|php|aspx|etc... that is loaded at the base IP on Port 80. Once this page is found it searches for the *team* tag and scores the box for the appropriate user that placed this tag.

**[TARGET NAME]** = **[TARGET IP]**

Example:

**metasploitable** =  **192.168.2.65**

If you wish to score a web server on a different port you can toggle the *enableCustomPorts* option to true, and set a custom port per target in the [PortConfig] section. **Note** the target name in PortConfig must match the name of the desired target you are setting a custom port for. For the above example, if we want to check for a team tag for a webserver on port 3000 instead of 80, we would set *enableCustomPorts* to true, and then edit the [PortConfig] section.

**[TARGET NAME]** = **[TARGET PORT]**

Example:

**metasploitable** =  **3000**




## Adding TARGETS/Changing Settings Dynamically

Previously it was stated that the propane_config.ini can be edited dynamically while the game is running. This means you can add servers or change the location of the scoreboard output "on the fly". So if you see things going to smoothly and wish to trip up competitors by adding a new machine, go for it!

Simply edit the file like you would normally and change the values you desire to change.

This includes adding new TARGETs. To add a new TARGET simply follow the previous instructions for adding a TARGET, and you can add them as the game is running.

After you make changes, on the next interval specified by the timer your settings should update. You can even change the timer interval if you want to speed up scoring!
