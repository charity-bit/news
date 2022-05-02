class Article:
    def __init__(self,image,title,description,time,source_name,url):
        self.image = image
        self.title = title
        self.description = description
        self.time = time
        self.source_name = source_name
        self.url = url
      

class Source:
    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

    