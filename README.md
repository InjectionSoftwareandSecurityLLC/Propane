# Propane

<p align="center">
<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/propane-logo.png" width=450px height=350px/>
</p>


## VERSION 1.2

An Open Source KoTH Platform based on [NetKotH](https://github.com/NetKotH/netkoth-python)

## Live Scoreboard:
[https://propane.injecti0n.org/](https://propane.injecti0n.org/)

## Documentation:
[Propane Documentation](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/)



## How to use Propane:
[Propane Setup Guide](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_setup.md)

### Docker:

#### Build from docker repo:
1. `docker run -v $PWD/tmp:/tmp -p <YOURWEBPORT>:80 3ndG4me/propane`

#### Manual build
From the root of the repo run:
1. `docker build -t propane .`
2. `docker run -v $PWD/tmp:/tmp -p <YOURWEBPORT>:80 propane`

To modify the default config, create a new `propane_config.ini` with your desired changes and place it in `$PWD/tmp`, propane will automatically copy it over on next update.


## Current Features:
1. Propane Accessories! (Plugins)
2. White/Black Lists
3. Timed Events
4. Templates
1. Improved Server Status Checks/Scoreboard Server Status
2. Target IP Scoreboard Toggle
3. Scoreboard backups
4. New docker container!

## TODO:
1. Improve logging functionality to help be more "service" friendly
3. ?Potential frontend and templating rewrite maybe?

Special thanks to [clamsec](https://github.com/ClamSec) and [myntal](https://github.com/Myntal) for their contributions!

## Screenshots:

### Scoreboard

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/scoreboard_screenshot.png">

### Rules

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/rules_screenshot.png">
