import Name as nm

me = nm.Name("Jonas", "Lundberg")

print(me.to_string())
# First name
print(me.get_first())
# Last name
print(me.get_last())

you = nm.Name()
you.first = "Arnold"
you.last = "Palmer"
print(you.get_short_name())
