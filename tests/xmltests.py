import xmlparser
from printmodel import print_model

model = xmlparser.build_model("tests/test.xml")
print_model(model)
