# Propane Accessories

Do you feel like Propane could do more? Like, yeah it's a cool scoring engine, but it doesn't check for `insert arbitrary service name here`. Well do we have good news for you!

Propane has plugins! They are appropriately named **"Propane Accessories"** and are extremely easy to make. Propane accessories are a completely empty barebones python script, which means that you can add in ANYTHING you want to Propane.

To get started you need to enable Propane Accessories via the `propane_config.ini` file. There is an option named `EnablePropAcc` that is a boolean value. By default this option is switched to *false* but switching it to *true* enables the plugins in the PropAcc (*pronounced: pro pack*) directory.

Example:


### Before
```
[General]
outfile = changeme/index.html
outdir = changeme/
sleeptime = 60
whiteListOn = false
blackListOn = false
EnablePropAcc = false

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

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
blackListOn = false
EnablePropAcc = true

[Targets]
linux = http://192.168.2.24/index.html
windoos = http://192.168.2.24/test.html
ms3 = http://192.168.2.24/homepage.html
webserver = http://192.168.2.24/prop.html

[WhiteList]
users = nate,myntal,clamsec

[BlackList]
users = 3ndG4me
```


Once PropAcc's are turned on, it's time to write your own! By default we include a `helloworld` PropAcc in this directory. This is a great barebones reference on for how to get started, and we will use this now as our example for how to get started building your own PropAcc.

First is directory structure. All plugins need to reside in the PropAcc directory that comes in the default Propane install. Inside of the PropAcc directory, create a new directory with the name of your new Propane Accessory:

```
-- Propane
    -- PropAcc
        --your_super_awesome_plugin_name
```

In this case we are going to call our plugin `helloworld`, so the structure will be as follows:

```
-- Propane
    -- PropAcc
        --helloworld
```

Now for the code. Every PropAcc must contain an `__init__.py` file like so:

```
-- Propane
    -- PropAcc
        --helloworld
            --__init__.py
```
 
 Once you create your `__init__.py` file, you will use this file as your main python script. This is the entry point for your Propane Accessory.

 Propane Accessories only require one special function in your code in order to work. This function is simply a main, but it has a specific name. This entry function is named start(). So open the `__init__.py` script and add the following function:

 ```py

 def start():


 ```

 That's it, now you can start programming your Propane Accessory! In our example we are just simply going to print "Hello World" into the console of the main Propane output. We can do this by simply adding a print statement inside our start() function.

 ```py

 def start():
    print("Hello World")

```

DONE! You can literally write anything you want, and your module will be loaded up and executed as Propane runs. If you want to write to the score file, or maybe update target machines or change configurations dynamically you have access to all of those things. All it takes is some simple directory traversal and looking at the main source for Propane and modifying it to your liking.

More example Propane Accessories will be provided over in our [PropaneAccessories](https://github.com/InjectionSoftwareDevelopment/PropaneAccessories) github repo.