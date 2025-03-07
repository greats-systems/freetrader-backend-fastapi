from pydantic import BaseModel
from datetime import date

class Farmer(BaseModel):
    NationalID: str
    FarmerID: str
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
    AccountNumber: str
    SpouseNationalID: str
    NextOfKinNationalID: str

class FarmerNextOfKin(BaseModel):
    NationalID: str
    FirstName: str
    Surname: str
    Address: str
    PhoneNumber: str

class FarmerBankDetails(BaseModel):
    AccountNumber: str
    BankName: str
    BranchName: str
    BranchCode: str
    AccountName: str
    AccountType: str
    WalletAddress: str
    WalletType: str

class FarmerSpouse(BaseModel):
    NationalID: str
    FirstName: str
    Surname: str
    Address: str
    PhoneNumber: str

class FarmerFacilityDetails(BaseModel):
    FarmID: str
    FarmName: str
    PhysicalAddress: str
    TownCity: str
    District: str
    Province: str
    CoordinatesLat: str
    CoordinatesLong: str
    LandOwnership: str
    LandSize: int
    LandType: str
    ArableLandSize: int
    NearestGMBDepot: str
    CropID: str
    OfferLetterPlotNumber: str
    AgritexReference: str
    CooperativeID: str

class FarmerFacilityCooperative(BaseModel):
    CooperativeID: str
    CooperativeName: str
    CooperativeLocation: str
    AgriculturalSector: str
    NumberOfFarmers: int
    LeadAgritexOfficer: str
    LeadAgronomist: str

class Crop(BaseModel):
    CropID: str
    CropName: str
    Season: str
    GMBCertificateID: str
    ProductionReferenceID: str

class CropProduction(BaseModel):
    ProductionReferenceID: str
    PlantingDate: str
    HarvestDate: str
    CropYield: float

class CropCertificate(BaseModel):
    CertificateID: str
    CertificateName: str
    IssuedBy: str
    DateOfIssue: str
    MarketValueOnDateOfIssue: float
    CropGrade: str
    DateOfExpiry: str
    MarketValueOnDateOfExpiry: float

class CertificateIssuer(BaseModel):
    IssuerID: str
    IssuerName: str
    AllowedToExport: str
    ContractID: str

class Contract(BaseModel):
    ContractID: str
    ContractTitle: str
    ContractDescription: str
    ContractValue: float
    TenderDate: str
    ClosingDate: str
    AwardDate: str
    AwardedTo: str

class ContractBid(BaseModel):
    BidID: str
    ContractID: str
    BidOpeningDate: str
    BidStatus: str
    BidAmount: float
    BidClosingDate: str

class LogisticsCompany(BaseModel):
    CompanyID: str
    CompanyName: str
    CompanyPhysicalAddress: str
    ContactNumber: str
    ContactEmail: str
    PerformanceRating: float
    VehicleID: str

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
    JourneyID: str
    DriverID: str

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