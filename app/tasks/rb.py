class RBTask:
    def __init__(
            self,
            title: str,
            description: str,
        ):
        self.title = title
        self.description = description

    def to_dict(self) -> dict:
        data = {'title': self.title, 'description': self.description}
        return data