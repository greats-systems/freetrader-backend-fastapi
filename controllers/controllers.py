from db.supabase import create_supabase_client
from models.models import *

supabase = create_supabase_client()

class FarmerController:
    def createFarmer(farmer: Farmer):
        try:
            supabase.table('Farmer').insert({
            'FarmerID' : farmer.FarmerID,
            'NationalID' : farmer.NationalID,
            'Title' : farmer.Title,
            'FirstName' : farmer.FirstName,
            'Gender' : farmer.Gender,
            'Surname' : farmer.Surname,
            'DateOfBirth' : farmer.DateOfBirth,
            'MaidenSurname' : farmer.MaidenSurname,
            'CountryOfBirth' : farmer.CountryOfBirth,
            'NumberOfDependants' : farmer.NumberOfDependants,
            'MaritalStatus' : farmer.MaritalStatus,
            'EmailAddress' : farmer.EmailAddress,
            'MobileNumber' : farmer.MobileNumber,
            'HomeTelephoneNumber' : farmer.HomeTelephoneNumber,
            'PhysicalAddress' : farmer.PhysicalAddress,
            'Province' : farmer.Province,
            'Country' : farmer.Country,
            'AccountNumber' : farmer.AccountNumber,
            'SpouseNationalID' : farmer.SpouseNationalID,
            'NextOfKinNationalID' : farmer.NextOfKinNationalID
        }).execute()
            return 'Farmer created successfully!'
        except Exception as e:
            return e

    def getFarmers():
        # supabase.from_('Farmer').select('*').order(column='id').execute()
        try:
            data = supabase.from_('Farmer').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getFarmerByID(params):
        try:
            data = supabase.from_('Farmer').select('*').eq('FarmerID', params['FarmerID']).execute()
            return data
        except Exception as e:
            return e

    def updateFarmer(farmer: Farmer):
        try:
            supabase.from_('Farmer').update({
                'NationalID' : farmer.NationalID,
                'Title' : farmer.Title,
                'FirstName' : farmer.FirstName,
                'Gender' : farmer.Gender,
                'Surname' : farmer.Surname,
                'DateOfBirth' : farmer.DateOfBirth,
                'MaidenSurname' : farmer.MaidenSurname,
                'CountryOfBirth' : farmer.CountryOfBirth,
                'NumberOfDependants' : farmer.NumberOfDependants,
                'MaritalStatus' : farmer.MaritalStatus,
                'EmailAddress' : farmer.EmailAddress,
                'MobileNumber' : farmer.MobileNumber,
                'HomeTelephoneNumber' : farmer.HomeTelephoneNumber,
                'PhysicalAddress' : farmer.PhysicalAddress,
                'Province' : farmer.Province,
                'Country' : farmer.Country,
                'AccountNumber' : farmer.AccountNumber,
                'SpouseNationalID' : farmer.SpouseNationalID,
                'NextOfKinNationalID' : farmer.NextOfKinNationalID
            }).eq('FarmerID', farmer.FarmerID).execute()
            return 'Farmer updated successfully!'
        except Exception as e:
            return e

    def deleteFarmer(params):
        try:
            data = supabase.table('Farmer').delete().eq('FarmerID', params['FarmerID']).execute()
            return data
        except Exception as e:
            return e


class FarmerNextOfKinController:
    def createFarmerNextOfKin(farmernextofkin: FarmerNextOfKin):
        try:
            supabase.table('FarmerNextOfKin').insert({
            'NationalID' : farmernextofkin.NationalID,
            'FirstName' : farmernextofkin.FirstName,
            'Surname' : farmernextofkin.Surname,
            'Address' : farmernextofkin.Address,
            'PhoneNumber' : farmernextofkin.PhoneNumber
        }).execute()
            return 'FarmerNextOfKin created successfully!'
        except Exception as e:
            return e

    def getFarmerNextOfKins():
        try:
            response = supabase.from_('FarmerNextOfKin').select('*').order(column='id').execute()
            return response
        except Exception as e:
            return e

    def getFarmerNextOfKinByID(params):
        try:
            # print(params)
            response = supabase.from_('FarmerNextOfKin').select('*').eq('NationalID', params['NationalID']).execute()
            return response.data
        except Exception as e:
            return e

    def updateFarmerNextOfKin(farmernextofkin: FarmerNextOfKin):
        try:
            supabase.from_('FarmerNextOfKin').update({
                'FirstName' : farmernextofkin.FirstName,
                'Surname' : farmernextofkin.Surname,
                'Address' : farmernextofkin.Address,
                'PhoneNumber' : farmernextofkin.PhoneNumber
            }).eq('NationalID', farmernextofkin.NationalID).execute()
            return 'FarmerNextOfKin updated successfully!'
        except Exception as e:
            return e

    def deleteFarmerNextOfKin(params):
        try:
            supabase.table('FarmerNextOfKin').delete().eq('NationalID', params['NationalID']).execute()
            return 'FarmerNextOfKin deleted successfully!'
        except Exception as e:
            return e


class FarmerBankDetailsController:
    def createFarmerBankDetails(farmerbankdetails: FarmerBankDetails):
        try:
            supabase.table('FarmerBankDetails').insert({
            'AccountNumber' : farmerbankdetails.AccountNumber,
            'BankName' : farmerbankdetails.BankName,
            'BranchName' : farmerbankdetails.BranchName,
            'BranchCode' : farmerbankdetails.BranchCode,
            'AccountName' : farmerbankdetails.AccountName,
            'AccountType' : farmerbankdetails.AccountType,
            'WalletAddress' : farmerbankdetails.WalletAddress,
            'WalletType' : farmerbankdetails.WalletType
        }).execute()
            return 'FarmerBankDetails created successfully!'
        except Exception as e:
            return e

    def getFarmerBankDetails():
        try:
            data = supabase.from_('FarmerBankDetails').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getFarmerBankDetailsByID(params):
        try:
            data = supabase.from_('FarmerBankDetails').select('*').eq('AccountNumber', params['AccountNumber']).execute()
            return data
        except Exception as e:
            return e

    def updateFarmerBankDetails(farmerbankdetails: FarmerBankDetails):
        try:
            supabase.from_('FarmerBankDetails').update({
                'BankName' : farmerbankdetails.BankName,
                'BranchName' : farmerbankdetails.BranchName,
                'BranchCode' : farmerbankdetails.BranchCode,
                'AccountName' : farmerbankdetails.AccountName,
                'AccountType' : farmerbankdetails.AccountType,
                'WalletAddress' : farmerbankdetails.WalletAddress,
                'WalletType' : farmerbankdetails.WalletType
            }).eq('AccountNumber', farmerbankdetails.AccountNumber).execute()
            return 'FarmerBankDetails updated successfully!'
        except Exception as e:
            return e

    def deleteFarmerBankDetails(params):
        try:
            data = supabase.table('FarmerBankDetails').delete().eq('AccountNumber', params['AccountNumber']).execute()
            return data
        except Exception as e:
            return e


class FarmerSpouseController:
    def createFarmerSpouse(farmerspouse: FarmerSpouse):
        try:
            supabase.table('FarmerSpouse').insert({
            'NationalID' : farmerspouse.NationalID,
            'FirstName' : farmerspouse.FirstName,
            'Surname' : farmerspouse.Surname,
            'Address' : farmerspouse.Address,
            'PhoneNumber' : farmerspouse.PhoneNumber
        }).execute()
            return 'FarmerSpouse created successfully!'
        except Exception as e:
            return e

    def getFarmersSpouses():
        try:
            data = supabase.from_('FarmerSpouse').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getFarmerSpouseByID(params):
        try:
            data = supabase.from_('FarmerSpouse').select('*').eq('NationalID', params['NationalID']).execute()
            return data
        except Exception as e:
            return e

    def updateFarmerSpouse(farmerspouse: FarmerSpouse):
        try:
            supabase.from_('FarmerSpouse').update({
                'FirstName' : farmerspouse.FirstName,
                'Surname' : farmerspouse.Surname,
                'Address' : farmerspouse.Address,
                'PhoneNumber' : farmerspouse.PhoneNumber
            }).eq('NationalID', farmerspouse.NationalID).execute()
            return 'FarmerSpouse updated successfully!'
        except Exception as e:
            return e

    def deleteFarmerSpouse(params):
        try:
            data = supabase.table('FarmerSpouse').delete().eq('NationalID', params['NationalID']).execute()
            return data
        except Exception as e:
            return e


class FarmerFacilityDetailsController:
    def createFarmerFacilityDetails(farmerfacilitydetails: FarmerFacilityDetails):
        try:
            supabase.table('FarmerFacilityDetails').insert({
            'FarmID' : farmerfacilitydetails.FarmID,
            'FarmName' : farmerfacilitydetails.FarmName,
            'PhysicalAddress' : farmerfacilitydetails.PhysicalAddress,
            'TownCity' : farmerfacilitydetails.TownCity,
            'District' : farmerfacilitydetails.District,
            'Province' : farmerfacilitydetails.Province,
            'Coordinates' : farmerfacilitydetails.Coordinates,
            'LandOwnership' : farmerfacilitydetails.LandOwnership,
            'LandSize' : farmerfacilitydetails.LandSize,
            'LandType' : farmerfacilitydetails.LandType,
            'ArableLandSize' : farmerfacilitydetails.ArableLandSize,
            'NearestGMBDepot' : farmerfacilitydetails.NearestGMBDepot,
            'CropID' : farmerfacilitydetails.CropID,
            'OfferLetterPlotNumber' : farmerfacilitydetails.OfferLetterPlotNumber,
            'AgritexReference' : farmerfacilitydetails.AgritexReference,
            'CooperativeID' : farmerfacilitydetails.CooperativeID
        }).execute()
            return 'FarmerFacilityDetails created successfully!'
        except Exception as e:
            return e

    def getFarmerFacilityDetails():
        try:
            data = supabase.from_('FarmerFacilityDetails').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getFarmerFacilityDetailsByID(params):
        try:
            data = supabase.from_('FarmerFacilityDetails').select('*').eq('FarmID', params['FarmID']).execute()
            return data
        except Exception as e:
            return e

    def updateFarmerFacilityDetails(farmerfacilitydetails: FarmerFacilityDetails):
        try:
            supabase.from_('FarmerFacilityDetails').update({
                'FarmName' : farmerfacilitydetails.FarmName,
                'PhysicalAddress' : farmerfacilitydetails.PhysicalAddress,
                'TownCity' : farmerfacilitydetails.TownCity,
                'District' : farmerfacilitydetails.District,
                'Province' : farmerfacilitydetails.Province,
                'Coordinates' : farmerfacilitydetails.Coordinates,
                'LandOwnership' : farmerfacilitydetails.LandOwnership,
                'LandSize' : farmerfacilitydetails.LandSize,
                'LandType' : farmerfacilitydetails.LandType,
                'ArableLandSize' : farmerfacilitydetails.ArableLandSize,
                'NearestGMBDepot' : farmerfacilitydetails.NearestGMBDepot,
                'CropID' : farmerfacilitydetails.CropID,
                'OfferLetterPlotNumber' : farmerfacilitydetails.OfferLetterPlotNumber,
                'AgritexReference' : farmerfacilitydetails.AgritexReference,
                'CooperativeID' : farmerfacilitydetails.CooperativeID
            }).eq('FarmID', farmerfacilitydetails.FarmID).execute()
            return 'FarmerFacilityDetails updated successfully!'
        except Exception as e:
            return e

    def deleteFarmerFacilityDetails(params):
        try:
            data = supabase.table('FarmerFacilityDetails').delete().eq('FarmID', params['FarmID']).execute()
            return data
        except Exception as e:
            return e


class FarmerFacilityCooperativeController:
    def createFarmerFacilityCooperative(farmerfacilitycooperative: FarmerFacilityCooperative):
        try:
            supabase.table('FarmerFacilityCooperative').insert({
            'CooperativeID' : farmerfacilitycooperative.CooperativeID,
            'CooperativeName' : farmerfacilitycooperative.CooperativeName,
            'CooperativeLocation' : farmerfacilitycooperative.CooperativeLocation,
            'AgriculturalSector' : farmerfacilitycooperative.AgriculturalSector,
            'NumberOfFarmers' : farmerfacilitycooperative.NumberOfFarmers,
            'LeadAgritexOfficer' : farmerfacilitycooperative.LeadAgritexOfficer,
            'LeadAgronomist' : farmerfacilitycooperative.LeadAgronomist
        }).execute()
            return 'FarmerFacilityCooperative created successfully!'
        except Exception as e:
            return e

    def getFarmerFacilityCooperatives():
        try:
            data = supabase.from_('FarmerFacilityCooperative').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getFarmerFacilityCooperativeByID(params):
        try:
            data = supabase.from_('FarmerFacilityCooperative').select('*').eq('CooperativeID', params['CooperativeID']).execute()
            return data
        except Exception as e:
            return e

    def updateFarmerFacilityCooperative(farmerfacilitycooperative: FarmerFacilityCooperative):
        try:
            supabase.from_('FarmerFacilityCooperative').update({
                'CooperativeName' : farmerfacilitycooperative.CooperativeName,
                'CooperativeLocation' : farmerfacilitycooperative.CooperativeLocation,
                'AgriculturalSector' : farmerfacilitycooperative.AgriculturalSector,
                'NumberOfFarmers' : farmerfacilitycooperative.NumberOfFarmers,
                'LeadAgritexOfficer' : farmerfacilitycooperative.LeadAgritexOfficer,
                'LeadAgronomist' : farmerfacilitycooperative.LeadAgronomist
            }).eq('CooperativeID', farmerfacilitycooperative.CooperativeID).execute()
            return 'FarmerFacilityCooperative updated successfully!'
        except Exception as e:
            return e

    def deleteFarmerFacilityCooperative(params):
        try:
            data = supabase.table('FarmerFacilityCooperative').delete().eq('CooperativeID', params['CooperativeID']).execute()
            return data
        except Exception as e:
            return e


class CropController:
    def createCrop(crop: Crop):
        try:
            supabase.table('Crop').insert({
            'CropID' : crop.CropID,
            'CropName' : crop.CropName,
            'Season' : crop.Season,
            'GMBCertificateID' : crop.GMBCertificateID,
            'ProductionReferenceID' : crop.ProductionReferenceID
        }).execute()
            return 'Crop created successfully!'
        except Exception as e:
            return e

    def getCrops():
        try:
            data = supabase.from_('Crop').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getCropByID(params):
        try:
            data = supabase.from_('Crop').select('*').eq('CropID', params['CropID']).execute()
            return data
        except Exception as e:
            return e

    def updateCrop(crop: Crop):
        try:
            supabase.from_('Crop').update({
                'CropName' : crop.CropName,
                'Season' : crop.Season,
                'GMBCertificateID' : crop.GMBCertificateID,
                'ProductionReferenceID' : crop.ProductionReferenceID
            }).eq('CropID', crop.CropID).execute()
            return 'Crop updated successfully!'
        except Exception as e:
            return e

    def deleteCrop(params):
        try:
            data = supabase.table('Crop').delete().eq('CropID', params['CropID']).execute()
            return data
        except Exception as e:
            return e


class CropProductionController:
    def createCropProduction(cropproduction: CropProduction):
        try:
            supabase.table('CropProduction').insert({
            'ProductionReferenceID' : cropproduction.ProductionReferenceID,
            'PlantingDate' : cropproduction.PlantingDate,
            'HarvestDate' : cropproduction.HarvestDate,
            'CropYield' : cropproduction.CropYield
        }).execute()
            return 'CropProduction created successfully!'
        except Exception as e:
            return e

    def getCropProductions():
        try:
            data = supabase.from_('CropProduction').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getCropProductionByID(params):
        try:
            data = supabase.from_('CropProduction').select('*').eq('ProductionReferenceID', params['ProductionReferenceID']).execute()
            return data
        except Exception as e:
            return e

    def updateCropProduction(cropproduction: CropProduction):
        try:
            supabase.from_('CropProduction').update({
                'PlantingDate' : cropproduction.PlantingDate,
                'HarvestDate' : cropproduction.HarvestDate,
                'CropYield' : cropproduction.CropYield
            }).eq('ProductionReferenceID', cropproduction.ProductionReferenceID).execute()
            return 'CropProduction updated successfully!'
        except Exception as e:
            return e

    def deleteCropProduction(params):
        try:
            data = supabase.table('CropProduction').delete().eq('ProductionReferenceID', params['ProductionReferenceID']).execute()
            return data
        except Exception as e:
            return e


class CropCertificateController:
    def createCropCertificate(cropcertificate: CropCertificate):
        try:
            supabase.table('CropCertificate').insert({
            'CertificateID' : cropcertificate.CertificateID,
            'CertificateName' : cropcertificate.CertificateName,
            'IssuedBy' : cropcertificate.IssuedBy,
            'DateOfIssue' : cropcertificate.DateOfIssue,
            'MarketValueOnDateOfIssue' : cropcertificate.MarketValueOnDateOfIssue,
            'CropGrade' : cropcertificate.CropGrade,
            'DateOfExpiry' : cropcertificate.DateOfExpiry,
            'MarketValueOnDateOfExpiry' : cropcertificate.MarketValueOnDateOfExpiry
        }).execute()
            return 'CropCertificate created successfully!'
        except Exception as e:
            return e

    def getCropCertificates():
        try:
            data = supabase.from_('CropCertificate').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getCropCertificateByID(params):
        try:
            data = supabase.from_('CropCertificate').select('*').eq('CertificateID', params['CertificateID']).execute()
            return data
        except Exception as e:
            return e

    def updateCropCertificate(cropcertificate: CropCertificate):
        try:
            supabase.from_('CropCertificate').update({
                'CertificateName' : cropcertificate.CertificateName,
                'IssuedBy' : cropcertificate.IssuedBy,
                'DateOfIssue' : cropcertificate.DateOfIssue,
                'MarketValueOnDateOfIssue' : cropcertificate.MarketValueOnDateOfIssue,
                'CropGrade' : cropcertificate.CropGrade,
                'DateOfExpiry' : cropcertificate.DateOfExpiry,
                'MarketValueOnDateOfExpiry' : cropcertificate.MarketValueOnDateOfExpiry
            }).eq('CertificateID', cropcertificate.CertificateID).execute()
            return 'CropCertificate updated successfully!'
        except Exception as e:
            return e

    def deleteCropCertificate(params):
        try:
            data = supabase.table('CropCertificate').delete().eq('CertificateID', params['CertificateID']).execute()
            return data
        except Exception as e:
            return e


class CertificateIssuerController:
    def createCertificateIssuer(certificateissuer: CertificateIssuer):
        try:
            supabase.table('CertificateIssuer').insert({
            'IssuerID' : certificateissuer.IssuerID,
            'IssuerName' : certificateissuer.IssuerName,
            'AllowedToExport' : certificateissuer.AllowedToExport,
            'ContractID' : certificateissuer.ContractID
        }).execute()
            return 'CertificateIssuer created successfully!'
        except Exception as e:
            return e

    def getCertificateIssuers():
        try:
            data = supabase.from_('CertificateIssuer').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getCertificateIssuerByID(params):
        try:
            data = supabase.from_('CertificateIssuer').select('*').eq('IssuerID', params['IssuerID']).execute()
            return data
        except Exception as e:
            return e

    def updateCertificateIssuer(certificateissuer: CertificateIssuer):
        try:
            supabase.from_('CertificateIssuer').update({
                'IssuerName' : certificateissuer.IssuerName,
                'AllowedToExport' : certificateissuer.AllowedToExport,
                'ContractID' : certificateissuer.ContractID
            }).eq('IssuerID', certificateissuer.IssuerID).execute()
            return 'CertificateIssuer updated successfully!'
        except Exception as e:
            return e

    def deleteCertificateIssuer(params):
        try:
            data = supabase.table('CertificateIssuer').delete().eq('IssuerID', params['IssuerID']).execute()
            return data
        except Exception as e:
            return e


class ContractController:
    def createContract(contract: Contract):
        try:
            supabase.table('Contract').insert({
            'ContractID' : contract.ContractID,
            'ContractTitle' : contract.ContractTitle,
            'ContractDescription' : contract.ContractDescription,
            'ContractValue' : contract.ContractValue,
            'TenderDate' : contract.TenderDate,
            'ClosingDate' : contract.ClosingDate,
            'AwardDate' : contract.AwardDate,
            'AwardedTo' : contract.AwardedTo
        }).execute()
            return 'Contract created successfully!'
        except Exception as e:
            return e

    def getContracts():
        try:
            data = supabase.from_('Contract').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getContractByID(params):
        try:
            data = supabase.from_('Contract').select('*').eq('ContractID', params['ContractID']).execute()
            return data
        except Exception as e:
            return e

    def updateContract(contract: Contract):
        try:
            supabase.from_('Contract').update({
                'ContractTitle' : contract.ContractTitle,
                'ContractDescription' : contract.ContractDescription,
                'ContractValue' : contract.ContractValue,
                'TenderDate' : contract.TenderDate,
                'ClosingDate' : contract.ClosingDate,
                'AwardDate' : contract.AwardDate,
                'AwardedTo' : contract.AwardedTo
            }).eq('ContractID', contract.ContractID).execute()
            return 'Contract updated successfully!'
        except Exception as e:
            return e

    def deleteContract(params):
        try:
            data = supabase.table('Contract').delete().eq('ContractID', params['ContractID']).execute()
            return data
        except Exception as e:
            return e


class ContractBidController:
    def createContractBid(contractbid: ContractBid):
        try:
            supabase.table('ContractBid').insert({
            'BidID' : contractbid.BidID,
            'ContractID' : contractbid.ContractID,
            'BidOpeningDate' : contractbid.BidOpeningDate,
            'BidStatus' : contractbid.BidStatus,
            'BidAmount' : contractbid.BidAmount,
            'BidClosingDate' : contractbid.BidClosingDate
        }).execute()
            return 'ContractBid created successfully!'
        except Exception as e:
            return e

    def getContractBids():
        try:
            data = supabase.from_('ContractBid').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getContractBidByID(params):
        try:
            data = supabase.from_('ContractBid').select('*').eq('BidID', params['BidID']).execute()
            return data
        except Exception as e:
            return e

    def updateContractBid(contractbid: ContractBid):
        try:
            supabase.from_('ContractBid').update({
                'ContractID' : contractbid.ContractID,
                'BidOpeningDate' : contractbid.BidOpeningDate,
                'BidStatus' : contractbid.BidStatus,
                'BidAmount' : contractbid.BidAmount,
                'BidClosingDate' : contractbid.BidClosingDate
            }).eq('BidID', contractbid.BidID).execute()
            return 'ContractBid updated successfully!'
        except Exception as e:
            return e

    def deleteContractBid(params):
        try:
            data = supabase.table('ContractBid').delete().eq('BidID', params['BidID']).execute()
            return data
        except Exception as e:
            return e


class LogisticsCompanyController:
    def createLogisticsCompany(logisticscompany: LogisticsCompany):
        try:
            supabase.table('LogisticsCompany').insert({
            'CompanyID' : logisticscompany.CompanyID,
            'CompanyName' : logisticscompany.CompanyName,
            'CompanyPhysicalAddress' : logisticscompany.CompanyPhysicalAddress,
            'ContactNumber' : logisticscompany.ContactNumber,
            'ContactEmail' : logisticscompany.ContactEmail,
            'PerformanceRating' : logisticscompany.PerformanceRating,
            'VehicleID' : logisticscompany.VehicleID
        }).execute()
            return 'LogisticsCompany created successfully!'
        except Exception as e:
            return e

    def getLogisticsCompanys():
        try:
            data = supabase.from_('LogisticsCompany').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getLogisticsCompanyByID(params):
        try:
            data = supabase.from_('LogisticsCompany').select('*').eq('CompanyID', params['CompanyID']).execute()
            return data
        except Exception as e:
            return e

    def updateLogisticsCompany(logisticscompany: LogisticsCompany):
        try:
            supabase.from_('LogisticsCompany').update({
                'CompanyName' : logisticscompany.CompanyName,
                'CompanyPhysicalAddress' : logisticscompany.CompanyPhysicalAddress,
                'ContactNumber' : logisticscompany.ContactNumber,
                'ContactEmail' : logisticscompany.ContactEmail,
                'PerformanceRating' : logisticscompany.PerformanceRating,
                'VehicleID' : logisticscompany.VehicleID
            }).eq('CompanyID', logisticscompany.CompanyID).execute()
            return 'LogisticsCompany updated successfully!'
        except Exception as e:
            return e

    def deleteLogisticsCompany(params):
        try:
            data = supabase.table('LogisticsCompany').delete().eq('CompanyID', params['CompanyID']).execute()
            return data
        except Exception as e:
            return e


class LogisticsCompanyDriverController:
    def createLogisticsCompanyDriver(logisticscompanydriver: LogisticsCompanyDriver):
        try:
            supabase.table('LogisticsCompanyDriver').insert({
            'DriverID' : logisticscompanydriver.DriverID,
            'FirstName' : logisticscompanydriver.FirstName,
            'Surname' : logisticscompanydriver.Surname,
            'LicenseNumber' : logisticscompanydriver.LicenseNumber,
            'DateOfLastRoadTest' : logisticscompanydriver.DateOfLastRoadTest
        }).execute()
            return 'LogisticsCompanyDriver created successfully!'
        except Exception as e:
            return e

    def getLogisticsCompanyDrivers():
        try:
            data = supabase.from_('LogisticsCompanyDriver').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getLogisticsCompanyDriverByID(params):
        try:
            data = supabase.from_('LogisticsCompanyDriver').select('*').eq('DriverID', params['DriverID']).execute()
            return data
        except Exception as e:
            return e

    def updateLogisticsCompanyDriver(logisticscompanydriver: LogisticsCompanyDriver):
        try:
            supabase.from_('LogisticsCompanyDriver').update({
                'FirstName' : logisticscompanydriver.FirstName,
                'Surname' : logisticscompanydriver.Surname,
                'LicenseNumber' : logisticscompanydriver.LicenseNumber,
                'DateOfLastRoadTest' : logisticscompanydriver.DateOfLastRoadTest
            }).eq('DriverID', logisticscompanydriver.DriverID).execute()
            return 'LogisticsCompanyDriver updated successfully!'
        except Exception as e:
            return e

    def deleteLogisticsCompanyDriver(params):
        try:
            data = supabase.table('LogisticsCompanyDriver').delete().eq('DriverID', params['DriverID']).execute()
            return data
        except Exception as e:
            return e


class LogisticsVehicleController:
    def createLogisticsVehicle(logisticsvehicle: LogisticsVehicle):
        try:
            supabase.table('LogisticsVehicle').insert({
            'VehicleID' : logisticsvehicle.VehicleID,
            'RegistrationNumber' : logisticsvehicle.RegistrationNumber,
            'Make' : logisticsvehicle.Make,
            'Model' : logisticsvehicle.Model,
            'NetVehicleMass' : logisticsvehicle.NetVehicleMass,
            'GrossVehicleMass' : logisticsvehicle.GrossVehicleMass,
            'LastMaintenanceDate' : logisticsvehicle.LastMaintenanceDate,
            'NextMaintenanceDate' : logisticsvehicle.NextMaintenanceDate,
            'JourneyID' : logisticsvehicle.JourneyID,
            'DriverID' : logisticsvehicle.DriverID
        }).execute()
            return 'LogisticsVehicle created successfully!'
        except Exception as e:
            return e

    def getLogisticsVehicles():
        try:
            data = supabase.from_('LogisticsVehicle').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getLogisticsVehicleByID(params):
        try:
            data = supabase.from_('LogisticsVehicle').select('*').eq('VehicleID', params['VehicleID']).execute()
            return data
        except Exception as e:
            return e

    def updateLogisticsVehicle(logisticsvehicle: LogisticsVehicle):
        try:
            supabase.from_('LogisticsVehicle').update({
                'RegistrationNumber' : logisticsvehicle.RegistrationNumber,
                'Make' : logisticsvehicle.Make,
                'Model' : logisticsvehicle.Model,
                'NetVehicleMass' : logisticsvehicle.NetVehicleMass,
                'GrossVehicleMass' : logisticsvehicle.GrossVehicleMass,
                'LastMaintenanceDate' : logisticsvehicle.LastMaintenanceDate,
                'NextMaintenanceDate' : logisticsvehicle.NextMaintenanceDate,
                'JourneyID' : logisticsvehicle.JourneyID,
                'DriverID' : logisticsvehicle.DriverID
            }).eq('VehicleID', logisticsvehicle.VehicleID).execute()
            return 'LogisticsVehicle updated successfully!'
        except Exception as e:
            return e

    def deleteLogisticsVehicle(params):
        try:
            data = supabase.table('LogisticsVehicle').delete().eq('VehicleID', params['VehicleID']).execute()
            return data
        except Exception as e:
            return e


class LogisticsVehicleJourneyController:
    def createLogisticsVehicleJourney(logisticsvehiclejourney: LogisticsVehicleJourney):
        try:
            supabase.table('LogisticsVehicleJourney').insert({
            'JourneyID' : logisticsvehiclejourney.JourneyID,
            'VehicleID' : logisticsvehiclejourney.VehicleID,
            'DriverID' : logisticsvehiclejourney.DriverID,
            'Origin' : logisticsvehiclejourney.Origin,
            'Destination' : logisticsvehiclejourney.Destination,
            'CurrentLocationLat' : logisticsvehiclejourney.CurrentLocationLat,
            'CurrentLocationLong' : logisticsvehiclejourney.CurrentLocationLong
        }).execute()
            return 'LogisticsVehicleJourney created successfully!'
        except Exception as e:
            return e

    def getLogisticsVehicleJourneys():
        try:
            data = supabase.from_('LogisticsVehicleJourney').select('*').order(column='id').execute()
            return data
        except Exception as e:
            return e

    def getLogisticsVehicleJourneyByID(params):
        try:
            data = supabase.from_('LogisticsVehicleJourney').select('*').eq('JourneyID', params['JourneyID']).execute()
            return data
        except Exception as e:
            return e

    def updateLogisticsVehicleJourney(logisticsvehiclejourney: LogisticsVehicleJourney):
        try:
            supabase.from_('LogisticsVehicleJourney').update({
                'VehicleID' : logisticsvehiclejourney.VehicleID,
                'DriverID' : logisticsvehiclejourney.DriverID,
                'Origin' : logisticsvehiclejourney.Origin,
                'Destination' : logisticsvehiclejourney.Destination,
                'CurrentLocationLat' : logisticsvehiclejourney.CurrentLocationLat,
                'CurrentLocationLong' : logisticsvehiclejourney.CurrentLocationLong
            }).eq('JourneyID', logisticsvehiclejourney.JourneyID).execute()
            return 'LogisticsVehicleJourney updated successfully!'
        except Exception as e:
            return e

    def deleteLogisticsVehicleJourney(params):
        try:
            data = supabase.table('LogisticsVehicleJourney').delete().eq('JourneyID', params['JourneyID']).execute()
            return data
        except Exception as e:
            return e