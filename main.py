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
async def createFarmer(farmer: Farmer):
    response = FarmerController.createFarmer(farmer)
    return response

@app.get('/farmers')
async def getFarmers():
    response = FarmerController.getFarmers()
    return response

@app.get('/farmer')
async def getFarmerByID(params: dict):
    response = FarmerController.getFarmerByID(params)
    return response

@app.put('/farmer/update')
async def updateFarmer(farmer: Farmer):
    response = FarmerController.updateFarmer(farmer)
    return response

@app.delete('/farmer/delete')
async def deleteFarmer(params: dict):
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
    return response

@app.get('/farmer/next-of-kin')
async def getNOKByID(params: dict):
    response = FarmerNextOfKinController.getFarmerNextOfKinByID(params)
    return response

@app.put('/farmer/next-of-kin/update')
async def updateNOK(nok: FarmerNextOfKin):
    response = FarmerNextOfKinController.updateFarmerNextOfKin(nok)
    return response

@app.delete('/farmer/next-of-kin/delete')
async def deleteNOK(params: dict):
    response = FarmerNextOfKinController.deleteFarmerNextOfKin(params)
    return response

# Farmer's bank details
@app.post('/farmer/bank-details/create')
async def createBankDetails(bankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.createFarmerBankDetails(bankdetails)
    return response

@app.get('/farmers/bank-details')
async def getBankDetails():
    response = FarmerBankDetailsController.getFarmerBankDetails()
    return response

@app.get('/farmer/bank-details')
async def getBankDetailsByID(params: dict):
    response = FarmerBankDetailsController.getFarmerBankDetailsByID(params)
    return response

@app.put('/farmer/bank-detail/update')
async def updateBankDetails(bankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.updateFarmerBankDetails(bankdetails)
    return response

@app.delete('/farmer/bank-detail/delete')
async def deleteBankDetails(params: dict):
    response = FarmerBankDetailsController.deleteFarmerBankDetails(params)
    return response

# Farmer's spouse
@app.post('/farmer/spouse/create')
async def createSpouse(spouse: FarmerSpouse):
    response = FarmerSpouseController.createFarmerSpouse(spouse)
    return response

@app.get('farmers/spouses')
async def getSpouses():
    response = FarmerSpouseController.getFarmersSpouses()
    return response

@app.get('/farmer/spouse')
async def getSpouseByID(params: dict):
    response = FarmerSpouseController.getFarmerSpouseByID(params)
    return response

@app.put('/farmer/spouse/update')
async def updateSpouse(spouse: FarmerSpouse):
    response = FarmerSpouseController.updateFarmerSpouse(spouse)
    return response

@app.delete('/farmer/spouse/delete')
async def deleteSpouse(params: dict):
    response = FarmerSpouseController.deleteFarmerSpouse(params)
    return response

# Farm
@app.post('/farm/create')
async def createFarm(farm: FarmerFacilityDetails):
    response = FarmerFacilityDetailsController.createFarmerFacilityDetails(farm)
    return response

@app.get('/farms')
async def getFarms():
    response = FarmerFacilityDetailsController.getFarmerFacilityDetails()
    return response

@app.get('/farm')
async def getFarmByID(params: dict):
    response = FarmerFacilityDetailsController.getFarmerFacilityDetailsByID(params)
    return response

@app.put('/farm/update')
async def updateFarm(farm: FarmerFacilityDetails):
    response = FarmerFacilityDetailsController.updateFarmerFacilityDetails(farm)
    return response

@app.delete('/farm/delete')
async def deleteFarm(params: dict):
    response = FarmerFacilityDetailsController.deleteFarmerFacilityDetails(params)
    return response

# Cooperative
@app.post('/cooperative/create')
async def createCooperative(coop: FarmerFacilityCooperative):
    response = FarmerFacilityCooperativeController.createFarmerFacilityCooperative(coop)
    return response

@app.get('/cooperatives')
async def getCooperatives():
    response = FarmerFacilityCooperativeController.getFarmerFacilityCooperatives()
    return response

@app.get('/cooperative')
async def getCooperativeByID(params: dict):
    response = FarmerFacilityCooperativeController.getFarmerFacilityCooperativeByID(params)
    return response

@app.put('/cooperative/update')
async def updateCooperative(coop: FarmerFacilityCooperative):
    response = FarmerFacilityCooperativeController.updateFarmerFacilityCooperative(coop)
    return response

@app.delete('/cooperative/delete')
async def deleteCooperative(params: dict):
    response = FarmerFacilityCooperativeController.deleteFarmerFacilityCooperative(params)
    return response

# Crop
@app.post('/crop/create')
async def createCrop(crop: Crop):
    response = CropController.createCrop(crop)
    return response

@app.get('/crops')
async def getCrops():
    response = CropController.getCrops()
    return response

@app.get('/crop')
async def getCropByID(params: dict):
    response = CropController.getCropByID(params)
    return response

@app.put('/crop/update')
async def updateCrop(crop: Crop):
    response = CropController.updateCrop(crop)
    return response

@app.delete('/crop/delete')
async def deleteCrop(params: dict):
    response = CropController.deleteCrop(params)
    return response

# Crop production
@app.post('/crop-production/create')
async def createCropProduction(prod: CropProduction):
    response = CropProductionController.createCropProduction(prod)
    return response

@app.get('/crop-productions')
async def getCropProductions():
    response = CropProductionController.getCropProductions()
    return response

@app.get('/crop-production')
async def getCropProductionByID(params: dict):
    response = CropProductionController.getCropProductionByID(params)
    return response

@app.put('/crop-production/update')
async def updateCropProduction(prod: CropProduction):
    response = CropProductionController.updateCropProduction(prod)
    return response

@app.delete('/crop-production/delete')
async def deleteCropProduction(params: dict):
    response = CropProductionController.deleteCropProduction(params)
    return response

# Crop certificate
@app.post('/crop-certificate')
async def createCropCertificate(cert: CropCertificate):
    response = CropCertificateController.createCropCertificate(cert)
    return response

@app.get('/crop-certificates')
async def getCropCertificates():
    response = CropCertificateController.getCropCertificates()
    return response

@app.get('/crop-certificate')
async def getCropCertificateByID(params: dict):
    response = CropCertificateController.getCropCertificateByID(params)
    return response

@app.put('/crop-certificate/update')
async def updateCropCertificate(cert: CropCertificate):
    response = CropCertificateController.updateCropCertificate(cert)
    return response

@app.delete('/crop-certificate/delete')
async def deleteCropCertificate(params: dict):
    response = CropCertificateController.deleteCropCertificate(params)
    return response

# Certificate issuer
@app.post('/certificate-issuer/create')
async def createCertificateIssuer(issuer: CertificateIssuer):
    response = CertificateIssuerController.createCertificateIssuer(issuer)
    return response

@app.get('/certificate-issuers')
async def getCertificateIssuers():
    response = CertificateIssuerController.getCertificateIssuers()
    return response

@app.get('/certificate-issuer')
async def getCertificateIssuerByID(params: dict):
    response = CertificateIssuerController.getCertificateIssuerByID(params)
    return response

@app.put('/certificate-issuer/update')
async def updateCertificateIssuer(issuer: CertificateIssuer):
    response = CertificateIssuerController.updateCertificateIssuer(issuer)
    return response

@app.delete('/certificate-issuer/delete')
async def deleteCertificateIssuer(params: dict):
    response = CertificateIssuerController.deleteCertificateIssuer(params)
    return response