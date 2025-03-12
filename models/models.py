from pydantic import BaseModel
from datetime import date
from typing import Optional

class Farmer(BaseModel):
    NationalID: str
    FarmerID: int
    Title: str
    FirstName: str
    Gender: str
    Surname: str
    DateOfBirth: str
    MaidenSurname: str
    CountryOfBirth: str
    NumberOfDependants: int
    MaritalStatus: str
    EmailAddress: str
    MobileNumber: str
    HomeTelephoneNumber: str
    PhysicalAddress: str
    Province: str
    Country: str

class FarmerNextOfKin(BaseModel):
    NationalID: str
    FirstName: str
    Surname: str
    Address: str
    PhoneNumber: str
    FarmerID: Optional[int]

class FarmerBankDetails(BaseModel):
    AccountNumber: str
    BankName: str
    BranchName: str
    BranchCode: str
    AccountName: str
    AccountType: str
    WalletAddress: str
    WalletType: str
    FarmerID: int

class FarmerSpouse(BaseModel):
    NationalID: str
    FirstName: str
    Surname: str
    Address: str
    PhoneNumber: str
    FarmerID: int

class FarmerFacilityDetails(BaseModel):
    FarmID: str
    FarmName: str
    PhysicalAddress: str
    TownCity: str
    District: str
    Province: str
    CoordinatesLat: float
    CoordinatesLong: float
    LandOwnership: str
    LandSize: int
    LandType: str
    ArableLandSize: int
    NearestGMBDepot: str
    OfferLetterPlotNumber: str
    AgritexReference: str
    FarmerID: int

class FarmerFacilityCooperative(BaseModel):
    CooperativeID: str
    CooperativeName: str
    CooperativeLocation: str
    AgriculturalSector: str
    NumberOfFarmers: int
    LeadAgritexOfficer: str
    LeadAgronomist: str
    FarmID: int

class Crop(BaseModel):
    CropID: str
    CropName: str
    Season: str
    FarmID: int

class CropProduction(BaseModel):
    ProductionReferenceID: str
    PlantingDate: str
    HarvestDate: str
    CropYield: float
    CropID: str

class CropCertificate(BaseModel):
    CertificateID: str
    CertificateName: str
    IssuedBy: str
    DateOfIssue: str
    MarketValueOnDateOfIssue: float
    CropGrade: str
    DateOfExpiry: str
    MarketValueOnDateOfExpiry: float
    CropID: str

class CertificateIssuer(BaseModel):
    IssuerID: str
    IssuerName: str
    AllowedToExport: bool
    CertificateID: str

class Contract(BaseModel):
    ContractID: str
    ContractTitle: str
    ContractDescription: str
    ContractValue: float
    TenderDate: str
    ClosingDate: str
    AwardDate: str
    AwardedTo: str
    IssuerID: str

class ContractBid(BaseModel):
    BidID: str
    BidOpeningDate: str
    BidStatus: str
    BidAmount: float
    BidClosingDate: str
    ContractID: str

class LogisticsCompany(BaseModel):
    CompanyID: str
    CompanyName: str
    CompanyPhysicalAddress: str
    ContactNumber: str
    ContactEmail: str
    PerformanceRating: float
    BidID: str

class LogisticsCompanyDriver(BaseModel):
    DriverID: str
    FirstName: str
    Surname: str
    LicenseNumber: str
    DateOfLastRoadTest: str

class LogisticsVehicle(BaseModel):
    VehicleID: str
    RegistrationNumber: str
    Make: str
    Model: str
    NetVehicleMass: int
    GrossVehicleMass: int
    LastMaintenanceDate: str
    NextMaintenanceDate: str
    BidID: str

class LogisticsVehicleJourney(BaseModel):
    JourneyID: str
    VehicleID: str
    DriverID: str
    Origin: str
    Destination: str
    CurrentLocationLat: float
    CurrentLocationLong: float
    
class GMBCertificate(BaseModel):
    GMBCertificateID: str
    IssuedBy: str
    DateOfIssue: str
    MarketValueOnDateOfIssue: float
    CropGrade: str
    DateOfExpiry: str
    MarketValueOnDateOfExpiry: float
    
class Commodity(BaseModel):
    CommodityID: str
    CommodityName: str
    CommodityProducerPrice: float