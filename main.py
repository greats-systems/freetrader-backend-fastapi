'''
* This is the entry point for the Freetrader backend. It assigns a controller to an API endpoint.
* There are 15 relations, each with its own CRUD controllers
* Scope for future work: routes that should be accessed by authenticated users
'''

from fastapi import FastAPI
from controllers.controllers import *
from models.models import *

app = FastAPI()

# Root
@app.get('/')
async def root():
    return 'Welcome to the Freetrader backend'

# Farmer
@app.post('/farmer/create')
def createFarmer(farmer: Farmer):
    response = FarmerController.createFarmer(farmer)
    return response

@app.get('/farmers')
def getFarmers():
    response = FarmerController.getFarmers()
    return response

@app.get('/farmer')
def getFarmerByID(params: dict):
    response = FarmerController.getFarmerByID(params)
    return response

@app.put('/farmer/update')
def updateFarmer(farmer: Farmer):
    response = FarmerController.updateFarmer(farmer)
    return response

@app.delete('/farmer/delete')
def deleteFarmer(params: dict):
    response = FarmerController.deleteFarmer(params)
    return response

# Farmer's next of kin
@app.post('/farmer/next-of-kin/create')
async def createNOK(nok: FarmerNextOfKin):
    response = FarmerNextOfKinController.createFarmerNextOfKin(nok)
    return response

@app.get('/farmer/next-of-kins')
async def getNOKs():
    response = FarmerNextOfKinController.getFarmerNextOfKins()
    return response.data

@app.get('/farmer/next-of-kin')
def getNOKByID(params: dict):
    response = FarmerNextOfKinController.getFarmerNextOfKinByID(params)
    return response

@app.put('/farmer/next-of-kin/update')
def updateNOK(nok: FarmerNextOfKin):
    response = FarmerNextOfKinController.updateFarmerNextOfKin(nok)
    return response

@app.delete('/farmer/next-of-kin/delete')
def deleteNOK(params: dict):
    response = FarmerNextOfKinController.deleteFarmerNextOfKin(params)
    return response

# Farmer's bank details
@app.post('/farmer/bank-details/create')
def createBankDetails(bankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.createFarmerBankDetails(bankdetails)
    return response

@app.get('/farmers/bank-details')
def getBankDetails():
    response = FarmerBankDetailsController.getFarmerBankDetails()
    return response

@app.get('/farmer/bank-details')
def getBankDetailsByID(params: dict):
    response = FarmerBankDetailsController.getFarmerBankDetailsByID(params)
    return response

@app.put('/farmer/bank-detail/update')
def updateBankDetails(bankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.updateFarmerBankDetails(bankdetails)
    return response

@app.delete('/farmer/bank-detail/delete')
def deleteBankDetails(params: dict):
    response = FarmerBankDetailsController.deleteFarmerBankDetails(params)
    return response

# Farmer's spouse
@app.post('/farmer/spouse/create')
def createSpouse(spouse: FarmerSpouse):
    response = FarmerSpouseController.createFarmerSpouse(spouse)
    return response

@app.get('farmers/spouses')
def getSpouses():
    response = FarmerSpouseController.getFarmersSpouses()
    return response

@app.get('/farmer/spouse')
def getSpouseByID(params: dict):
    response = FarmerSpouseController.getFarmerSpouseByID(params)
    return response

@app.put('/farmer/spouse/update')
def updateSpouse(spouse: FarmerSpouse):
    response = FarmerSpouseController.updateFarmerSpouse(spouse)
    return response

@app.delete('/farmer/spouse/delete')
def deleteSpouse(params: dict):
    response = FarmerSpouseController.deleteFarmerSpouse(params)
    return response

# Farm
@app.post('/farm/create')
def createFarm(farm: FarmerFacilityDetails):
    response = FarmerFacilityDetailsController.createFarmerFacilityDetails(farm)
    return response

@app.get('/farms')
def getFarms():
    response = FarmerFacilityDetailsController.getFarmerFacilityDetails()
    return response

@app.get('/farm')
def getFarmByID(params: dict):
    response = FarmerFacilityDetailsController.getFarmerFacilityDetailsByID(params)
    return response

@app.put('/farm/update')
def updateFarm(farm: FarmerFacilityDetails):
    response = FarmerFacilityDetailsController.updateFarmerFacilityDetails(farm)
    return response

@app.delete('/farm/delete')
def deleteFarm(params: dict):
    response = FarmerFacilityDetailsController.deleteFarmerFacilityDetails(params)
    return response

# Cooperative
@app.post('/cooperative/create')
def createCooperative(coop: FarmerFacilityCooperative):
    response = FarmerFacilityCooperativeController.createFarmerFacilityCooperative(coop)
    return response

@app.get('/cooperatives')
def getCooperatives():
    response = FarmerFacilityCooperativeController.getFarmerFacilityCooperatives()
    return response

@app.get('/cooperative')
def getCooperativeByID(params: dict):
    response = FarmerFacilityCooperativeController.getFarmerFacilityCooperativeByID(params)
    return response

@app.put('/cooperative/update')
def updateCooperative(coop: FarmerFacilityCooperative):
    response = FarmerFacilityCooperativeController.updateFarmerFacilityCooperative(coop)
    return response

@app.delete('/cooperative/delete')
def deleteCooperative(params: dict):
    response = FarmerFacilityCooperativeController.deleteFarmerFacilityCooperative(params)
    return response

# Crop
@app.post('/crop/create')
def createCrop(crop: Crop):
    response = CropController.createCrop(crop)
    return response

@app.get('/crops')
def getCrops():
    response = CropController.getCrops()
    return response

@app.get('/crop')
def getCropByID(params: dict):
    response = CropController.getCropByID(params)
    return response

@app.put('/crop/update')
def updateCrop(crop: Crop):
    response = CropController.updateCrop(crop)
    return response

@app.delete('/crop/delete')
def deleteCrop(params: dict):
    response = CropController.deleteCrop(params)
    return response

# Crop production
@app.post('/crop-production/create')
def createCropProduction(prod: CropProduction):
    response = CropProductionController.createCropProduction(prod)
    return response

@app.get('/crop-productions')
def getCropProductions():
    response = CropProductionController.getCropProductions()
    return response

@app.get('/crop-production')
def getCropProductionByID(params: dict):
    response = CropProductionController.getCropProductionByID(params)
    return response

@app.put('/crop-production/update')
def updateCropProduction(prod: CropProduction):
    response = CropProductionController.updateCropProduction(prod)
    return response

@app.delete('/crop-production/delete')
def deleteCropProduction(params: dict):
    response = CropProductionController.deleteCropProduction(params)
    return response

# Crop certificate
@app.post('/crop-certificate')
def createCropCertificate(cert: CropCertificate):
    response = CropCertificateController.createCropCertificate(cert)
    return response

@app.get('/crop-certificates')
def getCropCertificates():
    response = CropCertificateController.getCropCertificates()
    return response

@app.get('/crop-certificate')
def getCropCertificateByID(params: dict):
    response = CropCertificateController.getCropCertificateByID(params)
    return response

@app.put('/crop-certificate/update')
def updateCropCertificate(cert: CropCertificate):
    response = CropCertificateController.updateCropCertificate(cert)
    return response

@app.delete('/crop-certificate/delete')
def deleteCropCertificate(params: dict):
    response = CropCertificateController.deleteCropCertificate(params)
    return response