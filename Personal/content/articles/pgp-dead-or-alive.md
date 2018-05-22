Title: Schrödinger's PGP: Dead or Alive?
Date: 2018-5-18
Slug: pgp-dead-or-alive
Tags: privacy, encryption, vulnerabilities, pgp, efail
Category: privacy

![Schrödinger](https://imgs.xkcd.com/comics/schrodinger.jpg) <br>
Source: XKCD

Most people have wondered for a while now whether PGP is dead or alive. Here's my take on it: PGP has been in a zombie state since at least the 90's. PGP is both dead and alive simulataneously.

On it's face PGP is pretty dead tech. The interface to GnuPG is ancient looking. Key management in every PGP tool I've seen is abominable. Abominable to the degree that no average user could be reasonably expected to manage their keys properly. Add to that the fact that most of the encryption algorithms implemented in it are either obsolete or insecure. The PGP being implemented by third party email services like Google, Yahoo, etc. aren't winning any awards either.

Take for example [this article]('We're calling it: PGP is dead'){:href='http://www.wired.co.uk/article/efail-pgp-vulnerability-outlook-thunderbird-smime' target="_blank"} from Thursday and other articles concerning the eFail vulnerability. It's pretty clear those PGP implementations can't really do the one thing they're designed to - give your emails "pretty good privacy". For completeness sake I'll add the caveat parroted by many others that exploiting eFail entails an attacker already having intercepted your email. For them this means the exploit is unlikely to be encountered in the wild. 

For those who place greater value in heavy-duty foil for it's hatmaking properties, attackers intercepting encrypted emails through third parties is probably part of the threat-model (see [Prism]('Prism - Surveillance Program'){:href="https://en.wikipedia.org/wiki/PRISM_(surveillance_program)" target="_blank"}, [CISA]('Cybersecurity Information Sharing Act'){:href="https://en.wikipedia.org/wiki/Cybersecurity_Information_Sharing_Act" target="_blank"}). In all seriousness it's not that far-fetched to think that sensitive individuals, i.e. your journo/activist types of the world, could probably fall victim to a threat of this nature. The point is that today PGP in all of its forms should be completely dead, but that's not a solution.

Some really respectable work is being done by people like [Moxie Marlinspike]('Moxie'){:href="https://moxie.org/about.html" target="_blank"}, a role model of mine, through projects such as Signal, Wickr, and countless others. But encrypted and/or ephemeral messaging is not a silver bullet. Even these tools aren't immune to vulnerability. Just this week Signal fell victim to a pretty severe vulnerability. Big kudos to the OpenWhisper team for getting it fixed in five hours though.

<iframe  src="https://player.vimeo.com/video/270232223" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
Source: Ars Technica, courtesy of @hackancuba @iammandatory @ortegaalfredo @julianor

People need well-built tools to encrypt their data independant of a third-party. That was the real value in PGP. We need a successor to PGP that and it needs to be modern, easy-to-use, and ubiquitous. It should be common for people to take sensitive messages or files and copy/paste/attach them into their messenger of choice. I think the number of people who need that capability is vastly underestimated. It's our job as developers and hobbyists to help build the tools to make that possible. 

In quantum mechanics particles remain in uncertain states until they are measured. Once you look at one it collapses into one definite state. It's clear that PGP and personal cryptography in general warrant serious examination. Until we take that hard look and build better alternatives, PGP will keep on walking around half-dead - Schrödinger's zombie.

