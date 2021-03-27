# VS Code

Add shortcuts for uppercase and lowercase:

"File" -> "Preferences" -> "Keyboard Shortcuts"

Make uppercase -> "ctrl" + "alt" + "shift" + u
Make lowercase -> "ctrl" + "alt" + "shift" + l

# `recording_rules`

This entire directory is copied in just to change the verbal command for `Again`

For for further updates, the entire directory can be copied and wholesale with the only needed change being in `again.py`:

```python

    mapping = {
        "wink [<n>]":
            R(Function(lambda n: Again._create_asynchronous(n)), show=False),  # pylint: disable=E0602
    }
```