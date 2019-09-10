# Notes from Core Sprint

## Issues Brainstorming and Resources

##  Scripts and Proof of concepts

- [Search UI using JSON]()
- [Search personal issues]()
- [XML RPC to Jupyter script]()
- [XMLRPC docs](http://roundup.sourceforge.net/docs/xmlrpc.html)

## Priorities

1. Update Roundup

   * Update our clone from upstream, solve conflicts
   * [Update the instances](http://roundup.sourceforge.net/docs/upgrading.html#migrating-from-1-5-1-to-1-6-0)
   * Test and push the changes on bpo

2. GitHub Login

   * Create new tokens (ask Ernest)
   * Review/test/merge PR
   * Push the changes on bpo
   * (Contribute it upstream)

3. Rest API

   * Enable and test it after updating Roundup

4. UI update

   * Review Roundup responsive theme, GSoC student work, [wiki discussions](https://wiki.python.org/moin/DesiredTrackerFeatures) (see also [another wiki page](https://wiki.python.org/moin/DesiredTrackerFeatures) and the pages linked at the top)
   * Material design CSS https://material.io/
   * Mobile friendly theme

5. Write REST tools

6. Move bpo from bitbucket/mercurial to github/git

---

## Challenges with Roundup

### Current Deployment is brittle

#### Upstream Roundup

[Sourceforge Repo](https://sourceforge.net/p/roundup/code/ci/default/tree/)

To clone with Mercurial (read-only):
`hg clone http://hg.code.sf.net/p/roundup/code`

An up-to-date [mirror on GitHub](https://github.com/roundup-tracker/roundup) exists


Pros:
- Adding REST API
- Adding Python 3

Cons:
- Maintainers are few
- Complex old PHP UI frontend
- How ready is it for Python 3?

Decision points:
- which base: roundup, GitHub issues, or other (Bugzilla?)
- pay down technical debt now versus future (moving from round up later will likely be an even bigger undertaking)
- CRITICAL: Confidence in solid Python 3 support


#### Customized Python Roundup for bpo

[Bitbucket Project Repos containing roundup*, rietveld, etc](https://bitbucket.org/account/user/python/projects/BPO)

*[Clone of http://roundup.sourceforge.net/ for bugs.python.org](https://bitbucket.org/python/roundup/src/bugs.python.org/)

To clone with Mercurial:
`hg clone https://bitbucket.org/python/roundup`

Pros:
- Familiar workflow for long time contributors
- Better email support than GitHub for personal issue workflows
- Existing proof of concepts that we could add for usability as standalone web pages to the existing bpo navigation
    -  [Search UI using JSON]()
    - [Search personal issues]()
- Addition of GitHub OAuth for user login

Cons:
- Dated workflow and tools discourage new contributors especially from underrepresented groups
- Unfriendly and unproductive UI
- Modernizing UI
    - requires rewrite of html/css/sass with material design
    - ripping out all of the old PHP Template Attribute Language code which results in brittle, barely maintainable UI (CRITICAL)
    - PyPI warehouse css would be an excellent foundation to work from
- Upstream changes to roundup could break any improvements (best option: permanent fork of roundup with goal to rewrite in Python 3 and Django/Pyramid)

Action item:
- Migrating to GitHub and git from mercurial would increase the number of contributors and be more appealing to front end developers in our community. **Do at the sprint this week?**


#### docker-bpo

Bootstrap a development environment using Docker

Repo: https://github.com/python/docker-bpo

