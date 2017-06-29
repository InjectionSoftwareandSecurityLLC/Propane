# Propane Templates

This section of the documentation will go over Propane Templates. The templating system in Propane, like everything else, is extremely simple. However, there are a few specific standards to be followed that a required to insure things work as expected.


Essentially, the only file that actually matters inside the `templates/` directory is `template.html`.

You can build out your KoTH scoreboard/website however you want, as long as you treat the `templates/` directory as if it is the main web directory of your site (i.e. `/var/www/` or `/var/www/html/`). As you build your site however, you need to include the appropriate <TARGET> tags in you `template.html` file.


<TARGET> Tags should follow these rules:

1. All Capital Titles
2. Be opened by `<` and closed by ` >`


That's it!


The following are example <TARGET> tags for the example TARGETs from the [Propane Configuration](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) file:

```HTML
<LINUX>
<WINDOOS>
```

So if you create a TARGET in the Propane Configuration file like so:


`SuperCoolVulnBox = http://192.168.1.19/index.html`


Then you will need to add the following <TARGET> tag to your `template.html`:

`<SUPERCOOLVULNBOX>`


That is all you really need in order to customize the template. Below is an example of how to add the new <TARGET> tag to the default Propane template:

### Before

```HTML

<div class="content-section-a">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2>Scores</h1>
        <div class="table-responsive">
      <table class="table">
        <tr>
          <td valign="top" align="center">
            <LINUX>
          </td>
          <td valign="top" align="center">
            <WINDOOS>
          </td>
          <td valign="top" align="center">
            <TOTAL>
          </td>
        </tr>
      </table>
      </div>
    </div>
  </div>
</div>
</div>
```

### After
```HTML
<div class="content-section-a">
  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <h2>Scores</h1>
        <div class="table-responsive">
      <table class="table">
        <tr>
          <td valign="top" align="center">
            <LINUX>
          </td>
          <td valign="top" align="center">
            <WINDOOS>
          </td>
          <td valign="top" align="center">
            <SUPERCOOLVULNBOX>
          </td>
          <td valign="top" align="center">
            <TOTAL>
          </td>
        </tr>
      </table>
      </div>
    </div>
  </div>
</div>
</div>
```


## Adding TARGETS Dynamically

Adding targets to your template as the KoTH game is running supported by Propane!

The same way you add targets dynamically to the [Propane Configuration](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) is also how you do so for the template you just edit the file.

In fact if you add a TARGET to the config file, you HAVE to add it the template in order for it to appear.

For this you will want to follow instructions from the [Propane Configuration](https://github.com/InjectionSoftwareDevelopment/Propane/blob/master/doc/markdown/propane_config.md) about adding a new TARGET dynamically. Once you add your target to the config file, simple add the <TARGET> tag to the `template.html` as shown above.

This can be done as the game is running, but it is important to note that you **SHOULD NOT** edit the `index.html` generated from your `template.html`.

If you wish to dynamically add a new TARGET, add it to the `template.html` in the `templates/` directory. On the next scoring interval the new TARGET will appear on the scoreboard.
