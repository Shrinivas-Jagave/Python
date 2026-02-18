class Projector:
    def __init__(self,
            pj_Brand: str,
            pj_Model: tuple,
            pj_ItemTypeName: str,
            pj_ModelNumber: tuple,
            pj_Manufacture: str,
            pj_BoxContent: tuple,
            pj_Height: tuple,
            pj_Warranty: tuple,
            pj_MultiConnectivity: bool,
            pj_BestSellerRank: str,
            pj_ProductFeatures: tuple,
            pj_NetworkConnectivityTechnology: tuple,
            pj_MaximumDisplayResolution: tuple,
            pj_DisplayType: tuple,
            pj_FormFactor: str,
            pj_MountingType: str,
            pj_BuiltInSpeaker: bool,
            pj_Colour: str,
            pj_CompatibleDevice: tuple,
            pj_MaximumThrowDistance: tuple,
            pj_MinimumThrowDistance: tuple,
            pj_MaximumImageSize: tuple,
            pj_Weight: tuple,
            pj_Dimensions: tuple
        ):

        self.Brand = pj_Brand
        self.Model = pj_Model
        self.ItemTypeName = pj_ItemTypeName
        self.ModelNumber = pj_ModelNumber
        self.Manufacture = pj_Manufacture
        self.BoxContent = pj_BoxContent
        self.Height = pj_Height
        self.Warranty = pj_Warranty
        self.MultiConnectivity = pj_MultiConnectivity
        self.BestSellerRank = pj_BestSellerRank
        self.ProductFeatures = pj_ProductFeatures
        self.NetworkConnectivityTechnology = pj_NetworkConnectivityTechnology
        self.MaximumDisplayResolution = pj_MaximumDisplayResolution
        self.DisplayTyape = pj_DisplayType
        self.FormFactor = pj_FormFactor
        self.MountingType = pj_MountingType
        self.BuiltInSpeaker = pj_BuiltInSpeaker
        self.Colour = pj_Colour
        self.CompatibleDevice= pj_CompatibleDevice
        self.MaximumThrowDistance = pj_MaximumThrowDistance
        self.MinimumThrowDistance = pj_MinimumThrowDistance
        self.MaximumImageSize = pj_MaximumImageSize
        self.Weight = pj_Weight
        self.Dimensions = pj_Dimensions

    def show(self):
        print("Brand : ", self.Brand)
        print("Model : ", self.Model[0], self.Model[1])
        print("Item Type Name : ", self.ItemTypeName)
        print("Model Number : ", self.ModelNumber[0], self.ModelNumber[1])
        print("Manufacture : ", self.Manufacture)
        print("Box Content : ")
        for content in self.BoxContent:
            print('\t', content)
        print("Height : ", self.Height[0], self.Height[1])
        print("Warranty : ", self.Warranty[0], self.Warranty[1])
        print("Is Multi Connectivity ? : ", self.MultiConnectivity)
        print("Best Seller Rank : ", self.BestSellerRank)
        print("Product Features : ")
        for features in self.ProductFeatures:
            print('\t', features)
        print("Network Connectivity Technology : ")
        for technology in self.NetworkConnectivityTechnology:
            print('\t\t\t', technology)
        print("Maximum Display Resolution : ", self.MaximumDisplayResolution[0], 
                                                self.MaximumDisplayResolution[1],
                                                self.MaximumDisplayResolution[2],
                                                )
        print("Display Tyape : ", self.DisplayTyape[0], self.DisplayTyape[1])
        print("Form Factor : ", self.FormFactor)
        print("Mounting Type : ", self.MountingType)
        print("Is Built In Speaker : ", self.BuiltInSpeaker)
        print("Colour : ", self.Colour)
        print("Compatible Device : ")
        for devices in self.CompatibleDevice:
            print("\t", devices)
        print("Maximum Throw Distance : ", self.MaximumThrowDistance[0], self.MaximumThrowDistance[1])
        print("Minimum Throw Distance : ", self.MinimumThrowDistance[0], self.MinimumThrowDistance[1])
        print("Maximum Image Size: ", self.MaximumImageSize[0], self.MaximumImageSize[1])
        print("Weight: ", self.Weight[0], self.Weight[1])
        print("Dimensions : ", self.Dimensions[0],
                                self.Dimensions[1],
                                self.Dimensions[2],
                                self.Dimensions[3],
                                self.Dimensions[4],
                                self.Dimensions[5])

my_Projector = Projector(
    'ZEBRONICS',
    ('ZEBRONICS', 'PIXAPLAY', 59),
    'Pojector',
    ('ZEB-PIXAPLAY', 59),
    'Zebronics India Private Limited',
    (
        'Remote Control',
        'Power Cord',
        'HDMI Cable',
        'QR Code Guide',
        'Cotton Swab Pack'
    ),
    (18, 'Centimeters'),
    (1, 'year carry into service center'),
    True,
    59,
    (
        'Auto Obstacle Avoidance',
        'Auto Screen Alignment',
        'Multi Connectivity',
        'Built In Speakers',
        'Portable Mount'
    ),
    (
        'HDMI', 'USB', 'Type-C'
    ),
    (1920,'x',1080),
    ('LCD', 'LED'),
    'Portable',
    'Portable Mount',
    True,
    'Black',
    (
        'Laptops',
        'Smartphones',
        'Gaming Consoles',
        'Blu-ray Players',
        'Media Players'
    ),
    (6,'Metres'),
    (1.8, 'Metres'),
    (508, 'centimetres'),
    (4070, 'Metres'),
    ('29L', 'x', '28W', 'x', '18H', 'Centimeters')
)

my_Projector.show()
