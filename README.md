# loaddata-bug

This is a quick django project created to reproduce a bug with loaddata when loading database-specific fixtures
with natural keys

# Steps to reproduce

1. clone the repo and cd into to top-level directory:

    ```
    git clone git@github.com:christensenst/loaddata-example.git
    cd loaddata_example
    ```
2. Build the docker container

    `docker build -t loaddata-example .`

3. Run the tests

    `docker run -it --rm loaddata-example python loaddata_bug/manage.py test`

# Background

The support for database-specific fixtures appears to have been removed with
https://github.com/django/django/commit/d5b90c8e120687863c1d41cf92a4cdb11413ad7f in django 1.10 which switched
the 'fixture not found warning' to an exception.  There didn't appear to be any explicit support for ignoring
database-specific fixtures other than piggybacking off this warning; there also was no test in place to catch this
regression