class book:
    def __init__ (self, title, author, category, description, thumbnail):
        self.title = title
        self.author = author
        self.category = category
        self.description = description
        self.thumbnail = thumbnail
    def __str__ (self):
        return f'{self.title} - {self.author} - {self.category} - {self.description} - {self.thumbnail}'
    def get_title (self):
        return self.title
    def set_title (self, title):
        self.title = title
    def get_author (self):
        return self.author
    def set_author (self, author):
        self.author = author
    def get_category (self):
        return self.category
    def set_category (self, category):
        self.category = category
    def get_description (self):
        return self.description
    def set_description (self, description):
        self.description = description
    def get_thumbnail (self):
        return self.thumbnail
    def set_thumbnail (self, thumbnail):
        self.thumbnail = thumbnail