# README

This is the public repository for my personal [website](http://www.ryanrock.co). I hope you enjoy this work and that it helps you set up your own site. Cheers!

## Blog Workflow

If you're interested in writing a blog post to be hosted on my site, you need to:

- [Fork](https://github.com/ralexanderrock/ryanrock.co//fork) the repository
- Write a blog post using Markdown in the `content` directory
- Push the changes to a topic branch, like `an-example-article`, on *your* fork of the repository
- Make a [pull request](https://help.github.com/articles/using-pull-requests/) against the `source` branch

## Build Locally

If you decide to contribute to the blog or just want to make a modified copy for yourself you will need to install Pelican and clone the repository. The easiest way to do this is in a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). More detailed instructions follow.

### Create a Virtual Environment

First you should install `virtualenv`. Once you have it installed, create a virtual environment to hold Pelican and its dependencies:

    $ virtualenv ~/virtualenvs/pelican
    $ cd ~/virtualenvs/pelican
    $ source /bin/activate

This creates a virtual environment and then activates it. If you want to exit the virtual environment, type:

    $ deactivate

### Fork / Clone the Repo

If you haven't already, clone your version of the repo:

    $ git clone --recurse-submodules https://github.com/ralexanderrock/ryanrock.co/fork

### Install Pelican & Dependancies

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

    $ pip install pelican

### Generate the Website

Now that the dependencies exists, assuming you've installed Fabric, we can build:

    $ fab build

This will take the Markdown files from the `content/` directory and generates static HTML pages inside the `output/` directory. That's it. No database required.

If you do not have Fabric, you can install it using:

    $ pip install Fabric

### Preview the Website

You can serve the generated site so it can be previewed in your browser:

    $ fab serve

And you should see the blog if you visit [http://localhost:8000](http://localhost:8000).

## License
The source code for generation of the blog is under MIT License. Content is copyrighted under (Creative Commons Attribution-ShareAlike 4.0 International License)[http://creativecommons.org/licenses/by-sa/4.0/].

## Contact

If you have any questions, you can [email](mailto:r@ryanrock.co) me.
