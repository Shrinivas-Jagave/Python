class Ipad:
    def __init__(self,
            ip_Brand: str,
            ip_Model: str,
            ip_ModelNumber: str,
            ip_Manufacturer: str,
            ip_BoxContents: tuple,
            ip_TypeName: str,
            ip_Height: tuple,
            ip_Warranty: tuple,
            ip_OpeartingSystem: str,
            ip_Colour: str,
            ip_VideoProcessor: str,
            ip_Weight: tuple,
            ip_Dimensions: tuple,
            ip_GraphicsDescription: str,
            ip_MemoryStorageCapacity: tuple,
            ip_RAMMemoryInstalled: tuple,
            ip_MemorySlotsAvailable: str,
            ip_ScreenSizeUnitofMeasure: tuple,
            ip_MaximumDisplayResolution: tuple,
            ip_DisplayType: str,
            ip_BatteryCellType: str,
            ip_LithiumBatteryEnergyContent: tuple,
            ip_HardwareInterface: str,
            ip_WirelessTechnologyType: str,
            ip_CellularTechnology: str,
            ip_TotalUSBPorts: str,
            ip_NetworkConnectivityTechnology: str,
            ip_ProcessorBrand: str,
            ip_CameraDescription: str,
            ip_FrontPhotoSensorResolution: tuple
            
        ):

        self.Brand = ip_Brand
        self.Model = ip_Model
        self.ModelNumber = ip_ModelNumber
        self.Manufacturer = ip_Manufacturer
        self.BoxContents = ip_BoxContents
        self.TypeName = ip_TypeName
        self.Height = ip_Height
        self.Warranty = ip_Warranty
        self.OpeartingSystem = ip_OpeartingSystem
        self.Colour = ip_Colour
        self.VideoProcessor = ip_VideoProcessor
        self.Weight = ip_Weight
        self.Dimensions = ip_Dimensions
        self.GraphicsDescription = ip_GraphicsDescription
        self.MemoryStorageCapacity = ip_MemoryStorageCapacity
        self.RAMMemoryInstalled = ip_RAMMemoryInstalled
        self.MemorySlotsAvailable = ip_MemorySlotsAvailable
        self.ScreenSizeUnitofMeasure = ip_ScreenSizeUnitofMeasure
        self.MaximumDisplayResolution = ip_MaximumDisplayResolution
        self.DisplayType = ip_DisplayType
        self.BatteryCellType = ip_BatteryCellType
        self.LithiumBatteryEnergyContent = ip_LithiumBatteryEnergyContent
        self.HardwareInterface = ip_HardwareInterface
        self.WirelessTechnologyType = ip_WirelessTechnologyType
        self.CellularTechnology = ip_CellularTechnology
        self.TotalUSBPorts = ip_TotalUSBPorts
        self.NetworkConnectivityTechnology = ip_NetworkConnectivityTechnology
        self.ProcessorBrand = ip_ProcessorBrand
        self.CameraDescription = ip_CameraDescription
        self.FrontPhotoSensorResolution = ip_FrontPhotoSensorResolution

    def show(self):
        print("Brand : ", self.Brand)
        print("Model : ", self.Model)
        print("Model Number : ", self.ModelNumber)
        print("Manufacturer : ", self.Manufacturer)
        print("Box Contents : ")
        for content in self.BoxContents:
            print("\t", content)
        print("Type Name : ", self.TypeName)
        print("Height : ", self.Height[0], self.Height[1])
        print("Warranty : ", self.Warranty[0], self.Warranty[1])
        print("Opearting System : ", self.OpeartingSystem)
        print("Colour : ", self.Colour)
        print("Video Processor : ", self.VideoProcessor)
        print("Weight : ", self.Weight[0], self.Weight[1])
        print("Dimensions : ", self.Dimensions[0], self.Dimensions[1],
                                self.Dimensions[2], self.Dimensions[3],
                                self.Dimensions[4], self.Dimensions[5])
        print("Graphics Description : ", self.GraphicsDescription)
        print("Memory Storage Capacity : ", self.MemoryStorageCapacity[0], 
                                            self.MemoryStorageCapacity[1])
        print("RAMMemory Installed : ", self.RAMMemoryInstalled[0], 
                                        self.RAMMemoryInstalled[1])
        print("Memory Slots Available : ", self.MemorySlotsAvailable)
        print("Screen Size Unit of Measure : ", self.ScreenSizeUnitofMeasure[0], 
                                                self.ScreenSizeUnitofMeasure[1])
        print("Maximum Display Resolution : ", self.MaximumDisplayResolution[0],
                                                self.MaximumDisplayResolution[1],
                                                self.MaximumDisplayResolution[2],
                                                self.MaximumDisplayResolution[3])
        print("Display Type : ", self.DisplayType)
        print("Battery Cell Type : ", self.BatteryCellType)
        print("Lithium Battery Energy Content : ", self.LithiumBatteryEnergyContent[0],
                                                    self.LithiumBatteryEnergyContent[1])
        print("Hardware Interface : ", self.HardwareInterface)
        print("Wireless Technology Type : ", self.WirelessTechnologyType)
        print("Cellular Technology : ", self.CellularTechnology)
        print("Total USB Ports : ", self.TotalUSBPorts)
        print("Network Connectivity Technology : ", self.NetworkConnectivityTechnology)
        print("Processor Brand : ", self.ProcessorBrand)
        print("Camera Description : ", self.CameraDescription)
        print("Front Photo Sensor Resolution : ", self.FrontPhotoSensorResolution[0],
                                                    self.FrontPhotoSensorResolution[1])

my_Ipad = Ipad(
    'Apple',
    '13-inch iPad Pro (M4, 2024)',
    'MVX53HN/A',
    'Apple',
    (
        'USB-C Charge Cable',
        '20W USB-C Power Adapter',
        '13-inch iPad Pro'
    ),
    'iPad Pro',
    (33.1, 'Centimeters'),
    (1, 'Year'),
    'iOS',
    'Silver',
    'Apple',
    (0.58, 'Kilograms'),
    ('21.6L', 'x', '28.2W', 'x', '0.5Th', 'Centimeters'),
    'Integrated',
    (512, 'GB'),
    (8, 'GB'),
    '1',
    (13, 'Inches'),
    (2752, 'x', 2064, 'Pixels'),
    'Liquid Retina display',
    'Lithium Ion',
    (38.99, 'Watt Hours'),
    'USB Type C', 
    'WI-FI',
    '5G',
    '1',
    'WI-FI',
    'Apple',
    'Front',
    (12, 'MP')
)

my_Ipad.show()
