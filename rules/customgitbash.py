#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for git

"""
# ---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, Mimic, Dictation, Key, Text)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class CustomGitBashRule(MergeRule):
    pronunciation = "custom git bash"

    mapping = {
        "initialize repository":
            Text("git init") + Key("enter"),
        "log":
            Key("g, i, t, space, l, o, g") + Key("enter"),
        "Re-base":
            Key("g, i, t, space, r, e, b, a, s, e,  space"),
        "Re-base interactive":
            Key("g, i, t, space, r, e, b, a, s, e,  space, minus, i, space, H, E, A, D, ~"
                ),
        "add":
            R(Key("g, i, t, space, a, d, d, space, minus, p"), rdescript="GIT: Add All"),
        "status":
            R(Key("g, i, t, space, s, t, a, t, u, s, enter"), rdescript="GIT: Status"),
        "reset":
            R(Key(
                "g, i, t, space, r, e, s, e, t, space, minus, minus, s, o, f, t, space, H, E, A, D, ~"
            ),
              rdescript="GIT: Reset"),
        "commit":
            R(Key(
                "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, apostrophe, apostrophe, left"
            ),
              rdescript="GIT: Commit"),
        "bug fix commit <n>":
            R(Mimic("commit") + Text("fixes #%(n)d ") + Key("backspace"),
              rdescript="GIT: Bug Fix Commit"),
        "reference commit <n>":
            R(Mimic("commit") + Text("refs #%(n)d ") + Key("backspace"),
              rdescript="GIT: Reference Commit"),
        "checkout":
            R(Text("git checkout "), rdescript="GIT: Check Out"),
        "check out new branch":
            R(Text("git checkout -b "), rdescript="GIT: Check Out New Branch"),
        "difference":
            R(Text("git diff") + Key('enter'), rdescript="GIT: Diff"),
        "branch":
            R(Text("git branch") + Key("enter"), rdescript="GIT: Branch"),
        "remote":
            R(Text("git remote "), rdescript="GIT: Remote"),
        "merge":
            R(Text("git merge "), rdescript="GIT: Merge"),
        "merge tool":
            R(Text("git mergetool") + Key("enter"), rdescript="GIT: Merge Tool"),
        "fetch":
            R(Text("git fetch") + Key("enter"), rdescript="GIT: Fetch"),
        "(get push | push)":
            R(Text("git push "), rdescript="GIT: Push"),
        "(get push origin | push origin)":
            R(Text("git push -u origin "), rdescript="GIT: Push Origin"),
        "pull":
            R(Text("git pull") + Key("enter"), rdescript="GIT: Pull"),
        "dirrup":
            R(Text("cd ../ ; ls;") + Key("enter"), rdescript="GIT: Up Directory"),
        "list":
            R(Text("ls "), rdescript="GIT: List"),
        "list all":
            R(Text("ls -la "), rdescript="GIT: List all"),
        "Moved or":  # move dir
            R(Text("mv "), rdescript="GIT: Move"),
        "make directory":
            R(Text("mkdir "), rdescript="GIT: Make Directory"),
        "abort":
            R(Key("c-c "), rdescript="GIT: Abort"),
        "undo [last] commit":
            R(Text("git reset --soft HEAD~1") + Key("enter"),
              rdescript="GIT: Undo Commit"),
        "(undo changes | reset hard)":
            R(Text("git reset --hard") + Key("enter"),
              rdescript="GIT: Undo or Reset Since Last Commit"),
        "stop tracking [file]":
            R(Text("git rm --cached FILENAME"), rdescript="GIT: Stop Tracking"),
        "preview remove untracked":
            R(Text("git clean -nd") + Key("enter"),
              rdescript="GIT: Preview Remove Untracked"),
        "remove untracked":
            R(Text("git clean -fd") + Key("enter"), rdescript="GIT: Remove Untracked"),
        "visualize":
            R(Text("gitk") + Key("enter"), rdescript="GIT: gitk"),
        "visualize file":
            R(Text("gitk -- PATH"), rdescript="GIT: gitk Single File"),
        "visualize all":
            R(Text("gitk --all") + Key("enter"), rdescript="GIT: gitk All Branches"),
        "exit":
            R(Text("exit") + Key("enter"), rdescript="GIT: Exit"),
        "stash":
            R(Text("git stash "), rdescript="GIT: Stash"),
        # "stash apply [<n>]":            R(Text("git stash apply")+Function(_apply), rdescript="GIT: Stash Apply"),
        "stash list":
            R(Text("git stash list") + Key("enter"), rdescript="GIT: Stash List"),
        "stash branch":
            R(Text("git stash branch NAME"), rdescript="GIT: Stash Branch"),
        "cherry pick":
            R(Text("git cherry-pick "), rdescript="GIT: Cherry Pick"),
        "abort cherry pick":
            R(Text("git cherry-pick --abort"), rdescript="GIT: Abort Cherry Pick"),
        # "GUI | gooey":
        #     R(Text("git gui") + Key("enter"), rdescript="GIT: gui"),
        "blame":
            R(Text("git blame PATH -L FIRSTLINE,LASTLINE"), rdescript="GIT: Blame"),
        # "gooey blame":
        #     R(Text("git gui blame PATH"), rdescript="GIT: GUI Blame"),
        "search recursive":
            R(Text("grep -rinH \"PATTERN\" *"), rdescript="GREP: Search Recursive"),
        "search recursive count":
            R(Text("grep -rinH \"PATTERN\" * | wc -l"),
              rdescript="GREP: Search Recursive Count"),
        "search recursive filetype":
            R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;"),
              rdescript="GREP: Search Recursive Filetype"),
        "to file":
            R(Text(" > FILENAME"), rdescript="Bash: To File"),
        "search":
            R(Key("c-r"), rdescript="Bash: To File"),

        # Specific Commands
        "remove directory [<text>]":
            R(Text("rm -rf ") + Text("%(text)s"),
              rdescript="GIT: Navigate To Caster Directory"),
        "CD [<text>]":
            R(Text("cd ") + Text("%(text)s") + Text("; ls") + Key("left") + Key("left") +
              Key("left") + Key("left"),
              rdescript="GIT: Navigate To Caster Directory"),
        "CD Castor":
            R(Text("cd /c/NatLink/NatLink/MacroSystem/caster") + Key("enter"),
              rdescript="GIT: Navigate To Caster Directory"),
        "CD custom Castor":
            R(Text("cd /c/NatLink/NatLink/MacroSystem/caster/user") + Key("enter"),
              rdescript="GIT: Navigate To Caster Directory"),
        "checkout develop":
            R(Text("git checkout develop") + Key("enter"), rdescript="GIT: Check Out"),
        "Mungo":
            R(Text("mongo "), rdescript="GIT: Check Out"),
        "Clear":
            R(Text("clear") + Key("enter"), rdescript="GIT: Check Out"),
        "Cat":
            R(Text("cat "), rdescript="GIT: Check Out"),
        "SSH [<text>]":
            R(Text("ssh ") + Text("%(text)s"), rdescript="GIT: ssh"),
        "pseudo":
            R(Text("sudo "), rdescript="GIT: Check Out"),
        "apt get install":
            R(Text("apt-get install "), rdescript="GIT: Check Out"),
        "next tab":
            R(Key("c-tab"), rdescript="switch tab"),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
        Dictation("text"),
    ]
    defaults = {"n": 0, "text": ""}


# ---------------------------------------------------------------------------

context = AppContext(executable="\\sh.exe")
context2 = AppContext(executable="\\bash.exe")
context3 = AppContext(executable="\\mintty.exe")
context4 = AppContext(executable="\\ConEmu64.exe")

grammar = Grammar("MINGW32", context=(context | context2 | context3 | context4))

if settings.SETTINGS["apps"]["gitbash"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(CustomGitBashRule())
    else:
        rule = CustomGitBashRule(name="custom git bash")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
