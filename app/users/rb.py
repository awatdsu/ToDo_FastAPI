class RBUser:
    def __init__(self,
                 username: str | None = None,
                 first_name: str | None = None,
                 last_name: str | None = None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = {'username': self.username, 'first_name': self.first_name, "last_name": self.last_name}
        filtered_data = {key: value for key,value in data.items() if value is not None}
        return filtered_data