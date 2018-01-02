# loaddata-bug

This is a quick django project created to reproduce a bug with loaddata when loading database-specific fixtures
with natural keys

# Steps to reproduce

1. Clone the repo and `cd` into to top-level directory:

    ```
    git clone git@github.com:christensenst/loaddata-example.git
    cd loaddata_example
    ```
2. Build the docker container

    `docker build -t loaddata-example .`

3. Run the tests

    `docker run -it --rm loaddata-example python loaddata_bug/manage.py test`

This should produce the error:

```
ERROR: setUpClass (app.loaddata_bug.app_two.tests.TestAppTwo)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/django/test/testcases.py", line 997, in setUpClass
    call_command('loaddata', *cls.fixtures, **{'verbosity': 0, 'database': db_name})
  File "/usr/local/lib/python3.6/site-packages/django/core/management/__init__.py", line 141, in call_command
    return command.execute(*args, **defaults)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/base.py", line 335, in execute
    output = self.handle(*args, **options)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/commands/loaddata.py", line 72, in handle
    self.loaddata(fixture_labels)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/commands/loaddata.py", line 113, in loaddata
    self.load_label(fixture_label)
  File "/usr/local/lib/python3.6/site-packages/django/core/management/commands/loaddata.py", line 150, in load_label
    for fixture_file, fixture_dir, fixture_name in self.find_fixtures(fixture_label):
  File "/usr/local/lib/python3.6/site-packages/django/core/management/commands/loaddata.py", line 264, in find_fixtures
    raise CommandError("No fixture named '%s' found." % fixture_name)
django.core.management.base.CommandError: No fixture named 'app_two_data' found.

----------------------------------------------------------------------
Ran 0 tests in 0.011s

FAILED (errors=1)
```

Here, `app_two_data` is failing to be found because `loaddata` doesn't have support to determine that the fixture is
intended for a different database and should just move along instead of throwing an error

# Background

The support for database-specific fixtures appears to have been removed with
https://github.com/django/django/commit/d5b90c8e120687863c1d41cf92a4cdb11413ad7f in django 1.10 which switched
the 'fixture not found warning' to an exception.  There didn't appear to be any explicit support for ignoring
database-specific fixtures other than piggybacking off this warning; there also was no test in place to catch this
regression