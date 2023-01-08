# Propane Templates

This section of the documentation will go over Propane Templates. The templating system in Propane, like everything else, is extremely simple. However, there are a few specific standards to be followed that a required to insure things work as expected.


Essentially, the only file that actually matters inside the `templates/` directory is `template.html`.

You can build out your KoTH scoreboard/website however you want, as long as you treat the `templates/` directory as if it is the main web directory of your site (i.e. `/var/www/` or `/var/www/html/`). As you build your site however, you need to include the appropriate <SERVER> tag in you `template.html` file. This is a placeholder tag that defines where the data for each target server in the "Targets" configuration will populate. Propane automatically iterates this and writes to the template for you, but it cannot do so unless you specify the location in the template via the <SERVER> tag.



## Adding TARGETS Dynamically

Adding targets to your template as the KoTH game is running supported by Propane!

The same way you add targets dynamically to the [Propane Configuration](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) is also how you do so for the template you just edit the file.


This can be done as the game is running, but it is important to note that you **SHOULD NOT** edit the `index.html` generated from your `template.html`. You shouldn't need to edit the template to add new targets, but worth noting as editing the `index.html` file instead of the `template.html` file will result in any changes being overwritten as the game runs.

If you wish to dynamically add a new TARGET, add it to the TARGETS section of the `propane_config.ini` file. On the next scoring interval the new TARGET will appear on the scoreboard.
