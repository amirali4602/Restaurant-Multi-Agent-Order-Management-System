class MessageParser:

    @staticmethod
    def performative(message):

        return message.get_metadata(
            "performative"
        )

    @staticmethod
    def body(message):

        return message.body