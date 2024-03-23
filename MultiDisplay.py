class MultiDisplay:
    def first(self):
        self.message = ""
        self.count = 0

    def set_message(self, message):
        self.message = message

    def set_count(self, count):
        self.count = count

    def set_display(self, message, count):
        self.message = message
        self.count = count
        for i in range(count):
            print(message)

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def display(self):
        for i in range(self.count):
            print(self.message)

    def get_message(self):
        return self.message
