class Patient:
    def __init__(self, patient_id, patient_name, disease, bill_amount):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__disease = disease
        self.__bill_amount = bill_amount

    def get_patient_id(self):
        return self.__patient_id

    def get_patient_name(self):
        return self.__patient_name

    def get_disease(self):
        return self.__disease

    def get_bill_amount(self):
        return self.__bill_amount

    def set_patient_name(self, patient_name):
        self.__patient_name = patient_name

    def set_disease(self, disease):
        self.__disease = disease

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            print("Invalid bill amount.")

    def __str__(self):
        return (
            f"Patient ID   : {self.__patient_id}\n"
            f"Patient Name : {self.__patient_name}\n"
            f"Disease      : {self.__disease}\n"
            f"Bill Amount  : Rs.{self.__bill_amount}"
        )


class InPatient(Patient):
    def __init__(self, patient_id, patient_name, disease, bill_amount, days_admitted):
        super().__init__(patient_id, patient_name, disease, bill_amount)
        self.__days_admitted = days_admitted

    def get_days_admitted(self):
        return self.__days_admitted

    def set_days_admitted(self, days):
        if days > 0:
            self.__days_admitted = days
        else:
            print("Invalid number of days.")

    def calculate_total_bill(self):
        room_charge = self.__days_admitted * 1500
        total_bill = self.get_bill_amount() + room_charge
        return total_bill

    def __str__(self):
        return (
            super().__str__()
            + f"Days Admitted : {self.__days_admitted}"
            + f"Total Bill    : Rs.{self.calculate_total_bill()}"
        )


patient1 = InPatient(
    "P101",
    "Rijan Pariyar",
    "Dengue",
    12000,
    4
)

print("Patient Details")
print(patient1)

patient1.set_days_admitted(6)
patient1.set_bill_amount(15000)

print("\nAfter Updating Details")
print(patient1)