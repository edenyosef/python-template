"""Extend the course PostOffice with inbox reading and searching."""


class PostOffice:
    """Store messages in per-user inboxes, with urgent messages first."""

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        self._read_ids = set()

    def send_message(self, sender, recipient, message_body, urgent=False, *, subject=""):
        """Deliver a message to the recipient and return its new numeric ID."""
        user_box = self.boxes[recipient]
        self.message_id += 1
        message = {"id": self.message_id, "body": message_body, "sender": sender}
        if subject:
            message["subject"] = subject
        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
        return self.message_id

    def read_inbox(self, username, count=None):
        """Return up to count unread messages and mark them as read.

        Omit count to read all unread messages. A negative count raises ValueError.
        """
        if count is not None and count < 0:
            raise ValueError("Message count must be non-negative.")

        unread = [
            message for message in self.boxes[username]
            if message["id"] not in self._read_ids
        ]
        messages = unread[:count]
        self._read_ids.update(message["id"] for message in messages)
        return [message.copy() for message in messages]

    def search_inbox(self, username, query):
        """Find a case-sensitive substring in the subject or body of any message."""
        return [
            message.copy() for message in self.boxes[username]
            if query in message.get("subject", "") or query in message["body"]
        ]


def turtle_sent(usernames):
    """Create a post office for the supplied usernames."""
    return PostOffice(usernames)


if __name__ == "__main__":
    post_office = turtle_sent(["alice", "bob"])
    post_office.send_message("alice", "bob", "Bring an umbrella.", subject="Weather")
    print(post_office.read_inbox("bob", 1))
    print(post_office.search_inbox("bob", "Weather"))
