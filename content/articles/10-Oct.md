Title: Blog Setup and Automation
Date: 2021-10-10 12:20
Slug: blog-setup-and-automation
Authors: Ben Poile
Summary: Setting my blog up on a Sunday morning

I started work on my blog today with customizing the theme that I got off Pelican's [Github repository](https://github.com/getpelican/pelican-themes/tree/master/cebong).
Most of what was changed was related to the style of the site, like positioning, font, and color. I fixed the icons that had an invalid file paths and changed black 
icons to white. I then created a [CODEOWNERS](https://github.com/poiley/poiley.github.io/blob/master/.github/CODEOWNERS) file, a 
[README.md](https://github.com/poiley/poiley.github.io/blob/master/README.md), and added an MIT license. The repository on Github was then configured to automatically 
delete branches when a PR has been merged into master. I wanted to utilize Actions a bit more in the PR step, so I added a new workflow to perform a spell check on each 
new post added to the repository.

Later in the day, I added support for dependeabot via Github Actions, so security vulnerabilities in the site's dependencies will be automatically addressed.