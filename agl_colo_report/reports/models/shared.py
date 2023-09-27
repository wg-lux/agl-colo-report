# models/shared.py

def name_as_str(self, language="en"):
    if language == 'de':
        # check if name_de is not empty
        if self.name_de:
            return self.name_de
    elif language == 'en':
        if self.name_en:
            return self.name_en
    else:
        return self.name
