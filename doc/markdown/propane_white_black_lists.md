# Propane White/Black Lists

The Propane White and Black Lists are exactly what they sound like. These list allow you to block or explicitly allow specific team tags.

*The Black List is currently a WIP, when it is finished both the White and Black Lists will be usable at the same time if desired*

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

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

[WhiteList]
users = nate,myntal,clamsec
```


### After

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = true

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

[WhiteList]
users = nate,myntal,clamsec
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

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

[WhiteList]
users = 
```

### After

```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

[WhiteList]
users = nate,myntal,clamsec,3ndG4me
```