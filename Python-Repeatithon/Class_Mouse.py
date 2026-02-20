class Mouse: 
    def __init__(self,
            ms_Brand: str,
            ms_Model: str,
            ms_AntennaLocation: str,
            ms_ModelNumber: str,
            ms_AreBatteriesRequired: bool,
            ms_Manufacturer: str,
            ms_ASIN: str,
            ms_NetworkConnectivityTechnology: str,
            ms_ProductFeatures: str,
            ms_MovementDetection: str,
            ms_ButtonQuantity: str,
            ms_HandOrientation: str,
            ms_CompatibleDevices: str
            
        ):

        self.Brand = ms_Brand
        self.Model = ms_Model
        self.AntennaLocation = ms_AntennaLocation
        self.ModelNumber = ms_ModelNumber
        self.AreBatteriesRequired = ms_AreBatteriesRequired
        self.Manufacturer = ms_Manufacturer
        self.ASIN = ms_ASIN
        self.NetworkConnectivityTechnology = ms_NetworkConnectivityTechnology
        self.ProductFeatures = ms_ProductFeatures
        self.MovementDetection = ms_MovementDetection
        self.ButtonQuantity = ms_ButtonQuantity
        self.HandOrientation = ms_HandOrientation
        self.CompatibleDevices = ms_CompatibleDevices

    def show(self):
        print("Brand : ", self.Brand)
        print("Model : ", self.Model)
        print("Antenna Location : ", self.AntennaLocation)
        print("Model Number : ", self.ModelNumber)
        print("Are Batteries Required : ", self.AreBatteriesRequired)
        print("Manufacturer : ", self.Manufacturer)
        print("ASIN : ", self.ASIN)
        print("Network Connectivity Technology : ", self.NetworkConnectivityTechnology)
        print("Product Features : ", self.ProductFeatures)
        print("Movement Detection : ", self.MovementDetection)
        print("Button Quantity : ", self.ButtonQuantity)
        print("Hand Orientation : ", self.HandOrientation)
        print("Compatible Devices : ", self.CompatibleDevices)

my_Mouse = Mouse(
    'XUMLLGVQ',
    'XUMLLGVQ Wired Mouse',
    'Office',
    'OFS045',
    False,
    'XUMLLGVQ',
    'B0DR8GVP93',
    'USB',
    'Lightweight',
    'Optical',
    '3',
    'Ambidextrous',
    'Personal Computer'
)
        
my_Mouse.show()
