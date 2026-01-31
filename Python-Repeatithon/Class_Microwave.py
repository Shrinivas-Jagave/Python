class Microwave:
    def __init__(self,
            mw_Brand: str,
            mw_Model: str,
            mw_ModelNumber: str,
            mw_Size: tuple,
            mw_Colour: str,
            mw_FinishType: str,
            mw_HeatingMethod: str,
            mw_Capacity: tuple,
            mw_Warranty: tuple,
            mw_NoOfProgram: tuple,
            mw_FuelType: str,
            mw_InstallationType: str,
            mw_Wattage: str,
            mw_DefrostSystemType: str,
            mw_FrequencyUnit: tuple,
            mw_TimerFunction: bool,
            mw_Voltage: tuple,
            mw_DoorOrientation: str,
            mw_Automatic: bool,
            mw_Weight: tuple,
            mw_OpenBox: bool,
            mw_Replacement: str,
            mw_SpecialFeatures: tuple,
            mw_Energyconsumption: tuple,
            mw_Dimensions: tuple
        ):
        self.Brand = mw_Brand
        self.Model = mw_Model
        self.ModelNumber = mw_ModelNumber
        self.Size = mw_Size
        self.Colour = mw_Colour
        self.FinishType = mw_FinishType
        self.HeatingMethod = mw_HeatingMethod
        self.Capacity = mw_Capacity
        self.Warranty = mw_Warranty
        self.NoOfProgram = mw_NoOfProgram
        self.FuealType = mw_FuelType
        self.InstallationType = mw_InstallationType
        self.Wattage = mw_Wattage
        self.DefrostSystemType = mw_DefrostSystemType
        self.FrequencyUnit = mw_FrequencyUnit
        self.TimerFunction = mw_TimerFunction
        self.Voltage = mw_Voltage
        self.DoorOrientation = mw_DoorOrientation
        self.Automatic = mw_Automatic
        self.Weight = mw_Weight
        self.OpenBox = mw_OpenBox
        self.Replacement = mw_Replacement
        self.SpeacialFeatures = mw_SpecialFeatures
        self.Energyconsumption = mw_Energyconsumption
        self.Dimensions = mw_Dimensions

    def show(self):
        print("Brand Name : ", self.Brand)
        print("Model : ", self.Model)
        print("Model Number : ", self.ModelNumber)
        print("Size : ", self.Size[0], self.Size[1])
        print("Color : ", self.Colour)
        print("Finish Type : ", self.FinishType)
        print("Heating Method : ", self.HeatingMethod)
        print("Capacity : ", self.Capacity[0], self.Capacity[1], self.Capacity[2])
        print("Warranty : ", self.Warranty[0],self.Warranty[1],",\n\t",
              self.Warranty[2],self.Warranty[3])
        print("NO. Of Programs : ")
        for programs in self.NoOfProgram:
            print("\t", programs)
        print("Fuel Type : ", self.FuealType)
        print("Installation Type : ", self.InstallationType)
        print("Wattage : ", self.Wattage[0],self.Wattage[1])
        print("Defrost System Type : ", self.DefrostSystemType)
        print("Frequency Unit : ", self.FrequencyUnit[0], self.FrequencyUnit[1])
        print("Timer Function : ", self.TimerFunction)
        print("Voltage : ", self.Voltage[0], self.Voltage[1])
        print("Door Orientation : ", self.DoorOrientation)
        print("Automatic : ", self.Automatic)
        print("Weight : ", self.Weight[0], self.Weight[1])
        print("Open Box : ", self.OpenBox)
        print("Replacement : ", self.Replacement)
        print("Speacial Features : ")
        for features in self.SpeacialFeatures:
            print('\t', features)
        print("Energy consumption : ", self.Energyconsumption[0], self.Energyconsumption[1], self.Energyconsumption[2])
        print("Dimensions : ", self.Dimensions[0],self.Dimensions[1],
              self.Dimensions[2],self.Dimensions[3],
              self.Dimensions[4],self.Dimensions[5],)

MyMicrowave = Microwave(
    'Samsung',
    'Convection Microwave Oven',
    'MC32A7035CT/TL',
    (32, 'Liters'),
    'Grey',
    'Stainless Steel',
    'Convention',
    ('Suitable for', 12, 'Family Members'),
    (1, 'Year On Product', 10, 'Years on ceramic enamel cavity'),
    ('Micro', 'Grill', 'Combi', 'Preheat', 'Power defrost'),
    'Electricity',
    'Freestanding',
    (2100, 'Watts'),
    'Power Defrost',
    (230, 'Hz'),
    True,
    (230, 'Volts (DC)'),
    'Left',
    True,
    (20, 'Killograms'),
    True,
    'Availabel',
    (
        'Grill',
        'Low Power Consumption', 
        'Keep Warm Function',
        'Fully Automatic',
        'Various Coocking Mode',
        'Eco Mode',
        'SLIM FRY',
        'Preheat'
    ),
    ('power consumption', 1500, 'W'),
    (523,'x',309,'x',506,'mm'),

)

MyMicrowave.show()
