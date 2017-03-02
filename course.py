
class Course:
    def __init__(self, url = None, name = None, code = None, chapter = []):
        self.url = url
        self.name = name
        self.code = code
        self.chapter = chapter

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_chapter(self):
        return self.chapter

    def get_code(self):
        return self.code

    def add_chapter(self, cos):
        self.chapter.append(cos)
