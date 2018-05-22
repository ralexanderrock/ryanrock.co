Title: Font Awesome: Social Icons Don't Load
Date: 2018-5-20
Slug: font-awesome-icons-not-loading
Tags: font awesome, cross origin resources, htaccess
Category: website

Some of you may have experienced a bug on my page, which quite literally has been buggin' me for the last few days. My social icons wouldn't load when initially visiting the website, but would load properly after going to another page or waiting a long time and then refreshing. The last couple days I've been ruling out possible causes - leading to many possible fixes none of which worked. I'm happy to say I finally narrowed it down, but finding a solution online proved challenging so I'm providing the fix here. Turns out it was a cross origin resource issue. It's fixed by adding some lines to the .htaccess file on the server.

If you're having the same issue on your site, just add:

	#!apacheconf
	<FilesMatch "\.(ttf|otf|eot|woff)$">
	  <IfModule mod_headers.c>
	    Header set Access-Control-Allow-Origin "*"
	  </IfModule>
	</FilesMatch>

Depending on how you're hosting you may need to run "sudo a2enmod headers" and then restart the server. Happy Hunting!

