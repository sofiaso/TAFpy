from faker import Faker

class Category:
    result = {}
    fake = Faker()
    def __int__(self):
        pass

    def set_id(self, id=0):
        self.result["id"] = id
        return self

    def set_name(self):
        self.result["name"] = self.fake.first_name()
        return self

    def get(self):
        '''
        :return: result w random data samples
        '''
        self.set_id().set_name()
        return self.result

    def build(self):
        '''
        :return: result without data
        '''
        return self.result


class Tag:
    result = {}
    fake = Faker()
    def __int__(self, lang):
        pass

    def set_id(self, id=0):
        self.result["id"] = id
        return self

    def set_name(self):
        self.result["name"] = self.fake.first_name()
        return self

    def get(self):
        '''
        :return: result w random data samples
        '''
        self.set_id().set_name()
        return self.result

    def build(self):
        '''
        :return: result without data
        '''
        return self.result


class Pet:
    result = {}
    fake = Faker()
    def __int__(self):
        pass

    def set_id(self, id=0):
        self.result['id'] = id
        return self

    def set_category(self):
        category = Category()
        self.result["category"] = category.get()
        return self

    def set_name(self):
        self.result["name"] = self.fake.first_name()
        return self

    def set_photo_urls(self):
        l = []
        for _ in range(2):
            l.append(self.fake.uri())

        self.result["photoUrls"] = l
        return self

    def set_tags(self):
        l = []
        for _ in range(2):
            tag = Tag()
            l.append(tag.get())

        self.result["tags"] = l
        return self

    def ste_status(self):
        self.result["status"] = self.fake.word()
        return self

    def build(self):
        '''
        :return: result without data
        '''
        return self.result

    def get(self):
        '''
        :return: result w random data samples
        '''
        self.set_id().\
            set_category().\
            set_name()
        self.set_photo_urls().\
            set_tags().\
            ste_status()

        return self.result