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
async def createFarmerNextOfKin(farmernextofkin: FarmerNextOfKin):
    response = FarmerNextOfKinController.createFarmerNextOfKin(farmernextofkin)
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
def createFarmerBankDetails(bankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.createFarmerBankDetails(bankdetails)
    return response

@app.get('/farmer/bank-details')
def getFarmerBankDetails():
    response = FarmerBankDetailsController.getFarmerBankDetails()
    return response

@app.get('/farmer/bank-detail')
def getBankDetailsByID(params: dict):
    response = FarmerBankDetailsController.getFarmerBankDetailsByID(params)
    return response

@app.put('/farmer/bank-detail/update')
def updateFarmerBankDetails(farmerbankdetails: FarmerBankDetails):
    response = FarmerBankDetailsController.updateFarmerBankDetails(farmerbankdetails)
    return response

@app.delete('/farmer/bank-detail/delete')
def deleteFarmerBankDetails(params: dict):
    response = FarmerBankDetailsController.deleteFarmerBankDetails(params)
    return response

# Farmer's spouse
@app.post('/farmer/spouse/create')
def createFarmerSpouse(farmerspouse: FarmerSpouse):
    response = FarmerSpouseController.createFarmerSpouse(farmerspouse)
    return response

@app.get('/farmer/spouses')
def getFarmerSpouses():
    response = FarmerSpouseController.getFarmerSpouses()
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

# FarmerFacilityDetails
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
def updateFarmerFacilityDetails(farmerfacilitydetails: FarmerFacilityDetails):
    response = FarmerFacilityDetailsController.updateFarmerFacilityDetails(farmerfacilitydetails)
    return response

@app.delete('/farm/delete')
def deleteFarmerFacilityDetails(params: dict):
    response = FarmerFacilityDetailsController.deleteFarmerFacilityDetails(params)
    return response

# Cooperative
@app.post('/cooperative/create')
def createFarmerFacilityCooperative(farmerfacilitycooperative: FarmerFacilityCooperative):
    response = FarmerFacilityCooperativeController.createFarmerFacilityCooperative(farmerfacilitycooperative)
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
def createCropProduction(cropproduction: CropProduction):
    response = CropProductionController.createCropProduction(cropproduction)
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
def createCropCertificate(cropcertificate: CropCertificate):
    response = CropCertificateController.createCropCertificate(cropcertificate)
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

#Certificate Issuer
@app.post('/certificate-issuer/create')
def createCertificateIssuer(certificateissuer: CertificateIssuer):
    response = CertificateIssuerController.createCertificateIssuer(certificateissuer)
    return response

@app.get('/certificate-issuers')
def getCertificateIssuers():
    response = CertificateIssuerController.getCertificateIssuers()
    return response

@app.get('/certificate-issuer')
def getCertificateIssuerByID(params: dict):
    response = CertificateIssuerController.getCertificateIssuerByID(params)
    return response

@app.put('/certificate-issuer/update')
def updateCertificateIssuer(certificateissuer: CertificateIssuer):
    response = CertificateIssuerController.updateCertificateIssuer(certificateissuer)
    return response

@app.delete('/certificate-issuer/delete')
def deleteCertificateIssuer(params: dict):
    response = CertificateIssuerController.deleteCertificateIssuer(params)
    return response

# Contract
@app.post('/contract')
def createContract(contract: Contract):
    response = ContractController.createContract(contract)
    return response

@app.get('/contracts')
def getContracts():
    response = ContractController.getContracts()
    return response

@app.get('/contract')
def getContractByID(params: dict):
    response = ContractController.getContractByID(params)
    return response

@app.put('/contract/update')
def updateContract(contract: Contract):
    response = ContractController.updateContract(contract)
    return response

@app.delete('/contract/delete')
def deleteContract(params: dict):
    response = ContractController.deleteContract(params)
    return response

# ContractBid
@app.post('/contract-bid')
def createContractBid(contractbid: ContractBid):
    response = ContractBidController.createContractBid(contractbid)
    return response

@app.get('/contract-bids')
def getContractBids():
    response = ContractBidController.getContractBids()
    return response

@app.get('/contract-bid')
def getContractBidByID(params: dict):
    response = ContractBidController.getContractBidByID(params)
    return response

@app.put('/contract-bid/update')
def updateContractBid(contractbid: ContractBid):
    response = ContractBidController.updateContractBid(contractbid)
    return response

@app.delete('/contract-bid/delete')
def deleteContractBid(params: dict):
    response = ContractBidController.deleteContractBid(params)
    return response

# LogisticsCompany
@app.post('/logistics-company')
def createLogisticsCompany(logisticscompany: LogisticsCompany):
    response = LogisticsCompanyController.createLogisticsCompany(logisticscompany)
    return response

@app.get('/logistics-companies')
def getLogisticsCompanys():
    response = LogisticsCompanyController.getLogisticsCompanys()
    return response

@app.get('/logistics-company')
def getLogisticsCompanyByID(params: dict):
    response = LogisticsCompanyController.getLogisticsCompanyByID(params)
    return response

@app.put('/logistics-company/update')
def updateLogisticsCompany(logisticscompany: LogisticsCompany):
    response = LogisticsCompanyController.updateLogisticsCompany(logisticscompany)
    return response

@app.delete('/logistics-company/delete')
def deleteLogisticsCompany(params: dict):
    response = LogisticsCompanyController.deleteLogisticsCompany(params)
    return response

# LogisticsCompanyDriver
@app.post('/logistics-company-driver')
def createLogisticsCompanyDriver(logisticscompanydriver: LogisticsCompanyDriver):
    response = LogisticsCompanyDriverController.createLogisticsCompanyDriver(logisticscompanydriver)
    return response

@app.get('/logistics-company-drivers')
def getLogisticsCompanyDrivers():
    response = LogisticsCompanyDriverController.getLogisticsCompanyDrivers()
    return response

@app.get('/logistics-company-driver')
def getLogisticsCompanyDriverByID(params: dict):
    response = LogisticsCompanyDriverController.getLogisticsCompanyDriverByID(params)
    return response

@app.put('/logistics-company-driver/update')
def updateLogisticsCompanyDriver(logisticscompanydriver: LogisticsCompanyDriver):
    response = LogisticsCompanyDriverController.updateLogisticsCompanyDriver(logisticscompanydriver)
    return response

@app.delete('/logistics-company-driver/delete')
def deleteLogisticsCompanyDriver(params: dict):
    response = LogisticsCompanyDriverController.deleteLogisticsCompanyDriver(params)
    return response

# LogisticsVehicle
@app.post('/logistics-vehicle')
def createLogisticsVehicle(logisticsvehicle: LogisticsVehicle):
    response = LogisticsVehicleController.createLogisticsVehicle(logisticsvehicle)
    return response

@app.get('/logistics-vehicles')
def getLogisticsVehicles():
    response = LogisticsVehicleController.getLogisticsVehicles()
    return response

@app.get('/logistics-vehicle')
def getLogisticsVehicleByID(params: dict):
    response = LogisticsVehicleController.getLogisticsVehicleByID(params)
    return response

@app.put('/logistics-vehicle/update')
def updateLogisticsVehicle(logisticsvehicle: LogisticsVehicle):
    response = LogisticsVehicleController.updateLogisticsVehicle(logisticsvehicle)
    return response

@app.delete('/logistics-vehicle/delete')
def deleteLogisticsVehicle(params: dict):
    response = LogisticsVehicleController.deleteLogisticsVehicle(params)
    return response

# LogisticsVehicleJourney
@app.post('/logistics-vehicle-journey')
def createLogisticsVehicleJourney(logisticsvehiclejourney: LogisticsVehicleJourney):
    response = LogisticsVehicleJourneyController.createLogisticsVehicleJourney(logisticsvehiclejourney)
    return response

@app.get('/logistics-vehicle-journeys')
def getLogisticsVehicleJourneys():
    response = LogisticsVehicleJourneyController.getLogisticsVehicleJourneys()
    return response

@app.get('/logistics-vehicle-journey')
def getLogisticsVehicleJourneyByID(params: dict):
    response = LogisticsVehicleJourneyController.getLogisticsVehicleJourneyByID(params)
    return response

@app.put('/logistics-vehicle-journey/update')  
def updateLogisticsVehicleJourney(logisticsvehiclejourney: LogisticsVehicleJourney):
    response = LogisticsVehicleJourneyController.updateLogisticsVehicleJourney(logisticsvehiclejourney)
    return response

@app.delete('/logistics-vehicle-journey/delete')
def deleteLogisticsVehicleJourney(params: dict):
    response = LogisticsVehicleJourneyController.deleteLogisticsVehicleJourney(params)
    return response

@app.post('/gmbcertificate/create')
def createGmbCertificate(gmbcertificate: GMBCertificate):
    response = GMBCertificateController.createGMBCertificate(gmbcertificate)
    return response

@app.get('/gmbcertificates')
def getGMBCertificates():
    response = GMBCertificateController.getGMBCertificates()
    return response

@app.get('/gmbcertificate')
def getGMBCertificateByID(params: dict):
    response = GMBCertificateController.getGMBCertificateByID(params)
    return response

@app.put('/gmbcertificate/update')
def updateGMBCertificate(gmbcertificate: GMBCertificate):
    response = GMBCertificateController.updateGMBCertificate(gmbcertificate)
    return response

@app.delete('/gmbcertificate/delete')
def deleteGMBCertificate(params: dict):
    response = GMBCertificateController.deleteGMBCertificate(params)
    return response

# Commodity
@app.post('/commodity/create')
def  createCommodity(commodity: Commodity):
    response = CommodityController.createCommodity(commodity)
    return response

@app.get('/commodities')
def getCommodities():
    response = CommodityController.getCommodities()
    return response

@app.get('/commodity')
def getCommodityByID(params: dict):
    response = CommodityController.getCommodityByID(params)
    return response

@app.put('/commodity/update')
def updateCommodity(commodity: Commodity):
    response = CommodityController.updateCommodity(commodity)
    return response

@app.delete('/commodity/delete')
def deleteCommodity(params: dict):
    response = CommodityController.deleteCommodity(params)
    return response