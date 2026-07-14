class Patient:
    def __init__(self, patient_id, name, disease, bill):
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__bill = bill

    def getPatientID(self):
        return self.__patient_id

    def getName(self):
        return self.__name

    def getDisease(self):
        return self.__disease

    def getBill(self):
        return self.__bill

    def setPatientID(self, patient_id):
        self.__patient_id = patient_id

    def setName(self, name):
        self.__name = name

    def setDisease(self, disease):
        self.__disease = disease

    def setBill(self, bill):
        self.__bill = bill

    def addCharges(self, amount):
        self.__bill += amount
        print("Extra charges added.")

    def display(self):
        print("\nPatient Details")
        print("Patient ID :", self.__patient_id)
        print("Name       :", self.__name)
        print("Disease    :", self.__disease)
        print("Bill       :", self.__bill)

p1 = Patient(101, "Rijan", "Fever", 5000)

p1.display()

p1.addCharges(1500)

p1.display()