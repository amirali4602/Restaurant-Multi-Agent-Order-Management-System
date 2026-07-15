from spade.message import Message


class MessageBuilder:

    @staticmethod
    def create(
        to: str,
        performative: str,
        body: str
    ) -> Message:

        msg = Message(to=to)

        msg.set_metadata(
            "performative",
            performative
        )

        msg.body = body

        return msg