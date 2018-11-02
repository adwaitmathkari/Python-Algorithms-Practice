import json
print('hello world')
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("data1.json","w") as write_file:
	json.dump(data, write_file)

#
##>>> import json
##>>> bjhand=(8,"q")
#>>> encodedHand=json.dumps(bjhand)
#>>> decodedHand=json.loads(encodedHand)
#>>> bjhand==decodedHand
#False
#>>> bjHand==tuple(decodedHand)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'bjHand' is not defined
#>>> bjhand==tuple(decodedHand)
#True
#>>> bjHand
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'bjHand' is not defined
#>>> bjhand
#(8, 'q')
#>>> decodedHand
#[8, 'q']
#>>> 

with open("data1.json","r") as readFile:
	datanew=json.load(readFile)
print(datanew)
	
	
	
newJsonString = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(newJsonString)
	
	