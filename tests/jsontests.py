import jsonparser
from printmodel import print_model

model = jsonparser.build_model("./test.json")
print_model(model)



