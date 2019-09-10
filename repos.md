# Repos of bpo

This document attempts to capture the repos associated with bugs.python.org.
It is ordered in a rough progression from vanilla upstream to customized bpo.

## Roundup - Upstream Code Base

This is the base Roundup project.

Official Sourceforge: <https://sourceforge.net/p/roundup/code/ci/default/tree/>

- Current release on PyPI: 1.6.0
- Head of master (2.0dev) includes REST, Python 3 support

Mirror on GitHub: <https://github.com/roundup-tracker/roundup>

Mirror is kept up-to-date.

## Roundup Python - modifications and extensions

Bitbucket Project has several repos containing roundup-python-fork, rietveld, and instances
Project Organization: <https://bitbucket.org/account/user/python/projects/BPO>

### Roundup - Python fork

Official Python Roundup fork with modifications
- Repo: <https://bitbucket.org/account/user/python/projects/BPO/roundup>

This fork of upstream roundup includes the base Roundup project with additional
extensions for GitHub integration to PRs, etc.
- Roundup upstream bugs-python-org branch <https://hg.python.org/tracker/roundup/shortlog/bugs.python.org>

The diff between the Python fork and Upstream is now relatively small.

### Rietveld - review tool

<https://bitbucket.org/account/user/python/projects/BPO/rietveld>

## bpo instance - used for deployment

<https://bitbucket.org/account/user/python/projects/BPO/tracker/cpython>

### Additional instances hosted for others

- Jython <https://bitbucket.org/account/user/python/projects/BPO/tracker/jython>
- hosting of roundup's website and tracker <https://bitbucket.org/account/user/python/projects/BPO/tracker/roundup>


---

## Development Bootstrap with Docker

Docker image docker-bpo: <https://github.com/python/docker-bpo>