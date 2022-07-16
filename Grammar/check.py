from textblob import TextBlob


class Check:
    def process_message(self.message):
        user_input = TextBlob(self.message)
        print(user_input.correct())

