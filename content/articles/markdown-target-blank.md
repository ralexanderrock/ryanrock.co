Title: Markdown: Hyperlinks that open in new tabs
Date: 2018-05-17
Slug: markdown-target-blank
Tags: blog, pelican, markdown, hyperlinks
Category: website

I ran across a minor issue while setting up my blog that I'm sure some of you out there will find helpful. Pelican apparently does not natively support changing the targets of hyperlinks with Markdown. Comments as recent as 2016 said as much. Perhaps that's changed since then, but I've been unable to track down the documentation which says how to do it. Long story short, there are two ways to do it.

The ugly way of course is to write the link in html and allow it to eventually be rendered by the browser. The much neater way is to use the following:

	#!md
	[LINK]('LINK_TITLE'){:href="LINKURL" target="_blank"}

That's it! Neat and simple the way we like it. Hope someone finds this of use. Cheers!