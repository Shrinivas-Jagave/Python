class HeadPhones:
    def __init__(self,
            hp_Brand: str,
            hp_ModelName: str,
            hp_ModelNumber: str,
            hp_BoxContent: tuple,
            hp_IsAutographed: bool,
            hp_SeriesNumber: str,
            hp_Manufacturer: str,
            hp_GlobalTradeIdentificationNumber: str,
            hp_Height: tuple,
            hp_ExternalTestingCertification: str,
            hp_Warranty: tuple,
            hp_Weight: tuple,
            hp_ProductFeatures: tuple,
            hp_EnclosureMaterial: str,
            hp_CompatibleDevices: str,
            hp_ControlType: str,
            hp_ControlMethod: str,
            hp_BatteryAverageLife: tuple,
            hp_HeadphoneJack: str,
            hp_NetworkConnectivityTechnology: str,
            hp_BluetoothVersion: str,
            hp_ImpedanceUnitofMeasure: tuple,
            hp_IsNoiseCancellation: bool,
            hp_AudioDriverType: str,
            hp_HeadphoneFormFactor: str,
            hp_Colour: str,
            hp_Theme: str,
            hp_StyleName: str
        ):
        self.Brand = hp_Brand
        self.ModelName = hp_ModelName
        self.ModelNumber = hp_ModelNumber
        self.BoxContent = hp_BoxContent
        self.IsAutographed = hp_IsAutographed
        self.SeriesNumber = hp_SeriesNumber
        self.Manufacturer = hp_Manufacturer
        self.GlobalTradeIdentificationNumber = hp_GlobalTradeIdentificationNumber
        self.Height = hp_Height
        self.ExternalTestingCertification = hp_ExternalTestingCertification
        self.Warranty = hp_Warranty
        self.Weight = hp_Weight
        self.ProductFeatures = hp_ProductFeatures
        self.EnclosureMaterial = hp_EnclosureMaterial
        self.CompatibleDevices = hp_CompatibleDevices
        self.ControlType = hp_ControlType
        self.ControlMethod = hp_ControlMethod
        self.BatteryAverageLife = hp_BatteryAverageLife
        self.HeadphoneJack = hp_HeadphoneJack
        self.NetworkConnectivityTechnology = hp_NetworkConnectivityTechnology
        self.BluetoothVersion = hp_BluetoothVersion
        self.ImpedanceUnitofMeasure = hp_ImpedanceUnitofMeasure
        self.IsNoiseCancellation = hp_IsNoiseCancellation
        self.AudioDriverType = hp_AudioDriverType
        self.HeadphoneFormFactor = hp_HeadphoneFormFactor
        self.Colour = hp_Colour
        self.Theme = hp_Theme
        self.StyleName = hp_StyleName

    def show(self):
        print("Brand : ", self.Brand)
        print("ModelName : ", self.ModelName)
        print("ModelNumber : ", self.ModelNumber)
        print("BoxContent : ")
        for Content in self.BoxContent:
            print("\t", Content)
        print("Is Autographed : ", self.IsAutographed)
        print("Series Number : ", self.SeriesNumber)
        print("Global Trade Identification Number : ", self.GlobalTradeIdentificationNumber)
        print("Manufacturer : ", self.Manufacturer)
        print("Height : ", self.Height[0], self.Height[1])
        print("External Testing Certification : ", self.ExternalTestingCertification)
        print("Warranty : ", self.Warranty[0], self.Warranty[1])
        print("Weight : ", self.Weight[0], self.Weight[1])
        print("Product Features : ")
        for features in self.ProductFeatures:
            print("\t", features)
        print("Enclosure Material : ", self.EnclosureMaterial)
        print("Compatible Devices : ", self.CompatibleDevices)
        print("Control Type : ", self.ControlType)
        print("Control Method : ", self.ControlMethod)
        print("Battery Average Life : ", self.BatteryAverageLife[0], self.BatteryAverageLife[1])
        print("Headphone Jack : ", self.HeadphoneJack)
        print("Network Connectivity Technology : ", self.NetworkConnectivityTechnology)
        print("Bluetooth Version : ", self.BluetoothVersion)
        print("Impedance Unit of Measure : ", self.ImpedanceUnitofMeasure[0], self.ImpedanceUnitofMeasure[1])
        print("Is Noise Cancellation : ", self.IsNoiseCancellation)
        print("Audio Driver Type : ", self.AudioDriverType)
        print("Headphone Form Factor : ", self.HeadphoneFormFactor)
        print("Colour : ", self.Colour)
        print("Theme : ", self.Theme)
        print("Style Name : ", self.StyleName)

my_HeadPhones = HeadPhones(
    'JBL',
    'Quantum 910 Wireless',
    'JBLQ910WLBLK',
    (
        'USB wireless dongle',
        'Calibration Microphone',
        'USB Charging Cable',
        'JBL Quantum 910 Wireless headset'
    ),
    False,
    '91',
    'Harman International Industries',
    '06925281928420',
    (28,'Centimeters'),
    '160272207120',
    (1, 'Yaer'),
    (1000, 'Grams'),
    (
        'Play and charge at the same time',
        '39 hours of battery life that charges as you play with the USB charging cable, included',
        'Dual wireless communication',
        'Lightweight headband',
        'Premium leather-wrapped memory foam ear cushions',
        'Noise Cancellation'
    ),
    'Plastic',
    'Smartphones',
    'Touch Control',
    'Remote',
    (39, 'Hours'),
    'USB',
    'Wireless',
    '5.2',
    (500, 'Ohm'),
    True,
    'Dynamic Driver',
    'Over Ear',
    'Black',
    'Video Game',
    'Quantum 910'

)

my_HeadPhones.show()