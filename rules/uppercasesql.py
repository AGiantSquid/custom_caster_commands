from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

from caster.lib.dfplus.additions import IntegerRefST

from dragonfly import Text, Function, Repeat
from dragonfly.actions.action_key import Key


def _render_number(n):
    if n != 0:
        Text(str(int(n))).execute()


class UpperCaseSQL(MergeRule):
    pronunciation = "upper case sequel"
    mapping = {
        "select":
            R(Text("SELECT "), rdescript="SQL: Select"),
        "select top [<n>]":
            R(Text("SELECT TOP ") + Function(_render_number),
              rdescript="SQL: Select Top"),
        "select all":
            R(Text("SELECT * "), rdescript="SQL: Select All"),
        "from":
            R(Key("enter") + Text("FROM "), rdescript="SQL: From"),
        "where":
            R(Key("enter") + Text("WHERE "), rdescript="SQL: Where"),
        "group by":
            R(Key("enter") + Text("GROUP BY "), rdescript="SQL: Group By"),
        "order by":
            R(Key("enter") + Text("ORDER BY "), rdescript="Order By"),
        "ascending":
            R(Text(" ASC "), rdescript="SQL: Ascending"),
        "descending":
            R(Text(" DESC "), rdescript="SQL: Descending"),
        "left join":
            R(Key("enter") + Text("LEFT JOIN "), rdescript="SQL: Left Join"),
        "inner join":
            R(Key("enter") + Text("INNER JOIN "), rdescript="SQL: Inner Join"),
        "join":
            R(Text(" JOIN "), rdescript="SQL: Join"),
        "insert into":
            R(Text(" INSERT INTO "), rdescript="SQL: Insert"),
        "update":
            R(Text(" UPDATE TOKEN SET "), rdescript="SQL: Update"),
        "delete":
            R(Text("DELETE "), rdescript="SQL: Delete"),
        "like":
            R(Text(" LIKE '%%'") + Key("left/5:2"), rdescript="SQL: Like"),
        "union":
            R(Text(" UNION "), rdescript="SQL: Union"),
        "alias as":
            R(Text(" AS "), rdescript="SQL: Alias As"),
        "is null":
            R(Text(" IS NULL "), rdescript="SQL: Is Null"),
        "is not null":
            R(Text(" IS NOT NULL "), rdescript="SQL: Is Not Null"),
        "declare":
            R(Text(" DECLARE @ "), rdescript="SQL: Is Not Null"),
        "fun max":
            R(Text(" MAX() ") + Key("left/5:2"), rdescript="SQL: Max"),
        "fun count":
            R(Text(" COUNT() ") + Key("left/5:2"), rdescript="SQL: Count"),
        "int":
            R(Text(" INT "), rdescript="SQL: Count"),
        "var char | far char":
            R(Text(" VARCHAR() ") + Key("left:2"), rdescript="SQL: Count"),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}


control.nexus().merger.add_global_rule(UpperCaseSQL())
