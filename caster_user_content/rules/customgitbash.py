"""
Command-module for git
"""
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

from dragonfly import (Mimic, Function, Dictation, Text, ShortIntegerRef, MappingRule)
from castervoice.lib.actions import Key


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class CustomGitBashRule(MappingRule):
    pronunciation = "custom get bash"

    # GIT_ADD_ALL = "g, i, t, space, a, d, d, space, minus, A"
    # GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"
    BRANCH_PREFIX = 'feature/SWOPS-'
    mapping = {
        # "(git|get) base":
        #     Text("git "),

        "initialize repository":
            Text("git init"),
        "add":
            R(Text("git add -p")),


        # "(git|get) add all":
        #     R(Key(GIT_ADD_ALL)),
        # "(git|get) commit all":
        #     R(Key("%s, ;, space, %s" % (GIT_ADD_ALL, GIT_COMMIT))),

        "status":
            R(Text("git status") + Key("enter")),
        "commit":
            R(Text("git commit -m ") + Key("apostrophe, apostrophe, left")),

        # "(git|get) bug fix commit <n>":
        #     R(Mimic("get", "commit") + Text("fixes #%(n)d ") + Key("backspace")),
        # "(git|get) reference commit <n>":
        #     R(Mimic("get", "commit") + Text("refs #%(n)d ") + Key("backspace")),

        "checkout":
            R(Text("git checkout ")),
        "branch":
            R(Text("git branch") + Key("enter")),

        # "remote":
        #     R(Text("git remote ")),

        "merge":
            R(Text("git merge ")),
        # "merge tool":
        #     R(Text("git mergetool") + Key("enter")),

        "fetch":
            R(Text("git fetch") + Key("enter")),
        "push":
            R(Text("git push ")),

        "(get push origin | push origin)":
            R(Text("git push -u origin %s" % BRANCH_PREFIX)),

        "pull":
            R(Text("git pull") + Key("enter")),

        "dirrup":
            R(Text("cd ../ ; ls;") + Key("enter")),

        "list":
            R(Text("ls ")),

        "list all":
            R(Text("ls -la ")),
        "Moved or":  # move dir
            R(Text("mv ")),

        "make directory":
            R(Text("mkdir ")),

        "undo [last] commit | (git|get) reset soft head":
            R(Text("git reset --soft HEAD~1") + Key("enter")),
        "(undo changes | (git|get) reset hard)":
            R(Text("git reset --hard") + Key("enter")),

        # "stop tracking [file] | (git|get) remove":
        #     R(Text("git rm --cached ")),
        # "preview remove untracked | (git|get) clean preview":
        #     R(Text("git clean -nd")),
        # "remove untracked | (git|get) clean untracked":
        #     R(Text("git clean -fd")),
        # "(git|get) visualize":
        #     R(Text("gitk")),
        # "(git|get) visualize file":
        #     R(Text("gitk -- PATH")),
        # "(git|get) visualize all":
        #     R(Text("gitk --all")),
        "stash":
            R(Text("git stash ")),
        "stash apply [<n>]":
            R(Text("git stash apply") + Function(_apply)),

        "stash list":
            R(Text("git stash list") + Key("enter")),

        "stash branch":
            R(Text("git stash branch NAME")),
        "cherry pick":
            R(Text("git cherry-pick ")),
        "abort cherry pick":
            R(Text("git cherry-pick --abort")),
        # "GUI | gooey":
        #     R(Text("git gui") + Key("enter")),
        # "blame":
        #     R(Text("git blame PATH -L FIRSTLINE,LASTLINE")),
        # "gooey blame":
        #     R(Text("git gui blame PATH")),
        # "search recursive":
        #     R(Text("grep -rinH \"PATTERN\" *")),
        # "search recursive count":
        #     R(Text("grep -rinH \"PATTERN\" * | wc -l"),
        # ),
        # "search recursive filetype":
        #     R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;"),
        # ),
        # "to file":
        #     R(Text(" > FILENAME")),


        # Specific Commands

        # git
        "difference":
            R(Text("git diff") + Key('enter')),
        "log":
            R(Text("git log") + Key("enter")),
        "Re-base":
            R(Text("git rebase ")),
        "Re-base interactive":
            R(Text("git rebase -i HEAD~")),
        "checkout develop":
            R(Text("git checkout develop") + Key("enter")),
        "check out new branch":
            R(Text("git checkout -b %s" % BRANCH_PREFIX)),
        "reset":
            R(Text("git reset --soft HEAD~")),

        # shell
        "abort":
            R(Key("c-c ")),
        "exit":
            R(Text("exit") + Key("enter")),
        "search":
            R(Key("c-r")),
        "remove directory [<text>]":
            R(Text("rm -rf ") + Text("%(text)s")),
        "CD [<text>]":
            R(Text("cd %(text)s; ls") + (Key("left") * 4)),
        "CD Castor":
            R(Text("cd ~/Documents/Caster/") + Key("enter")),
        "CD custom Castor":
            R(Text("cd ~/AppData/Local/caster/") + Key("enter")),
        "CD archon":
            R(Text("cd ~/dev/arkon/") + Key("enter")),
        "CD strange":
            R(Text("cd ~/dev/strange/") + Key("enter")),
        "CD xavier":
            R(Text("cd ~/dev/xavier/") + Key("enter")),

        "Clear":
            R(Text("clear") + Key("enter")),
        "Cat":
            R(Text("cat ")),
        "SSH [<text>]":
            R(Text("ssh ") + Text("%(text)s")),
        "pseudo":
            R(Text("sudo ")),
        "apt get install":
            R(Text("apt-get install ")),
        "open new window":
            R(Key("cs-n"), rdescript="Custom Navigation: Open New window"),

        # terminal
        "next tab":
            R(Key("c-tab")),
        "prior tab":
            R(Key("cs-tab")),
        "marco":
            R(Key("cs-f")),
        "totch":
            R(Key("cs-w"), rdescript="Close Tab"),
        "peach":
            R(Key("cs-t")),

        # python
        "activate environment":
            R(Text("source .venv/bin/activate") + Key("enter")),
        # python
        "deactivate environment":
            R(Text("deactivate") + Key("enter")),
        "pytest":
            R(Text("pytest -s -vv")),
    }
    extras = [
        ShortIntegerRef("n", 1, 10000),
        Dictation("text"),
    ]
    defaults = {"n": 0, "text": ""}


_executables = [
    "\\sh.exe",
    "\\bash.exe",
    "\\cmd.exe",
    "\\mintty.exe",
    "\\powershell.exe",
    "debian",
    "bash",
    "mintty",
    "ConEmu64",
    "WindowsTerminal",
]


def get_rule():
    details = RuleDetails(name="custom get bash", executable=_executables)
    return CustomGitBashRule, details
