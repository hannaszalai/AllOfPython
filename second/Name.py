from dataclasses import dataclass


@dataclass
class Name:
    first: str = ""
    last: str = ""

    def to_string(self):
        return f"{self.first} {self.last}"

# first name
    def get_first(self):
        return self.first

# last name
    def get_last(self):
        return self.last

# short name
    def get_short_name(self):
        if self.first and self.last:
            return f"{self.first[0]}. {self.last[0:4]}"
        elif self.first:
            return self.first
        elif self.last:
            return self.last
        else:
            return ""
