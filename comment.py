"""Module contains Comment class for creating comments with replies."""

class Comment:
    """Class represents comment with replies."""

    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Add reply to the comment."""
        self.replies.append(reply)

    def remove_reply(self):
        """Remove reply from the comment."""
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """Display comment with replies."""
        indent = "    " * level
        if not self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}Цей коментар було видалено.")
        
        for reply in self.replies:
            reply.display(level + 1)

def main():
    """Main function."""
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()

if __name__ == "__main__":
    main()
