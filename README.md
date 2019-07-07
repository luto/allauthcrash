# allauth template crash demo

```
virtualenv venv --python python3
source venv/bin/activate
pip install -r requirements.txt
cd allauthcrash/
py.test --fail-on-template-vars
```

yields

```
self = <pytest_django.plugin._fail_for_invalid_template_variable.<locals>.InvalidVarException object at 0x7f1d57ba2eb8>, var = <Variable: 'scope'>

    def __mod__(self, var):
        """Handle TEMPLATE_STRING_IF_INVALID % var."""
        origin = self._get_origin()
        if origin:
            msg = "Undefined template variable '%s' in '%s'" % (var, origin)
        else:
            msg = "Undefined template variable '%s'" % var
        if self.fail:
>           pytest.fail(msg)
E           Failed: Undefined template variable 'scope' in '/tmp/allauthcrash/venv/lib/python3.7/site-packages/allauth/templates/socialaccount/snippets/provider_list.html'
```
