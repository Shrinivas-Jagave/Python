class Laptop:
    def __init__(self,
            lt_Brand: str,
            lt_Model: str,
            lt_ModelNumber: str,
            lt_Colour: str,
            lt_Warranty: str,
            lt_ScreenSize: tuple,
            lt_RefreshRate: tuple,
            lt_MaximumDisplayResolution: tuple,
            lt_DisplayType: str,
            lt_HardDiskSize: tuple,
            lt_CPUmodel: tuple,
            lt_RAM: tuple,
            lt_AvailableMemorySlots: bool,
            lt_Bluetooth: bool,
            lt_OperatingSystem: tuple,
            lt_SpecialFeatures: tuple,
            lt_GraphicsCard: str,
            lt_GraphicsCoProcessor: tuple,
            lt_GraphicsRAMsize: tuple,
            lt_Processor: str,
            lt_VideoProcessor: str,
            lt_BoxContents: tuple,
            lt_Height: tuple,
            lt_BatteryCellType: str,
            lt_LithiumBatteryEnergyContent: tuple,
            lt_Weight: tuple,
            lt_WebcamCapability: bool,
            lt_TotalUSBports: str
        ):

        self.Brand = lt_Brand
        self.Model = lt_Model
        self.ModelNumber = lt_ModelNumber
        self.Colour = lt_Colour
        self.Warranty = lt_Warranty
        self.ScreenSize = lt_ScreenSize
        self.Refreshrate = lt_RefreshRate
        self.MaximumDisplayResolution = lt_MaximumDisplayResolution
        self.DisplayType = lt_DisplayType
        self.HardDiskSize = lt_HardDiskSize
        self.CPUmodel = lt_CPUmodel
        self.RAM = lt_RAM
        self.AvailableMemorySlots = lt_AvailableMemorySlots
        self.OperatingSystem = lt_OperatingSystem
        self.Bluetooth = lt_Bluetooth
        self.SpeacialFeatures = lt_SpecialFeatures
        self.GraphicsCard = lt_GraphicsCard
        self.GraphicsCoProcessor = lt_GraphicsCoProcessor
        self.GraphicsRAMsize = lt_GraphicsRAMsize
        self.Processor = lt_Processor
        self.VideoProcessor = lt_VideoProcessor
        self.BoxContents = lt_BoxContents
        self.Height = lt_Height
        self.BatteryCellType = lt_BatteryCellType
        self.LithiumBatteryEnergyContent = lt_LithiumBatteryEnergyContent
        self.Weight = lt_Weight
        self.WebcamCapability = lt_WebcamCapability
        self.TotalUSBports = lt_TotalUSBports

    def show(self):
        print("Brand : ", self.Brand)
        print("Model : ", self.Model)
        print("Model Number : ", self.ModelNumber)
        print("Colour : ", self.Colour)
        print("Warranty : ", self.Warranty)
        print("Screen Size : ", self.ScreenSize[0],self.ScreenSize[1])
        print("Refreshrate : ", self.Refreshrate[0], self.Refreshrate[1])
        print("Maximum Display Resolution : ", self.MaximumDisplayResolution[0],
              self.MaximumDisplayResolution[1],self.MaximumDisplayResolution[2],
              self.MaximumDisplayResolution[3],)
        print("Display Type : ", self.DisplayType)
        print("Hard DiskSize : ", self.HardDiskSize[0], self.HardDiskSize[1])
        print("CPU model : ", self.CPUmodel[0], self.CPUmodel[1], self.CPUmodel[2])
        print("RAM : ", self.RAM[0], self.RAM[1])
        print("Available Memory Slots : ", self.AvailableMemorySlots)
        print("Operating System : ", self.OperatingSystem[0], self.OperatingSystem[1], self.OperatingSystem[2])
        print("Bluetooth : ", self.Bluetooth)
        print("Speacial Features : ")
        for features in self.SpeacialFeatures:
            print("\t", features)
        print("Graphics Card : ", self.GraphicsCard)
        print("Graphics CoProcessor : ", self.GraphicsCoProcessor[0], self.GraphicsCoProcessor[1],
                        self.GraphicsCoProcessor[2], self.GraphicsCoProcessor[3])
        print("Graphics RAM size : ", self.GraphicsRAMsize[0], self.GraphicsRAMsize[1])
        print("Processor : ", self.Processor)
        print("Video Processor : ", self.VideoProcessor)
        print("Box Contents : ")
        for content in self.BoxContents:
            print("\t", content)
        print("Height : ", self.Height[0], self.Height[1])
        print("Battery Cell Type : ", self.BatteryCellType)
        print("Lithium Battery Energy Content : ", self.LithiumBatteryEnergyContent[0],
               self.LithiumBatteryEnergyContent[1])
        print("Weight : ", self.Weight[0], self.Weight[1])
        print("Webcam Capability : ", self.WebcamCapability)
        print("Total USB ports : ", self.TotalUSBports)




myLaptop = Laptop(
'Hp',
'Victus',
'15-fa1319x',
'Mica Silver',
'Limited',
(39.6, 'Centimetres'),
(144, 'Hz'),
(1920,'x',1080,'Pixel'),
'LED',
(512, 'GB'),
('Intel Core','i',5),
(16, 'GB'),
True,
True,
('Windows', 11, 'Home'),
(
    'Anti Glare Screen',
    'Gaming Laptop',
    'High-speed memory and storage',
    'Dedicated Graphics Card',
    'Multiple Port Provide'
),
'Dedicated',
('NVIDIA', 'GeForce', 'RTX', 4050),
(6, 'GB'),
'Intel',
'Intel',
(   
    'Laptop',
    'Charger',
    'User Manual'
),
(51.9, 'Centimeters'),
'Lithium Ion',
(70, 'Watt Hours'),
(3380, 'Grams'),
True,
'7'
)
myLaptop.show()
        
