# Propane Setup

This is the guide on how to set up and run the Propane platform to host your very own King of the Hill (KoTH) style CTF events!

Propane is the "modern" and more up to date version of [NetKoTH](https://github.com/NetKotH/netkoth-python).

If you are familiar with NetKoTH already, then you will feel right at home with Propane.

If not, that's what this documentation is for so don't sweat it!

We reccommend using Apache to host the scoreboard on whatever machine you are using as the scoring server. This is just to keep things simple, however you can use whatever you want, and just replace Apache with your desired web server technology. The only real rule to follow is pointing Propane's outfile and outdir configurations to be able to write to the correct directory.


## Simple Install:

1. Install apache (comes default on a lot of linux distros and is default on macOS)
    - If it is not installed try `sudo apt-get install apache2` on Debian based linux distros
    - On macOS we reccommend [MAMP](https://www.mamp.info/en/) as a good alternative if you don't like the default set up.
2. Start your apache web server!
    - On Debian command is `sudo service apache2 start`
3. Clone/Download Propane
4. Run the follwing commands on the setup.sh in the main project directory:

`chmod +x setup.sh`
`./setup.sh`

During the setup you will be prompted to type the **PARENT** directory of the direcroy where your index file is located. If you want to do a more custome set up and know what you are doing then type whatever you want here, but depending on how apache is configured you will either want to type `/var/www/` or `/var/` here by default.

If your apache server is configured to point at a directory called `html` then you will want to install Propane to `/var/www`. If it is configured to `www` then you may want to install it to `/var/`. The same logic can be applied to wherever you server is pointing too.

EX: If your index.html is stored in `/foo/bar/wham`. Then you'll want to install Propane to `/foo/bar`.

After typing in your desired install directory, Propane will automatically install itself for you. From there you will need to follow steps 5, 6, and 7 from the manual installation guide to finish your set up.


## Manual Install

1. Install apache (comes default on a lot of linux distros and is default on macOS)
    - If it is not installed try `sudo apt-get install apache2` on Debian based linux distros
    - On macOS we reccommend [MAMP](https://www.mamp.info/en/) as a good alternative if you don't like the default set up.
2. Start your apache web server!
    - On Debian command is `sudo service apache2 start`
3. Clone/Download Propane
4. Move the files from the `Propane/` directory one level above the index page of your apache web server.
    -  `mv /Propane/Propane/* /var/` OR `mv /Propane/Propane/* /var/www/`
5. Change the [propane_config.ini](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) file to contain the proper output file. This should be wherever the index.html is stored on your apache web server.
    - Config should look as follows:

    ```
    [General]
    outfile = www/index.html
    outdir = www/
    sleeptime = 60

    [Targets]
    linux = http://192.168.1.13/index.html
    windoos = http://192.168.1.13/test.html

    ```

    **OR**


    ```
    [General]
    outfile = www/html/index.html
    outdir = www/html/
    sleeptime = 60

    [Targets]
    linux = http://192.168.1.13/index.html
    windoos = http://192.168.1.13/test.html
    ```
6. Add in the proper **TARGETS** to the config file. See [Propane Config](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) docs for more info.
7. Add in the **`<TARGET>` tags** to the `template.html` in your `templates/` directory. See [Propane Templates](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_templates.md) for how to edit templates.
7. Start Propane!
    - `chmod +x propane.py`
    - `./propane.py`

    **OR**

    - `python3 propane.py`

Now you should be playing a mean game of KoTH using Propane as your scoreboard!

The scoreboard should be accessible via the IP of the machine running Propane.
