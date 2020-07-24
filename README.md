# About

This is a minimal reproducable example for 
[issue 71](https://github.com/nedbat/django_coverage_plugin/issues/71)
 of [django_coverage_plugin](https://github.com/nedbat/django_coverage_plugin).


# How to run

```console
# virtualenv --python=python3 venv
# source venv/bin/activate
# pip install -r requirements.txt
# coverage run ./manage.py test -v2
# coverage report
Name                                                                                                 Stmts   Miss  Cover
------------------------------------------------------------------------------------------------------------------------
django_coverage_plugin_issue_71_demo/__init__.py                                                         0      0   100%
django_coverage_plugin_issue_71_demo/settings.py                                                        18      0   100%
django_coverage_plugin_issue_71_demo/templates/django_coverage_plugin_issue_71_demo/template1.html      10      0   100%
django_coverage_plugin_issue_71_demo/tests/__init__.py                                                   0      0   100%
django_coverage_plugin_issue_71_demo/tests/test_views.py                                                 7      0   100%
django_coverage_plugin_issue_71_demo/urls.py                                                             4      0   100%
django_coverage_plugin_issue_71_demo/views.py                                                            3      0   100%
manage.py                                                                                               12      2    83%
------------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                                   54      2    96%
```


# Observations

As demonstrated by the output above:
- Used template `template1.html` is mentioned by `coverage report`
- Unused template `template2.html` is _not_ mentioned by `coverage report`
