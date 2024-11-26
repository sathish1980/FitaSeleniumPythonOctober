import json
class jsonRead:


    def write(self):
        # Data to be written
        dictionary = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open("C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\newFitaStudent.json", "w") as outfile:
            outfile.write(json_object)

    def read(self):
        with open('C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Studentinfo.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)

        print(json_object)
        print(type(json_object))

    def readarrayOfData(self):
        # Opening JSON file
        f = open('C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Employeeinfo.json', )

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        for i in data['employee']:
            #print(i)
            name = i["name"]
            if name == "sunil":
                print("pass")

        # Closing file
        f.close()
obj = jsonRead()
obj.readarrayOfData()