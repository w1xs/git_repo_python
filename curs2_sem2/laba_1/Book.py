class Book:
    name: str
    author: str
    list_count: int
    cover_url: str

    def __init__(self, name, author, list_count, cover_url):
        self.name = name
        self.author = author
        self.list_count = list_count
        self.cover_url = cover_url

    def get_info(self) -> str:
        return (f"Book name: {self.name}\nBook author: {self.author}"+
                f"\nCount of lists: {self.list_count}")