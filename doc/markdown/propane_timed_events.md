# Propane Timed Events

Sometimes we want to schedule competitions to start and end at a certain time. Propane makes that simple with Timed Events. In the `propane_config.ini` file simply specify a 24 hour time format start and/or end time and Propane will take care of the rest! *(Ex: 9:20, 19:20, 21:45, etc...)*

Timed events only need either a start OR an end time, they do not NEED both to work but you can of course schedule a game to start and end at a specific time. However, perhaps you wish to start at a specific time and never end. Or maybe you wish to start immediately and end at a specifc time. Both of those options are available as well.

Example

### Before

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
enableBackUp = false
starttime = 
endtime =

[Targets]
linux = 192.168.2.51
windoos =  192.168.2.52
ms3 =  192.168.2.50
webserver =  192.168.2.60

[PortConfig]
linux = 1337

[WhiteList]
users = nate,myntal,clamsec

[BlackList]
users = 3ndG4me

```

### After (Start/End)

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
enableBackUp = false
starttime = 7:00
endtime = 19:00

[Targets]
linux = 192.168.2.51
windoos =  192.168.2.52
ms3 =  192.168.2.50
webserver =  192.168.2.60

[PortConfig]
linux = 1337

[WhiteList]
users = nate,myntal,clamsec

[BlackList]
users = 3ndG4me

```


### After (Start)

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
enableBackUp = false
starttime = 15:45
endtime =

[Targets]
linux = 192.168.2.51
windoos =  192.168.2.52
ms3 =  192.168.2.50
webserver =  192.168.2.60

[PortConfig]
linux = 1337

[WhiteList]
users = nate,myntal,clamsec

[BlackList]
users = 3ndG4me

```

### After (End)

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
enableBackUp = false
starttime = 
endtime = 21:30

[Targets]
linux = 192.168.2.51
windoos =  192.168.2.52
ms3 =  192.168.2.50
webserver =  192.168.2.60

[PortConfig]
linux = 1337

[WhiteList]
users = nate,myntal,clamsec

[BlackList]
users = 3ndG4me

```

If you specify an `endtime` a countdown will appear on the main scoreboard informing players how much time is left in the compeition. There is a slight delay when between time updates depending on the scoreboard refresh interval you set, but regardless the game will end at exactly the time you specified.


The countdown timer will display as follows:

### Normal Timer

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/doc/normal_countdown.png"/>

### Thirty Minutes Left

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/doc/orange_countdown.png"/>

### Final Countdown! (Ten Minutes Left)

<img src="https://raw.githubusercontent.com/InjectionSoftwareDevelopment/Propane/master/doc/final_countdown.png"/>


The countdown clock will turn orange when there is 30 minutes or less left, but once the clock reaches 10 minutes or less it will turn red and display "FINAL COUNTDOWN" as the pre-pending text like you see above.


## Minor Notes

Initially Propane will not be capable scheduling events spanning multiple days. If this is a desired feature by the community it will be added in the future!

The countdown timer is currently not easily customizeable without changing the main source code. However there are a few customizations you can make! First off to make the countdown timer appear in your theme add the following code wherever you want the countdown to appear in your DOM:

```html
<h3 id="countdown"></h3>
<script src="countdown.js"></script>
```

Now the countdown will appear in your template whenever an `endtime` is set (this is already in the default template). From here you can edit the CSS anyway you'd like, but changing verbiage or format is not really an option at this time without changing the main source.
