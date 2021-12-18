import xmlparser
from printmodel import print_model

model = xmlparser.build_model("./test.xml")
print_model(model)
