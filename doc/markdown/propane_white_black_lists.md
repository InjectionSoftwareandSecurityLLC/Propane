# Propane White/Black Lists

The Propane White and Black Lists are exactly what they sound like. These list allow you to block or explicitly allow specific team tags.

Both White and Black List features can be used simultaneously if desired (although there is not much point if you simply remove a user from one list or the other).

## White List

Using the White List is extremely simple. In the `propane_config.ini` two new configuration options have been added. One is the `whiteListOn` option, and the other is the `[WhiteList]` section itself which contains a `users` option.

To use the White List simple set the `whiteListOn` option to *true*:

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


### After

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = true
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
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


To add users to the White List simply add a team tag in comma delimited format (see the example below).
The best use for this feature is if you are running a KoTH set up with pre-registered users. If you require
your users to use a team tag they register for your KoTH with then you can add their tag to this White List and Propane will only score the team tags specified by the White List.

While you should probably run your KoTH set up on a closed off, secure network anyway, this system will prevent any rogue users from being able to score points and disrupt the scoreboard. This is just one example use case, but you may find many other uses for this White List.


Example:

### Before (no users)

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = true
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
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
users = 

[BlackList]
users = 

```

### After

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = true
blackListOn = false
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
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
users = 

```


## Black List

Much like the White List using the Black List is extremely simple. In the `propane_config.ini` two new configuration options have been added. One is the `blackListOn` option, and the other is the `[BlackList]` section itself which contains a `users` option.

To use the Black List simple set the `blackListOn` option to *true*:


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


### After

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = true
enablePropAcc = false
showTargetIP = true
enableCustomPorts = false
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

To add users to the Black List simply add a team tag in comma delimited format (see the example below).
The best use for this feature is to ban troublesome users while a competition is running.

This isn't full proof as a user could simply continue playing with a new team tag leading to a game of "whack-a-mole", but doing this combined with a score removal makes for a pretty effective punishment.


Example:

### Before (no users)

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
users =

[BlackList]
users = 

```

### After

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
users =

[BlackList]
users = 3ndG4me, nate, myntal, clamsec

```