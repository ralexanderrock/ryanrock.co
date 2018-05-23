Title: Flex Theme: Using a Custom Instagram Social
Date: 2018-5-18
Slug: flex-instagram-social
Tags: pelican, flex, instagram, social, css
Category: website

Some of you who use the Flex theme for Pelican may have noticed that the instagram social icon does not render nicely because it is not supported in the style.min.css file provided in the distribution. As a workaround (too lazy to fork and update the stylesheet properly) I found a nice version of the logo on codepen and modified it for insertion into custom.css file.

If you decide that you want a similar instagram social, just insert the following in custom.css:

```
ul.social a.sc-instagram {
  background:
    radial-gradient(circle farthest-corner at 35% 90%, #fec564, transparent 50%),
    radial-gradient(circle farthest-corner at 0 140%, #fec564, transparent 50%),
    radial-gradient(ellipse farthest-corner at 0 -25%, #5258cf, transparent 50%),
    radial-gradient(ellipse farthest-corner at 20% -50%, #5258cf, transparent 50%),
    radial-gradient(ellipse farthest-corner at 100% 0, #893dc2, transparent 50%),
    radial-gradient(ellipse farthest-corner at 60% -20%, #893dc2, transparent 50%),
    radial-gradient(ellipse farthest-corner at 100% 100%, #d9317a, transparent),
    linear-gradient(#6559ca, #bc318f 30%, #e33f5f 50%, #f77638 70%, #fec66d 100%);
}

```

I hope this finds you well. Happy hunting!