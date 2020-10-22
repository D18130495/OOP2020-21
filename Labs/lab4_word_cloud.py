class WordCloud:

    def __init__(self):
        self.my_dict = self.create_dict()
        if self.my_dict:
            self.create_html(self.my_dict)
        else:
            print("Issue with input file, please check!")

    def create_dict(self):

        my_dict = {}

        try:
            fo = open("gettisburg.txt", "r")
        except Exception as e:
            my_dict = False
            print("Caught this error: %s" % e.__class__.__name__)
        else:
            for line in fo:
                line = line.lower()
                line = line.split()
                for w in line:
                    self.add_to_dict(w, my_dict)
            fo.close()

        return my_dict

    def add_to_dict(self, word, the_dict):
        for key in the_dict.keys():
            if key == word:
                the_dict[key] = the_dict[key] + 1
                return the_dict
        else:
            the_dict[word] = 1
            return the_dict

    def create_html(self, the_dict):
        try:
            fo = open("output.html", "w")
        except Exception as e:
            print("Caught this error: %s" % e.__class__.__name__)
        else:
            fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

            for key in the_dict.keys():
                fo.write('<span style="font-size: ')
                fo.write(str(the_dict[key] * 10))
                fo.write('px"> ')
                fo.write(key)
                fo.write('</span>')

            fo.write('</div>\
        </body>\
        </html>')


wc = WordCloud()