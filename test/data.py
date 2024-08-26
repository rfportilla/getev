# Sample file with data for testing


TEST_POI_RESPONSE = r'''
[
    {
        "DataProvider": {
            "WebsiteURL": "http://www.afdc.energy.gov/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "This data is provided by the National Renewable Energy Laboratory (\"NREL\"), which is operated by the Alliance for Sustainable Energy, LLC (\"Alliance\"), for the U.S. Department of Energy (\"DOE\"), and may be used for any purpose whatsoever.",
            "DateLastImported": "2024-02-20T10:59:44.963Z",
            "ID": 2,
            "Title": "afdc.energy.gov"
        },
        "OperatorInfo": null,
        "UsageType": {
            "IsPayAtLocation": null,
            "IsMembershipRequired": true,
            "IsAccessKeyRequired": null,
            "ID": 2,
            "Title": "Private - Restricted Access"
        },
        "StatusType": {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 50,
            "Title": "Operational"
        },
        "SubmissionStatus": {
            "IsLive": true,
            "ID": 100,
            "Title": "Imported and Published"
        },
        "UserComments": null,
        "PercentageSimilarity": null,
        "MediaItems": null,
        "IsRecentlyVerified": true,
        "DateLastVerified": "2024-02-20T09:55:00Z",
        "ID": 221862,
        "UUID": "080FA53F-42A4-42C2-9F9C-1C9B08CD2759",
        "ParentChargePointID": null,
        "DataProviderID": 2,
        "DataProvidersReference": "184325",
        "OperatorID": null,
        "OperatorsReference": null,
        "UsageTypeID": 2,
        "UsageCost": null,
        "AddressInfo": {
            "ID": 222245,
            "Title": "FHWA - NC Division Office",
            "AddressLine1": "310 New Bern Ave",
            "AddressLine2": null,
            "Town": "Raleigh",
            "StateOrProvince": "NC",
            "Postcode": "27601",
            "CountryID": 2,
            "Country": {
                "ISOCode": "US",
                "ContinentCode": "NA",
                "ID": 2,
                "Title": "United States"
            },
            "Latitude": 35.779962,
            "Longitude": -78.633881,
            "ContactTelephone1": "",
            "ContactTelephone2": null,
            "ContactEmail": null,
            "AccessComments": "",
            "RelatedURL": "",
            "Distance": 0.12255813418437754,
            "DistanceUnit": 2
        },
        "Connections": [
            {
                "ID": 372584,
                "ConnectionTypeID": 1,
                "ConnectionType": {
                    "FormalName": "SAE J1772-2009",
                    "IsDiscontinued": null,
                    "IsObsolete": null,
                    "ID": 1,
                    "Title": "Type 1 (J1772)"
                },
                "Reference": null,
                "StatusTypeID": null,
                "StatusType": null,
                "LevelID": 2,
                "Level": {
                    "Comments": "Over 2 kW, usually non-domestic socket type",
                    "IsFastChargeCapable": false,
                    "ID": 2,
                    "Title": "Level 2 : Medium (Over 2kW)"
                },
                "Amps": 16,
                "Voltage": 230,
                "PowerKW": 3.7,
                "CurrentTypeID": 10,
                "CurrentType": {
                    "Description": "Alternating Current - Single Phase",
                    "ID": 10,
                    "Title": "AC (Single-Phase)"
                },
                "Quantity": 1,
                "Comments": "kW power is an estimate based on the connection type"
            }
        ],
        "NumberOfPoints": null,
        "GeneralComments": null,
        "DatePlanned": null,
        "DateLastConfirmed": null,
        "StatusTypeID": 50,
        "DateLastStatusUpdate": "2024-02-20T09:55:00Z",
        "MetadataValues": null,
        "DataQualityLevel": 3,
        "DateCreated": "2023-02-13T05:05:00Z",
        "SubmissionStatusTypeID": 100
    },
    {
        "DataProvider": {
            "WebsiteURL": "http://www.afdc.energy.gov/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "This data is provided by the National Renewable Energy Laboratory (\"NREL\"), which is operated by the Alliance for Sustainable Energy, LLC (\"Alliance\"), for the U.S. Department of Energy (\"DOE\"), and may be used for any purpose whatsoever.",
            "DateLastImported": "2024-02-20T10:59:44.963Z",
            "ID": 2,
            "Title": "afdc.energy.gov"
        },
        "OperatorInfo": {
            "WebsiteURL": "https://ampup.io/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3619,
            "Title": "AmpUp"
        },
        "UsageType": {
            "IsPayAtLocation": null,
            "IsMembershipRequired": true,
            "IsAccessKeyRequired": null,
            "ID": 2,
            "Title": "Private - Restricted Access"
        },
        "StatusType": {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 50,
            "Title": "Operational"
        },
        "SubmissionStatus": {
            "IsLive": true,
            "ID": 100,
            "Title": "Imported and Published"
        },
        "UserComments": null,
        "PercentageSimilarity": null,
        "MediaItems": null,
        "IsRecentlyVerified": true,
        "DateLastVerified": "2024-02-20T09:55:00Z",
        "ID": 269182,
        "UUID": "AE8A619B-1768-4E03-BDD1-E148A005FD70",
        "ParentChargePointID": null,
        "DataProviderID": 2,
        "DataProvidersReference": "262211",
        "OperatorID": 3619,
        "OperatorsReference": null,
        "UsageTypeID": 2,
        "UsageCost": null,
        "AddressInfo": {
            "ID": 269566,
            "Title": "Terry Sanford Federal Courthouse",
            "AddressLine1": "310 New Bern Ave",
            "AddressLine2": null,
            "Town": "Raleigh",
            "StateOrProvince": "NC",
            "Postcode": "27601",
            "CountryID": 2,
            "Country": {
                "ISOCode": "US",
                "ContinentCode": "NA",
                "ID": 2,
                "Title": "United States"
            },
            "Latitude": 35.7792287,
            "Longitude": -78.6340223,
            "ContactTelephone1": "",
            "ContactTelephone2": null,
            "ContactEmail": null,
            "AccessComments": "Contact station for hours of availability",
            "RelatedURL": "https://ampup.io/",
            "Distance": 0.12561749600221536,
            "DistanceUnit": 2
        },
        "Connections": [
            {
                "ID": 458738,
                "ConnectionTypeID": 1,
                "ConnectionType": {
                    "FormalName": "SAE J1772-2009",
                    "IsDiscontinued": null,
                    "IsObsolete": null,
                    "ID": 1,
                    "Title": "Type 1 (J1772)"
                },
                "Reference": null,
                "StatusTypeID": null,
                "StatusType": null,
                "LevelID": 2,
                "Level": {
                    "Comments": "Over 2 kW, usually non-domestic socket type",
                    "IsFastChargeCapable": false,
                    "ID": 2,
                    "Title": "Level 2 : Medium (Over 2kW)"
                },
                "Amps": 16,
                "Voltage": 230,
                "PowerKW": 3.7,
                "CurrentTypeID": 10,
                "CurrentType": {
                    "Description": "Alternating Current - Single Phase",
                    "ID": 10,
                    "Title": "AC (Single-Phase)"
                },
                "Quantity": 2,
                "Comments": "kW power is an estimate based on the connection type"
            }
        ],
        "NumberOfPoints": null,
        "GeneralComments": null,
        "DatePlanned": null,
        "DateLastConfirmed": null,
        "StatusTypeID": 50,
        "DateLastStatusUpdate": "2024-02-20T09:55:00Z",
        "MetadataValues": null,
        "DataQualityLevel": 3,
        "DateCreated": "2023-07-04T06:54:00Z",
        "SubmissionStatusTypeID": 100
    },
    {
        "DataProvider": {
            "WebsiteURL": "http://www.afdc.energy.gov/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "This data is provided by the National Renewable Energy Laboratory (\"NREL\"), which is operated by the Alliance for Sustainable Energy, LLC (\"Alliance\"), for the U.S. Department of Energy (\"DOE\"), and may be used for any purpose whatsoever.",
            "DateLastImported": "2024-02-20T10:59:44.963Z",
            "ID": 2,
            "Title": "afdc.energy.gov"
        },
        "OperatorInfo": null,
        "UsageType": {
            "IsPayAtLocation": null,
            "IsMembershipRequired": null,
            "IsAccessKeyRequired": null,
            "ID": 1,
            "Title": "Public"
        },
        "StatusType": {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 50,
            "Title": "Operational"
        },
        "SubmissionStatus": {
            "IsLive": true,
            "ID": 100,
            "Title": "Imported and Published"
        },
        "UserComments": null,
        "PercentageSimilarity": null,
        "MediaItems": null,
        "IsRecentlyVerified": true,
        "DateLastVerified": "2024-02-20T09:55:00Z",
        "ID": 123151,
        "UUID": "98F51B3E-099F-4E26-BABC-38E0FEBD660F",
        "ParentChargePointID": null,
        "DataProviderID": 2,
        "DataProvidersReference": "40751",
        "OperatorID": null,
        "OperatorsReference": null,
        "UsageTypeID": 1,
        "UsageCost": null,
        "AddressInfo": {
            "ID": 123497,
            "Title": "City of Raleigh - Wilmington Station Deck",
            "AddressLine1": "117 S Wilmington St",
            "AddressLine2": null,
            "Town": "Raleigh",
            "StateOrProvince": "NC",
            "Postcode": "27601",
            "CountryID": 2,
            "Country": {
                "ISOCode": "US",
                "ContinentCode": "NA",
                "ID": 2,
                "Title": "United States"
            },
            "Latitude": 35.77937,
            "Longitude": -78.638203,
            "ContactTelephone1": "919-996-3030",
            "ContactTelephone2": null,
            "ContactEmail": null,
            "AccessComments": "24 hours daily; pay garage",
            "RelatedURL": "",
            "Distance": 0.12674332838069063,
            "DistanceUnit": 2
        },
        "Connections": [
            {
                "ID": 173099,
                "ConnectionTypeID": 9,
                "ConnectionType": {
                    "FormalName": null,
                    "IsDiscontinued": false,
                    "IsObsolete": false,
                    "ID": 9,
                    "Title": "NEMA 5-20R"
                },
                "Reference": null,
                "StatusTypeID": null,
                "StatusType": null,
                "LevelID": 1,
                "Level": {
                    "Comments": "Under 2 kW, usually domestic socket types",
                    "IsFastChargeCapable": false,
                    "ID": 1,
                    "Title": "Level 1 : Low (Under 2kW)"
                },
                "Amps": 16,
                "Voltage": 120,
                "PowerKW": 1.9,
                "CurrentTypeID": 10,
                "CurrentType": {
                    "Description": "Alternating Current - Single Phase",
                    "ID": 10,
                    "Title": "AC (Single-Phase)"
                },
                "Quantity": 1,
                "Comments": "kW power is an estimate based on the connection type"
            },
            {
                "ID": 173100,
                "ConnectionTypeID": 1,
                "ConnectionType": {
                    "FormalName": "SAE J1772-2009",
                    "IsDiscontinued": null,
                    "IsObsolete": null,
                    "ID": 1,
                    "Title": "Type 1 (J1772)"
                },
                "Reference": null,
                "StatusTypeID": null,
                "StatusType": null,
                "LevelID": 2,
                "Level": {
                    "Comments": "Over 2 kW, usually non-domestic socket type",
                    "IsFastChargeCapable": false,
                    "ID": 2,
                    "Title": "Level 2 : Medium (Over 2kW)"
                },
                "Amps": 16,
                "Voltage": 230,
                "PowerKW": 3.7,
                "CurrentTypeID": 10,
                "CurrentType": {
                    "Description": "Alternating Current - Single Phase",
                    "ID": 10,
                    "Title": "AC (Single-Phase)"
                },
                "Quantity": 1,
                "Comments": "kW power is an estimate based on the connection type"
            }
        ],
        "NumberOfPoints": null,
        "GeneralComments": null,
        "DatePlanned": null,
        "DateLastConfirmed": null,
        "StatusTypeID": 50,
        "DateLastStatusUpdate": "2024-02-20T09:55:00Z",
        "MetadataValues": null,
        "DataQualityLevel": 3,
        "DateCreated": "2019-04-06T05:03:00Z",
        "SubmissionStatusTypeID": 100
    }
]
'''

TEST_CORE_REFERENCE_RESPONSE = r'''
{
    "ChargerTypes": [
        {
            "Comments": "Under 2 kW, usually domestic socket types",
            "IsFastChargeCapable": false,
            "ID": 1,
            "Title": "Level 1 : Low (Under 2kW)"
        },
        {
            "Comments": "Over 2 kW, usually non-domestic socket type",
            "IsFastChargeCapable": false,
            "ID": 2,
            "Title": "Level 2 : Medium (Over 2kW)"
        },
        {
            "Comments": "40KW and Higher",
            "IsFastChargeCapable": true,
            "ID": 3,
            "Title": "Level 3:  High (Over 40kW)"
        }
    ],
    "ConnectionTypes": [
        {
            "FormalName": "Avcon SAE J1772-2001",
            "IsDiscontinued": true,
            "IsObsolete": false,
            "ID": 7,
            "Title": "Avcon Connector"
        },
        {
            "FormalName": null,
            "IsDiscontinued": null,
            "IsObsolete": null,
            "ID": 4,
            "Title": "Blue Commando (2P+E)"
        },
        {
            "FormalName": "BS1363 / Type G",
            "IsDiscontinued": null,
            "IsObsolete": null,
            "ID": 3,
            "Title": "BS1363 3 Pin 13 Amp"
        },
        {
            "FormalName": "IEC 62196-3 Configuration EE",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 32,
            "Title": "CCS (Type 1)"
        },
        {
            "FormalName": "IEC 62196-3 Configuration FF",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 33,
            "Title": "CCS (Type 2)"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 16,
            "Title": "CEE 3 Pin"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 17,
            "Title": "CEE 5 Pin"
        },
        {
            "FormalName": "CEE 7/4",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 28,
            "Title": "CEE 7/4 - Schuko - Type F"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 23,
            "Title": "CEE 7/5"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 18,
            "Title": "CEE+ 7 Pin"
        },
        {
            "FormalName": "IEC 62196-3 Configuration AA",
            "IsDiscontinued": null,
            "IsObsolete": null,
            "ID": 2,
            "Title": "CHAdeMO"
        },
        {
            "FormalName": "Europlug 2-Pin (CEE 7/16)",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 13,
            "Title": "Europlug 2-Pin (CEE 7/16)"
        },
        {
            "FormalName": "GB-T AC - GB/T 20234.2 (Socket)",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1038,
            "Title": "GB-T AC - GB/T 20234.2 (Socket)"
        },
        {
            "FormalName": "GB-T AC - GB/T 20234.2 (Tethered Cable)",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1039,
            "Title": "GB-T AC - GB/T 20234.2 (Tethered Cable)"
        },
        {
            "FormalName": "GB-T DC - GB/T 20234.3",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1040,
            "Title": "GB-T DC - GB/T 20234.3"
        },
        {
            "FormalName": "IEC 60309 3-pin",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 34,
            "Title": "IEC 60309 3-pin"
        },
        {
            "FormalName": "IEC 60309 5-pin",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 35,
            "Title": "IEC 60309 5-pin"
        },
        {
            "FormalName": "Large Paddle Inductive",
            "IsDiscontinued": true,
            "IsObsolete": true,
            "ID": 5,
            "Title": "LP Inductive"
        },
        {
            "FormalName": "SAE J3400",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 27,
            "Title": "NACS / Tesla Supercharger"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 10,
            "Title": "NEMA 14-30"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 11,
            "Title": "NEMA 14-50"
        },
        {
            "FormalName": "NEMA 5-15R",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 22,
            "Title": "NEMA 5-15R"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 9,
            "Title": "NEMA 5-20R"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 15,
            "Title": "NEMA 6-15"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 14,
            "Title": "NEMA 6-20"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1042,
            "Title": "NEMA TT-30R"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 36,
            "Title": "SCAME Type 3A (Low Power)"
        },
        {
            "FormalName": "IEC 62196-2 Type 3",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 26,
            "Title": "SCAME Type 3C (Schneider-Legrand)"
        },
        {
            "FormalName": "Small Paddle Inductive",
            "IsDiscontinued": true,
            "IsObsolete": true,
            "ID": 6,
            "Title": "SP Inductive"
        },
        {
            "FormalName": "T13/ IEC Type J",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1037,
            "Title": "T13 - SEC1011 ( Swiss domestic 3-pin ) - Type J"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 30,
            "Title": "Tesla (Model S/X)"
        },
        {
            "FormalName": "Tesla Connector",
            "IsDiscontinued": true,
            "IsObsolete": false,
            "ID": 8,
            "Title": "Tesla (Roadster)"
        },
        {
            "FormalName": "Tesla Battery Swap Station",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 31,
            "Title": "Tesla Battery Swap"
        },
        {
            "FormalName": "AS/NZS 3123 Three Phase",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1041,
            "Title": "Three Phase 5-Pin (AS/NZ 3123)"
        },
        {
            "FormalName": "SAE J1772-2009",
            "IsDiscontinued": null,
            "IsObsolete": null,
            "ID": 1,
            "Title": "Type 1 (J1772)"
        },
        {
            "FormalName": "IEC 62196-2 Type 2",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 25,
            "Title": "Type 2 (Socket Only)"
        },
        {
            "FormalName": "IEC 62196-2",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1036,
            "Title": "Type 2 (Tethered Connector) "
        },
        {
            "FormalName": "Type I/AS 3112/CPCS-CCC",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 29,
            "Title": "Type I (AS 3112)"
        },
        {
            "FormalName": "IEC Type M (SANS 164-1, IS 1293:2005)",
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 1043,
            "Title": "Type M"
        },
        {
            "FormalName": "Not Specified",
            "IsDiscontinued": null,
            "IsObsolete": null,
            "ID": 0,
            "Title": "Unknown"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 24,
            "Title": "Wireless Charging"
        },
        {
            "FormalName": null,
            "IsDiscontinued": false,
            "IsObsolete": false,
            "ID": 21,
            "Title": "XLR Plug (4 pin)"
        }
    ],
    "CurrentTypes": [
        {
            "Description": "Alternating Current - Single Phase",
            "ID": 10,
            "Title": "AC (Single-Phase)"
        },
        {
            "Description": "Alternating Current - Three Phase",
            "ID": 20,
            "Title": "AC (Three-Phase)"
        },
        {
            "Description": "Direct Current",
            "ID": 30,
            "Title": "DC"
        }
    ],
    "Countries": [
        {
            "ISOCode": "GB",
            "ContinentCode": "EU",
            "ID": 1,
            "Title": "United Kingdom"
        },
        {
            "ISOCode": "US",
            "ContinentCode": "NA",
            "ID": 2,
            "Title": "United States"
        },
        {
            "ISOCode": "IE",
            "ContinentCode": "EU",
            "ID": 3,
            "Title": "Ireland"
        },
        {
            "ISOCode": "HK",
            "ContinentCode": "AS",
            "ID": 4,
            "Title": "Hong Kong"
        },
        {
            "ISOCode": "AF",
            "ContinentCode": "AS",
            "ID": 5,
            "Title": "Afghanistan"
        },
        {
            "ISOCode": "AX",
            "ContinentCode": "EU",
            "ID": 6,
            "Title": "Aland Islands"
        },
        {
            "ISOCode": "AL",
            "ContinentCode": "EU",
            "ID": 7,
            "Title": "Albania"
        },
        {
            "ISOCode": "DZ",
            "ContinentCode": "AF",
            "ID": 8,
            "Title": "Algeria"
        },
        {
            "ISOCode": "AS",
            "ContinentCode": "OC",
            "ID": 9,
            "Title": "American Samoa"
        },
        {
            "ISOCode": "AD",
            "ContinentCode": "EU",
            "ID": 10,
            "Title": "Andorra"
        },
        {
            "ISOCode": "AO",
            "ContinentCode": "AF",
            "ID": 11,
            "Title": "Angola"
        },
        {
            "ISOCode": "AI",
            "ContinentCode": "NA",
            "ID": 12,
            "Title": "Anguilla"
        },
        {
            "ISOCode": "AQ",
            "ContinentCode": "AN",
            "ID": 13,
            "Title": "Antarctica"
        },
        {
            "ISOCode": "AG",
            "ContinentCode": "NA",
            "ID": 14,
            "Title": "Antigua And Barbuda"
        },
        {
            "ISOCode": "AR",
            "ContinentCode": "SA",
            "ID": 15,
            "Title": "Argentina"
        },
        {
            "ISOCode": "AM",
            "ContinentCode": "AS",
            "ID": 16,
            "Title": "Armenia"
        },
        {
            "ISOCode": "AW",
            "ContinentCode": "NA",
            "ID": 17,
            "Title": "Aruba"
        },
        {
            "ISOCode": "AU",
            "ContinentCode": "OC",
            "ID": 18,
            "Title": "Australia"
        },
        {
            "ISOCode": "AT",
            "ContinentCode": "EU",
            "ID": 19,
            "Title": "Austria"
        },
        {
            "ISOCode": "AZ",
            "ContinentCode": "AS",
            "ID": 20,
            "Title": "Azerbaijan"
        },
        {
            "ISOCode": "BS",
            "ContinentCode": "NA",
            "ID": 21,
            "Title": "Bahamas"
        },
        {
            "ISOCode": "BH",
            "ContinentCode": "AS",
            "ID": 22,
            "Title": "Bahrain"
        },
        {
            "ISOCode": "BD",
            "ContinentCode": "AS",
            "ID": 23,
            "Title": "Bangladesh"
        },
        {
            "ISOCode": "BB",
            "ContinentCode": "NA",
            "ID": 24,
            "Title": "Barbados"
        },
        {
            "ISOCode": "BY",
            "ContinentCode": "EU",
            "ID": 25,
            "Title": "Belarus"
        },
        {
            "ISOCode": "BE",
            "ContinentCode": "EU",
            "ID": 26,
            "Title": "Belgium"
        },
        {
            "ISOCode": "BZ",
            "ContinentCode": "NA",
            "ID": 27,
            "Title": "Belize"
        },
        {
            "ISOCode": "BJ",
            "ContinentCode": "AF",
            "ID": 28,
            "Title": "Benin"
        },
        {
            "ISOCode": "BM",
            "ContinentCode": "NA",
            "ID": 29,
            "Title": "Bermuda"
        },
        {
            "ISOCode": "BT",
            "ContinentCode": "AS",
            "ID": 30,
            "Title": "Bhutan"
        },
        {
            "ISOCode": "BO",
            "ContinentCode": "SA",
            "ID": 31,
            "Title": "Bolivia, Plurinational State Of"
        },
        {
            "ISOCode": "BQ",
            "ContinentCode": null,
            "ID": 32,
            "Title": "Bonaire, Saint Eustatius And Saba"
        },
        {
            "ISOCode": "BA",
            "ContinentCode": "EU",
            "ID": 33,
            "Title": "Bosnia And Herzegovina"
        },
        {
            "ISOCode": "BW",
            "ContinentCode": "AF",
            "ID": 34,
            "Title": "Botswana"
        },
        {
            "ISOCode": "BV",
            "ContinentCode": "AN",
            "ID": 35,
            "Title": "Bouvet Island"
        },
        {
            "ISOCode": "BR",
            "ContinentCode": "SA",
            "ID": 36,
            "Title": "Brazil"
        },
        {
            "ISOCode": "IO",
            "ContinentCode": "AS",
            "ID": 37,
            "Title": "British Indian Ocean Territory"
        },
        {
            "ISOCode": "BN",
            "ContinentCode": "AS",
            "ID": 38,
            "Title": "Brunei Darussalam"
        },
        {
            "ISOCode": "BG",
            "ContinentCode": "EU",
            "ID": 39,
            "Title": "Bulgaria"
        },
        {
            "ISOCode": "BF",
            "ContinentCode": "AF",
            "ID": 40,
            "Title": "Burkina Faso"
        },
        {
            "ISOCode": "BI",
            "ContinentCode": "AF",
            "ID": 41,
            "Title": "Burundi"
        },
        {
            "ISOCode": "KH",
            "ContinentCode": "AS",
            "ID": 42,
            "Title": "Cambodia"
        },
        {
            "ISOCode": "CM",
            "ContinentCode": "AF",
            "ID": 43,
            "Title": "Cameroon"
        },
        {
            "ISOCode": "CA",
            "ContinentCode": "NA",
            "ID": 44,
            "Title": "Canada"
        },
        {
            "ISOCode": "CV",
            "ContinentCode": "AF",
            "ID": 45,
            "Title": "Cape Verde"
        },
        {
            "ISOCode": "KY",
            "ContinentCode": "NA",
            "ID": 46,
            "Title": "Cayman Islands"
        },
        {
            "ISOCode": "CF",
            "ContinentCode": "AF",
            "ID": 47,
            "Title": "Central African Republic"
        },
        {
            "ISOCode": "TD",
            "ContinentCode": "AF",
            "ID": 48,
            "Title": "Chad"
        },
        {
            "ISOCode": "CL",
            "ContinentCode": "SA",
            "ID": 49,
            "Title": "Chile"
        },
        {
            "ISOCode": "CN",
            "ContinentCode": "AS",
            "ID": 50,
            "Title": "China"
        },
        {
            "ISOCode": "CX",
            "ContinentCode": "AS",
            "ID": 51,
            "Title": "Christmas Island"
        },
        {
            "ISOCode": "CC",
            "ContinentCode": "AS",
            "ID": 52,
            "Title": "Cocos (Keeling) Islands"
        },
        {
            "ISOCode": "CO",
            "ContinentCode": "SA",
            "ID": 53,
            "Title": "Colombia"
        },
        {
            "ISOCode": "KM",
            "ContinentCode": "AF",
            "ID": 54,
            "Title": "Comoros"
        },
        {
            "ISOCode": "CG",
            "ContinentCode": "AF",
            "ID": 55,
            "Title": "Congo"
        },
        {
            "ISOCode": "CD",
            "ContinentCode": "AF",
            "ID": 56,
            "Title": "Congo, Democratic Republic Of The"
        },
        {
            "ISOCode": "CK",
            "ContinentCode": "OC",
            "ID": 57,
            "Title": "Cook Islands"
        },
        {
            "ISOCode": "CR",
            "ContinentCode": "NA",
            "ID": 58,
            "Title": "Costa Rica"
        },
        {
            "ISOCode": "CI",
            "ContinentCode": "AF",
            "ID": 59,
            "Title": "Cote D'Ivoire"
        },
        {
            "ISOCode": "HR",
            "ContinentCode": "EU",
            "ID": 60,
            "Title": "Croatia"
        },
        {
            "ISOCode": "CU",
            "ContinentCode": "NA",
            "ID": 61,
            "Title": "Cuba"
        },
        {
            "ISOCode": "CW",
            "ContinentCode": null,
            "ID": 62,
            "Title": "Curacao"
        },
        {
            "ISOCode": "CY",
            "ContinentCode": "AS",
            "ID": 63,
            "Title": "Cyprus"
        },
        {
            "ISOCode": "CZ",
            "ContinentCode": "EU",
            "ID": 64,
            "Title": "Czech Republic"
        },
        {
            "ISOCode": "DK",
            "ContinentCode": "EU",
            "ID": 65,
            "Title": "Denmark"
        },
        {
            "ISOCode": "DJ",
            "ContinentCode": "AF",
            "ID": 66,
            "Title": "Djibouti"
        },
        {
            "ISOCode": "DM",
            "ContinentCode": "NA",
            "ID": 67,
            "Title": "Dominica"
        },
        {
            "ISOCode": "DO",
            "ContinentCode": "NA",
            "ID": 68,
            "Title": "Dominican Republic"
        },
        {
            "ISOCode": "EC",
            "ContinentCode": "SA",
            "ID": 69,
            "Title": "Ecuador"
        },
        {
            "ISOCode": "EG",
            "ContinentCode": "AF",
            "ID": 70,
            "Title": "Egypt"
        },
        {
            "ISOCode": "SV",
            "ContinentCode": "NA",
            "ID": 71,
            "Title": "El Salvador"
        },
        {
            "ISOCode": "GQ",
            "ContinentCode": "AF",
            "ID": 72,
            "Title": "Equatorial Guinea"
        },
        {
            "ISOCode": "ER",
            "ContinentCode": "AF",
            "ID": 73,
            "Title": "Eritrea"
        },
        {
            "ISOCode": "EE",
            "ContinentCode": "EU",
            "ID": 74,
            "Title": "Estonia"
        },
        {
            "ISOCode": "ET",
            "ContinentCode": "AF",
            "ID": 75,
            "Title": "Ethiopia"
        },
        {
            "ISOCode": "FK",
            "ContinentCode": "SA",
            "ID": 76,
            "Title": "Falkland Islands (Malvinas)"
        },
        {
            "ISOCode": "FO",
            "ContinentCode": "EU",
            "ID": 77,
            "Title": "Faroe Islands"
        },
        {
            "ISOCode": "FJ",
            "ContinentCode": "OC",
            "ID": 78,
            "Title": "Fiji"
        },
        {
            "ISOCode": "FI",
            "ContinentCode": "EU",
            "ID": 79,
            "Title": "Finland"
        },
        {
            "ISOCode": "FR",
            "ContinentCode": "EU",
            "ID": 80,
            "Title": "France"
        },
        {
            "ISOCode": "GF",
            "ContinentCode": "SA",
            "ID": 81,
            "Title": "French Guiana"
        },
        {
            "ISOCode": "PF",
            "ContinentCode": "OC",
            "ID": 82,
            "Title": "French Polynesia"
        },
        {
            "ISOCode": "TF",
            "ContinentCode": "AN",
            "ID": 83,
            "Title": "French Southern Territories"
        },
        {
            "ISOCode": "GA",
            "ContinentCode": "AF",
            "ID": 84,
            "Title": "Gabon"
        },
        {
            "ISOCode": "GM",
            "ContinentCode": "AF",
            "ID": 85,
            "Title": "Gambia"
        },
        {
            "ISOCode": "GE",
            "ContinentCode": "AS",
            "ID": 86,
            "Title": "Georgia"
        },
        {
            "ISOCode": "DE",
            "ContinentCode": "EU",
            "ID": 87,
            "Title": "Germany"
        },
        {
            "ISOCode": "GH",
            "ContinentCode": "AF",
            "ID": 88,
            "Title": "Ghana"
        },
        {
            "ISOCode": "GI",
            "ContinentCode": "EU",
            "ID": 89,
            "Title": "Gibraltar"
        },
        {
            "ISOCode": "GR",
            "ContinentCode": "EU",
            "ID": 90,
            "Title": "Greece"
        },
        {
            "ISOCode": "GL",
            "ContinentCode": "NA",
            "ID": 91,
            "Title": "Greenland"
        },
        {
            "ISOCode": "GD",
            "ContinentCode": "NA",
            "ID": 92,
            "Title": "Grenada"
        },
        {
            "ISOCode": "GP",
            "ContinentCode": "NA",
            "ID": 93,
            "Title": "Guadeloupe"
        },
        {
            "ISOCode": "GU",
            "ContinentCode": "OC",
            "ID": 94,
            "Title": "Guam"
        },
        {
            "ISOCode": "GT",
            "ContinentCode": "NA",
            "ID": 95,
            "Title": "Guatemala"
        },
        {
            "ISOCode": "GG",
            "ContinentCode": "EU",
            "ID": 96,
            "Title": "Guernsey"
        },
        {
            "ISOCode": "GN",
            "ContinentCode": "AF",
            "ID": 97,
            "Title": "Guinea"
        },
        {
            "ISOCode": "GW",
            "ContinentCode": "AF",
            "ID": 98,
            "Title": "Guinea-Bissau"
        },
        {
            "ISOCode": "GY",
            "ContinentCode": "SA",
            "ID": 99,
            "Title": "Guyana"
        },
        {
            "ISOCode": "HT",
            "ContinentCode": "NA",
            "ID": 100,
            "Title": "Haiti"
        },
        {
            "ISOCode": "HM",
            "ContinentCode": "AN",
            "ID": 101,
            "Title": "Heard Island And Mcdonald Islands"
        },
        {
            "ISOCode": "VA",
            "ContinentCode": "EU",
            "ID": 102,
            "Title": "Holy See (Vatican City State)"
        },
        {
            "ISOCode": "HN",
            "ContinentCode": "NA",
            "ID": 103,
            "Title": "Honduras"
        },
        {
            "ISOCode": "HU",
            "ContinentCode": "EU",
            "ID": 104,
            "Title": "Hungary"
        },
        {
            "ISOCode": "IS",
            "ContinentCode": "EU",
            "ID": 105,
            "Title": "Iceland"
        },
        {
            "ISOCode": "IN",
            "ContinentCode": "AS",
            "ID": 106,
            "Title": "India"
        },
        {
            "ISOCode": "ID",
            "ContinentCode": "AS",
            "ID": 107,
            "Title": "Indonesia"
        },
        {
            "ISOCode": "IR",
            "ContinentCode": "AS",
            "ID": 108,
            "Title": "Iran, Islamic Republic Of"
        },
        {
            "ISOCode": "IQ",
            "ContinentCode": "AS",
            "ID": 109,
            "Title": "Iraq"
        },
        {
            "ISOCode": "IM",
            "ContinentCode": "EU",
            "ID": 110,
            "Title": "Isle Of Man"
        },
        {
            "ISOCode": "IL",
            "ContinentCode": "AS",
            "ID": 111,
            "Title": "Israel"
        },
        {
            "ISOCode": "IT",
            "ContinentCode": "EU",
            "ID": 112,
            "Title": "Italy"
        },
        {
            "ISOCode": "JM",
            "ContinentCode": "NA",
            "ID": 113,
            "Title": "Jamaica"
        },
        {
            "ISOCode": "JP",
            "ContinentCode": "AS",
            "ID": 114,
            "Title": "Japan"
        },
        {
            "ISOCode": "JE",
            "ContinentCode": "EU",
            "ID": 115,
            "Title": "Jersey"
        },
        {
            "ISOCode": "JO",
            "ContinentCode": "AS",
            "ID": 116,
            "Title": "Jordan"
        },
        {
            "ISOCode": "KZ",
            "ContinentCode": "AS",
            "ID": 117,
            "Title": "Kazakhstan"
        },
        {
            "ISOCode": "KE",
            "ContinentCode": "AF",
            "ID": 118,
            "Title": "Kenya"
        },
        {
            "ISOCode": "KI",
            "ContinentCode": "OC",
            "ID": 119,
            "Title": "Kiribati"
        },
        {
            "ISOCode": "KP",
            "ContinentCode": "AS",
            "ID": 120,
            "Title": "Korea, Democratic People's Rep."
        },
        {
            "ISOCode": "KR",
            "ContinentCode": "AS",
            "ID": 121,
            "Title": "Korea, Republic Of"
        },
        {
            "ISOCode": "KW",
            "ContinentCode": "AS",
            "ID": 122,
            "Title": "Kuwait"
        },
        {
            "ISOCode": "KG",
            "ContinentCode": "AS",
            "ID": 123,
            "Title": "Kyrgyzstan"
        },
        {
            "ISOCode": "LA",
            "ContinentCode": "AS",
            "ID": 124,
            "Title": "Lao People's Democratic Republic"
        },
        {
            "ISOCode": "LV",
            "ContinentCode": "EU",
            "ID": 125,
            "Title": "Latvia"
        },
        {
            "ISOCode": "LB",
            "ContinentCode": "AS",
            "ID": 126,
            "Title": "Lebanon"
        },
        {
            "ISOCode": "LS",
            "ContinentCode": "AF",
            "ID": 127,
            "Title": "Lesotho"
        },
        {
            "ISOCode": "LR",
            "ContinentCode": "AF",
            "ID": 128,
            "Title": "Liberia"
        },
        {
            "ISOCode": "LY",
            "ContinentCode": "AF",
            "ID": 129,
            "Title": "Libyan Arab Jamahiriya"
        },
        {
            "ISOCode": "LI",
            "ContinentCode": "EU",
            "ID": 130,
            "Title": "Liechtenstein"
        },
        {
            "ISOCode": "LT",
            "ContinentCode": "EU",
            "ID": 131,
            "Title": "Lithuania"
        },
        {
            "ISOCode": "LU",
            "ContinentCode": "EU",
            "ID": 132,
            "Title": "Luxembourg"
        },
        {
            "ISOCode": "MO",
            "ContinentCode": "AS",
            "ID": 133,
            "Title": "Macao"
        },
        {
            "ISOCode": "MK",
            "ContinentCode": "EU",
            "ID": 134,
            "Title": "Macedonia"
        },
        {
            "ISOCode": "MG",
            "ContinentCode": "AF",
            "ID": 135,
            "Title": "Madagascar"
        },
        {
            "ISOCode": "MW",
            "ContinentCode": "AF",
            "ID": 136,
            "Title": "Malawi"
        },
        {
            "ISOCode": "MY",
            "ContinentCode": "AS",
            "ID": 137,
            "Title": "Malaysia"
        },
        {
            "ISOCode": "MV",
            "ContinentCode": "AS",
            "ID": 138,
            "Title": "Maldives"
        },
        {
            "ISOCode": "ML",
            "ContinentCode": "AF",
            "ID": 139,
            "Title": "Mali"
        },
        {
            "ISOCode": "MT",
            "ContinentCode": "EU",
            "ID": 140,
            "Title": "Malta"
        },
        {
            "ISOCode": "MH",
            "ContinentCode": "OC",
            "ID": 141,
            "Title": "Marshall Islands"
        },
        {
            "ISOCode": "MQ",
            "ContinentCode": "NA",
            "ID": 142,
            "Title": "Martinique"
        },
        {
            "ISOCode": "MR",
            "ContinentCode": "AF",
            "ID": 143,
            "Title": "Mauritania"
        },
        {
            "ISOCode": "MU",
            "ContinentCode": "AF",
            "ID": 144,
            "Title": "Mauritius"
        },
        {
            "ISOCode": "YT",
            "ContinentCode": "AF",
            "ID": 145,
            "Title": "Mayotte"
        },
        {
            "ISOCode": "MX",
            "ContinentCode": "NA",
            "ID": 146,
            "Title": "Mexico"
        },
        {
            "ISOCode": "FM",
            "ContinentCode": "OC",
            "ID": 147,
            "Title": "Micronesia, Federated States Of"
        },
        {
            "ISOCode": "MD",
            "ContinentCode": "EU",
            "ID": 148,
            "Title": "Moldova, Republic Of"
        },
        {
            "ISOCode": "MC",
            "ContinentCode": "EU",
            "ID": 149,
            "Title": "Monaco"
        },
        {
            "ISOCode": "MN",
            "ContinentCode": "AS",
            "ID": 150,
            "Title": "Mongolia"
        },
        {
            "ISOCode": "ME",
            "ContinentCode": "EU",
            "ID": 151,
            "Title": "Montenegro"
        },
        {
            "ISOCode": "MS",
            "ContinentCode": "NA",
            "ID": 152,
            "Title": "Montserrat"
        },
        {
            "ISOCode": "MA",
            "ContinentCode": "AF",
            "ID": 153,
            "Title": "Morocco"
        },
        {
            "ISOCode": "MZ",
            "ContinentCode": "AF",
            "ID": 154,
            "Title": "Mozambique"
        },
        {
            "ISOCode": "MM",
            "ContinentCode": "AS",
            "ID": 155,
            "Title": "Myanmar"
        },
        {
            "ISOCode": "NA",
            "ContinentCode": "AF",
            "ID": 156,
            "Title": "Namibia"
        },
        {
            "ISOCode": "NR",
            "ContinentCode": "OC",
            "ID": 157,
            "Title": "Nauru"
        },
        {
            "ISOCode": "NP",
            "ContinentCode": "AS",
            "ID": 158,
            "Title": "Nepal"
        },
        {
            "ISOCode": "NL",
            "ContinentCode": "EU",
            "ID": 159,
            "Title": "Netherlands"
        },
        {
            "ISOCode": "NC",
            "ContinentCode": "OC",
            "ID": 160,
            "Title": "New Caledonia"
        },
        {
            "ISOCode": "NZ",
            "ContinentCode": "OC",
            "ID": 161,
            "Title": "New Zealand"
        },
        {
            "ISOCode": "NI",
            "ContinentCode": "NA",
            "ID": 162,
            "Title": "Nicaragua"
        },
        {
            "ISOCode": "NE",
            "ContinentCode": "AF",
            "ID": 163,
            "Title": "Niger"
        },
        {
            "ISOCode": "NG",
            "ContinentCode": "AF",
            "ID": 164,
            "Title": "Nigeria"
        },
        {
            "ISOCode": "NU",
            "ContinentCode": "OC",
            "ID": 165,
            "Title": "Niue"
        },
        {
            "ISOCode": "NF",
            "ContinentCode": "OC",
            "ID": 166,
            "Title": "Norfolk Island"
        },
        {
            "ISOCode": "MP",
            "ContinentCode": "OC",
            "ID": 167,
            "Title": "Northern Mariana Islands"
        },
        {
            "ISOCode": "NO",
            "ContinentCode": "EU",
            "ID": 168,
            "Title": "Norway"
        },
        {
            "ISOCode": "OM",
            "ContinentCode": "AS",
            "ID": 169,
            "Title": "Oman"
        },
        {
            "ISOCode": "PK",
            "ContinentCode": "AS",
            "ID": 170,
            "Title": "Pakistan"
        },
        {
            "ISOCode": "PW",
            "ContinentCode": "OC",
            "ID": 171,
            "Title": "Palau"
        },
        {
            "ISOCode": "PS",
            "ContinentCode": "AS",
            "ID": 172,
            "Title": "Palestinian Territory, Occupied"
        },
        {
            "ISOCode": "PA",
            "ContinentCode": "NA",
            "ID": 173,
            "Title": "Panama"
        },
        {
            "ISOCode": "PG",
            "ContinentCode": "OC",
            "ID": 174,
            "Title": "Papua New Guinea"
        },
        {
            "ISOCode": "PY",
            "ContinentCode": "SA",
            "ID": 175,
            "Title": "Paraguay"
        },
        {
            "ISOCode": "PE",
            "ContinentCode": "SA",
            "ID": 176,
            "Title": "Peru"
        },
        {
            "ISOCode": "PH",
            "ContinentCode": "AS",
            "ID": 177,
            "Title": "Philippines"
        },
        {
            "ISOCode": "PN",
            "ContinentCode": "OC",
            "ID": 178,
            "Title": "Pitcairn"
        },
        {
            "ISOCode": "PL",
            "ContinentCode": "EU",
            "ID": 179,
            "Title": "Poland"
        },
        {
            "ISOCode": "PT",
            "ContinentCode": "EU",
            "ID": 180,
            "Title": "Portugal"
        },
        {
            "ISOCode": "PR",
            "ContinentCode": "NA",
            "ID": 181,
            "Title": "Puerto Rico"
        },
        {
            "ISOCode": "QA",
            "ContinentCode": "AS",
            "ID": 182,
            "Title": "Qatar"
        },
        {
            "ISOCode": "RE",
            "ContinentCode": "AF",
            "ID": 183,
            "Title": "Reunion"
        },
        {
            "ISOCode": "RO",
            "ContinentCode": "EU",
            "ID": 184,
            "Title": "Romania"
        },
        {
            "ISOCode": "RU",
            "ContinentCode": "EU",
            "ID": 185,
            "Title": "Russian Federation"
        },
        {
            "ISOCode": "RW",
            "ContinentCode": "AF",
            "ID": 186,
            "Title": "Rwanda"
        },
        {
            "ISOCode": "BL",
            "ContinentCode": "NA",
            "ID": 187,
            "Title": "Saint Barthelemy"
        },
        {
            "ISOCode": "SH",
            "ContinentCode": "AF",
            "ID": 188,
            "Title": "Saint Helena"
        },
        {
            "ISOCode": "KN",
            "ContinentCode": "NA",
            "ID": 189,
            "Title": "Saint Kitts And Nevis"
        },
        {
            "ISOCode": "LC",
            "ContinentCode": "NA",
            "ID": 190,
            "Title": "Saint Lucia"
        },
        {
            "ISOCode": "MF",
            "ContinentCode": "NA",
            "ID": 191,
            "Title": "Saint Martin (French Part)"
        },
        {
            "ISOCode": "PM",
            "ContinentCode": "NA",
            "ID": 192,
            "Title": "Saint Pierre And Miquelon"
        },
        {
            "ISOCode": "VC",
            "ContinentCode": "NA",
            "ID": 193,
            "Title": "Saint Vincent And The Grenadines"
        },
        {
            "ISOCode": "WS",
            "ContinentCode": "OC",
            "ID": 194,
            "Title": "Samoa"
        },
        {
            "ISOCode": "SM",
            "ContinentCode": "EU",
            "ID": 195,
            "Title": "San Marino"
        },
        {
            "ISOCode": "ST",
            "ContinentCode": "AF",
            "ID": 196,
            "Title": "Sao Tome And Principe"
        },
        {
            "ISOCode": "SA",
            "ContinentCode": "AS",
            "ID": 197,
            "Title": "Saudi Arabia"
        },
        {
            "ISOCode": "SN",
            "ContinentCode": "AF",
            "ID": 198,
            "Title": "Senegal"
        },
        {
            "ISOCode": "RS",
            "ContinentCode": "EU",
            "ID": 199,
            "Title": "Serbia"
        },
        {
            "ISOCode": "SC",
            "ContinentCode": "AF",
            "ID": 200,
            "Title": "Seychelles"
        },
        {
            "ISOCode": "SL",
            "ContinentCode": "AF",
            "ID": 201,
            "Title": "Sierra Leone"
        },
        {
            "ISOCode": "SG",
            "ContinentCode": "AS",
            "ID": 202,
            "Title": "Singapore"
        },
        {
            "ISOCode": "SX",
            "ContinentCode": null,
            "ID": 203,
            "Title": "Sint Maarten (Dutch Part)"
        },
        {
            "ISOCode": "SK",
            "ContinentCode": "EU",
            "ID": 204,
            "Title": "Slovakia"
        },
        {
            "ISOCode": "SI",
            "ContinentCode": "EU",
            "ID": 205,
            "Title": "Slovenia"
        },
        {
            "ISOCode": "SB",
            "ContinentCode": "OC",
            "ID": 206,
            "Title": "Solomon Islands"
        },
        {
            "ISOCode": "SO",
            "ContinentCode": "AF",
            "ID": 207,
            "Title": "Somalia"
        },
        {
            "ISOCode": "ZA",
            "ContinentCode": "AF",
            "ID": 208,
            "Title": "South Africa"
        },
        {
            "ISOCode": "GS",
            "ContinentCode": "AN",
            "ID": 209,
            "Title": "South Georgia"
        },
        {
            "ISOCode": "ES",
            "ContinentCode": "EU",
            "ID": 210,
            "Title": "Spain"
        },
        {
            "ISOCode": "LK",
            "ContinentCode": "AS",
            "ID": 211,
            "Title": "Sri Lanka"
        },
        {
            "ISOCode": "SD",
            "ContinentCode": "AF",
            "ID": 212,
            "Title": "Sudan"
        },
        {
            "ISOCode": "SR",
            "ContinentCode": "SA",
            "ID": 213,
            "Title": "Suriname"
        },
        {
            "ISOCode": "SJ",
            "ContinentCode": "EU",
            "ID": 214,
            "Title": "Svalbard And Jan Mayen"
        },
        {
            "ISOCode": "SZ",
            "ContinentCode": "AF",
            "ID": 215,
            "Title": "Swaziland"
        },
        {
            "ISOCode": "SE",
            "ContinentCode": "EU",
            "ID": 216,
            "Title": "Sweden"
        },
        {
            "ISOCode": "CH",
            "ContinentCode": "EU",
            "ID": 217,
            "Title": "Switzerland"
        },
        {
            "ISOCode": "SY",
            "ContinentCode": "AS",
            "ID": 218,
            "Title": "Syrian Arab Republic"
        },
        {
            "ISOCode": "TW",
            "ContinentCode": "AS",
            "ID": 219,
            "Title": "Taiwan, Province Of China"
        },
        {
            "ISOCode": "TJ",
            "ContinentCode": "AS",
            "ID": 220,
            "Title": "Tajikistan"
        },
        {
            "ISOCode": "TZ",
            "ContinentCode": "AF",
            "ID": 221,
            "Title": "Tanzania, United Republic Of"
        },
        {
            "ISOCode": "TH",
            "ContinentCode": "AS",
            "ID": 222,
            "Title": "Thailand"
        },
        {
            "ISOCode": "TL",
            "ContinentCode": "AS",
            "ID": 223,
            "Title": "Timor-Leste"
        },
        {
            "ISOCode": "TG",
            "ContinentCode": "AF",
            "ID": 224,
            "Title": "Togo"
        },
        {
            "ISOCode": "TK",
            "ContinentCode": "OC",
            "ID": 225,
            "Title": "Tokelau"
        },
        {
            "ISOCode": "TO",
            "ContinentCode": "OC",
            "ID": 226,
            "Title": "Tonga"
        },
        {
            "ISOCode": "TT",
            "ContinentCode": "NA",
            "ID": 227,
            "Title": "Trinidad And Tobago"
        },
        {
            "ISOCode": "TN",
            "ContinentCode": "AF",
            "ID": 228,
            "Title": "Tunisia"
        },
        {
            "ISOCode": "TR",
            "ContinentCode": "EU",
            "ID": 229,
            "Title": "Turkey"
        },
        {
            "ISOCode": "TM",
            "ContinentCode": "AS",
            "ID": 230,
            "Title": "Turkmenistan"
        },
        {
            "ISOCode": "TC",
            "ContinentCode": "NA",
            "ID": 231,
            "Title": "Turks And Caicos Islands"
        },
        {
            "ISOCode": "TV",
            "ContinentCode": "OC",
            "ID": 232,
            "Title": "Tuvalu"
        },
        {
            "ISOCode": "UG",
            "ContinentCode": "AF",
            "ID": 233,
            "Title": "Uganda"
        },
        {
            "ISOCode": "UA",
            "ContinentCode": "EU",
            "ID": 234,
            "Title": "Ukraine"
        },
        {
            "ISOCode": "AE",
            "ContinentCode": "AS",
            "ID": 235,
            "Title": "United Arab Emirates"
        },
        {
            "ISOCode": "UM",
            "ContinentCode": "OC",
            "ID": 236,
            "Title": "United States Minor Outlying Islands"
        },
        {
            "ISOCode": "UY",
            "ContinentCode": "SA",
            "ID": 237,
            "Title": "Uruguay"
        },
        {
            "ISOCode": "UZ",
            "ContinentCode": "AS",
            "ID": 238,
            "Title": "Uzbekistan"
        },
        {
            "ISOCode": "VU",
            "ContinentCode": "OC",
            "ID": 239,
            "Title": "Vanuatu"
        },
        {
            "ISOCode": "VE",
            "ContinentCode": "SA",
            "ID": 240,
            "Title": "Venezuela, Bolivarian Republic Of"
        },
        {
            "ISOCode": "VN",
            "ContinentCode": "AS",
            "ID": 241,
            "Title": "Viet Nam"
        },
        {
            "ISOCode": "VG",
            "ContinentCode": "NA",
            "ID": 242,
            "Title": "Virgin Islands, British"
        },
        {
            "ISOCode": "VI",
            "ContinentCode": "NA",
            "ID": 243,
            "Title": "Virgin Islands, U.S."
        },
        {
            "ISOCode": "WF",
            "ContinentCode": "OC",
            "ID": 244,
            "Title": "Wallis And Futuna"
        },
        {
            "ISOCode": "EH",
            "ContinentCode": "AF",
            "ID": 245,
            "Title": "Western Sahara"
        },
        {
            "ISOCode": "YE",
            "ContinentCode": "AS",
            "ID": 246,
            "Title": "Yemen"
        },
        {
            "ISOCode": "ZM",
            "ContinentCode": "AF",
            "ID": 247,
            "Title": "Zambia"
        },
        {
            "ISOCode": "ZW",
            "ContinentCode": "AF",
            "ID": 248,
            "Title": "Zimbabwe"
        },
        {
            "ISOCode": "SS",
            "ContinentCode": "AF",
            "ID": 249,
            "Title": "South Sudan"
        },
        {
            "ISOCode": "XK",
            "ContinentCode": "EU",
            "ID": 250,
            "Title": "Kosovo"
        }
    ],
    "DataProviders": [
        {
            "WebsiteURL": "http://openchargemap.org",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 1,
                "Title": "Manual Data Entry"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)",
            "DateLastImported": null,
            "ID": 1,
            "Title": "Open Charge Map Contributors"
        },
        {
            "WebsiteURL": "http://www.afdc.energy.gov/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "This data is provided by the National Renewable Energy Laboratory (\"NREL\"), which is operated by the Alliance for Sustainable Energy, LLC (\"Alliance\"), for the U.S. Department of Energy (\"DOE\"), and may be used for any purpose whatsoever.",
            "DateLastImported": "2024-02-20T10:59:44.963Z",
            "ID": 2,
            "Title": "afdc.energy.gov"
        },
        {
            "WebsiteURL": "http://www.mobie.pt",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Public Data redistributed by agreement",
            "DateLastImported": "2023-12-04T08:43:37.94Z",
            "ID": 7,
            "Title": "Mobie.pt"
        },
        {
            "WebsiteURL": "http://e-tankstellen-finder.com/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 10,
                "Title": "Manual (Bulk Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 8,
            "Title": "ev-charging.com"
        },
        {
            "WebsiteURL": "http://www.uppladdning.nu",
            "Comments": "This data provider has explicitly asked that OCM do not import their data. (Ref: Nikolay  Shishkov)",
            "DataProviderStatusType": {
                "IsProviderEnabled": false,
                "ID": 1000,
                "Title": "Delisted - Data Use Permission Denied"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 13,
            "Title": "www.uppladdning.nu"
        },
        {
            "WebsiteURL": "http://www.e-laad.nl",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 10,
                "Title": "Manual (Bulk Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 14,
            "Title": "e-Laad"
        },
        {
            "WebsiteURL": "http://www.carstations.com",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": false,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": "2017-11-04T14:07:02.687Z",
            "ID": 15,
            "Title": "CarStations.com"
        },
        {
            "WebsiteURL": "http://www.blinknetwork.com",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 17,
            "Title": "BlinkNetwork.com"
        },
        {
            "WebsiteURL": "http://chargepoints.dft.gov.uk",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Contains public sector information licensed under the Open Government Licence v2.0.",
            "DateLastImported": "2023-12-07T08:14:38.417Z",
            "ID": 18,
            "Title": "UK National Charge Point Registry"
        },
        {
            "WebsiteURL": "https://nobil.no/",
            "Comments": "NOBIL is an open, publicly owned charging point database for the Nordic countries.",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "NOBIL by Enova is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License.",
            "DateLastImported": "2024-02-20T07:44:16.16Z",
            "ID": 19,
            "Title": "NOBIL"
        },
        {
            "WebsiteURL": "http://www.chargepoint.net/",
            "Comments": "Coulomb Chargepoint Network",
            "DataProviderStatusType": {
                "IsProviderEnabled": false,
                "ID": 1001,
                "Title": "Delisted - Not Used"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 20,
            "Title": "Chargepoint.net"
        },
        {
            "WebsiteURL": "https://www.rwe-mobility.com/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 21,
            "Title": "RWE Mobility"
        },
        {
            "WebsiteURL": "http://www.chademo.com",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 100,
                "Title": "Not Currently Used/Imported"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": false,
            "IsApprovedImport": false,
            "License": null,
            "DateLastImported": null,
            "ID": 22,
            "Title": "CHAdeMO.com"
        },
        {
            "WebsiteURL": "http://www.esb.ie/electric-cars/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": false,
            "IsApprovedImport": false,
            "License": null,
            "DateLastImported": "2016-05-29T07:34:20.087Z",
            "ID": 23,
            "Title": "ESB eCars"
        },
        {
            "WebsiteURL": "http://www.addenergietechnologies.com/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "http://creativecommons.org/licenses/by/3.0",
            "DateLastImported": "2019-06-26T09:00:39.553Z",
            "ID": 24,
            "Title": "AddÉnergie Technologies Inc."
        },
        {
            "WebsiteURL": "http://icaen.gencat.cat/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "General public data",
            "DateLastImported": "2016-03-03T14:18:07.287Z",
            "ID": 25,
            "Title": "Catalan Energy Institute (ICAEN)"
        },
        {
            "WebsiteURL": "http://www.oplaadpalen.nl/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under Attribution-NonCommercial-ShareAlike 3.0 : http://creativecommons.org/licenses/by-nc-sa/3.0/",
            "DateLastImported": "2016-06-04T03:04:53.05Z",
            "ID": 26,
            "Title": "Oplaadpalen.nl"
        },
        {
            "WebsiteURL": "https://www.placetoplug.com",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": false,
            "IsApprovedImport": false,
            "License": null,
            "DateLastImported": null,
            "ID": 27,
            "Title": "Place To Plug"
        },
        {
            "WebsiteURL": "https://www.data.gouv.fr/fr/datasets/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Open License: https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf",
            "DateLastImported": "2022-08-23T10:39:51.413Z",
            "ID": 28,
            "Title": "data.gouv.fr"
        },
        {
            "WebsiteURL": "https://bundesnetzagentur.de",
            "Comments": null,
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 20,
                "Title": "Automated Import"
            },
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Provided by Bundesnetzagentur.de under the CC-BY 4.0 license",
            "DateLastImported": "2021-07-12T02:21:34.507Z",
            "ID": 29,
            "Title": "Bundesnetzagentur.de"
        },
        {
            "WebsiteURL": "https://go-evio.com/",
            "Comments": "OCPI with Data Sharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)",
            "DateLastImported": "2024-06-06T09:01:41.273Z",
            "ID": 30,
            "Title": "EVIO"
        },
        {
            "WebsiteURL": "https://www.sitronics-electro.com",
            "Comments": "OCPI with Data Sharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under CC0  by data sharing agreement",
            "DateLastImported": null,
            "ID": 31,
            "Title": "Sitronics"
        },
        {
            "WebsiteURL": "https://ev.lakd.lt/en/open_source",
            "Comments": "OCPI with Data Sharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)",
            "DateLastImported": "2023-07-04T00:00:00Z",
            "ID": 32,
            "Title": "Lithuanian Road Administration"
        },
        {
            "WebsiteURL": "https://gaiacharge.com",
            "Comments": "OCPI with Data Sharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under CC0  by data sharing agreement",
            "DateLastImported": "2024-06-06T09:28:30.75Z",
            "ID": 33,
            "Title": "Gaia Green Tech"
        },
        {
            "WebsiteURL": "https://toger.co",
            "Comments": "OCPI with Datasharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under CC0  by data sharing agreement",
            "DateLastImported": "2024-06-06T09:19:18.263Z",
            "ID": 34,
            "Title": "Toger.co"
        },
        {
            "WebsiteURL": "https://electriceratechnologies.com/",
            "Comments": "OCPI with Data Sharing Agreement",
            "DataProviderStatusType": {
                "IsProviderEnabled": true,
                "ID": 30,
                "Title": "Partially Automated (Ad-Hoc Import)"
            },
            "IsRestrictedEdit": true,
            "IsOpenDataLicensed": true,
            "IsApprovedImport": true,
            "License": "Licensed under CC0 by data sharing agreement",
            "DateLastImported": "2024-06-06T09:08:21.427Z",
            "ID": 35,
            "Title": "Electric Era"
        }
    ],
    "Operators": [
        {
            "WebsiteURL": null,
            "Comments": "For use when the operator of the equipment is a single business owner connected to the location and equipment is not part of a larger network",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 45,
            "Title": "(Business Owner at Location)"
        },
        {
            "WebsiteURL": null,
            "Comments": "For use when the operator is a home owner or private individual making their own facilities available to the public",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": true,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 44,
            "Title": "(Private Residence/Individual)"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 1,
            "Title": "(Unknown Operator)"
        },
        {
            "WebsiteURL": "https://www.7-eleven.com/7charge",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3697,
            "Title": "7-Charge (7-Eleven)"
        },
        {
            "WebsiteURL": "https://a2a.it/casa/emoving",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3728,
            "Title": "a2a emoving (Italia)"
        },
        {
            "WebsiteURL": "https://www.aae.at/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3333,
            "Title": "AAE"
        },
        {
            "WebsiteURL": "https://www.abcasemat.fi/fi/abc-lataus/sahkoauton-lataus",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3506,
            "Title": "ABC Lataus"
        },
        {
            "WebsiteURL": "https://recarga.acciona.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3459,
            "Title": "ACCIONA - Cargacoches"
        },
        {
            "WebsiteURL": "https://www.acea.it/e-mobility",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3525,
            "Title": "Acea"
        },
        {
            "WebsiteURL": "http://www.avinc.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 26,
            "Title": "AeroVironment"
        },
        {
            "WebsiteURL": "https://www.afconev.co.il/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3435,
            "Title": "Afcon (Israel)"
        },
        {
            "WebsiteURL": "https://www.agsm.it/I-servizi/Electrify-Verona",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 118,
            "Title": "AGSM Electrify Verona"
        },
        {
            "WebsiteURL": "https://www.aimove.it",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3463,
            "Title": "AIMove"
        },
        {
            "WebsiteURL": "https://www.aldi-sued.de/de/nachhaltigkeit/neuigkeiten/e-ladestationen.html",
            "Comments": null,
            "PhonePrimaryContact": "08008002534",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3464,
            "Title": "ALDI SÜD"
        },
        {
            "WebsiteURL": "https://www.alfapower.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3326,
            "Title": "Alfapower (UK)"
        },
        {
            "WebsiteURL": "http://www.alfen.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 180,
            "Title": "Alfen"
        },
        {
            "WebsiteURL": "https://alizecharge.com/en/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3336,
            "Title": "Alizé"
        },
        {
            "WebsiteURL": "https://alizecharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3543,
            "Title": "Alizé"
        },
        {
            "WebsiteURL": "https://alizecharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3410,
            "Title": "Alizé Liberté"
        },
        {
            "WebsiteURL": "https://www.allego.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@allego.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 103,
            "Title": "Allego BV"
        },
        {
            "WebsiteURL": "http://www.alterbase86.soregies.fr/portal/#/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service-recharge@soregies.fr",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3383,
            "Title": "AlterBase - Sorégies (FR)"
        },
        {
            "WebsiteURL": "https://www.amb.cat/en/web/mobilitat/mobilitat-sostenible/electrolineres",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3305,
            "Title": "AMB (Àrea metropolitana de Barcelona)"
        },
        {
            "WebsiteURL": "https://ambuenergy.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-416-408-0623",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ambuenergy.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3748,
            "Title": "AmbuEnergy"
        },
        {
            "WebsiteURL": "http://nou.amersam.cat/",
            "Comments": null,
            "PhonePrimaryContact": " +34 977 300 006",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "amersam@amersam.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 212,
            "Title": "Amersam"
        },
        {
            "WebsiteURL": "https://www.amperio.eu/",
            "Comments": "amperio GmbH DE*AMP",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3680,
            "Title": "Amperio (DE)"
        },
        {
            "WebsiteURL": "https://ampcharge.ampol.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3625,
            "Title": "Ampol AmpCharge"
        },
        {
            "WebsiteURL": "https://ampup.io/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3619,
            "Title": "AmpUp"
        },
        {
            "WebsiteURL": "https://www.apcoaconnect.com/",
            "Comments": "Car park operator",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3637,
            "Title": "APCOA Parking"
        },
        {
            "WebsiteURL": "https://www.applegreenelectric.com/",
            "Comments": "IE*APG,GB*APG",
            "PhonePrimaryContact": "+353 1 512 4800",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3516,
            "Title": "Applegreen Electric"
        },
        {
            "WebsiteURL": "https://www.aral.de/de/global/retail/pulse.html",
            "Comments": "BP's brand name in Germany",
            "PhonePrimaryContact": "0049 234 315-0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "nfo@aral.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3455,
            "Title": "Aral pulse"
        },
        {
            "WebsiteURL": "https://www.astorsarj.com.tr/",
            "Comments": null,
            "PhonePrimaryContact": "+90 850 400 00 00 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3753,
            "Title": "Astor Şarj (TR)"
        },
        {
            "WebsiteURL": "https://www.atherenergy.com/grid",
            "Comments": "Scooter manufacturer that provides a charging network for their customers, with 15A domestic connectors for other EVs",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3549,
            "Title": "Ather Grid Point (India)"
        },
        {
            "WebsiteURL": "https://atlante.energy/",
            "Comments": "FR*ATL",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3588,
            "Title": "Atlante"
        },
        {
            "WebsiteURL": "https://www.atmevs.com.br/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "manoel@atmsistema.com.br",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3569,
            "Title": "ATM.EV"
        },
        {
            "WebsiteURL": "http://www.auto-bleue.org/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 56,
            "Title": "Auto Bleue"
        },
        {
            "WebsiteURL": "https://www.autoenterprise.com.ua/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3362,
            "Title": "Autoenterprise / АвтоЭнтерпрайз"
        },
        {
            "WebsiteURL": "https://www.autolib.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 53,
            "Title": "Autolib (Paris)"
        },
        {
            "WebsiteURL": "http://autopildyk.lt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "pagalba@autopildyk.lt",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3284,
            "Title": "autoPilDYK"
        },
        {
            "WebsiteURL": "https://www.avacon.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 5351 1230",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@avacon.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3303,
            "Title": "Avacon"
        },
        {
            "WebsiteURL": null,
            "Comments": "Obsolete inductive paddle charging",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 43,
            "Title": "AVCON"
        },
        {
            "WebsiteURL": "https://avia-e-mobilite.com/",
            "Comments": null,
            "PhonePrimaryContact": "+33 9 72 54 42 05",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@avia-e-mobilite.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3652,
            "Title": "Avia (FR)"
        },
        {
            "WebsiteURL": "https://www.axpo.com/axpo/it/it/chi-siamo/localita-europa/sedi-italia.html",
            "Comments": "IT*AXP",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3352,
            "Title": "Axpo Energy Solutions Italia"
        },
        {
            "WebsiteURL": "https://azra.ca/en/",
            "Comments": null,
            "PhonePrimaryContact": "450 477-8008",
            "PhoneSecondaryContact": "1-844-279-2972",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@reseauazra.com",
            "FaultReportEmail": "info@reseauazra.com",
            "IsRestrictedEdit": false,
            "ID": 186,
            "Title": "Azra Network"
        },
        {
            "WebsiteURL": "https://www.aparcamentsbsm.cat/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3577,
            "Title": "B:SM (ES)"
        },
        {
            "WebsiteURL": "https://www.badenova.de/web/Privatkunden/E-Mobilit%C3%A4t/%C3%96ffentliches-Laden/index-2.jsp",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "e-mobility@badenova.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3292,
            "Title": "Badenova (DE)"
        },
        {
            "WebsiteURL": "https://www.barterenergy.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3552,
            "Title": "BarterGo (ES)"
        },
        {
            "WebsiteURL": "https://ev.bchydro.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3385,
            "Title": "BC Hydro"
        },
        {
            "WebsiteURL": "https://www.bec.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3327,
            "Title": "Be Charge (Italy)"
        },
        {
            "WebsiteURL": "http://www.be-emobil.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 30 20847590",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "dialog@be-emobil.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 214,
            "Title": "be emobil"
        },
        {
            "WebsiteURL": "https://has-to-be.com",
            "Comments": "also known as has.to.be",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3261,
            "Title": "Be Energised (has-to-be)"
        },
        {
            "WebsiteURL": "https://be-ev.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "0800 917 3208",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@be-ev.co.uk",
            "FaultReportEmail": "support@be-ev.co.uk",
            "IsRestrictedEdit": false,
            "ID": 3481,
            "Title": "Be.EV"
        },
        {
            "WebsiteURL": "http://www.becharged.eu/",
            "Comments": null,
            "PhonePrimaryContact": "+32 (0)9 395.05.93",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@becharged.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 94,
            "Title": "BeCharged"
        },
        {
            "WebsiteURL": "http://belib.paris/",
            "Comments": null,
            "PhonePrimaryContact": "09.69.322.500 (7j/7 de 7h à 22h)",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@sodetrel.fr",
            "FaultReportEmail": "sav@sodetrel.fr",
            "IsRestrictedEdit": false,
            "ID": 1235,
            "Title": "Belib’"
        },
        {
            "WebsiteURL": "https://www.believ.com/",
            "Comments": "GB*LCL",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3511,
            "Title": "Believ"
        },
        {
            "WebsiteURL": "http://www.belorusneft.by/beloil-map/?lang=en",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3268,
            "Title": "Belorusneft"
        },
        {
            "WebsiteURL": "https://www.bigge-energie.de/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3443,
            "Title": "BIGGIE Energie"
        },
        {
            "WebsiteURL": "https://bladecocharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@bladeco.com.tr",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3736,
            "Title": "BladecoCharge (TR)"
        },
        {
            "WebsiteURL": "https://blinkcharging.com/",
            "Comments": null,
            "PhonePrimaryContact": "888.998.BLINK (2546)",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 9,
            "Title": "Blink Charging"
        },
        {
            "WebsiteURL": "https://blinkcharging.gr/en/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3426,
            "Title": "Blink Charging (Europe)"
        },
        {
            "WebsiteURL": "https://blinkcharging.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3737,
            "Title": "Blink Charging (UK)"
        },
        {
            "WebsiteURL": "http://www.bluecorner.be/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 36,
            "Title": "Blue Corner (Belgium)"
        },
        {
            "WebsiteURL": "https://www.bluemarblecharging.com/",
            "Comments": null,
            "PhonePrimaryContact": "+31 850186990",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": "Info@bluemarblecharging.com",
            "IsRestrictedEdit": false,
            "ID": 3441,
            "Title": "Blue Marble Charging"
        },
        {
            "WebsiteURL": "https://www.bluetorino.eu/ricarica",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3331,
            "Title": "BLUETORINO"
        },
        {
            "WebsiteURL": "https://www.bp.com/en_nz/new-zealand/home/products-and-services/bpevcharging.html",
            "Comments": null,
            "PhonePrimaryContact": "0800 002 788",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3593,
            "Title": "BP EV Charging (NZ)"
        },
        {
            "WebsiteURL": "https://www.bp.com/en_au/australia/home/products-services/bppulse.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3659,
            "Title": "BP Pulse (AU)"
        },
        {
            "WebsiteURL": "https://www.bppulse.co.uk/",
            "Comments": "Formerly known as Polar Network, or BP Chargemaster",
            "PhonePrimaryContact": "01582 400331",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 32,
            "Title": "BP Pulse (UK)"
        },
        {
            "WebsiteURL": "https://www.bp.com/en_us/united-states/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3788,
            "Title": "BP Pulse (US)"
        },
        {
            "WebsiteURL": "https://brsupercarga.com/",
            "Comments": null,
            "PhonePrimaryContact": "+55 85 994028343",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3726,
            "Title": "BR Super Carga"
        },
        {
            "WebsiteURL": "http://www.bs-energy.de/engagement/umwelt/elektromobilitaet/elektrotankstellen/",
            "Comments": null,
            "PhonePrimaryContact": " 0531 3838000",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "energieberatung@bs-energy.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 129,
            "Title": "BS Energie"
        },
        {
            "WebsiteURL": "https://www.bump-charge.com/",
            "Comments": null,
            "PhonePrimaryContact": "+33 1 76 40 12 80",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3661,
            "Title": "Bump (FR)"
        },
        {
            "WebsiteURL": "https://dot.ca.gov/news-releases/news-release-2021-001",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3729,
            "Title": "Caltrans (USA)"
        },
        {
            "WebsiteURL": "https://eletropostocelesc.com.br/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3567,
            "Title": "Celesc"
        },
        {
            "WebsiteURL": "https://www.celsia.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3304,
            "Title": "Celsia"
        },
        {
            "WebsiteURL": "https://www.cepsa.es/",
            "Comments": "App: CEPSA Gow",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3584,
            "Title": "CEPSA (ES)"
        },
        {
            "WebsiteURL": "http://www.elektromobilita.cz/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 115,
            "Title": "ČEZ"
        },
        {
            "WebsiteURL": "https://char.gy",
            "Comments": "different organisation to similarly named organisation in Luxembourg",
            "PhonePrimaryContact": "0800 086 9606",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3345,
            "Title": "Char.gy"
        },
        {
            "WebsiteURL": "http://www.fortum.no/hurtigladere",
            "Comments": null,
            "PhonePrimaryContact": "22 55 54 24",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "chargedrive.no@fortum.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 202,
            "Title": "Charge & Drive (Fortum - NO)"
        },
        {
            "WebsiteURL": "https://chargeandfuel.vwfs.com/",
            "Comments": null,
            "PhonePrimaryContact": "+49 531 212-03",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "tankkarten@vwfs.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 215,
            "Title": "Charge & Fuel"
        },
        {
            "WebsiteURL": "https://chargemyride.mt/",
            "Comments": null,
            "PhonePrimaryContact": "+356 2779 9299",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3678,
            "Title": "Charge My Ride (Malta)"
        },
        {
            "WebsiteURL": "https://chargemystreet.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "+44 1524 881227",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3687,
            "Title": "Charge My Street (UK)"
        },
        {
            "WebsiteURL": "http://www.chargeyourcar.org.uk/",
            "Comments": null,
            "PhonePrimaryContact": "0191 26 50 500",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "admin@chargeyourcar.org.uk",
            "FaultReportEmail": "admin@chargeyourcar.org.uk",
            "IsRestrictedEdit": false,
            "ID": 20,
            "Title": "Charge Your Car"
        },
        {
            "WebsiteURL": "https://chargebay.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3575,
            "Title": "Chargebay"
        },
        {
            "WebsiteURL": "https://www.chargecloud.de/",
            "Comments": "DE*136,DE*CHC",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3758,
            "Title": "Chargecloud (DE)"
        },
        {
            "WebsiteURL": "https://chargefox.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3339,
            "Title": "Chargefox"
        },
        {
            "WebsiteURL": "https://chargegrid.in/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "tech.support@magentapower.in",
            "FaultReportEmail": "tech.support@magentapower.in",
            "IsRestrictedEdit": false,
            "ID": 3374,
            "Title": "ChargeGrid"
        },
        {
            "WebsiteURL": "https://chargehub.solutions",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3775,
            "Title": "Chargehub"
        },
        {
            "WebsiteURL": "http://www.chargeit-mobility.com/",
            "Comments": null,
            "PhonePrimaryContact": "+49 9321 268 -0700",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@chargeit-mobility.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 101,
            "Title": "ChargeIT mobility"
        },
        {
            "WebsiteURL": "https://www.chargelab.co/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3621,
            "Title": "Chargelab"
        },
        {
            "WebsiteURL": "http://www.chargelounge.de/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@chargelounge.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 96,
            "Title": "ChargeLounge"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": "+44 (0)1582 400331",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 8,
            "Title": "Chargemaster"
        },
        {
            "WebsiteURL": "https://chargemod.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3780,
            "Title": "ChargeMod (IN)"
        },
        {
            "WebsiteURL": "http://chargenet.lk/",
            "Comments": null,
            "PhonePrimaryContact": "+94-1-5551-551 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@vega.lk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 227,
            "Title": "chargeNET (lk)"
        },
        {
            "WebsiteURL": "https://charge.net.nz/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 229,
            "Title": "ChargeNet NZ"
        },
        {
            "WebsiteURL": "https://www.chargengo.net.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3718,
            "Title": "ChargeN'Go"
        },
        {
            "WebsiteURL": "https://chargenode.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3765,
            "Title": "ChargeNode (SE)"
        },
        {
            "WebsiteURL": "https://www.chargenow.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 173,
            "Title": "ChargeNow"
        },
        {
            "WebsiteURL": "http://chargeplacescotland.org/",
            "Comments": "Operated by SWARCO on behalf of Transport Scotland. CYC cards/app accepted",
            "PhonePrimaryContact": "0141 648 0750",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3315,
            "Title": "Chargeplace Scotland"
        },
        {
            "WebsiteURL": "http://www.chargepoint.net/",
            "Comments": null,
            "PhonePrimaryContact": "1-408-841-4500",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 5,
            "Title": "ChargePoint"
        },
        {
            "WebsiteURL": "https://www.chargepoly.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3707,
            "Title": "Chargepoly (FR)"
        },
        {
            "WebsiteURL": "https://chargerquest.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-888-310-6630",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3741,
            "Title": "ChargerQuest"
        },
        {
            "WebsiteURL": "https://www.chargesini.com/",
            "Comments": null,
            "PhonePrimaryContact": "+60 10-908 9453",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@chargesini.com",
            "FaultReportEmail": "support@chargesini.com",
            "IsRestrictedEdit": false,
            "ID": 3660,
            "Title": "ChargeSini"
        },
        {
            "WebsiteURL": "http://chargestar.com.au/",
            "Comments": null,
            "PhonePrimaryContact": "1300 661 895",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3310,
            "Title": "Chargestar (AU)"
        },
        {
            "WebsiteURL": "https://chargeupev.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3734,
            "Title": "ChargeUp (NovaCharge)"
        },
        {
            "WebsiteURL": "https://chargev.my/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "chargev@greentechmalaysia.my",
            "FaultReportEmail": "chargev@greentechmalaysia.my",
            "IsRestrictedEdit": false,
            "ID": 3338,
            "Title": "chargEV"
        },
        {
            "WebsiteURL": "https://chargy.lu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3321,
            "Title": "Chargy (LU)"
        },
        {
            "WebsiteURL": "https://www.circlek.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3510,
            "Title": "Circle K"
        },
        {
            "WebsiteURL": "http://www.lecircuitelectrique.com",
            "Comments": null,
            "PhonePrimaryContact": "1 855 999-8378",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "infocircuitelectrique@caaquebec.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 90,
            "Title": "Circuit Electrique"
        },
        {
            "WebsiteURL": "https://www.citipark.co.uk",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3670,
            "Title": "CitiPark (UK)"
        },
        {
            "WebsiteURL": "https://cityev.net/user-instructions/",
            "Comments": "Lamp post mounted chargers, plugsurfing RFID or app",
            "PhonePrimaryContact": "+44 23 9319 0109",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3349,
            "Title": "City EV"
        },
        {
            "WebsiteURL": "https://m.clenergy.online/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3605,
            "Title": "Clenergy"
        },
        {
            "WebsiteURL": "https://www.clever.dk/",
            "Comments": null,
            "PhonePrimaryContact": "+45 8230 3030",
            "PhoneSecondaryContact": "8230 3030",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kundeservice@clever.dk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 185,
            "Title": "CLEVER"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 31,
            "Title": "Clipper Creek"
        },
        {
            "WebsiteURL": "https://www.defa.com/ev-charging/cloudcharge/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3548,
            "Title": "CloudCharge"
        },
        {
            "WebsiteURL": "https://www.cnr.tm.fr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3360,
            "Title": "CNR (Compagnie Nationale du Rhône)"
        },
        {
            "WebsiteURL": "https://www.cogeserenergia.it/mosaic/search/it/mobilita-elettrica",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3474,
            "Title": "Cogeser Energia (Italia)"
        },
        {
            "WebsiteURL": "https://www.comfortcharge.de/",
            "Comments": "Deutsche Telekom Comfortcharge",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3369,
            "Title": "Comfortcharge"
        },
        {
            "WebsiteURL": "https://www.connectedkerb.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3509,
            "Title": "Connected Kerb"
        },
        {
            "WebsiteURL": "https://plugcharge.continente.pt",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3431,
            "Title": "Continente Plug&Charge"
        },
        {
            "WebsiteURL": "https://ww2.copec.cl/voltex",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3364,
            "Title": "Copec Voltex"
        },
        {
            "WebsiteURL": "https://www.copel.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3566,
            "Title": "Copel"
        },
        {
            "WebsiteURL": "https://www.countiesenergy.co.nz/articles/ev-charging",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3547,
            "Title": "Counties Energy"
        },
        {
            "WebsiteURL": "https://cv-charging.com/tr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@cv-charging.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3628,
            "Title": "CV Charging Vehicles"
        },
        {
            "WebsiteURL": "http://www.da-emobil.com/ladenetz",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3320,
            "Title": "da emobil"
        },
        {
            "WebsiteURL": "https://www.dchandal.com/",
            "Comments": null,
            "PhonePrimaryContact": "+60108226222",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "helpme@dchandal.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3776,
            "Title": "DC Handal"
        },
        {
            "WebsiteURL": "http://dccenergy.com.br/",
            "Comments": null,
            "PhonePrimaryContact": "85 9 9199.2187",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3760,
            "Title": "DCC Energy"
        },
        {
            "WebsiteURL": "https://www.deiblue.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3498,
            "Title": "DEI Blue"
        },
        {
            "WebsiteURL": "https://www.dewa.gov.ae/",
            "Comments": "Dubai Electricity and Water Authority (DEWA)",
            "PhonePrimaryContact": "+971 4- 601 9999",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3263,
            "Title": "DEWA"
        },
        {
            "WebsiteURL": "https://digavel.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3572,
            "Title": "Digavel (ES)"
        },
        {
            "WebsiteURL": "https://dragoncharging.online",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3496,
            "Title": "Dragon Charging"
        },
        {
            "WebsiteURL": "https://energy.drax.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3614,
            "Title": "Drax Energy Solutions Limited"
        },
        {
            "WebsiteURL": "https://www.dream-energy.fr/",
            "Comments": null,
            "PhonePrimaryContact": "+33 1 55 78 95 62",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3651,
            "Title": "Dream Energy"
        },
        {
            "WebsiteURL": "http://www.drehstromnetz.de",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 66,
            "Title": "Drehstromnetz"
        },
        {
            "WebsiteURL": "http://driv-eco.com/index.php/en/home-eng/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3316,
            "Title": "Drive Eco"
        },
        {
            "WebsiteURL": "https://driveenergychargers.com",
            "Comments": null,
            "PhonePrimaryContact": "+79780162216",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3674,
            "Title": "DriveEnergy (RU)"
        },
        {
            "WebsiteURL": "https://www.driwe.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3332,
            "Title": "Driwe"
        },
        {
            "WebsiteURL": "https://mobility.dufercoenergia.com/",
            "Comments": null,
            "PhonePrimaryContact": "+39 345 7051126",
            "PhoneSecondaryContact": "800 92 22 00",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "mobility@dueenergie.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3267,
            "Title": "Duferco Energie"
        },
        {
            "WebsiteURL": "http://www.ekobonus.cz/ekologicka-doprava/elektromobilita",
            "Comments": "CZ*EON",
            "PhonePrimaryContact": "+420 731 809 090",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "emobilita@eon.cz",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 192,
            "Title": "E.ON (CZ)"
        },
        {
            "WebsiteURL": "https://www.eon.de/de/eonde/pk/produkteUndPreise/E.ON_eMobil/index.htm",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 46,
            "Title": "E.ON (DE)"
        },
        {
            "WebsiteURL": "https://www.eon.dk/privat/strom-til-din-elbil.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3251,
            "Title": "E.ON (DK)"
        },
        {
            "WebsiteURL": "https://www.eon.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3359,
            "Title": "E.ON (HU)"
        },
        {
            "WebsiteURL": "https://www.eonenergy.com/eon-drive-ev-charging.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3403,
            "Title": "E.ON Drive"
        },
        {
            "WebsiteURL": "https://www.eac.com.cy/En/CustomerService/eCharge/Pages/default.aspx",
            "Comments": "Electricity Authority of Cyprus",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3294,
            "Title": "EAC e-charge"
        },
        {
            "WebsiteURL": "http://www.eam.de/ueber-uns/unternehmensprofil/standorte/",
            "Comments": null,
            "PhonePrimaryContact": " ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 140,
            "Title": "EAM"
        },
        {
            "WebsiteURL": "http://www.easy-4-you.ch",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3314,
            "Title": "Easy4You"
        },
        {
            "WebsiteURL": "https://easygo.ie/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1241,
            "Title": "EasyGO (aka Carcharger.ie)"
        },
        {
            "WebsiteURL": "https://easypark.fi/",
            "Comments": "Parking operator, EV chargers activated by mobile phone app",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3302,
            "Title": "Easypark"
        },
        {
            "WebsiteURL": "http://www.eaton.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 42,
            "Title": "EATON"
        },
        {
            "WebsiteURL": "https://ebcharging.co.uk/",
            "Comments": "owned by Blink Charging",
            "PhonePrimaryContact": "+44 1727 807 263",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3391,
            "Title": "EB Charging"
        },
        {
            "WebsiteURL": "https://www.eborn.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3408,
            "Title": "eborn"
        },
        {
            "WebsiteURL": "http://www.ecarni.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "ecar@drdni.gov.uk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 93,
            "Title": "E-Car"
        },
        {
            "WebsiteURL": "http://e-charge.ro/",
            "Comments": "Renovatio E-Charge",
            "PhonePrimaryContact": "+40 372 756 599",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "office@e-charge.ro",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3271,
            "Title": "e-Charge (Romania)"
        },
        {
            "WebsiteURL": "https://www.e-charge50.fr/",
            "Comments": null,
            "PhonePrimaryContact": "+33 809 10 75 84 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3755,
            "Title": "E-Charge50 (FR)"
        },
        {
            "WebsiteURL": "http://www.echargenet.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3309,
            "Title": "echargenet - State Grid Corportation of China"
        },
        {
            "WebsiteURL": "https://ecocharge77.fr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3413,
            "Title": "EcoCharge77"
        },
        {
            "WebsiteURL": "https://ecofactor.ua/app-for-drivers",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3497,
            "Title": "EcoFactor Network"
        },
        {
            "WebsiteURL": "https://www.ecoinside.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3647,
            "Title": "Ecoinside (PT)"
        },
        {
            "WebsiteURL": "http://www.ecoplug.be/index.html",
            "Comments": null,
            "PhonePrimaryContact": "+32 (0) 483 425 255",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ecoplug.be",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 77,
            "Title": "Ecoplug"
        },
        {
            "WebsiteURL": "http://www.ecospazio.it/",
            "Comments": null,
            "PhonePrimaryContact": "+39 0464 401121",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ecospazio.it",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 83,
            "Title": "Ecospazio (Italy)"
        },
        {
            "WebsiteURL": "http://www.ecotap.nl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 179,
            "Title": "Ecotap"
        },
        {
            "WebsiteURL": "https://ecpoints.es/",
            "Comments": "Place To Plug app",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3551,
            "Title": "ECPoints"
        },
        {
            "WebsiteURL": "https://www.edfenergy.com/electric-cars",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3312,
            "Title": "EDF"
        },
        {
            "WebsiteURL": "https://edgecontrol.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3655,
            "Title": "EdgeControl (IL)"
        },
        {
            "WebsiteURL": "http://www.edp.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3276,
            "Title": "EDP"
        },
        {
            "WebsiteURL": "http://www.edp.pt/",
            "Comments": null,
            "PhonePrimaryContact": " +351 21 001 2500",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 199,
            "Title": "EDP MOP"
        },
        {
            "WebsiteURL": "https://www.edpsmart.com.br/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3445,
            "Title": "EDP Smart"
        },
        {
            "WebsiteURL": "http://www.edrop.ch/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@edrop.ch",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 208,
            "Title": "eDrop"
        },
        {
            "WebsiteURL": "http://www.ee-mobil.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 2520 93118 0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ee-mobil.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3264,
            "Title": "EE-Mobil"
        },
        {
            "WebsiteURL": "http://www.ewb-duderstadt.de/de/Strom/Ausgezeichnet.html",
            "Comments": null,
            "PhonePrimaryContact": "(05527) 911-0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@eew-duderstadt.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 171,
            "Title": "EEW Duderstadt"
        },
        {
            "WebsiteURL": "https://www.resaplace.com/",
            "Comments": "Resaplace Parking",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3281,
            "Title": "Effia"
        },
        {
            "WebsiteURL": "https://www.e-flux.io/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3579,
            "Title": "E-Flux"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3599,
            "Title": "EG Group EV Point (UK)"
        },
        {
            "WebsiteURL": "https://www.eins.de/privatkunden/elektromobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": "+49 371 525-5403",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "Robby.Hartl@eins.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2243,
            "Title": "eins"
        },
        {
            "WebsiteURL": "https://www.ejoin.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3415,
            "Title": "ejoin"
        },
        {
            "WebsiteURL": "https://ekoen.pl/",
            "Comments": null,
            "PhonePrimaryContact": "+48 699 58 58 58",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3636,
            "Title": "Ekoen"
        },
        {
            "WebsiteURL": "https://www.ekomobil.it",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3342,
            "Title": "Ekomobil"
        },
        {
            "WebsiteURL": "http://www.e-laad.nl",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 29,
            "Title": "e-Laad"
        },
        {
            "WebsiteURL": "https://elanga.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3624,
            "Title": "Elanga (AU)"
        },
        {
            "WebsiteURL": "https://www.eldrive.eu",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3692,
            "Title": "Eldrive Lithuania (LT)"
        },
        {
            "WebsiteURL": "https://www.go-electra.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3489,
            "Title": "Electra"
        },
        {
            "WebsiteURL": "https://www.e55c.com/",
            "Comments": null,
            "PhonePrimaryContact": "+33 9 75 89 15 01",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3513,
            "Title": "Electric 55 Charging (FR)"
        },
        {
            "WebsiteURL": "https://electriceratechnologies.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3789,
            "Title": "Electric Era (US)"
        },
        {
            "WebsiteURL": "https://electrichighway.gridserve.com",
            "Comments": "Formerly known as the Ecotricity Electric Highway",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 24,
            "Title": "Electric Highway (UK)"
        },
        {
            "WebsiteURL": "https://www.electrichighwaytasmania.com.au",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3406,
            "Title": "Electric Highway Tasmania"
        },
        {
            "WebsiteURL": "http://www.ev-institute.com/",
            "Comments": null,
            "PhonePrimaryContact": "+1 (410)-685-1109",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3524,
            "Title": "Electric Vehicle Institute"
        },
        {
            "WebsiteURL": "http://electric-driving.colruytgroup.com",
            "Comments": null,
            "PhonePrimaryContact": "+32 (0)2 363 55 45",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "electric-driving@colruytgroup.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 232,
            "Title": "electric-driving.colruytgroup.com"
        },
        {
            "WebsiteURL": "https://electrico.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3704,
            "Title": "Electrico.es"
        },
        {
            "WebsiteURL": "https://electrifly.ru",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@electrifly.ru",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3638,
            "Title": "Electrifly"
        },
        {
            "WebsiteURL": "https://www.electrifyamerica.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3318,
            "Title": "Electrify America"
        },
        {
            "WebsiteURL": "https://www.electrify-canada.ca/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3400,
            "Title": "Electrify Canada"
        },
        {
            "WebsiteURL": "https://www.etpvolga.ru/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3606,
            "Title": "Electro Transport Plus (RU)"
        },
        {
            "WebsiteURL": "https://electro.cars/",
            "Comments": null,
            "PhonePrimaryContact": "+7 800 775-81-87",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3507,
            "Title": "Electro.Cars (RU)"
        },
        {
            "WebsiteURL": "https://www.electroad.uk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3740,
            "Title": "ElectRoad (UK)"
        },
        {
            "WebsiteURL": "http://www.electrodrive-europe.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 67,
            "Title": "ElectroDrive"
        },
        {
            "WebsiteURL": "http://www.electrodrive-salzburg.at",
            "Comments": null,
            "PhonePrimaryContact": "0800 / 810 102",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "office@electrodrive-salzburg.at",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 141,
            "Title": "ElectroDrive Salzburg"
        },
        {
            "WebsiteURL": "http://www.mark-e.de/",
            "Comments": null,
            "PhonePrimaryContact": " +49 2331 12322437",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "electrodrive@mark-e.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 184,
            "Title": "ElectroDrive/Mark-E (DE)"
        },
        {
            "WebsiteURL": "https://www.emtmadrid.es/",
            "Comments": "Empresa Municipal de Transportes de Madrid",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3553,
            "Title": "Electro-EMT"
        },
        {
            "WebsiteURL": "https://www.electromaps.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3401,
            "Title": "Electromaps"
        },
        {
            "WebsiteURL": "https://electroukraine.com.ua/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3390,
            "Title": "Electroukraine"
        },
        {
            "WebsiteURL": "http://www.elektro-ljubljana.si/1/Obnovljivi-viri-energije/Polnilna-mesta-za-elektricna-vozila.aspx",
            "Comments": null,
            "PhonePrimaryContact": "+386 1 230 40 00",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@elektro-ljubljana.si",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3258,
            "Title": "Elektro Ljublana"
        },
        {
            "WebsiteURL": "http://www.elektromotive.com",
            "Comments": null,
            "PhonePrimaryContact": "+ 44 (0)1273 704775",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@elektromotive.com",
            "FaultReportEmail": "info@elektromotive.com",
            "IsRestrictedEdit": null,
            "ID": 2,
            "Title": "Elektrobay (UK)"
        },
        {
            "WebsiteURL": "http://www.elektromotive.com",
            "Comments": null,
            "PhonePrimaryContact": "+ 44 (0)1273 704775",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": "http://www.elektromotive.com/html/application_forms.php",
            "ContactEmail": "info@elektromotive.com",
            "FaultReportEmail": "info@elektromotive.com",
            "IsRestrictedEdit": null,
            "ID": 16,
            "Title": "Elektromotive (UK)"
        },
        {
            "WebsiteURL": "http://elen.hep.hr/ELEN-charging-stations.aspx",
            "Comments": null,
            "PhonePrimaryContact": "+385 163 22123",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3311,
            "Title": "Elen"
        },
        {
            "WebsiteURL": "https://www.elevat.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3767,
            "Title": "Elevat/MasterCharge (EU)"
        },
        {
            "WebsiteURL": "https://www.elintacharge.com/en/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3414,
            "Title": "Elinta Charge"
        },
        {
            "WebsiteURL": "http://ella.at/",
            "Comments": "uses the Be Energised backend",
            "PhonePrimaryContact": "+43 800 203004",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3287,
            "Title": "Ella"
        },
        {
            "WebsiteURL": "https://www.elli.eco/de/startseite",
            "Comments": "DE*GCE",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3437,
            "Title": "Elli (Volkswagen Group Charging GmbH)"
        },
        {
            "WebsiteURL": "http://www.elmo.ee/",
            "Comments": "When calling 651 1911 the price of the call depends on the selected service package. When calling 1911, the price of the call is 0.23 euros (including VAT). The price of content service of calls to call service numbers does not depend on the service package of a customer; it is the same for all callers.",
            "PhonePrimaryContact": "6 511 911",
            "PhoneSecondaryContact": "1911",
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elmo@kredex.ee",
            "FaultReportEmail": "tugi@elmo.ee",
            "IsRestrictedEdit": null,
            "ID": 76,
            "Title": "ELMO"
        },
        {
            "WebsiteURL": "https://www.elmotion.ro/harta",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3519,
            "Title": "ELMotion"
        },
        {
            "WebsiteURL": "http://www.e-autozas.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 187,
            "Title": "ELMŰ"
        },
        {
            "WebsiteURL": "https://elo.city",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3368,
            "Title": "Elocity"
        },
        {
            "WebsiteURL": "https://elpefuture.gr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3478,
            "Title": "ElpeFuture"
        },
        {
            "WebsiteURL": "https://www.emallorca.io/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3671,
            "Title": "eMallorca (ES)"
        },
        {
            "WebsiteURL": "https://emeo.sk/verejne_nabijanie",
            "Comments": "emewatts s.r.o.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3681,
            "Title": "Emeo (SK)"
        },
        {
            "WebsiteURL": "https://emfree.eu/",
            "Comments": null,
            "PhonePrimaryContact": "0032494207066",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@emfree.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3486,
            "Title": "Emfree"
        },
        {
            "WebsiteURL": "http://www.friedrichshafen.de/wirtschaft-verkehr/emma",
            "Comments": null,
            "PhonePrimaryContact": "+49 7541 603380",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@fn-dienste.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1238,
            "Title": "emma"
        },
        {
            "WebsiteURL": "https://e-mobi.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3319,
            "Title": "E-Mobi"
        },
        {
            "WebsiteURL": "https://www.emobilitabrno.cz/en/chargers",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3532,
            "Title": "e-Mobilita Brno (cz)"
        },
        {
            "WebsiteURL": "https://www.emobilitabrno.cz/cs/verejne-dobijecky",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@emobilitabrno.cz",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3783,
            "Title": "E-mobilita Brno (CZ)"
        },
        {
            "WebsiteURL": "http://www.emobitaly.it/come-ricaricare/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3282,
            "Title": "Emobitaly (Italy)"
        },
        {
            "WebsiteURL": "http://www.e-moving.it/",
            "Comments": null,
            "PhonePrimaryContact": "800035151",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "e-moving@a2a.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 82,
            "Title": "E-moving (Italy)"
        },
        {
            "WebsiteURL": "http://www.empora.eu",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 68,
            "Title": "Empora"
        },
        {
            "WebsiteURL": "https://enyakit.com.tr/",
            "Comments": null,
            "PhonePrimaryContact": "+90 850 202 0 251",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3601,
            "Title": "En Yakıt (TR)"
        },
        {
            "WebsiteURL": "https://www.enbw.com/privatkunden/tarife-und-produkte/e-mobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 86,
            "Title": "EnBW (D)"
        },
        {
            "WebsiteURL": "http://www.endesa.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 207,
            "Title": "Endesa"
        },
        {
            "WebsiteURL": "https://www.eneco-emobility.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3394,
            "Title": "Eneco"
        },
        {
            "WebsiteURL": "https://eneldrive.enelx.com/",
            "Comments": "IT*ELX",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 80,
            "Title": "Enel X"
        },
        {
            "WebsiteURL": " https://enercharge.at/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3405,
            "Title": "Enercharge"
        },
        {
            "WebsiteURL": "https://www.enercity.de/privatkunden/mobilitaet/e-mobilitaet/formular-reg-e-tanken/index.jsx",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 121,
            "Title": "EnerCity"
        },
        {
            "WebsiteURL": "https://www.ene-eifel.de/privatkunden-strom/e-mobilität",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service@ene-eifel.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3260,
            "Title": "Energie der Eifel"
        },
        {
            "WebsiteURL": "http://ebt-halblech.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 8368 9280",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kontakt@ebt-halblech.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 219,
            "Title": "Energieversorgung Buching-Trauchgau"
        },
        {
            "WebsiteURL": "http://www.enerhub.it/ricarica/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3370,
            "Title": "Enerhub"
        },
        {
            "WebsiteURL": "https://enerstock.fr/",
            "Comments": "FR*ENR",
            "PhonePrimaryContact": "+33 4 67 55 17 25",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3774,
            "Title": "Enerstock"
        },
        {
            "WebsiteURL": "http://www.enewa.de/",
            "Comments": null,
            "PhonePrimaryContact": "0228 / 377368 0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@enewa.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 172,
            "Title": "ENEWA"
        },
        {
            "WebsiteURL": "https://www.enelx.com/",
            "Comments": null,
            "PhonePrimaryContact": "600 350 2000",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "enexdirecto@enex.cl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3461,
            "Title": "Enex E-Pro"
        },
        {
            "WebsiteURL": "https://www.engie.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3595,
            "Title": "Engie"
        },
        {
            "WebsiteURL": "http://www.enovates.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 181,
            "Title": "eNovates"
        },
        {
            "WebsiteURL": "http://www.enovos.lu/particuliers/ecomobilite",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 52,
            "Title": "Enovos"
        },
        {
            "WebsiteURL": "http://www.enspirion.pl/?page_id=728",
            "Comments": null,
            "PhonePrimaryContact": "+48 58 888 88 00",
            "PhoneSecondaryContact": "+48 785 888 805",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "biuro@enspirion.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 216,
            "Title": "Enspirion"
        },
        {
            "WebsiteURL": "https://www.entega.de/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3297,
            "Title": "Entega"
        },
        {
            "WebsiteURL": "https://www.eocharging.com/",
            "Comments": null,
            "PhonePrimaryContact": "+44 333 772 0383 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3298,
            "Title": "EO Charging"
        },
        {
            "WebsiteURL": "https://www.eondrive.ro/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3422,
            "Title": "eondrive.ro"
        },
        {
            "WebsiteURL": "https://en.web.eparking.fi/",
            "Comments": null,
            "PhonePrimaryContact": "+358 34 108 9272",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@eparking.fi",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3793,
            "Title": "eparking (Finland)"
        },
        {
            "WebsiteURL": "https://www.epower.ie/",
            "Comments": "Mostly in Ireland, but some outside the country",
            "PhonePrimaryContact": "1800 99 88 77",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@epower.ie",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3449,
            "Title": "ePower"
        },
        {
            "WebsiteURL": "https://eranovum.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3583,
            "Title": "Eranovum (ES)"
        },
        {
            "WebsiteURL": "http://esarj.com/uyelik",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 70,
            "Title": "Eşarj (TR)"
        },
        {
            "WebsiteURL": "http://www.esb.ie/electric-cars/index.jsp",
            "Comments": null,
            "PhonePrimaryContact": " 1890 372 387",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "ecars@esb.ie",
            "FaultReportEmail": "ecars@esb.ie",
            "IsRestrictedEdit": null,
            "ID": 22,
            "Title": "ESB Ecars"
        },
        {
            "WebsiteURL": "https://www.esbenergy.co.uk/ev",
            "Comments": "Distinct network from the one they operate on the island of Ireland",
            "PhonePrimaryContact": "+44 345 609 0372",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3357,
            "Title": "ESB Energy (UK)"
        },
        {
            "WebsiteURL": "https://e-space.ge/",
            "Comments": null,
            "PhonePrimaryContact": "+995322433473",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@e-space.ge",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3631,
            "Title": "e-space (GE)"
        },
        {
            "WebsiteURL": "https://www.esph-sa.com/centros-de-carga-vehiculos-electricos",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3480,
            "Title": "ESPH"
        },
        {
            "WebsiteURL": "http://www.essent.nl/content/particulier/producten/elektrisch_rijden/index.html",
            "Comments": null,
            "PhonePrimaryContact": "0800 377 36 83",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elektrischrijden@essent.nl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 78,
            "Title": "Essent (NL)"
        },
        {
            "WebsiteURL": "http://www.e-mobilitat.cat/",
            "Comments": null,
            "PhonePrimaryContact": "+34 900 250 260",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 209,
            "Title": "Estabanell Energia"
        },
        {
            "WebsiteURL": "http://www.estonteco.eu/live/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 205,
            "Title": "Estonteca"
        },
        {
            "WebsiteURL": "http://www.etecnic.es",
            "Comments": null,
            "PhonePrimaryContact": " (+34) 977 276 952",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "etecnic@etecnic.es",
            "FaultReportEmail": "etecnic@etecnic.es",
            "IsRestrictedEdit": false,
            "ID": 3377,
            "Title": "eTecnic"
        },
        {
            "WebsiteURL": "http://etop.sk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 222,
            "Title": "ETOP"
        },
        {
            "WebsiteURL": "http://www.e-totem.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 55,
            "Title": "e-totem"
        },
        {
            "WebsiteURL": "https://evbox.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3722,
            "Title": "EV Box"
        },
        {
            "WebsiteURL": "https://www.evconnect.com/",
            "Comments": null,
            "PhonePrimaryContact": "866) 816-7584",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@evconnect.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3372,
            "Title": "EV Connect"
        },
        {
            "WebsiteURL": "https://evdirect.hu/",
            "Comments": null,
            "PhonePrimaryContact": "+36 30 550 9858",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@evdirect.hu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3424,
            "Title": "EV Direct"
        },
        {
            "WebsiteURL": "https://www.ev-dot.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3446,
            "Title": "EV Dot"
        },
        {
            "WebsiteURL": "https://evenergygroup.com/e",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3399,
            "Title": "EV Energy Group (FCN)"
        },
        {
            "WebsiteURL": "https://ev-georgia.net",
            "Comments": null,
            "PhonePrimaryContact": "+995514070033",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ev-georgia.net",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3630,
            "Title": "EV Georgia"
        },
        {
            "WebsiteURL": "https://www.horizonpower.com.au/for-home/electric-vehicles/",
            "Comments": "Rapid charging network in Western Australia",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3554,
            "Title": "EV Highway (Horizon Power)"
        },
        {
            "WebsiteURL": "https://evloader.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3428,
            "Title": "EV Loader"
        },
        {
            "WebsiteURL": "https://evmatch.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3725,
            "Title": "EV Match"
        },
        {
            "WebsiteURL": "https://www.evoasis.com.tw/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3482,
            "Title": "EV Oasis"
        },
        {
            "WebsiteURL": "https://evpoint.md/",
            "Comments": null,
            "PhonePrimaryContact": "+373 60 60 99 00",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3502,
            "Title": "EV Point Moldova"
        },
        {
            "WebsiteURL": "https://www.evrange.com/",
            "Comments": null,
            "PhonePrimaryContact": "+1-833-387-2643",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@evrange.com",
            "FaultReportEmail": "support@evrange.com",
            "IsRestrictedEdit": false,
            "ID": 3526,
            "Title": "EV Range Charging Network"
        },
        {
            "WebsiteURL": "https://ev2go.ru/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "hello@ev2go.ru",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3703,
            "Title": "Ev2Go (RU)"
        },
        {
            "WebsiteURL": "https://www.e-vadea.fr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3594,
            "Title": "e-Vadea"
        },
        {
            "WebsiteURL": "https://www.evaz.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3648,
            "Title": "eVaz Energy (PT)"
        },
        {
            "WebsiteURL": "http://www.evbility.eu/",
            "Comments": null,
            "PhonePrimaryContact": "+390396015174",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@evbility.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 87,
            "Title": "EVbility (Italy)"
        },
        {
            "WebsiteURL": "http://www.ev-box.com",
            "Comments": null,
            "PhonePrimaryContact": "+31 (0)88 77 55 444",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ev-box.com",
            "FaultReportEmail": "info@ev-box.com",
            "IsRestrictedEdit": null,
            "ID": 73,
            "Title": "EV-Box"
        },
        {
            "WebsiteURL": "https://www.ev-chargersuk.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "0330 111 2999",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@evc.co.uk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3562,
            "Title": "EVC"
        },
        {
            "WebsiteURL": "https://www.evce.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3693,
            "Title": "EVCE (PT)"
        },
        {
            "WebsiteURL": "https://evcharge.online/",
            "Comments": "Rolec. Pre-payment, minimum topup £5.00",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "Contact@power-portal.co.uk",
            "FaultReportEmail": "Contact@power-portal.co.uk",
            "IsRestrictedEdit": false,
            "ID": 3295,
            "Title": "evcharge.online"
        },
        {
            "WebsiteURL": "https://evconnect.ro/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3418,
            "Title": "evconnect.ro (Romania)"
        },
        {
            "WebsiteURL": "https://opigo.se/ev-core",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3764,
            "Title": "EVcore (SE)"
        },
        {
            "WebsiteURL": "https://evcs.com/",
            "Comments": "US*NDO",
            "PhonePrimaryContact": "+1 866 300 3827",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3542,
            "Title": "EVCS"
        },
        {
            "WebsiteURL": "http://www.evd-dormagen.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 2133 97150",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3254,
            "Title": "Evd Dormagen"
        },
        {
            "WebsiteURL": "https://evdutystore.elmec.ca/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3505,
            "Title": "EVduty"
        },
        {
            "WebsiteURL": " https://user.evedge.co.il/#/portal/locations",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3434,
            "Title": "EVEdge (Israel)"
        },
        {
            "WebsiteURL": " https://evergonet.com/",
            "Comments": null,
            "PhonePrimaryContact": "(+1) 809 469 5050",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "soporte@evergonet.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3500,
            "Title": "Evergo"
        },
        {
            "WebsiteURL": "https://www.everse.one/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3535,
            "Title": "EVerse"
        },
        {
            "WebsiteURL": "https://everty.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3609,
            "Title": "Everty"
        },
        {
            "WebsiteURL": "http://evgateway.com/",
            "Comments": null,
            "PhonePrimaryContact": "+1 949-945-2000",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3389,
            "Title": "EVGateway"
        },
        {
            "WebsiteURL": "https://www.evgo.com/",
            "Comments": "Imported by ADFC import",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 15,
            "Title": "eVgo Network"
        },
        {
            "WebsiteURL": "http://goevie.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3398,
            "Title": "Evie"
        },
        {
            "WebsiteURL": "https://go-evio.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3792,
            "Title": "EVIO (PT)"
        },
        {
            "WebsiteURL": "https://www.eviso.it",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3472,
            "Title": "eVISO"
        },
        {
            "WebsiteURL": "http://www.swiss-emobility.ch/home/evite.html",
            "Comments": null,
            "PhonePrimaryContact": "+41 (0)58 827 34 09 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@swiss-emobility.ch",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 110,
            "Title": "EVite (ch)"
        },
        {
            "WebsiteURL": "https://www.evl.de/e-mobilitaet/e-tanken-in-limburg/",
            "Comments": "Uses NewMotion backend",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3351,
            "Title": "EVL (de)"
        },
        {
            "WebsiteURL": "https://ev-mag.ro/stations/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3419,
            "Title": "EV-Mag"
        },
        {
            "WebsiteURL": "http://www.evmapa.cz",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 221,
            "Title": "Evmapa (CZ)"
        },
        {
            "WebsiteURL": "https://evn.bg/SpecialPages/e-mobility.aspx",
            "Comments": null,
            "PhonePrimaryContact": "0700 1 7777",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "emobility@evn.bg",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3616,
            "Title": "EVN (Bulgaria)"
        },
        {
            "WebsiteURL": "http://www.evnet.nl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 178,
            "Title": "EVnetNL"
        },
        {
            "WebsiteURL": "https://evologyparking.com/charging/",
            "Comments": "GB*EYE",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3759,
            "Title": "Evology Parking"
        },
        {
            "WebsiteURL": "https://e-voltt.nl/",
            "Comments": null,
            "PhonePrimaryContact": "+31(0)85 1054135",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "nederland@e-voltt.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3442,
            "Title": "e-VOLTT"
        },
        {
            "WebsiteURL": "https://www.evpass.ch/",
            "Comments": "Android & IOS Apps, Swisspass travel RFID can be registered",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3272,
            "Title": "EVPass (CH)"
        },
        {
            "WebsiteURL": "http://www.ev-point.be",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 49,
            "Title": "EV-Point"
        },
        {
            "WebsiteURL": "http://www.evpower.my/",
            "Comments": null,
            "PhonePrimaryContact": "+601155558686",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3663,
            "Title": "EVPower (MY)"
        },
        {
            "WebsiteURL": "https://www.evpower.pt",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3643,
            "Title": "EVPower (PT)"
        },
        {
            "WebsiteURL": "https://www.energieversorgung-sylt.de/mobilitaet/e-mobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": "04651 925-925",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kundenservice@energieversorgung-sylt.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 137,
            "Title": "EVS Energieversorgung Sylt"
        },
        {
            "WebsiteURL": "",
            "Comments": "Imported by ADFC import",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 11,
            "Title": "EVSE LLC WebNet"
        },
        {
            "WebsiteURL": "https://ev-spots.jimdosite.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3662,
            "Title": "EVSpots (RO)"
        },
        {
            "WebsiteURL": "https://evstart.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-437-999-3863",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3745,
            "Title": "EVStart (CA)"
        },
        {
            "WebsiteURL": "https://evtech.co.il/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3781,
            "Title": "EVTECH (IL)"
        },
        {
            "WebsiteURL": "http://ev-time.ru/",
            "Comments": null,
            "PhonePrimaryContact": "8 800 500 80 56",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3700,
            "Title": "EV-Time (RU)"
        },
        {
            "WebsiteURL": "https://www.evup.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3623,
            "Title": "EVUp (AU)"
        },
        {
            "WebsiteURL": "https://evway.net",
            "Comments": null,
            "PhonePrimaryContact": "+39 02 35954219",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3291,
            "Title": "Evway"
        },
        {
            "WebsiteURL": "https://evx.tech/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3627,
            "Title": "EVX (AU)"
        },
        {
            "WebsiteURL": "https://www.evyve.co.uk/",
            "Comments": "GB*DRV formerly Drivenergy Ltd) Contactless payment pre-auth is £5.00",
            "PhonePrimaryContact": "+44 330 053 1802",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3587,
            "Title": "evyve"
        },
        {
            "WebsiteURL": "https://www.evzen.com",
            "Comments": null,
            "PhonePrimaryContact": "+33 9 69 39 09 03",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@evzen.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3641,
            "Title": "EVzen (FR)"
        },
        {
            "WebsiteURL": "http://www.evziiin.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3427,
            "Title": "EVziiin"
        },
        {
            "WebsiteURL": "http://shop.e-wald.eu/produkt/e-wald-ladekarte-monatskarte/",
            "Comments": null,
            "PhonePrimaryContact": "+49 9923 8045-310",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@e-wald.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 189,
            "Title": "E-Wald"
        },
        {
            "WebsiteURL": "https://e-way.ru/",
            "Comments": null,
            "PhonePrimaryContact": " +7 800 234-38-93",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3675,
            "Title": "E-Way (RU)"
        },
        {
            "WebsiteURL": "https://eway.aass.sm/",
            "Comments": null,
            "PhonePrimaryContact": "+378 549 883700",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3533,
            "Title": "E-Way (San Marino)"
        },
        {
            "WebsiteURL": "https://www.eways.se/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3444,
            "Title": "eways"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-bruchsal.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 7251 7060",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-bruchsal.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2241,
            "Title": "EWB"
        },
        {
            "WebsiteURL": "http://www.ewe.de/privatkunden/ewe-stromtankstellen.php",
            "Comments": null,
            "PhonePrimaryContact": "04418030",
            "PhoneSecondaryContact": "08001014432",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "stromtankkarte@ewe.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 127,
            "Title": "EWE"
        },
        {
            "WebsiteURL": "http://www.ewi-isernhagen.de/energieeffizienz/elektromobilitaet.aspx",
            "Comments": null,
            "PhonePrimaryContact": " 0511 6165475",
            "PhoneSecondaryContact": " 0511 6165476",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kontakt@ewi-isernhagen.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 145,
            "Title": "EWI  Energiewerke Isernhagen"
        },
        {
            "WebsiteURL": "https://ewiva.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3720,
            "Title": "Ewiva (IT)"
        },
        {
            "WebsiteURL": "https://www.swp-potsdam.de/de/energie/elektromobilit%C3%A4t/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3325,
            "Title": "EWP : Energie und Wasser Potsdam GmbH"
        },
        {
            "WebsiteURL": "http://www.ewr-e-mobil.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 6241 848-0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ewr-e-mobil.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 109,
            "Title": "EWR gmbh e-mobile"
        },
        {
            "WebsiteURL": "https://exploren.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3622,
            "Title": "Exploren"
        },
        {
            "WebsiteURL": "https://www.ez-charge.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "+44 1869 322500",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3515,
            "Title": "EZ-Charge"
        },
        {
            "WebsiteURL": "https://ezvolt.com.br/",
            "Comments": null,
            "PhonePrimaryContact": "+55 21 3900-7077",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contato@ezvolt.com.br",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3564,
            "Title": "EZVolt"
        },
        {
            "WebsiteURL": "https://factorenergia.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3685,
            "Title": "Factor Energia (PT)"
        },
        {
            "WebsiteURL": "https://fastnedcharging.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@fastned.nl",
            "FaultReportEmail": "contact@fastned.nl",
            "IsRestrictedEdit": false,
            "ID": 74,
            "Title": "FastNed"
        },
        {
            "WebsiteURL": "https://fastvolt.net/",
            "Comments": null,
            "PhonePrimaryContact": "+212520100115",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@fastvolt.net",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3677,
            "Title": "Fastvolt"
        },
        {
            "WebsiteURL": "http://recarga.fenieenergia.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3279,
            "Title": "Fenie Energía (Spain)"
        },
        {
            "WebsiteURL": "https://www.ferrovial.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3772,
            "Title": "Ferrovial (ES)"
        },
        {
            "WebsiteURL": "https://flashchargingev.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3723,
            "Title": "Flash Charging"
        },
        {
            "WebsiteURL": "https://flo.ca/",
            "Comments": "RéseauVER / VERnetwork        http://www.reseauver.com/          (877) 505-2674          service@reseauver.com",
            "PhonePrimaryContact": "+1 877 505-2674",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@flo.ca",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 89,
            "Title": "flo"
        },
        {
            "WebsiteURL": "http://www.flowcharging.com/",
            "Comments": null,
            "PhonePrimaryContact": "+31 4012734",
            "PhoneSecondaryContact": "+31 4012735",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@flow-nederland.nl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 197,
            "Title": "FLOW Charging"
        },
        {
            "WebsiteURL": "https://www.flowbird.group/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3739,
            "Title": "Flowbird (UK)"
        },
        {
            "WebsiteURL": "http://www.fortisis.eu",
            "Comments": "Operator based on Greence and Cyprus",
            "PhonePrimaryContact": "+30.215.54.09.814 (Greece)",
            "PhoneSecondaryContact": "+357.22.31.63.18 (Cyprus)",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@fortisis.eu",
            "FaultReportEmail": "info@fortisis.eu",
            "IsRestrictedEdit": false,
            "ID": 85,
            "Title": "FORTISIS"
        },
        {
            "WebsiteURL": "https://fpl.com/ev",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3749,
            "Title": "FPL EVolution"
        },
        {
            "WebsiteURL": "https://francisenergy.com/ev-charging-stations/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3733,
            "Title": "Francis Energy"
        },
        {
            "WebsiteURL": "https://www.freeto-x.it/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3503,
            "Title": "Free To X"
        },
        {
            "WebsiteURL": "https://www.freshmile.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3379,
            "Title": "Freshmile"
        },
        {
            "WebsiteURL": "https://fuuse.io/driver-app",
            "Comments": "GB*FSE",
            "PhonePrimaryContact": "+44 333 050 4950",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "hello@fuuse.io",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3673,
            "Title": "Fuuse"
        },
        {
            "WebsiteURL": "http://www.g2mobility.com/",
            "Comments": null,
            "PhonePrimaryContact": "01 45 34 25 34.",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 116,
            "Title": "G2mobility"
        },
        {
            "WebsiteURL": "https://gaiagreen.tech/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3790,
            "Title": "Gai Charge"
        },
        {
            "WebsiteURL": "http://galactico.pl/",
            "Comments": null,
            "PhonePrimaryContact": " +58 52 44 500",
            "PhoneSecondaryContact": " +48 68 328 20 89",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kontakt@galactico.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 218,
            "Title": "Galactico.pl"
        },
        {
            "WebsiteURL": "https://www.galp.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3557,
            "Title": "GALP Electric"
        },
        {
            "WebsiteURL": "http://www.gardauno.it/la-mappa-dei-punti-di-ricarica/",
            "Comments": null,
            "PhonePrimaryContact": "800-133 966",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 204,
            "Title": "GardaUno"
        },
        {
            "WebsiteURL": "https://g-charge.co/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@g-charge.co",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3735,
            "Title": "G-Charge (Gersan Elektrik)"
        },
        {
            "WebsiteURL": "https://info.chargepoint.com/ge_welcome",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1242,
            "Title": "GE WattStation (No longer active)"
        },
        {
            "WebsiteURL": "https://www.getelectric.com.au",
            "Comments": null,
            "PhonePrimaryContact": "1800 438669",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@getelectric.com.au",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3560,
            "Title": "GET Electric (AU)"
        },
        {
            "WebsiteURL": "http://www.ggew.de/UN/Elektromobilitaet",
            "Comments": null,
            "PhonePrimaryContact": "06251 1301-0",
            "PhoneSecondaryContact": "0800 80 30 300",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ggew.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 163,
            "Title": "GGEW"
        },
        {
            "WebsiteURL": "http://www.recargagic.com/",
            "Comments": null,
            "PhonePrimaryContact": "(+34) 902 103 498",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@recargagic.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 210,
            "Title": "GIC"
        },
        {
            "WebsiteURL": "https://www.gioev.com/",
            "Comments": null,
            "PhonePrimaryContact": " 444 91 54",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3604,
            "Title": "GioEV (TR)"
        },
        {
            "WebsiteURL": "https://www.gnrgy.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3334,
            "Title": "Gnrgy"
        },
        {
            "WebsiteURL": "http://www.goelectric-emobility.com/",
            "Comments": null,
            "PhonePrimaryContact": "+55 11 99953-7172",
            "PhoneSecondaryContact": "+55 (11) 2324-7763",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3711,
            "Title": "Go Electric E-Mobility (BR)"
        },
        {
            "WebsiteURL": " https://go-tou.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3494,
            "Title": "Go ToU"
        },
        {
            "WebsiteURL": "https://gopluseauto.pl/",
            "Comments": null,
            "PhonePrimaryContact": "+48 515 515 243",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "biuro@gopluseauto.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3450,
            "Title": "GO+EAuto"
        },
        {
            "WebsiteURL": "https://www.gocharge.ie/charge-with-us/",
            "Comments": null,
            "PhonePrimaryContact": "+353 1 254 6126",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3402,
            "Title": "GoCharge (IE)"
        },
        {
            "WebsiteURL": "http://gofastcharge.com/",
            "Comments": "Accepts Hubject roaming partners of Swisscharge",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@gofastcharge.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3313,
            "Title": "GOFAST (Gotthard Fastcharge)"
        },
        {
            "WebsiteURL": "https://gravitienergy.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3695,
            "Title": "Graviti Energy"
        },
        {
            "WebsiteURL": "http://green-frontiers.net/",
            "Comments": null,
            "PhonePrimaryContact": " +94 11 2884738",
            "PhoneSecondaryContact": "+94710710271",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@green-frontiers.net",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 226,
            "Title": "Green Frontiers (lk)"
        },
        {
            "WebsiteURL": "http://greenlandmobility.it/",
            "Comments": null,
            "PhonePrimaryContact": "02/27208182",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "redazione@greenlandmobility.it",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 84,
            "Title": "Green Land Mobility (Italy)"
        },
        {
            "WebsiteURL": "https://www.greencar.me/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@greencar.me",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3768,
            "Title": "Greencar (Montenegro)"
        },
        {
            "WebsiteURL": "http://www.greenflux.nl/",
            "Comments": null,
            "PhonePrimaryContact": "088 60 50 700",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@greenflux.nl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 63,
            "Title": "Greenflux"
        },
        {
            "WebsiteURL": "https://greenway.sk",
            "Comments": null,
            "PhonePrimaryContact": "+421 2 330 56 236",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@greenway.sk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 88,
            "Title": "Greenway"
        },
        {
            "WebsiteURL": "https://greenwaypolska.pl/",
            "Comments": null,
            "PhonePrimaryContact": "+48583251077",
            "PhoneSecondaryContact": "+48583251017",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "bok@greenwaypolska.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3451,
            "Title": "Greenway Polska (PL)"
        },
        {
            "WebsiteURL": "https://www.gridcars.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3386,
            "Title": "GridCars"
        },
        {
            "WebsiteURL": "https://www.gridserve.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3430,
            "Title": "GridServe"
        },
        {
            "WebsiteURL": "http://gronnkontakt.no/",
            "Comments": null,
            "PhonePrimaryContact": "47 67 08 00 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3247,
            "Title": "Grønn Kontakt"
        },
        {
            "WebsiteURL": "https://www.grupoice.com/wps/portal/ICE/Electricidad/carga-elect",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3404,
            "Title": "Grupo ICE"
        },
        {
            "WebsiteURL": "https://gsspowersl.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3732,
            "Title": "GSS Power (ES)"
        },
        {
            "WebsiteURL": "https://www.gtischarging.sk/",
            "Comments": null,
            "PhonePrimaryContact": "+420 530 508 424",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3787,
            "Title": "GTIS Charging (SK)"
        },
        {
            "WebsiteURL": "https://gyorstoltok.hu/",
            "Comments": null,
            "PhonePrimaryContact": "+362 03649639",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3477,
            "Title": "Gyorstöltők"
        },
        {
            "WebsiteURL": "http://www.harzenergie.de/index.cfm?fuseaction=portal.showcontent&viewmode=content&num_obj_id=30312&language=de&menu=30305&rootmenu=25325&page=30306&bp=30306",
            "Comments": null,
            "PhonePrimaryContact": "05522/503-9345",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "mobilitaet@harzenergie.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 122,
            "Title": "Harz Energie"
        },
        {
            "WebsiteURL": "https://helexia.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3645,
            "Title": "Helexia (PT)"
        },
        {
            "WebsiteURL": "http://www.helen.fi/",
            "Comments": null,
            "PhonePrimaryContact": " 010 802 802 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 95,
            "Title": "Helsingin Energia"
        },
        {
            "WebsiteURL": "https://heracomm.gruppohera.it/casa/mobilita-sostenibile/ricarica-pubblica",
            "Comments": null,
            "PhonePrimaryContact": "800.087.591",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3440,
            "Title": "HeraRicarica Pubblica"
        },
        {
            "WebsiteURL": "https://www.hikotron.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3530,
            "Title": "Hikotron"
        },
        {
            "WebsiteURL": "https://www.holtoltsek.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3730,
            "Title": "Holtoltsek.hu"
        },
        {
            "WebsiteURL": "http://www.hkevpower.com/",
            "Comments": null,
            "PhonePrimaryContact": "+852 2210 7122",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@hkevpower.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 111,
            "Title": "Hong Kong EV Power"
        },
        {
            "WebsiteURL": "https://www.holtoltsek.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@holtoltsek.hu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3731,
            "Title": "Hotoltsek (HU)"
        },
        {
            "WebsiteURL": "https://www.hrvatskitelekom.hr/",
            "Comments": "Primarily a telco, but operates some EV chargepoints",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3384,
            "Title": "Hrvatski Telekom"
        },
        {
            "WebsiteURL": "http://www.hubsta.co.uk/en/home/",
            "Comments": "UK*HUB*",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3356,
            "Title": "Hubsta"
        },
        {
            "WebsiteURL": "https://www.hyperfuel.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": "support@hyperfuel.com",
            "IsRestrictedEdit": false,
            "ID": 3762,
            "Title": "Hyperfuel"
        },
        {
            "WebsiteURL": "https://www.hyundaimobil.co.id/",
            "Comments": null,
            "PhonePrimaryContact": "+62 8001821407",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3665,
            "Title": "Hyundai Indonesia"
        },
        {
            "WebsiteURL": "https://www.iberdrola.es/clientes/hogar/movilidad-verde/recarga",
            "Comments": null,
            "PhonePrimaryContact": "900 22 45 22",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2247,
            "Title": "Iberdrola | BP Pulse (ES)"
        },
        {
            "WebsiteURL": "https://iecharge.io",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3639,
            "Title": "IECharge (FR)"
        },
        {
            "WebsiteURL": "https://ignitison.lt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3688,
            "Title": "Ignitis UAB (LT)"
        },
        {
            "WebsiteURL": "https://www.ikaruselectric.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ikaruselectric.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3744,
            "Title": "IKARUS (Egypt)"
        },
        {
            "WebsiteURL": "https://www.inbalancegrid.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3690,
            "Title": "Inbalance grid (LT)"
        },
        {
            "WebsiteURL": "http://inchanet.cz/products_en.html#fast_charging_station",
            "Comments": null,
            "PhonePrimaryContact": "+420 776 333 155",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@inchanet.cz",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 191,
            "Title": "inChaNet"
        },
        {
            "WebsiteURL": "https://www.goincharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3343,
            "Title": "Incharge"
        },
        {
            "WebsiteURL": "https://infinityevcharge.com/",
            "Comments": null,
            "PhonePrimaryContact": "Toll-free: 16051",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@infinityevcharge.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3742,
            "Title": "Infinity EV (Egypt)"
        },
        {
            "WebsiteURL": "https://www.rwe-mobility.com/",
            "Comments": null,
            "PhonePrimaryContact": "+49(0) 800 88 88 862",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 105,
            "Title": "Innogy SE (RWE eMobility)"
        },
        {
            "WebsiteURL": "http://instavolt.co.uk/",
            "Comments": "Pay-as-you-go, charged per kWh, contactless bank card payment.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3296,
            "Title": "InstaVolt Ltd"
        },
        {
            "WebsiteURL": "https://www.ion.jo/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3457,
            "Title": "ION (Jordan)"
        },
        {
            "WebsiteURL": "http://www.ionity.eu/",
            "Comments": "NO*IOY,NL*IOY,FR*IOY,GB*IOY,IE*IOY,DE*IOY,BE*IOY,CH*IOY,IT*IOY,ES*IOY,HR*IOY,HU*IOY,PL*IOY,CZ*IOY,SK*IOY,AT*IOY,DK*IOY,SE*IOY,FI*IOY,EE*IOY,LV*IOY,LT*IOY Pan-European High-power CCS charging network joint venture of BMW Group, Daimler AG, Ford Motor Company and the Volkswagen Group",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3299,
            "Title": "Ionity"
        },
        {
            "WebsiteURL": "https://itcharge.ru/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3650,
            "Title": "it Charge (RU)"
        },
        {
            "WebsiteURL": "https://ivycharge.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-888-550-5155",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3416,
            "Title": "IVY"
        },
        {
            "WebsiteURL": "https://www.izivia.com/le-reseau-izivia",
            "Comments": "Formerly known as Sodetrel",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@sodetrel.fr",
            "FaultReportEmail": "sav@sodetrel.fr",
            "IsRestrictedEdit": false,
            "ID": 213,
            "Title": "Izivia (Sodetrel)"
        },
        {
            "WebsiteURL": "https://www.jec.co.uk/your-home/electric-vehicles/charging-your-ev/",
            "Comments": "Access via mechanical keyswitch, montly subscription fee.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3288,
            "Title": "Jersey Electricity Evolve"
        },
        {
            "WebsiteURL": "https://www.jetlocal.co.uk/jet-charge/",
            "Comments": null,
            "PhonePrimaryContact": "+44 808 1964572",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3752,
            "Title": "Jet Charge (UK)"
        },
        {
            "WebsiteURL": "https://www.jojusolar.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3393,
            "Title": "Joju Ltd"
        },
        {
            "WebsiteURL": "https://jolt.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3529,
            "Title": "Jolt"
        },
        {
            "WebsiteURL": "https://jomcharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3517,
            "Title": "Jom Charge"
        },
        {
            "WebsiteURL": "http://www.jopetrol.com.jo/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3458,
            "Title": "JoPetrol"
        },
        {
            "WebsiteURL": "http://www.juicepoint.co.nz/",
            "Comments": null,
            "PhonePrimaryContact": "+64 9 354 3869",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@juicepoint.co.nz",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 120,
            "Title": "JuicePoint"
        },
        {
            "WebsiteURL": "https://www.julepower.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3488,
            "Title": "Jule"
        },
        {
            "WebsiteURL": "https://justplugin.nl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3746,
            "Title": "Justplugin (NL)"
        },
        {
            "WebsiteURL": "https://k-lataus.fi",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3354,
            "Title": "K Lataus"
        },
        {
            "WebsiteURL": "https://filiale.kaufland.de/service/e-ladestationen.html",
            "Comments": null,
            "PhonePrimaryContact": "+49 71 32 / 94 13 33",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3714,
            "Title": "Kaufland eCharge"
        },
        {
            "WebsiteURL": "https://www.kelag.at/privat/kelag-autostrom-111.htm",
            "Comments": null,
            "PhonePrimaryContact": "+43 463 525 9660",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3285,
            "Title": "Kelag AG"
        },
        {
            "WebsiteURL": "https://kilowatt.ma",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3727,
            "Title": "Kilowatt.ma"
        },
        {
            "WebsiteURL": "http://www.kiwhipass.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@kiwhipass.fr",
            "FaultReportEmail": "assistance@kiwhipass.fr",
            "IsRestrictedEdit": null,
            "ID": 62,
            "Title": "KiWhi Pass"
        },
        {
            "WebsiteURL": "https://www.kiwev.co.nz/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3544,
            "Title": "Kiwi EV"
        },
        {
            "WebsiteURL": "https://www.kople.no/veiledning/ladepris",
            "Comments": null,
            "PhonePrimaryContact": "+47 32 11 00 11",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3536,
            "Title": "Kople"
        },
        {
            "WebsiteURL": "https://www.e-leclerc.com/catalogue/services/la-borne-electrique",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3411,
            "Title": "La Borne"
        },
        {
            "WebsiteURL": "https://ladopp.no/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3541,
            "Title": "Lad Opp"
        },
        {
            "WebsiteURL": "https://ladefoxx.de/",
            "Comments": null,
            "PhonePrimaryContact": "05261 255-251",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ladefoxx.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 106,
            "Title": "Ladefoxx"
        },
        {
            "WebsiteURL": "http://ladenetz.de",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": "info@smartlab-gmbh.de",
            "IsRestrictedEdit": false,
            "ID": 69,
            "Title": "ladenetz.de"
        },
        {
            "WebsiteURL": "https://lakd.lt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3691,
            "Title": "LAKD (LT)"
        },
        {
            "WebsiteURL": "https://lakelandsolutions.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-705-645-1550",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3761,
            "Title": "Lakeland Solutions"
        },
        {
            "WebsiteURL": "https://www.lastmilesolutions.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3387,
            "Title": "Last Mile Solutions"
        },
        {
            "WebsiteURL": "http://www.latvenergo.lv",
            "Comments": null,
            "PhonePrimaryContact": "+371 67 723 511",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@latvenergo.lv",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 182,
            "Title": "Latvenergo (LV)"
        },
        {
            "WebsiteURL": "https://leap24.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3504,
            "Title": "Leap24 (NL)"
        },
        {
            "WebsiteURL": "https://electracaldenseenergia.com/es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3770,
            "Title": "L'electra (ES)"
        },
        {
            "WebsiteURL": "http://lenenergo.ru/ev/",
            "Comments": "Utility in St. Petersburg, Russia",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3286,
            "Title": "Lenenergo"
        },
        {
            "WebsiteURL": "http://www.level2.ee/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3348,
            "Title": "Level2.ee"
        },
        {
            "WebsiteURL": "https://info.lidl/en",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 38,
            "Title": "Lidl"
        },
        {
            "WebsiteURL": "https://rawcharging.com/franklin/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3555,
            "Title": "LiFe (Raw Charging) (UK)"
        },
        {
            "WebsiteURL": "http://w41.bcn.cat/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 206,
            "Title": "LIVE Barcelona"
        },
        {
            "WebsiteURL": "https://www.solution.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3620,
            "Title": "Livingston Charge Port"
        },
        {
            "WebsiteURL": "https://loopglobal.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3757,
            "Title": "Loop"
        },
        {
            "WebsiteURL": "http://www.elektrofahrzeuge.lsw.de/",
            "Comments": null,
            "PhonePrimaryContact": " 05361 1893600",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "mobilitaet@lsw.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 128,
            "Title": "LSW Energie"
        },
        {
            "WebsiteURL": null,
            "Comments": "Obsolete inductive paddle charging standard",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 41,
            "Title": "MAGNE Charge"
        },
        {
            "WebsiteURL": "https://www.mainova.de/privatkunden/mobilitaet/stromtankstellen.html",
            "Comments": null,
            "PhonePrimaryContact": "069 / 213-24221 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "Efahrzeug-Foerderung@mainova.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 165,
            "Title": "Mainova"
        },
        {
            "WebsiteURL": "https://evportugal.maksu.com/pt",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3649,
            "Title": "Maksu (PT)"
        },
        {
            "WebsiteURL": "https://www.mgc-gas.jo/gasStations/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3456,
            "Title": "Manaseer"
        },
        {
            "WebsiteURL": "http://www.manxelectricity.com",
            "Comments": null,
            "PhonePrimaryContact": "(01624) 687687",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "mea@gov.im",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 135,
            "Title": "Manx Electricity Authority"
        },
        {
            "WebsiteURL": "https://www.maxol.ie/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3598,
            "Title": "Maxol"
        },
        {
            "WebsiteURL": "http://www.caib.es/sites/energiaicanviclimatic/ca/mobilitat_elactrica_a_les_illes_balears_melib/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3283,
            "Title": "MELIB (ES)"
        },
        {
            "WebsiteURL": "https://www.mer.eco/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3492,
            "Title": "MER"
        },
        {
            "WebsiteURL": "  https://www.mercadona.es/ ",
            "Comments": null,
            "PhonePrimaryContact": "900 500 103 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3499,
            "Title": "Mercadona"
        },
        {
            "WebsiteURL": "https://www.metropolis-recharge.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3490,
            "Title": "Métropolis"
        },
        {
            "WebsiteURL": "https://www.motorfuelgroup.com/mfg-ev-power/",
            "Comments": "Fossil fuel filling station franchise operator group now doing their own thing in EV charging",
            "PhonePrimaryContact": "+44 20 8515 8559",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3471,
            "Title": "MFG EV Power"
        },
        {
            "WebsiteURL": "https://www.midgardelectric.com/",
            "Comments": "Bangalore",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info.midgardelectric@gmail.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3363,
            "Title": "Midgard Electric"
        },
        {
            "WebsiteURL": "http://thefastchargernetwork.com/",
            "Comments": null,
            "PhonePrimaryContact": "+ 31 20 7719 026",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@mistergreen.nl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 112,
            "Title": "MisterGreen, The Fast Charger Network"
        },
        {
            "WebsiteURL": "http://www.mobecpoint.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@mobecpoint.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 92,
            "Title": "MobecPoint (Es)"
        },
        {
            "WebsiteURL": "http://www.mobib.be/index.htm",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 79,
            "Title": "Mobib (Belgium)"
        },
        {
            "WebsiteURL": "http://www.mobie.pt",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 21,
            "Title": "Mobie.pt"
        },
        {
            "WebsiteURL": "https://mobiliti.hu/emobilitas",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3467,
            "Title": "Mobiliti.hu"
        },
        {
            "WebsiteURL": "https://mobiliti.hu/emobilitas",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3468,
            "Title": "Mobiliti.hu"
        },
        {
            "WebsiteURL": "https://mobiliti.hu/emobilitas",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3469,
            "Title": "Mobiliti.hu"
        },
        {
            "WebsiteURL": "https://mobiliti.hu/emobilitas",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3470,
            "Title": "Mobiliti.hu"
        },
        {
            "WebsiteURL": "https://www.mobive.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3407,
            "Title": "MObiVE"
        },
        {
            "WebsiteURL": "https://molplugee.si/en",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3378,
            "Title": "MOL"
        },
        {
            "WebsiteURL": " https://monta.app/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@monta.app",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3479,
            "Title": "Monta"
        },
        {
            "WebsiteURL": "https://www.moon-power.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3644,
            "Title": "Moon Power"
        },
        {
            "WebsiteURL": "https://www.motionbox.gr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3476,
            "Title": "Motionbox"
        },
        {
            "WebsiteURL": "https://www.motonet.fi/fi/sivut/motolataus/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3355,
            "Title": "Motolataus"
        },
        {
            "WebsiteURL": "https://www.move.ch",
            "Comments": null,
            "PhonePrimaryContact": "0800 29 29 29",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3274,
            "Title": "MOVE (CH)"
        },
        {
            "WebsiteURL": "https://www.bayernwerk.de/cps/rde/xchg/bayernwerk/hs.xsl/278.htm",
            "Comments": null,
            "PhonePrimaryContact": "+49 89 61413-536",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "BAG-e-mobility@bayernwerk.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 201,
            "Title": "München Umland"
        },
        {
            "WebsiteURL": "https://www.mvmpartner.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "mvmp@mvmp.hu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3289,
            "Title": "MVM Partner Zrt."
        },
        {
            "WebsiteURL": "https://my.ecars.su/",
            "Comments": null,
            "PhonePrimaryContact": "8 804 333 28 86",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3701,
            "Title": "my.eCars (RU)"
        },
        {
            "WebsiteURL": "https://www.naturenergie.de/e-mobil/oeffentliche-ladeinfrastruktur",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 224,
            "Title": "Naturenergie (DE)"
        },
        {
            "WebsiteURL": "https://www.naturgy.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3573,
            "Title": "Naturgy (ES)"
        },
        {
            "WebsiteURL": "https://echargenetwork.com/",
            "Comments": null,
            "PhonePrimaryContact": "+1 844 661‑6272",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3365,
            "Title": "NBP eCharge Network"
        },
        {
            "WebsiteURL": "https://www.neoenergia.com/pt-br/te-interessa/inovacao/Paginas/mobilidade-eletrica.aspx",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3568,
            "Title": "NeoEnergia"
        },
        {
            "WebsiteURL": "https://www.neogy.it/",
            "Comments": null,
            "PhonePrimaryContact": "800 832 855",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@neogy.it",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 164,
            "Title": "Neogy"
        },
        {
            "WebsiteURL": "https://www.n-ergie.de/header/die-n-ergie/aktiv-fuer-die-umwelt/elektromobilitaet.html",
            "Comments": null,
            "PhonePrimaryContact": "+49 911 80201",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elektromobilitaet@n-ergie.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 234,
            "Title": "N-ERGIE"
        },
        {
            "WebsiteURL": "https://neste.fi/",
            "Comments": null,
            "PhonePrimaryContact": "+358800196196",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3596,
            "Title": "Neste Lataus"
        },
        {
            "WebsiteURL": "https://nextstepmobility.de/",
            "Comments": null,
            "PhonePrimaryContact": "+497243 2006101",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@nextstepmobility.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3466,
            "Title": "Next Step Mobility (DE)"
        },
        {
            "WebsiteURL": "https://nextcharge.app/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3657,
            "Title": "NEXTCHARGE"
        },
        {
            "WebsiteURL": "https://www.nissan.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3558,
            "Title": "Nissan (ES) Dealer Network"
        },
        {
            "WebsiteURL": "http://www.nissan.de/DE/de/vehicle/electric-vehicles/leaf/charging-and-battery/freistrom-info.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 167,
            "Title": "Nissan DE Freistrom"
        },
        {
            "WebsiteURL": "http://www.nissan.co.uk",
            "Comments": "Network of franchised Nissan Dealers",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 7,
            "Title": "Nissan UK Dealer Network"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 6,
            "Title": "Nissan US Dealer Network"
        },
        {
            "WebsiteURL": "http://www.mobiliti.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3307,
            "Title": "NKM mobiliti"
        },
        {
            "WebsiteURL": "http://www.nomadpower.eu",
            "Comments": null,
            "PhonePrimaryContact": "+31 348435512",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@nomadpower.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 196,
            "Title": "Nomadpower"
        },
        {
            "WebsiteURL": "http://www.noodoe.com/ev",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3346,
            "Title": "Noodoe EV"
        },
        {
            "WebsiteURL": "https://www.northecharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3766,
            "Title": "Northe (SE)"
        },
        {
            "WebsiteURL": "https://www.nrgevgo.com/",
            "Comments": null,
            "PhonePrimaryContact": "855-509-5581",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3252,
            "Title": "NRG EVgo"
        },
        {
            "WebsiteURL": "https://customer.restation.eu/stations",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@nrg4you.it",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3438,
            "Title": "NRG4YOU"
        },
        {
            "WebsiteURL": "https://www.nrgincharge.gr/en",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3491,
            "Title": "NRGincharge"
        },
        {
            "WebsiteURL": "https://www.mynrma.com.au/cars-and-driving/electric-vehicles",
            "Comments": "National Roads and Motorists' Association, Australia",
            "PhonePrimaryContact": "1300 233 544",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3388,
            "Title": "NRMA"
        },
        {
            "WebsiteURL": "http://www.nuon.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 177,
            "Title": "Nuon"
        },
        {
            "WebsiteURL": "https://oeste.solar/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3608,
            "Title": "OESTE Movilidad (ES)"
        },
        {
            "WebsiteURL": "https://www.ok.dk/privat/produkter/opladning/ude/ladestander-priser",
            "Comments": null,
            "PhonePrimaryContact": "+45 89 32 24 88",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3791,
            "Title": "OK (DK)"
        },
        {
            "WebsiteURL": "https://www.okq8.se/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3763,
            "Title": "OKQ8 (SE)"
        },
        {
            "WebsiteURL": "https://olife-energy.net/",
            "Comments": null,
            "PhonePrimaryContact": "+420 724 196 587",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@olife-energy.com",
            "FaultReportEmail": "info@olife-energy.com",
            "IsRestrictedEdit": false,
            "ID": 3425,
            "Title": "OlifeEnergy"
        },
        {
            "WebsiteURL": "https://www.ontherunstores.com/ev-charging",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3756,
            "Title": "On the Run (CA)"
        },
        {
            "WebsiteURL": "https://www.oncharge.com.tr/",
            "Comments": null,
            "PhonePrimaryContact": "+90 216 706 00 10",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3600,
            "Title": "OnCharge (TR)"
        },
        {
            "WebsiteURL": "https://www.opconnect.com/",
            "Comments": null,
            "PhonePrimaryContact": "1-855-885-9571",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "nisaacs@opconnect.com",
            "FaultReportEmail": "support@opconnect.com",
            "IsRestrictedEdit": false,
            "ID": 107,
            "Title": "OpConnect"
        },
        {
            "WebsiteURL": "https://www.openloop.co.nz/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3527,
            "Title": "OpenLoop"
        },
        {
            "WebsiteURL": "https://optimile.eu/",
            "Comments": "BE*OPT",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3590,
            "Title": "Optimile"
        },
        {
            "WebsiteURL": "https://optimumway.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@optimumway.hu",
            "FaultReportEmail": "info@optimumway.hu",
            "IsRestrictedEdit": false,
            "ID": 3395,
            "Title": "Optimum Way"
        },
        {
            "WebsiteURL": "http://www.ores.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1236,
            "Title": "ORES"
        },
        {
            "WebsiteURL": "https://oriontelekom.rs/emobility/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3585,
            "Title": "Orion Telekom (Serbia)"
        },
        {
            "WebsiteURL": "http://www.on.is/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "on@on.is",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 102,
            "Title": "Orka Náttúrunnar"
        },
        {
            "WebsiteURL": "https://www.ov.is/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3708,
            "Title": "Orkubú Vestfjarða"
        },
        {
            "WebsiteURL": "https://orlencharge.orlen.pl/",
            "Comments": null,
            "PhonePrimaryContact": " +48502167536",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3396,
            "Title": "Orlencharge"
        },
        {
            "WebsiteURL": "https://ospreycharging.co.uk/ev-drivers/",
            "Comments": "GB*OSP,formerly known as Engenie",
            "PhonePrimaryContact": "0330 010 1757",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@ospreycharging.co.uk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 203,
            "Title": "Osprey Charging"
        },
        {
            "WebsiteURL": "https://www.osterholzer-stadtwerke.de/service/fahren-mit-strom-erdgas/strom/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 124,
            "Title": "Osterholzer Stadtwerke"
        },
        {
            "WebsiteURL": "https://ouestcharge.fr",
            "Comments": null,
            "PhonePrimaryContact": "+33 2 52 07 00 06",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "seviceclient@ouestcharge.fr",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3640,
            "Title": "Ouest Charge"
        },
        {
            "WebsiteURL": "http://www.ovag-energie.de/oe/ovag-energie.nsf/c/Umwelt,E-Mobilit%C3%A4t",
            "Comments": null,
            "PhonePrimaryContact": "+49 6031 6848-0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service@ovag-energie.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 188,
            "Title": "OVAG Energie"
        },
        {
            "WebsiteURL": "http://www.park-charge.ch/",
            "Comments": null,
            "PhonePrimaryContact": "+41 44 820 24 55  ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "park-charge@gmx.net",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 97,
            "Title": "Park & Charge (CH)"
        },
        {
            "WebsiteURL": "http://www.park-charge.de/",
            "Comments": null,
            "PhonePrimaryContact": "030-32 59 91 80 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@park-charge.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 98,
            "Title": "Park & Charge (D)"
        },
        {
            "WebsiteURL": "https://www.parkeasy.co/",
            "Comments": null,
            "PhonePrimaryContact": "+60 16-299 1468",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3518,
            "Title": "ParkEasy"
        },
        {
            "WebsiteURL": "https://www.parkkisahko.fi/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3322,
            "Title": "Parking Energy"
        },
        {
            "WebsiteURL": "https://passpasselectrique.fr",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3409,
            "Title": "pass pass électrique"
        },
        {
            "WebsiteURL": "http://www.paz.co.il/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3531,
            "Title": "Paz (Israel)"
        },
        {
            "WebsiteURL": "https://www.pcharge.com.cy/",
            "Comments": "CY*PHL",
            "PhonePrimaryContact": "+357 80002100",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@pcharge.com.cy",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3773,
            "Title": "PCharge"
        },
        {
            "WebsiteURL": "https://www.pea.co.th/",
            "Comments": "Provincial Electricity Authority, Thailand",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3460,
            "Title": "PEA Volta"
        },
        {
            "WebsiteURL": "https://www.petro-canada.ca/en/personal/fuel/ev-fast-charge-network",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3375,
            "Title": "Petro-Canada"
        },
        {
            "WebsiteURL": "http://www.petrol.eu/road/car/electrical-mobility-petrol",
            "Comments": "PETROL is a fuel supplier and runs charge points in Slovenia, part of the CENTRAL EUROPEAN GREEN CORRIDORS (CEGC) PROJECT",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 13,
            "Title": "PETROL"
        },
        {
            "WebsiteURL": "https://sarjweb.petroo.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3751,
            "Title": "Petroo (TR)"
        },
        {
            "WebsiteURL": "http://www.pfalzwerke.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 6215850",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@pfalzwerke.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1240,
            "Title": "Pfalzwerke"
        },
        {
            "WebsiteURL": "https://pgene.pl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3397,
            "Title": "PGE Nowa Energia"
        },
        {
            "WebsiteURL": "https://pkp.pl/pkpmobility",
            "Comments": null,
            "PhonePrimaryContact": "+48509895890",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "stacjeladowania@pkp.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3453,
            "Title": "PKP Mobility"
        },
        {
            "WebsiteURL": "https://placetoplug.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3556,
            "Title": "Place To Plug"
        },
        {
            "WebsiteURL": "https://plenoil.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3750,
            "Title": "Plenoil (ES)"
        },
        {
            "WebsiteURL": "https://web.pln.co.id/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3664,
            "Title": "PLN (Indonesia)"
        },
        {
            "WebsiteURL": "https://plug-n-go.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3613,
            "Title": "Plug N Go Ltd"
        },
        {
            "WebsiteURL": "https://plugnroll.com/elektroautofahrer/netzwerk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3280,
            "Title": "Plug n Roll"
        },
        {
            "WebsiteURL": "http://www.pluggedinmidlands.co.uk",
            "Comments": null,
            "PhonePrimaryContact": "0845 838 0551",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "enquiries@pluggedinmidlands.co.uk",
            "FaultReportEmail": "enquiries@pluggedinmidlands.co.uk",
            "IsRestrictedEdit": false,
            "ID": 71,
            "Title": "Plugged In Midlands (UK)"
        },
        {
            "WebsiteURL": "http://www.pluginncw.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "plugincenter@gmail.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 119,
            "Title": "Plug-In North Central Washington"
        },
        {
            "WebsiteURL": "https://www.plugitcloud.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3353,
            "Title": "Plugit"
        },
        {
            "WebsiteURL": "https://www.plugpoint.ro/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3420,
            "Title": "plugpoint.ro"
        },
        {
            "WebsiteURL": "https://www.plugsurfing.com/",
            "Comments": null,
            "PhonePrimaryContact": "+49 30 9599814 10 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@plugsurfing.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3266,
            "Title": "PlugSurfing"
        },
        {
            "WebsiteURL": "http://www.pobad.co/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3483,
            "Title": "POBAD International"
        },
        {
            "WebsiteURL": "http://www.pod-point.com/",
            "Comments": "Part of Groupe EDF",
            "PhonePrimaryContact": "020 7247 4114",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "enquiries@pod-point.com",
            "FaultReportEmail": "enquiries@pod-point.com",
            "IsRestrictedEdit": false,
            "ID": 3,
            "Title": "POD Point (UK)"
        },
        {
            "WebsiteURL": "https://pogocharge.com/",
            "Comments": "Sub-Brand of SWARCO Smart Charging.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3769,
            "Title": "Pogo Charge (GB)"
        },
        {
            "WebsiteURL": "https://polenergia-emobility.pl",
            "Comments": null,
            "PhonePrimaryContact": "+48514850100",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "bok.pem@polenergia.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3611,
            "Title": "Polenergia eMobility"
        },
        {
            "WebsiteURL": "http://polyfazer.cz/",
            "Comments": null,
            "PhonePrimaryContact": "+420 270 007 900﻿",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@polyfazer.cz",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1239,
            "Title": "Polyfazer (CZ)"
        },
        {
            "WebsiteURL": "https://polyfazer.ro/map/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3520,
            "Title": "Polyfazer (RO)"
        },
        {
            "WebsiteURL": null,
            "Comments": "GB*911,AT*911,CH*911,DE*911,LU*911,NO*911",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3523,
            "Title": "Porsche Smart Mobility GmbH"
        },
        {
            "WebsiteURL": "https://portalenergy.tech/",
            "Comments": null,
            "PhonePrimaryContact": "8 812 565 50 59",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3702,
            "Title": "Portal Energy (RU)"
        },
        {
            "WebsiteURL": "https://powerdot.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3538,
            "Title": "Power Dot"
        },
        {
            "WebsiteURL": "http://power-station.be/power-card-laadpas/",
            "Comments": null,
            "PhonePrimaryContact": "+32 (0)488 985 200",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@power-station.be",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 114,
            "Title": "Power Station"
        },
        {
            "WebsiteURL": "https://powerdot.es/",
            "Comments": null,
            "PhonePrimaryContact": "+34 91 901 4816",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@powerdot.es",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3550,
            "Title": "PowerDot (Es)"
        },
        {
            "WebsiteURL": "https://www.powerflex.com/technologies/ev-charging/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3618,
            "Title": "Powerflex"
        },
        {
            "WebsiteURL": "https://www.powergo.es/public-charging/",
            "Comments": "Charge using the PowerGo Charge App.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3632,
            "Title": "PowerGo (ES)"
        },
        {
            "WebsiteURL": "https://www.powersarj.com/",
            "Comments": null,
            "PhonePrimaryContact": "+90 850 308 9696",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3602,
            "Title": "Powerşarj"
        },
        {
            "WebsiteURL": "https://powy.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3586,
            "Title": "POWY"
        },
        {
            "WebsiteURL": "https://www.pre.cz/cs/profil-spolecnosti/dalsi-aktivity-pre/premobilita/",
            "Comments": null,
            "PhonePrimaryContact": "840 550 055",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 190,
            "Title": "PRE (cz)"
        },
        {
            "WebsiteURL": "http://www.prioenergy.com/produtos-e-servicos/mobilidade-electrica/",
            "Comments": "Prio.E Mobility Solutions",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 200,
            "Title": "PRIOE"
        },
        {
            "WebsiteURL": "https://procreditbank-kos.com/eng/news/procredit-bank-launches-mobile-application-fo-1485/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3576,
            "Title": "Procredit"
        },
        {
            "WebsiteURL": "https://www.projectev.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "0800 599 9582",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3629,
            "Title": "Project EV"
        },
        {
            "WebsiteURL": "https://protergiacharge.gr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3501,
            "Title": "Protergia Charge"
        },
        {
            "WebsiteURL": "https://punkt-e.ru/",
            "Comments": null,
            "PhonePrimaryContact": "+78002223700",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3634,
            "Title": "Punkt-E"
        },
        {
            "WebsiteURL": "http://www.putevi-srbije.rs/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3358,
            "Title": "Putevi Srbije / ЈП Путеви Србије / Roads of Serbia"
        },
        {
            "WebsiteURL": "https://www.q1.eu/",
            "Comments": null,
            "PhonePrimaryContact": "+49 541 602-0",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3429,
            "Title": "Q1 Autostrom"
        },
        {
            "WebsiteURL": "https://www.qovoltis.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3495,
            "Title": "Qovoltis"
        },
        {
            "WebsiteURL": "https://www.qld.gov.au/transport/projects/electricvehicles/map",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3317,
            "Title": "Queensland Electric Super Highway"
        },
        {
            "WebsiteURL": "https://www.r3-charge.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3484,
            "Title": "R3"
        },
        {
            "WebsiteURL": "http://chargestar.com.au/rac-electric-highway/",
            "Comments": null,
            "PhonePrimaryContact": "1300 661895",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@chargestar.com.au",
            "FaultReportEmail": "info@chargestar.com.au",
            "IsRestrictedEdit": false,
            "ID": 194,
            "Title": "RAC Electric Highway/ChargeStar"
        },
        {
            "WebsiteURL": "http://www.raumanenergia.fi/yritys/fi_FI/sahkoautoilu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 133,
            "Title": "Rauman Energia"
        },
        {
            "WebsiteURL": "https://revitalizechargingsolutions.com/",
            "Comments": null,
            "PhonePrimaryContact": " 1-817-659-1030",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@revitalizechargingsolutions.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 217,
            "Title": "RCS (Revitalize Charging Solutions)"
        },
        {
            "WebsiteURL": "http://www.rechargeinfra.com/",
            "Comments": null,
            "PhonePrimaryContact": "+358 20 33 4455",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "rami.syvari@fortum.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 198,
            "Title": "Recharge (Formerly Fortum Charge & Drive)"
        },
        {
            "WebsiteURL": "https://www.rechargealaska.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3580,
            "Title": "Recharge Alaska"
        },
        {
            "WebsiteURL": "http://www.recharge-power.com/",
            "Comments": "Imported by ADFC import",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 12,
            "Title": "RechargeAccess"
        },
        {
            "WebsiteURL": "https://www.redecharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3696,
            "Title": "Red E Charge"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3335,
            "Title": "RedePiloto"
        },
        {
            "WebsiteURL": "https://reev.com/",
            "Comments": "DE*ONE",
            "PhonePrimaryContact": "+49 89 889 970 48 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@reev.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3582,
            "Title": "Reev (DE)"
        },
        {
            "WebsiteURL": "https://reluxelectric.com/",
            "Comments": null,
            "PhonePrimaryContact": "044 2233 0402",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3777,
            "Title": "Relux Electric (India)"
        },
        {
            "WebsiteURL": "http://www.renault.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3275,
            "Title": "Renault"
        },
        {
            "WebsiteURL": "https://renewing.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3684,
            "Title": "Renewing (PT)"
        },
        {
            "WebsiteURL": "https://www.repower.com/it/la-mobilita-elettrica/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3330,
            "Title": "Repower (Italy)"
        },
        {
            "WebsiteURL": "https://www.repsol.es/particulares/vehiculos/movilidad-electrica/",
            "Comments": null,
            "PhonePrimaryContact": "902 540 810",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 91,
            "Title": "Repsol - Ibil (ES)"
        },
        {
            "WebsiteURL": "https://www.reveocharge.com/",
            "Comments": "Sud de la France",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3257,
            "Title": "Révéo (FR)"
        },
        {
            "WebsiteURL": "https://www.revoltaegypt.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@revoltaegypt.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3293,
            "Title": "Revolta Egypt"
        },
        {
            "WebsiteURL": "https://www.rewag.de/privatkunden/strom/rewariostrommobil.html",
            "Comments": null,
            "PhonePrimaryContact": " +49 941 6010",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@rewag.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3265,
            "Title": "REWAG"
        },
        {
            "WebsiteURL": "https://rexharge.net/",
            "Comments": null,
            "PhonePrimaryContact": "+6011 5166 2025",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3610,
            "Title": "Rexcharge (Malaysia)"
        },
        {
            "WebsiteURL": "http://www.rheinenergie.com/TankEn-Registrierung",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "energieberatung@rheinenergie.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 72,
            "Title": "RheinEnergie AG"
        },
        {
            "WebsiteURL": "https://re-fd.de/",
            "Comments": null,
            "PhonePrimaryContact": "+49 661 12-100",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@re-fd.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2242,
            "Title": "RhönEnergie"
        },
        {
            "WebsiteURL": "https://rivian.com/support/article/where-are-rivian-adventure-network-chargers-located",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3607,
            "Title": "Rivian Adventure Network"
        },
        {
            "WebsiteURL": "https://rivian.com/experience/charging",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3617,
            "Title": "Rivian Waypoints L2 Network"
        },
        {
            "WebsiteURL": "https://rompetrol.ro",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3421,
            "Title": "Rompetrol"
        },
        {
            "WebsiteURL": "https://rossetimr.ru/",
            "Comments": "App: rs.em",
            "PhonePrimaryContact": "+78002200220",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3633,
            "Title": "Rosseti (RU"
        },
        {
            "WebsiteURL": "http://rpsnet.cz",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3250,
            "Title": "RPSnet"
        },
        {
            "WebsiteURL": "https://charge.rubicon.tech/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3782,
            "Title": "Rubicon E-Mobility"
        },
        {
            "WebsiteURL": "http://www.npower.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 104,
            "Title": "RWE / Npower"
        },
        {
            "WebsiteURL": "http://www.essent.nl",
            "Comments": "Essent is part of the RWE group",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 48,
            "Title": "RWE Mobility/Essent"
        },
        {
            "WebsiteURL": "https://sa-ev.com",
            "Comments": "India",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "sa@sa-ev.com",
            "FaultReportEmail": "sa@sa-ev.com",
            "IsRestrictedEdit": false,
            "ID": 3376,
            "Title": "SAEV"
        },
        {
            "WebsiteURL": "http://www.sahkoinenliikenne.fi/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sahkoinenliikenne.fi",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 113,
            "Title": "Sähköinenliikenne (fi)"
        },
        {
            "WebsiteURL": "http://www.saiel.it/it_IT/rep/divisione_energia/mobilita_elettrica",
            "Comments": null,
            "PhonePrimaryContact": "+39 434 759167 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3521,
            "Title": "Saiel (IT)"
        },
        {
            "WebsiteURL": "https://smartcharge.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": "+44 345 850 5247",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3747,
            "Title": "Sainsbury's Smart Charge (UK)"
        },
        {
            "WebsiteURL": "https://www.salzburg-ag.at/e-mobilitaet/elektromobilitaet.html",
            "Comments": "AT*SZG",
            "PhonePrimaryContact": "+43 800 660 660",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3713,
            "Title": "Salzburg AG"
        },
        {
            "WebsiteURL": " http://www.sarjon.com.tr",
            "Comments": null,
            "PhonePrimaryContact": "+90 216 387 0620",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3561,
            "Title": "Şarjon (TR)"
        },
        {
            "WebsiteURL": "https://www.schleswiger-stadtwerke.de/content/unternehmen/emobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": "(0 46 21) 801-414",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "matthias.beier@schleswiger-stadtwerke.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 139,
            "Title": "Schleswiger Stadtwerke"
        },
        {
            "WebsiteURL": "http://www.schnell-laden-berlin.de",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "wirkuemmernuns@schnell-laden-berlin.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 223,
            "Title": "Schnell Laden Berlin"
        },
        {
            "WebsiteURL": "https://www.swu.de/privatkunden/energie-wasser/elektromobilitaet/kunde-werden.html",
            "Comments": null,
            "PhonePrimaryContact": "+49 731 166-8810",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@swu.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2245,
            "Title": "Schwabencard"
        },
        {
            "WebsiteURL": "https://www.scottishpower.co.uk",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3537,
            "Title": "Scottish Power"
        },
        {
            "WebsiteURL": "http://www.sde76.fr/",
            "Comments": "Can be Accessed via Sodetrel pass",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3262,
            "Title": "SDE76 (FR)"
        },
        {
            "WebsiteURL": "https://sdeg16.fr/nos-competences/les-bornes-vehicules-electriques/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3380,
            "Title": "SDEG 16 (Syndicat Départemental d'Electricité et de Gaz de la Charente)"
        },
        {
            "WebsiteURL": "https://www.te81.fr/transition-energetique/bornes-de-recharge-pour-vehicules-electriques/",
            "Comments": "+33 5 63 43 21 40",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3654,
            "Title": "SDET (FR)"
        },
        {
            "WebsiteURL": "http://sdey.fr/nos-missions/mobilite-electrique/",
            "Comments": "Syndicat Départemental d'Énergies de l'Yonne",
            "PhonePrimaryContact": "03 86 52 22 00",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 33,
            "Title": "SDEY (Fr)"
        },
        {
            "WebsiteURL": "https://semaconnect.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 39,
            "Title": "SemaConnect"
        },
        {
            "WebsiteURL": "https://www.seom.se/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3347,
            "Title": "Seom"
        },
        {
            "WebsiteURL": "https://www.7ev.co.il",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3635,
            "Title": "Seven (IL)"
        },
        {
            "WebsiteURL": "https://www.sfa-ss.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3721,
            "Title": "SFA Sustainability Services"
        },
        {
            "WebsiteURL": "https://www.sha7en.co",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sha7en.co",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3743,
            "Title": "Sha7en (Egypt)"
        },
        {
            "WebsiteURL": "https://www.sharz.net/",
            "Comments": null,
            "PhonePrimaryContact": " (0850) 811 72 75",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3367,
            "Title": "Sharz.Net"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/fr-fr",
            "Comments": null,
            "PhonePrimaryContact": "+33 9 77 55 43 49",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3709,
            "Title": "Shell EV Charging Solutions France"
        },
        {
            "WebsiteURL": "https://www.shell.es/movilidad-electrica.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3508,
            "Title": "Shell Recharge (ES) (Cable Energia)"
        },
        {
            "WebsiteURL": "https://www.shell.in/motorists/shell-recharge.html",
            "Comments": "Shell India",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3778,
            "Title": "Shell Recharge (IN)"
        },
        {
            "WebsiteURL": "https://www.shell.com.my/motorists/shell-recharge/shell-recharge-hpc.html",
            "Comments": "quite different network to that operated in Europe",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3591,
            "Title": "Shell Recharge (Malaysia)"
        },
        {
            "WebsiteURL": "https://shell.co.id",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3666,
            "Title": "Shell Recharge Indonesia"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/nl-be/solutions",
            "Comments": null,
            "PhonePrimaryContact": " +32 (0)2 588 1251",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@thenewmotion.be",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 157,
            "Title": "Shell Recharge Solutions (BE)"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/de-de/solutions",
            "Comments": null,
            "PhonePrimaryContact": "030 215 028 48",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@thenewmotion.de",
            "FaultReportEmail": "service@thenewmotion.de",
            "IsRestrictedEdit": false,
            "ID": 156,
            "Title": "Shell Recharge Solutions (DE)"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/nl-nl/solutions",
            "Comments": null,
            "PhonePrimaryContact": "088 01 09 500",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@thenewmotion.com",
            "FaultReportEmail": "klantenservice@thenewmotion.com",
            "IsRestrictedEdit": false,
            "ID": 47,
            "Title": "Shell Recharge Solutions (NL)"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/en-gb/solutions",
            "Comments": "Shell Recharge",
            "PhonePrimaryContact": "08000294601",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3392,
            "Title": "Shell Recharge Solutions (UK)"
        },
        {
            "WebsiteURL": "https://shellrecharge.com/en-us/solutions",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 59,
            "Title": "Shell Recharge Solutions (US)"
        },
        {
            "WebsiteURL": "http://www.shorepower.com/",
            "Comments": "Imported by ADFC import",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 14,
            "Title": "Shorepower"
        },
        {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3308,
            "Title": "SIEL"
        },
        {
            "WebsiteURL": "https://www.sigeif.fr/",
            "Comments": null,
            "PhonePrimaryContact": "+33 1 44 13 92 44",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3512,
            "Title": "Sigeif (FR)"
        },
        {
            "WebsiteURL": "http://www.silfi.it/IT/index.php?id=63&label=Mappa%20colonnine%20ricarica%20veicoli%20elettrici%22",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 81,
            "Title": "Silfi (Italy)"
        },
        {
            "WebsiteURL": "https://www.silverstonegreenenergy.co.uk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3615,
            "Title": "Silverstone Green Energy"
        },
        {
            "WebsiteURL": "https://sitronics.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3656,
            "Title": "Sitronics Electro (RU)"
        },
        {
            "WebsiteURL": "https://sepredaj.seas.sk/elektricka-mobilita",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sepredaj.sk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2246,
            "Title": "Slovenské elektrárne"
        },
        {
            "WebsiteURL": "https://www.smappee.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3754,
            "Title": "Smappee"
        },
        {
            "WebsiteURL": "https://smart-charge.com.au/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3658,
            "Title": "Smart Charge (AU)"
        },
        {
            "WebsiteURL": "https://smatrics.com/ladenetz#",
            "Comments": "SMATRICS runs charge points in Austria and Germany, part of the CENTRAL EUROPEAN GREEN CORRIDORS (CEGC) PROJECT",
            "PhonePrimaryContact": " +43 1 532 24 00",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@smatrics.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3253,
            "Title": "SMATRICS Netz"
        },
        {
            "WebsiteURL": "https://en.sodo.si/fast-charging-stations/list-of-active-fast-charging-stations-on-slovenian-highways",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3255,
            "Title": "SODO"
        },
        {
            "WebsiteURL": "http://www.sofos.es/productos-y-servicios/estaciones-de-recarga/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 211,
            "Title": "sofos"
        },
        {
            "WebsiteURL": "https://solarhub.net.au/solarhub-charge/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3719,
            "Title": "SolarHub Charge (AU)"
        },
        {
            "WebsiteURL": "https://account.sonolevi.co.il/findCharger",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3433,
            "Title": "Sonol-evi (Israel)"
        },
        {
            "WebsiteURL": "http://www.sourceeast.net/",
            "Comments": "Defunct network.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "sourceeast@sourceeast.net",
            "FaultReportEmail": "sourceeast@sourceeast.net",
            "IsRestrictedEdit": true,
            "ID": 60,
            "Title": "Source East (UK)"
        },
        {
            "WebsiteURL": "http://www.sourcelondon.net/",
            "Comments": "Monthly post-payment membership system, with per-minute billing and optional lower tariffs in return for monthly subscription payment.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": "https://www.sourcelondon.net/membership",
            "ContactEmail": "membership@sourcelondon.net",
            "FaultReportEmail": "membership@sourcelondon.net",
            "IsRestrictedEdit": false,
            "ID": 25,
            "Title": "Source London"
        },
        {
            "WebsiteURL": "http://sparkev.lk/smart-plug-in-membership/",
            "Comments": null,
            "PhonePrimaryContact": "+94117590590",
            "PhoneSecondaryContact": "+94117727539",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sparkev.lk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 228,
            "Title": "Spark EV (lk)"
        },
        {
            "WebsiteURL": "https://www.sperto.dk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sperto.dk",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3522,
            "Title": "Sperto (DK)"
        },
        {
            "WebsiteURL": "https://www.emotion-team.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3329,
            "Title": "SpotLink – e.motion"
        },
        {
            "WebsiteURL": "http://www.sw-magdeburg.de/",
            "Comments": null,
            "PhonePrimaryContact": " 0800 0796796",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@sw-magdeburg.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 152,
            "Title": "Städtische Werke Magdeburg"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-clausthal.de/",
            "Comments": null,
            "PhonePrimaryContact": " 05323 715-0 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-clausthal.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 162,
            "Title": "Stadtwerke Clausthal-Zellerfeld"
        },
        {
            "WebsiteURL": "https://www.dvv-dessau.de/",
            "Comments": null,
            "PhonePrimaryContact": " 0340 8992000",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 158,
            "Title": "Stadtwerke Dessau"
        },
        {
            "WebsiteURL": "https://www.swd-ag.de",
            "Comments": null,
            "PhonePrimaryContact": "0211/821-8210",
            "PhoneSecondaryContact": "0211/821-4093 (Emergency Contact Number 24/7)",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elektromobilitaet@swd-ag.de",
            "FaultReportEmail": "elektromobilitaet@swd-ag.de",
            "IsRestrictedEdit": false,
            "ID": 235,
            "Title": "Stadtwerke Düsseldorf AG"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-elmshorn.de/cms/Dienstleistungen/E-Mobilitaet/Stadtwerke-investieren-in-E-Mobilitaet-.html",
            "Comments": null,
            "PhonePrimaryContact": "(04121) 645-0",
            "PhoneSecondaryContact": "(04121) 645-751",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-elmshorn.de",
            "FaultReportEmail": "service.technik@stadtwerke-elmshorn.de",
            "IsRestrictedEdit": false,
            "ID": 170,
            "Title": "Stadtwerke Elmshorn"
        },
        {
            "WebsiteURL": "http://www.swgoe.de/",
            "Comments": null,
            "PhonePrimaryContact": "0551 301290",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 132,
            "Title": "Stadtwerke Göttingen"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-gvm.de/",
            "Comments": null,
            "PhonePrimaryContact": "03881 78450",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-gvm.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 151,
            "Title": "Stadtwerke Grevesmühlen"
        },
        {
            "WebsiteURL": "http://www.swhdl.de/strom/e_mobility/",
            "Comments": null,
            "PhonePrimaryContact": "03904 725995 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 148,
            "Title": "Stadtwerke Haldensleben  SWH"
        },
        {
            "WebsiteURL": "http://www.evh.de/EVH/Privatkunden/Natuerlich-EVH/Mit-Strom-fahren/",
            "Comments": null,
            "PhonePrimaryContact": "(0345) 581 33 33",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kontakt@evh.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 161,
            "Title": "Stadtwerke Halle"
        },
        {
            "WebsiteURL": "https://www.stadtwerke-hameln.de/service/beratung.html",
            "Comments": null,
            "PhonePrimaryContact": " 05151-7880",
            "PhoneSecondaryContact": " 0800 788 0000",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 146,
            "Title": "Stadtwerke Hameln"
        },
        {
            "WebsiteURL": "http://www.swl.de/web/swl/DE/Unternehmen/Elektromobilitaet/Elektromobilitaet.htm",
            "Comments": null,
            "PhonePrimaryContact": "0341 121-6404",
            "PhoneSecondaryContact": "0800 121-3001 ",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elektromobilitaet@swl.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 155,
            "Title": "Stadtwerke Leipzig SWL"
        },
        {
            "WebsiteURL": "http://www.swhl.de/e-mobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 123,
            "Title": "Stadtwerke Lübeck"
        },
        {
            "WebsiteURL": "https://www.stadtwerke-muenster.de/privatkunden/strom/alle-stromprodukte/e-mobilitaet/uebersicht.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 225,
            "Title": "Stadtwerke Münster"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-neumuenster.de/wDeutsch/privatkunden/unser-einsatz-fuer-die-umwelt/e-mobilitaet.php?navid=172",
            "Comments": null,
            "PhonePrimaryContact": " 04321 202654 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "swn@swn.net",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 147,
            "Title": "Stadtwerke Neumünster (SWN)."
        },
        {
            "WebsiteURL": "http://www.stadtwerke-northeim.de/site/de/580/stromtankstelle.html",
            "Comments": null,
            "PhonePrimaryContact": "(0 55 51) 60 05 - 0 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-northeim.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 131,
            "Title": "Stadtwerke Northeim  SWN"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-rinteln.de/",
            "Comments": null,
            "PhonePrimaryContact": "05751 700-0 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-rinteln.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 143,
            "Title": "Stadtwerke Rinteln"
        },
        {
            "WebsiteURL": "http://www.swrag.de/",
            "Comments": null,
            "PhonePrimaryContact": " 0381 8051901",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kundenzentrum@swrag.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 154,
            "Title": "Stadtwerke Rostock"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-soest.de/index.php?id=280",
            "Comments": null,
            "PhonePrimaryContact": "02921.392-0",
            "PhoneSecondaryContact": "02921.392-150",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stadtwerke-soest.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 149,
            "Title": "Stadtwerke Soest"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-stralsund.de/energie/elektrofahrzeuge/elektrofahrzeuge/foerderung.php",
            "Comments": null,
            "PhonePrimaryContact": " 03831 2410",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service@stadtwerke-stralsund.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 153,
            "Title": "Stadtwerke Strahlsund"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-uetersen.de/?page_id=1722",
            "Comments": null,
            "PhonePrimaryContact": " +49 4122 92786 80",
            "PhoneSecondaryContact": "04122 / 9 27 86 82",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service@stadtwerke-uetersen.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 169,
            "Title": "Stadtwerke Uetersen"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-verden.de/privatkunden/energiedienstleistungen/elektromobilitaet.html",
            "Comments": null,
            "PhonePrimaryContact": "04231 915112",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 134,
            "Title": "Stadtwerke Verden"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-wernigerode.de/published_page.aspx?id=132",
            "Comments": null,
            "PhonePrimaryContact": "03943  556-111",
            "PhoneSecondaryContact": "(03943) 556-270 ",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "stefan.streichert@stadtwerke-wernigerode.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 130,
            "Title": "Stadtwerke Wernigerode"
        },
        {
            "WebsiteURL": "http://stadtwerke.wittenberg.de/",
            "Comments": null,
            "PhonePrimaryContact": " 03491 4700",
            "PhoneSecondaryContact": "0800 759 0800",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "slw@stadtwerke.wittenberg.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 159,
            "Title": "Stadtwerke Wittenberg"
        },
        {
            "WebsiteURL": "http://www.stadtwerke-wf.de/",
            "Comments": null,
            "PhonePrimaryContact": "(0 53 31) 4 08 - 1 14 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "service@stadtwerke-wf.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 166,
            "Title": "Stadtwerke Wolfenbüttel"
        },
        {
            "WebsiteURL": "https://starvo.co.id/",
            "Comments": null,
            "PhonePrimaryContact": "+62 2129215000",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3669,
            "Title": "Starvo (Indonesia)"
        },
        {
            "WebsiteURL": "http://www.sgcc.com.cn/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3290,
            "Title": "State Grid Corporation of China (SGCC)"
        },
        {
            "WebsiteURL": "https://stations-e.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3485,
            "Title": "Stations-e"
        },
        {
            "WebsiteURL": "https://www.statiq.in/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3779,
            "Title": "Statiq (IN)"
        },
        {
            "WebsiteURL": "http://www.stromnetz.hamburg/ueber-uns/innovationen/e-mobility/",
            "Comments": null,
            "PhonePrimaryContact": "+49 40 4920200",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@stromnetz-hamburg.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 220,
            "Title": "Stromnetz Hamburg"
        },
        {
            "WebsiteURL": "http://stromticket.de/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 160,
            "Title": "StromTicket"
        },
        {
            "WebsiteURL": "http://www.stromtreter.de/",
            "Comments": null,
            "PhonePrimaryContact": " +49 800 7333532",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3269,
            "Title": "Stromtreter"
        },
        {
            "WebsiteURL": "http://www.stromtreter.de/",
            "Comments": null,
            "PhonePrimaryContact": " +49 800 7333532",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3270,
            "Title": "Stromtreter"
        },
        {
            "WebsiteURL": "http://suncountryhighway.ca/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 51,
            "Title": "Sun Country Highway"
        },
        {
            "WebsiteURL": "http://www.sun-stadtwerke.de/energien-der-zukunft/e-mobilitaet/ladekarte.html",
            "Comments": null,
            "PhonePrimaryContact": "0800 0 22 88 44 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "sun@sun-stadtwerke.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 138,
            "Title": "SUN Stadtwerke Union Nordhessen"
        },
        {
            "WebsiteURL": "https://www.sunenergy.pt/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3646,
            "Title": "Sunenergy (PT)"
        },
        {
            "WebsiteURL": "https://www.fmconway.co.uk/our-services/surecharge/",
            "Comments": "street lighting contractor. Mostly lamp-post chargers, proprietary app or Bonnet app required.",
            "PhonePrimaryContact": "+44 1732 600 700",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3612,
            "Title": "SureCharge (FM Conway) (UK)"
        },
        {
            "WebsiteURL": "https://www.swarcoeconnect.org/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3341,
            "Title": "Swarco E.Connect"
        },
        {
            "WebsiteURL": "https://www.swb-gruppe.de/verantwortung/swb-und-umwelt/fahren-mit-strom.php",
            "Comments": null,
            "PhonePrimaryContact": " 0421 3590",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 125,
            "Title": "SWB / EWE"
        },
        {
            "WebsiteURL": "https://swisscharge.ch/",
            "Comments": null,
            "PhonePrimaryContact": "071 388 11 50",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@swisscharge.ch",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3273,
            "Title": "Swisscharge (CH)"
        },
        {
            "WebsiteURL": " https://charge.swtchenergy.com/",
            "Comments": null,
            "PhonePrimaryContact": "+1-844-798-2438",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3493,
            "Title": "SWTCH - Charge Everywhere"
        },
        {
            "WebsiteURL": "http://www.syane.orios-infos.com/",
            "Comments": "Syndicat des énergies et de l'améngement numérique de la Haute-Savoie",
            "PhonePrimaryContact": "+33 4 50 33 50 60",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3277,
            "Title": "Syane"
        },
        {
            "WebsiteURL": "https://www.sydego.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3412,
            "Title": "Sydego"
        },
        {
            "WebsiteURL": "http://tank.rast.de/emobility/",
            "Comments": null,
            "PhonePrimaryContact": "+49 228 9220",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "kundenservice@tank.rast.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3248,
            "Title": "Tank & Rast"
        },
        {
            "WebsiteURL": "http://www.tanke-wienenergie.at/",
            "Comments": null,
            "PhonePrimaryContact": "0800 510 820",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 142,
            "Title": "TANKE Wien Energie"
        },
        {
            "WebsiteURL": "https://nexonev.tatamotors.com/charging-locator/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3436,
            "Title": "Tata Power"
        },
        {
            "WebsiteURL": "https://www.tauron.pl/tauron/tauron-innowacje/elektromobilnosc",
            "Comments": null,
            "PhonePrimaryContact": "+48572886552",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "emap@tauron.pl",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3452,
            "Title": "TAURON Nowe Technologie"
        },
        {
            "WebsiteURL": "https://www.teapont.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3462,
            "Title": "TEA."
        },
        {
            "WebsiteURL": "https://www.empark.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3559,
            "Title": "Telepark (Empark)"
        },
        {
            "WebsiteURL": "https://www.terpel.com/nueva-movilidad-y-energias/terpel-voltex",
            "Comments": null,
            "PhonePrimaryContact": " 01 8000 518 555",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3705,
            "Title": "Terpel Voltex (Columbia)"
        },
        {
            "WebsiteURL": "https://www.tesla.com/en_AU/support/non-tesla-supercharging",
            "Comments": "Tesla charging including support for non-tesla vehicles",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3534,
            "Title": "Tesla (including non-tesla)"
        },
        {
            "WebsiteURL": "http://www.teslamotors.com",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 23,
            "Title": "Tesla (Tesla-only charging)"
        },
        {
            "WebsiteURL": "https://www.geniepoint.co.uk/",
            "Comments": "also known as Revive, Engie EV Solutions regional branding",
            "PhonePrimaryContact": "+44(0)20 3598 4087",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "geniepointsupport@engie.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 150,
            "Title": "The GeniePoint Network ( EQUANS EV Solutions )"
        },
        {
            "WebsiteURL": "http://therevproject.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "rev@therevproject.com",
            "FaultReportEmail": "rev@therevproject.com",
            "IsRestrictedEdit": false,
            "ID": 57,
            "Title": "The REV Project (UWA - Australia)"
        },
        {
            "WebsiteURL": "http://www.theplugincompany.com/en/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 35,
            "Title": "ThePluginCompany (Belgium)"
        },
        {
            "WebsiteURL": "https://www.thundergrid.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3546,
            "Title": "Thundergrid"
        },
        {
            "WebsiteURL": "https://www.tiwag.at/no_cache/privatkunden/energieeffizienz/mobilitaet/",
            "Comments": null,
            "PhonePrimaryContact": "0800 818 819",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 18,
            "Title": "TIWAG Tiroler Wasserkraft AG (AT)"
        },
        {
            "WebsiteURL": "https://toger.co/",
            "Comments": null,
            "PhonePrimaryContact": "90 212 980 01 44",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3784,
            "Title": "Toger (TR)"
        },
        {
            "WebsiteURL": "https://toka.energy/",
            "Comments": "ЗАРЯДНЫЕ СТАНЦИИ ТОКА, Based in Ukraine",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@toka.energy",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3361,
            "Title": "Toka Energy"
        },
        {
            "WebsiteURL": "https://www.tonikenergy.com/products/ev-charging/",
            "Comments": "Accepts Fortum Charge & Drive",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "ev@tonikenergy.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3366,
            "Title": "Tonik Energy"
        },
        {
            "WebsiteURL": "https://torasarj.com/",
            "Comments": null,
            "PhonePrimaryContact": " +90 0850 808 86 72",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3717,
            "Title": "ToraŞarj (TR)"
        },
        {
            "WebsiteURL": "http://www.total.be/fr/carburants/carburant-station/plug-to-drive/finder-plugtodrive.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 175,
            "Title": "TOTAL Be PlugToDrive"
        },
        {
            "WebsiteURL": "http://www.total.nl/services-tankstations/plug-to-drive.html",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 174,
            "Title": "TOTAL Nl PlugToDrive"
        },
        {
            "WebsiteURL": "https://www.totalenergies.es/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3571,
            "Title": "TotalEnergies (ES)"
        },
        {
            "WebsiteURL": "https://apps.total-ev-charge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3447,
            "Title": "TotalEnergies (FR)"
        },
        {
            "WebsiteURL": "https://touch-station.com/",
            "Comments": null,
            "PhonePrimaryContact": " 8 800 550 30 41",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3698,
            "Title": "Touch (RU)"
        },
        {
            "WebsiteURL": "https://www.tsk.sk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3306,
            "Title": "Trenčiansky samosprávny kraj"
        },
        {
            "WebsiteURL": "https://trojan.energy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3738,
            "Title": "Trojan Energy"
        },
        {
            "WebsiteURL": "https://www.trugo.com.tr/",
            "Comments": "Operated by Togg",
            "PhonePrimaryContact": "+908508087846",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "toggcare@togg.com.tr",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3712,
            "Title": "Trugo (TR)"
        },
        {
            "WebsiteURL": "https://tupinambaenergia.com.br/",
            "Comments": null,
            "PhonePrimaryContact": "+55 (11) 98182-8203",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "camilo@tupinambaenergia.com.br",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3563,
            "Title": "Tupinambá"
        },
        {
            "WebsiteURL": "https://www.ubitricity.com/",
            "Comments": null,
            "PhonePrimaryContact": "+49 (0)30 398 371 690",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contact@ubitricity.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 2244,
            "Title": "ubitricity"
        },
        {
            "WebsiteURL": "http://www.ultra-fast.nl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 64,
            "Title": "Ultra-Fast"
        },
        {
            "WebsiteURL": "https://www.umbrellasolarinvestment.com/e-mobility",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3786,
            "Title": "Umbrella eMobility (ES)"
        },
        {
            "WebsiteURL": "http://www.umeaenergi.se/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "umea.energi@umeaenergi.se",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3249,
            "Title": "Umeå Energi"
        },
        {
            "WebsiteURL": "https://unipark.lt/en/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3689,
            "Title": "Unipark [Stova] (LT)"
        },
        {
            "WebsiteURL": "https://unitcharge.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "support@unitcharge.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3686,
            "Title": "UnitCharge (RU)"
        },
        {
            "WebsiteURL": "https://universalevcharging.com/services/charging-network/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3694,
            "Title": "Universal EV Charging"
        },
        {
            "WebsiteURL": "https://www.u-power.com.tw/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3679,
            "Title": "U-Power"
        },
        {
            "WebsiteURL": "https://www.urbener.com/",
            "Comments": null,
            "PhonePrimaryContact": "+34 976 29 89 84",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "urbener@urbener.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3278,
            "Title": "Urbener Energía"
        },
        {
            "WebsiteURL": "http://www.useda.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3256,
            "Title": "USEDA (FR)"
        },
        {
            "WebsiteURL": "https://movilidad.ute.com.uy/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": "movilidadelectrica@ute.com.uy",
            "IsRestrictedEdit": false,
            "ID": 3597,
            "Title": "UTE (Uruguay)"
        },
        {
            "WebsiteURL": "http://www.uewag.de/energie/stromtankstellen",
            "Comments": null,
            "PhonePrimaryContact": "0661 12-100",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 65,
            "Title": "UWAG"
        },
        {
            "WebsiteURL": "http://www.vattenfall.de/de/emobility/emobility.htm",
            "Comments": null,
            "PhonePrimaryContact": "0800 - 2 335 335",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "emobility@vattenfall.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 108,
            "Title": "Vattenfall InCharge"
        },
        {
            "WebsiteURL": "https://vector.co.nz/evcharging",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 233,
            "Title": "Vector (NZ)"
        },
        {
            "WebsiteURL": "https://app.vendelectric.com/getstarted",
            "Comments": "Apparently operated by Rolec Services.",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3473,
            "Title": "Vend Electric"
        },
        {
            "WebsiteURL": "https://www.veolia.cz",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3340,
            "Title": "Veolia"
        },
        {
            "WebsiteURL": "http://www.versorgungsbetriebe.de/hannmuendenGips/Gips?SessionMandant=HannMuenden&Anwendung=CMSWebpage&Methode=ShowHTMLAusgabe&RessourceID=12045",
            "Comments": null,
            "PhonePrimaryContact": " 01802 707800",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@versorgungsbetriebe.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 144,
            "Title": "Versorgungsbetriebe Hann. Münden"
        },
        {
            "WebsiteURL": "http://www.emobility-vibrate.eu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@emobility-vibrate.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 231,
            "Title": "Vibrate"
        },
        {
            "WebsiteURL": "https://www.viesgo.com/es/nuevas-tecnologias-e-innovacion/movilidad-electrica/puntos-de-recarga-publica",
            "Comments": "Formerly known as E.ON Energía",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 1237,
            "Title": "Viesgo (Spain)"
        },
        {
            "WebsiteURL": "https://www.vilaltacorp.es/es/electricidad",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3785,
            "Title": "Vilalta Greenergy (ES)"
        },
        {
            "WebsiteURL": "http://virta.fi/",
            "Comments": null,
            "PhonePrimaryContact": "0800-02200",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 136,
            "Title": "VIRTA"
        },
        {
            "WebsiteURL": "http://vitaemobility.com/",
            "Comments": null,
            "PhonePrimaryContact": "+32 473 94 98 27",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@vitaemobility.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 61,
            "Title": "Vitaemobility"
        },
        {
            "WebsiteURL": "http://www.vlotte.at/",
            "Comments": null,
            "PhonePrimaryContact": "+43 5574 9000 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "elektromobil@vkw.at",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 99,
            "Title": "Vlotte"
        },
        {
            "WebsiteURL": "http://www.voltacharging.com",
            "Comments": null,
            "PhonePrimaryContact": "  1-888-264-2208",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@voltacharging.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 50,
            "Title": "Volta Charging"
        },
        {
            "WebsiteURL": "https://volthero.hu/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@volthero.hu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3432,
            "Title": "Volthero"
        },
        {
            "WebsiteURL": "https://voltron.id/",
            "Comments": "formerly EVCuzz",
            "PhonePrimaryContact": "+62 8781 0584 499",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3668,
            "Title": "Voltron (Indonesia)"
        },
        {
            "WebsiteURL": "https://www.voltrun.com/en/",
            "Comments": null,
            "PhonePrimaryContact": "+908507778658",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3439,
            "Title": "Voltrun"
        },
        {
            "WebsiteURL": "http://www.schneller-strom-tanken.de/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 126,
            "Title": "VR Schneller-Strom-tanken"
        },
        {
            "WebsiteURL": "http://www.zelenabuducnost.sk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 193,
            "Title": "VSE"
        },
        {
            "WebsiteURL": "https://www.synergy.net.au/Our-energy/Projects/Electric-Vehicle-fast-charging-network",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3626,
            "Title": "WA EV Network (AU)"
        },
        {
            "WebsiteURL": "https://www.watmobilite.com/",
            "Comments": null,
            "PhonePrimaryContact": "+90 850 755 98 98",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3603,
            "Title": "WAT Mobilite"
        },
        {
            "WebsiteURL": "https://wattifev.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3667,
            "Title": "Wattif EV"
        },
        {
            "WebsiteURL": "https://wavecharging.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3724,
            "Title": "Wave Charging"
        },
        {
            "WebsiteURL": "https://www.wedrivesolar.nl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3574,
            "Title": "We Drive Solar"
        },
        {
            "WebsiteURL": "https://webasto-charging.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@webasto-charging.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3373,
            "Title": "Webasto"
        },
        {
            "WebsiteURL": "https://www.wecharge.com.br/",
            "Comments": null,
            "PhonePrimaryContact": "+55-800-291-0045",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "contato@wecharge.com.br",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3710,
            "Title": "WeCharge (BR)"
        },
        {
            "WebsiteURL": "https://weev.ie/",
            "Comments": null,
            "PhonePrimaryContact": "+44 29 9031 3031",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "hello@weev.ie",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3578,
            "Title": "Weev"
        },
        {
            "WebsiteURL": "https://www.wel.co.nz/projects/electric-vehicles/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 28,
            "Title": "WEL Networks Ltd"
        },
        {
            "WebsiteURL": "http://www.wenea.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3371,
            "Title": "Wenea"
        },
        {
            "WebsiteURL": "http://www.werraenergie.de/www/werraenergie/webinfo/webinfo.nsf/DocsID/E-Mobilitaet",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 195,
            "Title": "Werraenergie"
        },
        {
            "WebsiteURL": "http://westarelectrogo.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 34,
            "Title": "Westar Energy ElectroGo"
        },
        {
            "WebsiteURL": "https://www.ww-netz.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3423,
            "Title": "Westfalen Weser Netz"
        },
        {
            "WebsiteURL": "https://westmorlandfamily.com/charging/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3672,
            "Title": "Westmorland Family"
        },
        {
            "WebsiteURL": "https://wevolt.com.au",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3716,
            "Title": "WeVolt (AU)"
        },
        {
            "WebsiteURL": "http://www.wirtschaftsbetriebe-nienburg.de/",
            "Comments": null,
            "PhonePrimaryContact": "(05021) 87-315 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "wirtschaftsbetriebe@nienburg.de",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 183,
            "Title": "Wirtschaftsbetriebe Stadt Nienburg"
        },
        {
            "WebsiteURL": "https://wroom.org/",
            "Comments": "App based access",
            "PhonePrimaryContact": "+39 035 36 92 145",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3382,
            "Title": "Wroom"
        },
        {
            "WebsiteURL": "https://yasno.com.ua",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3344,
            "Title": "YASNO E-mobility"
        },
        {
            "WebsiteURL": "https://www.yawatt.com/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3589,
            "Title": "Yawatt (Es)"
        },
        {
            "WebsiteURL": "https://yellotmob.com.br/",
            "Comments": null,
            "PhonePrimaryContact": "+55 62 9 9806-6114",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3771,
            "Title": "Yellotmob (Brasil)"
        },
        {
            "WebsiteURL": null,
            "Comments": "Energy company based in Argentina",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3300,
            "Title": "YPF"
        },
        {
            "WebsiteURL": "https://www.z.co.nz/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3545,
            "Title": "Z Energy"
        },
        {
            "WebsiteURL": "https://www.zapgrid.net/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3328,
            "Title": "ZapGrid"
        },
        {
            "WebsiteURL": "http://www.zeag-energie.de",
            "Comments": null,
            "PhonePrimaryContact": "07131 610-0",
            "PhoneSecondaryContact": "07131 56-4248",
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 176,
            "Title": "ZEAG Energie"
        },
        {
            "WebsiteURL": "https://www.zefenergy.com/",
            "Comments": null,
            "PhonePrimaryContact": "612.688.4596",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "solutions@zefenergy.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3454,
            "Title": "ZEF Energy"
        },
        {
            "WebsiteURL": "http://www.ze-mo.be/",
            "Comments": null,
            "PhonePrimaryContact": "+32 10 750 650",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@ze-mo.be",
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 54,
            "Title": "ZE-MO (Be)"
        },
        {
            "WebsiteURL": "https://z-e-n.fr/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3448,
            "Title": "ZEN (Zero Emission Network)/PROVIRIDIS"
        },
        {
            "WebsiteURL": "https://www.zencar.eu/",
            "Comments": null,
            "PhonePrimaryContact": "+32 2 669 77 91",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@zencar.eu",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 100,
            "Title": "ZenCar"
        },
        {
            "WebsiteURL": "https://zeoncharging.com/",
            "Comments": null,
            "PhonePrimaryContact": "+91 9789 616161",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "care@zeon.in",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3539,
            "Title": "Zeon Charging"
        },
        {
            "WebsiteURL": "https://zepto.pl/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3475,
            "Title": "Zepto"
        },
        {
            "WebsiteURL": "https://www.meridianenergy.co.nz/for-home/zero",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3528,
            "Title": "Zero (Meridian Energy)"
        },
        {
            "WebsiteURL": "http://zerocarbonworld.org/",
            "Comments": "UK Charity promoting carbon reduction",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@zerocarbonworld.com",
            "FaultReportEmail": "info@zerocarbonworld.com",
            "IsRestrictedEdit": null,
            "ID": 19,
            "Title": "Zero Carbon World"
        },
        {
            "WebsiteURL": "http://www.zes.net/",
            "Comments": "Zorlu Energy Solutions, Turkey",
            "PhonePrimaryContact": "0850 339 99 37",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3323,
            "Title": "ZES"
        },
        {
            "WebsiteURL": "https://map.zest.uk.com/",
            "Comments": "bespoke mobile phone app required",
            "PhonePrimaryContact": "+44 333 577 6760",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3581,
            "Title": "Zest Charging"
        },
        {
            "WebsiteURL": "https://zevs.group/",
            "Comments": null,
            "PhonePrimaryContact": " +7 800 222-14-16",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@rucharge.com",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3676,
            "Title": "ZEVS (RU)"
        },
        {
            "WebsiteURL": "https://ze-watt.com/",
            "Comments": null,
            "PhonePrimaryContact": "+33 5 36 09 14 00",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3514,
            "Title": "Ze-Watt (FR)"
        },
        {
            "WebsiteURL": "https://www.zletric.com.br/",
            "Comments": null,
            "PhonePrimaryContact": " +55 11 5199 3399 ",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@zletric.com.br",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3565,
            "Title": "Zletric"
        },
        {
            "WebsiteURL": "https://zokoenergy.zoko.co.il/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3540,
            "Title": "Zoko"
        },
        {
            "WebsiteURL": "https://zsedrive.sk/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3259,
            "Title": "ZSE Drive"
        },
        {
            "WebsiteURL": "https://www.zunder.com/en/",
            "Comments": "formerly known as EasyCharger",
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3324,
            "Title": "Zunder"
        },
        {
            "WebsiteURL": "https://www.elektrodistribucija.mk/Electromobility/Charger-locations.aspx",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3350,
            "Title": "ЕВН (EVN) (Macedonia)"
        },
        {
            "WebsiteURL": "https://customer.malankabn.by/map",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3642,
            "Title": "Маланка (Belarus)"
        },
        {
            "WebsiteURL": "https://mgts.ru/home/chargestation",
            "Comments": null,
            "PhonePrimaryContact": "+7 800 250-93-36",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3487,
            "Title": "МГТС"
        },
        {
            "WebsiteURL": "https://www.moesk.ru/spec_projects/moesk_ev/",
            "Comments": null,
            "PhonePrimaryContact": "8 (800) 700-40-70",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3301,
            "Title": "МОЭСК (Russia)"
        },
        {
            "WebsiteURL": "https://nesk.ru/zse",
            "Comments": null,
            "PhonePrimaryContact": " +7 861 944-77–40",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3683,
            "Title": "НЭСК (RU)"
        },
        {
            "WebsiteURL": "https://www.rushydro.ru/",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3592,
            "Title": "РусГидро (Russia)"
        },
        {
            "WebsiteURL": "https://staves.ru/",
            "Comments": null,
            "PhonePrimaryContact": "+7 961 463-77-36",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "info@staves.ru",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3706,
            "Title": "СтавЭС (RU)"
        },
        {
            "WebsiteURL": "https://gridcom-rt.ru/",
            "Comments": null,
            "PhonePrimaryContact": " 8 800 2000 878",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": "office@gridcom-rt.ru",
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3699,
            "Title": "ЭЗС СК"
        },
        {
            "WebsiteURL": "https://transport.mos.ru/electro",
            "Comments": null,
            "PhonePrimaryContact": "+74950181920",
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3653,
            "Title": "Энергия Москвы"
        },
        {
            "WebsiteURL": "https://zapravki.yandex.ru",
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": false,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": false,
            "ID": 3682,
            "Title": "Яндекс.Заправки (RU)"
        }
    ],
    "StatusTypes": [
        {
            "IsOperational": null,
            "IsUserSelectable": true,
            "ID": 0,
            "Title": "Unknown"
        },
        {
            "IsOperational": true,
            "IsUserSelectable": false,
            "ID": 10,
            "Title": "Currently Available (Automated Status)"
        },
        {
            "IsOperational": true,
            "IsUserSelectable": false,
            "ID": 20,
            "Title": "Currently In Use (Automated Status)"
        },
        {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 30,
            "Title": "Temporarily Unavailable"
        },
        {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 50,
            "Title": "Operational"
        },
        {
            "IsOperational": true,
            "IsUserSelectable": true,
            "ID": 75,
            "Title": "Partly Operational (Mixed)"
        },
        {
            "IsOperational": false,
            "IsUserSelectable": true,
            "ID": 100,
            "Title": "Not Operational"
        },
        {
            "IsOperational": false,
            "IsUserSelectable": true,
            "ID": 150,
            "Title": "Planned For Future Date"
        },
        {
            "IsOperational": false,
            "IsUserSelectable": true,
            "ID": 200,
            "Title": "Removed (Decommissioned)"
        },
        {
            "IsOperational": false,
            "IsUserSelectable": true,
            "ID": 210,
            "Title": "Removed (Duplicate Listing)"
        }
    ],
    "SubmissionStatusTypes": [
        {
            "IsLive": false,
            "ID": 1,
            "Title": "Submission Under Review"
        },
        {
            "IsLive": false,
            "ID": 50,
            "Title": "Imported and Under Review"
        },
        {
            "IsLive": true,
            "ID": 100,
            "Title": "Imported and Published"
        },
        {
            "IsLive": true,
            "ID": 200,
            "Title": "Submission Published"
        },
        {
            "IsLive": false,
            "ID": 250,
            "Title": "Submission Rejected - Incomplete"
        },
        {
            "IsLive": false,
            "ID": 1000,
            "Title": "Delisted"
        },
        {
            "IsLive": false,
            "ID": 1001,
            "Title": "Delisted - Duplicate"
        },
        {
            "IsLive": false,
            "ID": 1002,
            "Title": "Delisted - No Longer Active/Decommissioned"
        },
        {
            "IsLive": false,
            "ID": 1005,
            "Title": "Delisted - Superseded by Update"
        },
        {
            "IsLive": false,
            "ID": 1010,
            "Title": "Delisted - Not Public Information/Is Private Residence"
        },
        {
            "IsLive": false,
            "ID": 1020,
            "Title": "Delisted - Removed by Import Data Provider"
        }
    ],
    "UsageTypes": [
        {
            "IsPayAtLocation": null,
            "IsMembershipRequired": null,
            "IsAccessKeyRequired": null,
            "ID": 0,
            "Title": "(Unknown)"
        },
        {
            "IsPayAtLocation": false,
            "IsMembershipRequired": false,
            "IsAccessKeyRequired": false,
            "ID": 6,
            "Title": "Private - For Staff, Visitors or Customers"
        },
        {
            "IsPayAtLocation": null,
            "IsMembershipRequired": true,
            "IsAccessKeyRequired": null,
            "ID": 2,
            "Title": "Private - Restricted Access"
        },
        {
            "IsPayAtLocation": null,
            "IsMembershipRequired": null,
            "IsAccessKeyRequired": null,
            "ID": 3,
            "Title": "Privately Owned - Notice Required"
        },
        {
            "IsPayAtLocation": null,
            "IsMembershipRequired": null,
            "IsAccessKeyRequired": null,
            "ID": 1,
            "Title": "Public"
        },
        {
            "IsPayAtLocation": false,
            "IsMembershipRequired": true,
            "IsAccessKeyRequired": true,
            "ID": 4,
            "Title": "Public - Membership Required"
        },
        {
            "IsPayAtLocation": false,
            "IsMembershipRequired": false,
            "IsAccessKeyRequired": false,
            "ID": 7,
            "Title": "Public - Notice Required"
        },
        {
            "IsPayAtLocation": true,
            "IsMembershipRequired": false,
            "IsAccessKeyRequired": false,
            "ID": 5,
            "Title": "Public - Pay At Location"
        }
    ],
    "UserCommentTypes": [
        {
            "ID": 10,
            "Title": "General Comment"
        },
        {
            "ID": 50,
            "Title": "Important Notice (For Other Users)"
        },
        {
            "ID": 100,
            "Title": "Suggested Change (Note To Editors)"
        },
        {
            "ID": 110,
            "Title": "Suggested Changed (Actioned By Editor)"
        },
        {
            "ID": 1000,
            "Title": "Fault Report (Notice To Users And Operator)"
        }
    ],
    "CheckinStatusTypes": [
        {
            "IsPositive": null,
            "IsAutomatedCheckin": false,
            "ID": 0,
            "Title": "Did Not Visit Location"
        },
        {
            "IsPositive": true,
            "IsAutomatedCheckin": false,
            "ID": 10,
            "Title": "Charged Successfully"
        },
        {
            "IsPositive": true,
            "IsAutomatedCheckin": true,
            "ID": 15,
            "Title": "Charged Successfully (Automated Checkin)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 20,
            "Title": "Failed to Charge (Equipment Not Operational)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 22,
            "Title": "Failed to Charge (Equipment Not Fully Installed)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 25,
            "Title": "Failed to Charge (Equipment Problem)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 30,
            "Title": "Failed to Charge (Equipment Not Compatible)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 40,
            "Title": "Failed to Charge (Required Other Access Card/Fob etc.)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 50,
            "Title": "Failed to Charge (No Charging Equipment Present)"
        },
        {
            "IsPositive": true,
            "IsAutomatedCheckin": false,
            "ID": 100,
            "Title": "Charging Spot In Use (Other EV Parked)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 110,
            "Title": "Charging Spot In Use (Non-EV Parked)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 120,
            "Title": "Charging Spot Not Accessible (Access locked or site closed)"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 130,
            "Title": "Charging Spot Not Found (Inadequate or Incorrect Details)"
        },
        {
            "IsPositive": true,
            "IsAutomatedCheckin": false,
            "ID": 140,
            "Title": "Equipment & Location Confirmed Correct"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 150,
            "Title": "Location Is A Duplicate"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 160,
            "Title": "Equipment/Location Has Been Decommissioned"
        },
        {
            "IsPositive": false,
            "IsAutomatedCheckin": false,
            "ID": 200,
            "Title": "Other (Negative/Bad)"
        },
        {
            "IsPositive": true,
            "IsAutomatedCheckin": false,
            "ID": 210,
            "Title": "Other (Positive/Good)"
        }
    ],
    "DataTypes": [
        {
            "ID": 1,
            "Title": "Single Line Text"
        },
        {
            "ID": 2,
            "Title": "Multi Line Text"
        },
        {
            "ID": 3,
            "Title": "Number"
        },
        {
            "ID": 4,
            "Title": "Date"
        },
        {
            "ID": 5,
            "Title": "Boolean"
        },
        {
            "ID": 10,
            "Title": "Option List"
        }
    ],
    "MetadataGroups": [
        {
            "DataProviderID": 1,
            "IsRestrictedEdit": false,
            "IsPublicInterest": true,
            "MetadataFields": [
                {
                    "MetadataGroupID": 1,
                    "DataTypeID": 10,
                    "DataType": null,
                    "MetadataFieldOptions": [
                        {
                            "MetadataFieldID": 1,
                            "ID": 1,
                            "Title": "Shopping"
                        },
                        {
                            "MetadataFieldID": 1,
                            "ID": 2,
                            "Title": "Hotel"
                        },
                        {
                            "MetadataFieldID": 1,
                            "ID": 3,
                            "Title": "Restaurant"
                        },
                        {
                            "MetadataFieldID": 1,
                            "ID": 8,
                            "Title": "Parking"
                        },
                        {
                            "MetadataFieldID": 1,
                            "ID": 9,
                            "Title": "Secure"
                        }
                    ],
                    "ID": 1,
                    "Title": "POI Type"
                },
                {
                    "MetadataGroupID": 1,
                    "DataTypeID": 1,
                    "DataType": null,
                    "MetadataFieldOptions": null,
                    "ID": 2,
                    "Title": "Access Hours"
                },
                {
                    "MetadataGroupID": 1,
                    "DataTypeID": 10,
                    "DataType": null,
                    "MetadataFieldOptions": [
                        {
                            "MetadataFieldID": 4,
                            "ID": 4,
                            "Title": "Positioning"
                        }
                    ],
                    "ID": 4,
                    "Title": "Attribution"
                },
                {
                    "MetadataGroupID": 1,
                    "DataTypeID": 10,
                    "DataType": null,
                    "MetadataFieldOptions": [
                        {
                            "MetadataFieldID": 5,
                            "ID": 5,
                            "Title": "Car"
                        },
                        {
                            "MetadataFieldID": 5,
                            "ID": 6,
                            "Title": "Motorcycle"
                        },
                        {
                            "MetadataFieldID": 5,
                            "ID": 7,
                            "Title": "Bus"
                        },
                        {
                            "MetadataFieldID": 5,
                            "ID": 10,
                            "Title": "Goods/Delivery Vehicles"
                        },
                        {
                            "MetadataFieldID": 5,
                            "ID": 11,
                            "Title": "Taxi"
                        },
                        {
                            "MetadataFieldID": 5,
                            "ID": 12,
                            "Title": "Bike"
                        }
                    ],
                    "ID": 5,
                    "Title": "Vehicle Type"
                }
            ],
            "ID": 1,
            "Title": "Extended Information"
        },
        {
            "DataProviderID": 1,
            "IsRestrictedEdit": false,
            "IsPublicInterest": false,
            "MetadataFields": [
                {
                    "MetadataGroupID": 2,
                    "DataTypeID": 10,
                    "DataType": null,
                    "MetadataFieldOptions": null,
                    "ID": 3,
                    "Title": "Group of Companies"
                },
                {
                    "MetadataGroupID": 2,
                    "DataTypeID": 1,
                    "DataType": null,
                    "MetadataFieldOptions": null,
                    "ID": 6,
                    "Title": "External Reference Id"
                },
                {
                    "MetadataGroupID": 2,
                    "DataTypeID": 1,
                    "DataType": null,
                    "MetadataFieldOptions": null,
                    "ID": 8,
                    "Title": "External Url"
                }
            ],
            "ID": 2,
            "Title": "Supporting Data"
        }
    ],
    "UserProfile": null,
    "ChargePoint": {
        "DataProvider": {
            "WebsiteURL": null,
            "Comments": null,
            "DataProviderStatusType": null,
            "IsRestrictedEdit": false,
            "IsOpenDataLicensed": null,
            "IsApprovedImport": null,
            "License": null,
            "DateLastImported": null,
            "ID": 0,
            "Title": null
        },
        "OperatorInfo": {
            "WebsiteURL": null,
            "Comments": null,
            "PhonePrimaryContact": null,
            "PhoneSecondaryContact": null,
            "IsPrivateIndividual": null,
            "AddressInfo": null,
            "BookingURL": null,
            "ContactEmail": null,
            "FaultReportEmail": null,
            "IsRestrictedEdit": null,
            "ID": 0,
            "Title": null
        },
        "UsageType": {
            "IsPayAtLocation": null,
            "IsMembershipRequired": null,
            "IsAccessKeyRequired": null,
            "ID": 0,
            "Title": null
        },
        "StatusType": {
            "IsOperational": null,
            "IsUserSelectable": false,
            "ID": 0,
            "Title": null
        },
        "SubmissionStatus": null,
        "UserComments": null,
        "PercentageSimilarity": null,
        "MediaItems": null,
        "IsRecentlyVerified": true,
        "DateLastVerified": "2024-06-20T15:22:24.389Z",
        "ID": -1,
        "UUID": "0208ab43-8de6-449d-9496-997f09cf6c30",
        "ParentChargePointID": null,
        "DataProviderID": null,
        "DataProvidersReference": null,
        "OperatorID": null,
        "OperatorsReference": null,
        "UsageTypeID": null,
        "UsageCost": null,
        "AddressInfo": {
            "ID": 0,
            "Title": null,
            "AddressLine1": null,
            "AddressLine2": null,
            "Town": null,
            "StateOrProvince": null,
            "Postcode": null,
            "CountryID": null,
            "Country": null,
            "Latitude": 0,
            "Longitude": 0,
            "ContactTelephone1": null,
            "ContactTelephone2": null,
            "ContactEmail": null,
            "AccessComments": null,
            "RelatedURL": null,
            "Distance": null,
            "DistanceUnit": 0
        },
        "Connections": [
            {
                "ID": 0,
                "ConnectionTypeID": null,
                "ConnectionType": null,
                "Reference": null,
                "StatusTypeID": null,
                "StatusType": null,
                "LevelID": null,
                "Level": null,
                "Amps": null,
                "Voltage": null,
                "PowerKW": null,
                "CurrentTypeID": null,
                "CurrentType": null,
                "Quantity": null,
                "Comments": null
            }
        ],
        "NumberOfPoints": 1,
        "GeneralComments": "",
        "DatePlanned": null,
        "DateLastConfirmed": "2024-06-20T15:22:24.389Z",
        "StatusTypeID": null,
        "DateLastStatusUpdate": "2024-06-20T15:22:24.389Z",
        "MetadataValues": null,
        "DataQualityLevel": 1,
        "DateCreated": "2024-06-20T15:22:24.389Z",
        "SubmissionStatusTypeID": null
    },
    "UserComment": {
        "ID": 0,
        "ChargePointID": 0,
        "CommentTypeID": null,
        "CommentType": {
            "ID": 10,
            "Title": "General Comment"
        },
        "UserName": null,
        "Comment": "",
        "Rating": null,
        "RelatedURL": null,
        "DateCreated": "2024-06-20T15:22:24.389Z",
        "User": null,
        "CheckinStatusTypeID": null,
        "CheckinStatusType": {
            "IsPositive": null,
            "IsAutomatedCheckin": false,
            "ID": 0,
            "Title": "Did Not Visit Location"
        },
        "IsActionedByEditor": null
    }
}
'''

TEST_OPENAPI_RESPONSE = r"""
openapi: 3.0.3
info:
  title: Open Charge Map API
  version: '3.0'
  termsOfService: 'https://openchargemap.org/site/about/terms'
  contact:
    name: Contact
    url: 'https://openchargemap.org/site/about'
  description: "The Open Charge Map API provides access to the worlds largest registry of charging locations as Open Data. You can integrate this API into your own apps or services and export charging location data into your own systems. \n\nTo retrieve site (POI) data, see the `/poi` endpoint. To fetch general lookup information such as connector types, network operators etc, use the `/referencedata` endpoint.\n\n**Use of the OCM API is subject to terms and conditions. By using the API you indicate acceptance of these terms.**\n\nIf you wish to export charging location data into your own systems or applications the most flexible way is to use our API, which provides an export in a variety of formats. If you wish to regularly refresh the entire dataset, please clone our data from GitHub. You can also opt to run your own private API mirror.\n\n### Fair Usage Policy\nThe basic API is provided as a free service with no warranty or service level agreement. Providing this API to you costs us actual money for server resources and data transfer fees.\n\nIf you will be calling the API regularly (from an app or server) you must provide your API key as an `X-API-Key header` (case sensitive) or set the `key=YourAPIKey` url parameter. You should also set your http user-agent to a custom value to help identify your app.\n\n**To obtain a free API key Sign In and choose 'my apps' from the profile menu.**\n\n*Do not repeatedly call the API with duplicate queries. Debounce/throttle your API requests to minimise the work our API has to do. The API administrator (Open Charge Map) reserves the right to ban API callers (including automated banning) if callers make excessive/indescriminate use of the API, at the discretion of the OCM administrator.*\n\nIf you need to make a high volume of queries against the API please host your own API mirror or import the data into your own API.\n\n### Example API Calls\nReturn charging location information for the US in JSON format, limited to the first 10 results: `https://api.openchargemap.io/v3/poi/?output=json&countrycode=US&maxresults=10?key=<your key>`\n\nThe default output contains a lot of information. Here is the same call as above, but with the most compact output (formatting removed, reference data as IDs instead of full objects, null fields skipped): \n`https://api.openchargemap.io/v3/poi/?output=json&countrycode=US&maxresults=100&compact=true&verbose=false&key=<your key>`\n\nReturn KML format results suitable for viewing in google earth/maps etc (UK, max 500 locations): `https://api.openchargemap.io/v3/poi/?output=kml&countrycode=GB&maxresults=500&key=<your key>`\n\nData returned by the API has mixed licensing and applicable copyright attribution (included in results as \"Data Provider\"). If you require Open licensed data you currently must filter by opendata=true to return data marked specifically with Open Data licenses.\n\n### Linking to OCM\nIn addition to using our  API you can link directly to specific Open Charge Map URLs in order to perform specific actions, with {OCM-ID} is the numeric ID of the POI to add work with.\n\n* Add a New POI:\t`https://openchargemap.org/site/poi/add`\n* View POI Details: `https://openchargemap.org/site/poi/details/{OCM-ID}`\n* Add a Comment/Check-In to an existing POI: \t`https://openchargemap.org/site/poi/addcomment/{OCM-ID}` \n* Add a Photo to an existing POI:\t`https://openchargemap.org/site/poi/addmediaitem/{OCM-ID}`"
servers:
  - url: 'https://api.openchargemap.io/v3'
    description: API Base URL
paths:
  /poi:
    get:
      summary: Retrieve POI list (sites)
      tags: []
      responses:
        '200':
          $ref: '#/components/responses/POI'
      operationId: get-poi
      parameters:
        - schema:
            type: string
            default: json
          in: query
          name: output
          description: 'Optional output format `json`,`geojson`,`xml`,`csv`, JSON is the default and recommended as the highest fidelity.'
        - schema:
            type: string
          in: query
          name: client
          description: String to identify your client application. Optional but recommended to distinguish your client from other bots/crawlers
        - schema:
            type: integer
            default: 100
          in: query
          name: maxresults
          description: Limit on max number of results returned
        - schema:
            type: string
          in: query
          name: countrycode
          description: 2-character ISO Country code to filter to one specific country
        - schema:
            type: array
            items:
              type: string
            example: 'US,GB'
          in: query
          name: countryid
          description: Exact match on a given numeric country id (comma separated list)
        - schema:
            type: integer
          in: query
          name: latitude
          description: Latitude for distance calculation and filtering
        - schema:
            type: number
          in: query
          name: longitude
          description: Longitude for distance calculation and filtering
        - schema:
            type: number
          in: query
          name: distance
          description: Optionally filter results by a max distance from the given latitude/longitude
        - schema:
            type: string
            default: Miles
          in: query
          name: distanceunit
          description: '`miles` or `km` distance unit'
        - schema:
            type: array
            example: '1,2,3'
          in: query
          name: operatorid
          description: Exact match on a given EVSE operator id (comma separated list)
        - schema:
            type: array
            example: '1,2,3'
          in: query
          name: connectiontypeid
          description: Exact match on a given connection type id (comma separated list)
        - schema:
            type: array
            example: '1,2,3'
          in: query
          name: levelid
          description: Exact match on a given charging level (1-3) id (comma separated list)
          deprecated: true
        - schema:
            type: array
            example: '1,2,3'
          in: query
          name: usagetypeid
          description: Exact match on a given usage type id (comma separated list)
        - schema:
            type: array
            example: '1,2,3'
          in: query
          name: statustypeid
          description: Exact match on a given status type id (comma separated list)
        - schema:
            type: array
          in: query
          name: dataproviderid
          description: 'Exact match on a given data provider id id (comma separated list). '
        - schema:
            type: boolean
          in: query
          name: opendata
          description: Use opendata=true for only OCM provided ("Open") data.
        - schema:
            type: boolean
            default: 'false'
          in: query
          name: includecomments
          description: 'If true, user comments and media items will be include in result set'
        - schema:
            type: boolean
            default: 'true'
          in: query
          name: verbose
          description: Set to false to get a smaller result set with null items removed.
        - schema:
            type: boolean
            default: 'false'
          in: query
          name: compact
          description: Set to true to remove reference data objects from output (just returns IDs for common reference data such as DataProvider etc).
        - schema:
            type: boolean
            default: 'false'
          in: query
          name: camelcase
          description: Set to true to get a property names in camelCase format.
        - schema:
            type: string
          in: query
          name: chargepointid
          description: Exact match on a given OCM POI ID (comma separated list)
        - schema:
            type: array
          in: query
          name: boundingbox
          description: 'Filter results to a given bounding box. specify top left and bottom right box corners as: (lat,lng),(lat2,lng2)'
        - schema:
            type: string
          in: query
          name: polygon
          description: Filter results within a given Polygon. Specify an encoded polyline for the polygon shape. Polygon will be automatically closed from the last point to the first point.
        - schema:
            type: string
          in: query
          name: polyline
          description: 'Filter results along an encoded polyline, use with distance param to increase search distance along line. Polyline is expanded into a polygon to cover the search distance.'
      description: Used to fetch a list of POIs (sites) within a geographic boundary or near a specific latitude/longitude. This is the primary method for most applications and services to consume data from Open Charge Map.
      x-internal: false
    parameters: []
  /referencedata:
    get:
      summary: Core Reference Data
      tags: []
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CoreReferenceData'
      operationId: get-referencedata
      description: |-
        Returns the core reference data used for looking up IDs such as Connection Types, Operators, Countries etc. 

        This information is useful for UIs such as editing systems or for fetching results in the lighter non-verbose mode, then hydrating POI results back into complex objects.
      parameters:
        - schema:
            type: array
          in: query
          description: 'Optional filter on countryid, exact match on a given numeric country id (comma separated list)'
          name: countryid
    parameters: []
  /profile/authenticate:
    post:
      summary: Authenticate User
      operationId: post-authenticate
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                description: ''
                type: object
                x-examples:
                  example-1:
                    Data:
                      UserProfile:
                        ID: 1000
                        Username: Joe Bloggs
                        Profile: "Example person who uses open charge map \U0001F918"
                        Location: 'San Francisco, US'
                        WebsiteURL: 'https://openchargemap.org'
                        ReputationPoints: 2008
                        Permissions: '{"Permissions":[{"Level":100},{"Level":1000}],"LegacyPermissions":"[CountryLevel_Editor=All];[Administrator=true];"}'
                        DateCreated: '2011-09-28T15:11:00'
                        DateLastLogin: '2021-11-09T07:49:00'
                        IsProfilePublic: true
                        Latitude: -31
                        Longitude: 115
                        EmailAddress: example@example.com
                        EmailHash: null
                        ProfileImageURL: 'https://www.gravatar.com/avatar/e3e76940eb5e85220db216603ee6b00f?s=80&d=robohash'
                      access_token: eXampleJwt.AccessTOKEN
                    Metadata:
                      StatusCode: 200
                properties:
                  Data:
                    type: object
                    required:
                      - UserProfile
                      - access_token
                    properties:
                      UserProfile:
                        $ref: '#/components/schemas/UserProfile'
                      access_token:
                        type: string
                        minLength: 1
                        description: JWT Bearer Token to use in subsequent authenticated requests
                  Metadata:
                    type: object
                    required:
                      - StatusCode
                    properties:
                      StatusCode:
                        type: integer
                required:
                  - Data
                  - Metadata
      description: 'Perform user authentication, returning a model which includes the users profile and a JWT auth token to re-use in subsequent requests.'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                emailaddress:
                  type: string
                password:
                  type: string
            examples:
              example-1:
                value:
                  emailaddress: string
                  password: string
        description: ''
    parameters: []
  /comment:
    post:
      summary: Submit Comment or Checkin
      operationId: post-comment
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                description: ''
                type: object
                properties:
                  status:
                    type: string
                    minLength: 1
                  description:
                    type: string
                    minLength: 1
                required:
                  - status
                  - description
                x-examples:
                  example-1:
                    status: OK
                    description: OK
              examples:
                example-response:
                  value:
                    status: OK
                    description: OK
        '400':
          description: Bad Request
      description: Submit a user comment or checkin for a specific charging location
      security:
        - UserAuthentication: []
      requestBody:
        content:
          application/json:
            schema:
              description: ''
              type: object
              x-examples:
                example-1:
                  ChargePointID: 12345
                  CommentTypeID: 10
                  UserName: A. Nickname
                  Comment: 'This place is awesome, free cake for EV owners!'
                  Rating: 5
                  RelatedURL: 'http://awesomevplace.com'
                  CheckinStatusTypeID: 0
              properties:
                chargePointID:
                  type: integer
                  description: This must be a valid POI ID
                commentTypeID:
                  type: integer
                  description: This must be a valid Comment Type ID as per UserCommentTypes found in Core Reference Data. If left as null then General Comment will be used.
                userName:
                  type: string
                  minLength: 1
                  description: 'This is an optional name to associate with the submission, for authenticated users their profile username is used.'
                  maxLength: 100
                comment:
                  type: string
                  minLength: 1
                  maxLength: 4000
                  description: 'This is an optional comment to describe the charging experience, may include guidance for future users.'
                rating:
                  type: integer
                  example: 3
                  description: 'Optional integer rating between 1 = Worst, 5 = Best.'
                relatedURL:
                  type: string
                  minLength: 1
                  description: Optional website URL for related information
                  maxLength: 500
                checkinStatusTypeID:
                  type: integer
                  description: Optional valid CheckStatusTypeID to indicate overall catgeory and success/failure to use equipment e.g. 10 = Charged Successfully.
              required:
                - chargePointID
            examples:
              example-1:
                value:
                  chargePointID: 0
                  commentTypeID: 0
                  userName: string
                  comment: string
                  rating: 3
                  relatedURL: string
                  checkinStatusTypeID: 0
  /mediaitem:
    post:
      summary: Add Media Item (Photo)
      operationId: post-mediaitem
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                description: ''
                type: object
                x-examples:
                  example-1:
                    chargePointID: 156185
                    comment: Test
                    imageDataBase64: 'data:image/jpeg;base64,EXAMPLEBASE64ENCODEDJPEGORPNG'
                properties:
                  status:
                    type: string
                    description: status code OK
                  description:
                    type: string
                required:
                  - status
              examples:
                example-response:
                  value:
                    status: OK
                    description: OK
      description: Submit a photo for a specific charging location
      security:
        - UserAuthentication: []
      requestBody:
        content:
          application/json:
            schema:
              description: ''
              type: object
              x-examples:
                example-1:
                  chargePointID: 0
                  comment: string
                  imageDataBase64: string
              properties:
                chargePointID:
                  type: integer
                  description: ID value for the OCM site (POI) this image relates to.
                comment:
                  type: string
                  minLength: 1
                  description: Optional description of image or context
                imageDataBase64:
                  type: string
                  minLength: 1
                  description: BASE64 encoded data
              required:
                - chargePointID
                - imageDataBase64
            examples:
              example-media-upload:
                value:
                  chargePointID: 1234
                  comment: An example comment
                  imageDataBase64: 'data:image/jpeg;base64,<BASE64_ENCODED_DATA>'
  /openapi:
    get:
      summary: Retrieve OpenAPI definition
      tags: []
      operationId: get-openapi
      description: 'Retrieve the current OpenAPI format (YAML) definition for this API. This is useful for documentation tools, mocking, testing and client generation.'
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: object
                properties: {}
              examples:
                example-response:
                  value:
                    openapi: 3.0.3
                    info:
                      title: Open Charge Map API
                      version: '3.0'
components:
  schemas:
    POI:
      title: POI
      type: object
      description: |-
        A POI (Point of Interest), also referred to as a `Site` or `ChargePoint`, is the top-level set of information regarding a geographic site with one or more electric vehicle charging equipment present. The term `ChargePointID` is used to reference the unique ID for each POI, as called OCM ID. This reference appears in various UI elements in the format `OCM-12345` to distinguish the ID number as being a reference for a specific POI/site.

        Note: If the API is called in verbose mode properties expanded properties are included in the results (e.g. UsageType, StatusType, DataProvider, OperatorInfo, SubmissionStatus).  With the exception of the AddressInfo property, other object properties will not be populated in a compact result set and instead only the associated reference IDs will be set (e.g. UsageTypeID, DataProviderID etc)
      properties:
        ID:
          type: integer
          description: The OCM reference ID for this POI (Point of Interest).
          example: 148527
        UUID:
          type: string
          description: 'A universally unique identifier used as surrogate key. ID and UUID must be preserved when submitting POI update information. '
          example: 4C524AA1-3413-4D56-804C-480304FEB0FB
          format: uuid
        UserComments:
          description: A list of user comments or check-ins for this site
          type: array
          items:
            $ref: '#/components/schemas/UserComment'
        MediaItems:
          type: array
          description: A list of user submitted photos for this site
          items:
            $ref: '#/components/schemas/MediaItem'
        IsRecentlyVerified:
          type: boolean
          description: A dynamically computed value indicating of any recently confirmation activity has taken place for this site (positive check-ins etc)
          default: false
          example: true
        DateLastVerified:
          format: date-time
          description: 'A dynamically computed value, the date and time (UTC, ISO 8601) this POI was last confirmed by a user edit or related user comment'
          example: '2020-02-04T06:33:00Z'
          type: string
        ParentChargePointID:
          type: integer
          description: 'If present, this data in this POI supercedes information in another POI. Generally not relevant to consumers.'
        DataProviderID:
          type: integer
          description: The reference ID for the Data Provider of this POI
          example: 1
        DataProvidersReference:
          type: string
          description: 'If present, this is the Data Providers own key for this POI within their source data set'
        OperatorID:
          type: integer
          description: The reference ID of the equipment network operator or owner
          default: 0
          example: 3
        OperatorsReference:
          type: string
          description: The network operators own reference for this site (may be a site reference or a single equipment reference)
          example: PG-84306
        UsageTypeID:
          type: integer
          description: 'The reference ID for the site Usage Type, 0 == Unknown'
          default: 0
          example: 4
        UsageCost:
          type: string
          description: Free text description of likely usage costs associated with this site. Generally relates to parking charges whether network operates this site as Free
          example: See network operators app for current charges
        AddressInfo:
          $ref: '#/components/schemas/AddressInfo'
        Connections:
          type: array
          description: List of equipment summary information for this site
          items:
            $ref: '#/components/schemas/ConnectionInfo'
        NumberOfPoints:
          type: integer
          description: The number of bays or discreet stations available overall at this site. This indicates the limiting for number of simultaneous site users.
          default: 0
          example: 2
        GeneralComments:
          type: string
          description: General additional factual information for the POI. Users are discouraged from using this field for opinions on site quality etc.
          default: ''
          example: 'This is an open charge unit installed at the Coneygear Centre at Buttsgrove Way, Huntingdon'
        DatePlanned:
          type: string
          format: date-time
          description: 'The date and time (UTC, ISO 8601) this POI is or was planned for commissioning. In general planned POIs should not be presented to end users until confirmed operational.'
          example: '2020-02-04T06:33:00Z'
        DateLastConfirmed:
          type: string
          format: date-time
          description: 'The date and time (UTC, ISO 8601) this POI was last confirmed according to the data provider or a user. See DateLastVerified for a dynamically computed date based on multiple signals.'
          example: '2020-02-04T06:33:00Z'
        StatusTypeID:
          type: integer
          description: The overall operational status type reference ID for this POI (i.e. Operational etc). 0 == Unknown
          default: 0
          example: 50
        DateLastStatusUpdate:
          type: string
          format: date-time
          description: 'The date and time (UTC, ISO 8601) this POI or directly related child properties were updated.'
          example: '2020-02-04T06:33:00Z'
        MetadataValues:
          type: array
          description: 'Optional array of metadata values. Generally used to indicate data attribution but is also intended for future use to indicate surrounding amenties, links or foreign key values into other data sets.'
          items: {}
        DataQualityLevel:
          type: integer
          description: A metric applied during imports to indicate a quality level based on available information detail (5 == best). Largely unused currently.
          example: 5
        DateCreated:
          type: string
          format: date-time
          description: 'The date and time (UTC, ISO 8601) this POI was added to the Open Charge Map database'
          example: '2020-02-04T06:33:00Z'
        SubmissionStatusTypeID:
          type: integer
          description: The reference ID for the submission status type which applied to this POI.
          default: 0
          example: 200
        DataProvider:
          $ref: '#/components/schemas/DataProvider'
        OperatorInfo:
          $ref: '#/components/schemas/OperatorInfo'
        UsageType:
          $ref: '#/components/schemas/UsageType'
        StatusType:
          $ref: '#/components/schemas/StatusType'
        SubmissionStatus:
          $ref: '#/components/schemas/SubmissionStatusType'
      x-examples:
        Example POI Results:
          ID: 148527
          UUID: 4C524AA1-3413-4D56-804C-480304FEB0FB
          UserComments:
            - ID: string
              ChargePointID: 0
              CommentTypeID: 0
              CommentType: {}
              UserName: string
              Comment: string
              RelatedURL: string
              DateCreated: '2019-08-24T14:15:22Z'
              User:
                ID: 0
                Username: string
                ReputationPoints: 0
                ProfileImageURL: string
              CheckinStatusTypeID: 0
              CheckinStatusType: {}
              '': string
          MediaItems:
            - ID: string
              ChargePointID: string
              ItemURL: string
              ItemThumbnailURL: string
              Comment: string
              IsEnabled: true
              IsVideo: true
              IsFeaturedItem: true
              IsExternalResource: true
              User:
                ID: 0
                Username: string
                ReputationPoints: 0
                ProfileImageURL: string
              DateCreated: string
          IsRecentlyVerified: false
          DateLastVerified: '2020-02-04T06:33:00Z'
          ParentChargePointID: 0
          DataProviderID: 1
          DataProvidersReference: string
          OperatorID: 0
          OperatorsReference: PG-84306
          UsageTypeID: 0
          UsageCost: See network operators app for current charges
          AddressInfo:
            ID: 148879
            description: Coneygear Centre
            AddressLine1: Buttsgrove Way
            AddressLine2: null
            Town: Huntingdon
            StateOrProvince: string
            Postcode: PE29 1PE
            CountryID: 1
            Country:
              ISOCode: GB
              ContinentCode: EU
              ID: 1
              description: United Kingdom
            Latitude: 52.343197
            Longitude: -0.170632
            ContactTelephone1: null
            ContactTelephone2: null
            ContactEmail: string
            AccessComments: string
            RelatedURL: null
            Distance: null
            DistanceUnit: 1
          Connections:
            - ID: 206241
              ConnectionTypeID: 25
              ConnectionType:
                FormalName: IEC 62196-2 Type 2
                IsDiscontinued: false
                IsObsolete: false
                ID: 25
                description: Type 2 (Socket Only)
              Reference: null
              StatusTypeID: 50
              StatusType:
                IsOperational: true
                IsUserSelectable: true
                ID: 50
                description: Operational
              LevelID: 2
              Level:
                ID: 2
                description: 'Level 2 : Medium (Over 2kW)'
                Comments: 'Over 2 kW, usually non-domestic socket type'
                IsFastChargeCapable: false
              Amps: 32
              Voltage: 230
              PowerKW: 7.4
              CurrentTypeID: 10
              CurrentType:
                Description: Alternating Current - Single Phase
                ID: 10
                description: AC (Single-Phase)
              Quantity: 2
              Comments: string
          NumberOfPoints: 0
          GeneralComments: ''
          DatePlanned: '2020-02-04T06:33:00Z'
          DateLastConfirmed: '2020-02-04T06:33:00Z'
          StatusTypeID: 0
          DateLastStatusUpdate: '2020-02-04T06:33:00Z'
          MetadataValues:
            - null
          DataQualityLevel: 5
          DateCreated: '2020-02-04T06:33:00Z'
          SubmissionStatusTypeID: 0
          DataProvider:
            WebsiteURL: 'https://openchargemap.org'
            Comments: string
            DataProviderStatusType:
              IsProviderEnabled: true
              ID:
                - 1
              description:
                - Manual Data Entry
            IsRestrictedEdit: false
            IsOpenDataLicensed: null - true
            IsApprovedImport: null - true
            License: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
            DateLastImported: 'null - ''2020-02-04T23:09:00Z'''
            ID: 1
            description: Open Charge Map Contributors
          OperatorInfo:
            WebsiteURL: 'http://www.pod-point.com/'
            Comments: null
            PhonePrimaryContact: null
            PhoneSecondaryContact: null
            IsPrivateIndividual: false
            AddressInfo:
              ID: 148879
              description: Coneygear Centre
              AddressLine1: Buttsgrove Way
              AddressLine2: null
              Town: Huntingdon
              StateOrProvince: string
              Postcode: PE29 1PE
              CountryID: 1
              Country:
                ISOCode: GB
                ContinentCode: EU
                ID: 1
                description: United Kingdom
              Latitude: 52.343197
              Longitude: -0.170632
              ContactTelephone1: null
              ContactTelephone2: null
              ContactEmail: string
              AccessComments: string
              RelatedURL: null
              Distance: null
              DistanceUnit: 1
            BookingURL: string
            ContactEmail: enquiries@pod-point.com
            FaultReportEmail: enquiries@pod-point.com
            IsRestrictedEdit: true
            ID: 0
            description: POD Point (UK)
          UsageType:
            IsPayAtLocation: true
            IsMembershipRequired: true
            IsAccessKeyRequired: true
            ID: 0
            description: Public - Membership Required
          StatusType:
            IsOperational: true
            IsUserSelectable: true
            ID: 50
            description: Operational
          SubmissionStatus:
            IsLive: true
            ID: 200
            description: Submission Published
    DataProvider:
      type: object
      description: A Data Provider is the controller of the source data set used to construct the details for this POI. Data has been transformed and interpreted from it's original form. Each Data Provider provides data either by an explicit license or agreement.
      properties:
        WebsiteURL:
          type: string
          description: Website URL for this data provider
          example: 'https://openchargemap.org'
          pattern: ^(.*)$
        Comments:
          type: string
          description: General public comments with information about this Data Provider.
        DataProviderStatusType:
          type: object
          description: 'Status object describing whether this data provider is currently enabled and the type of source (manual entry, imported etc)'
          properties:
            IsProviderEnabled:
              type: boolean
              description: 'If false, results from this data provider are not currently enabled'
              default: false
              example: true
            ID:
              type: integer
              description: The reference ID for this provider status type
              default: 0
              example:
                - 1
            description:
              type: string
              description: The Title of this status type
              example:
                - Manual Data Entry
              pattern: ^(.*)$
          required:
            - IsProviderEnabled
            - ID
        IsRestrictedEdit:
          type: boolean
          description: Currently not implemented. Indicates a potential editing restriction.
          default: false
          example: false
        IsOpenDataLicensed:
          type: boolean
          description: 'If true, data provider uses an Open Data license'
          example: true
        IsApprovedImport:
          type: boolean
          description: 'If false, data may not be imported for this provider.'
          example: true
        License:
          type: string
          description: Summary of the licensing which applies for this Data Provider. Each Data Provider has one specific license or agreement. Usage of the data requires acceptance of the given license.
          example: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
          pattern: ^(.*)$
        DateLastImported:
          type: string
          format: date-time
          description: Date and time (UTC) the last import was performed for this data provider (if an import).
          example: '2020-02-04T23:09:00Z'
        ID:
          type: integer
          description: The reference ID for this Data Provider
          example: 1
        Title:
          type: string
          description: The Title for this Data Provider
          example: Open Charge Map Contributors
          pattern: ^(.*)$
      required:
        - IsRestrictedEdit
        - ID
    OperatorInfo:
      type: object
      description: An Operator is the public organisation which controls a network of charging points.
      properties:
        WebsiteURL:
          type: string
          description: Website for more information about this network
          example: 'http://www.pod-point.com/'
          pattern: ^(.*)$
        Comments:
          type: string
          example: null
        PhonePrimaryContact:
          type: string
          description: Primary contact number for network users
          default: null
        PhoneSecondaryContact:
          type: string
          description: Secondary contact number
          default: null
          pattern: ^(.*)$
        IsPrivateIndividual:
          type: boolean
          description: 'If true, this operator represents a private individual'
          deprecated: true
          default: false
          example: false
        AddressInfo:
          $ref: '#/components/schemas/AddressInfo'
        BookingURL:
          type: string
        ContactEmail:
          type: string
          default: ''
          example: enquiries@pod-point.com
          pattern: ^(.*)$
        FaultReportEmail:
          type: string
          description: Used to send automated notification to network operator if a user submits a fault report comment/check-in
          example: enquiries@pod-point.com
          pattern: ^(.*)$
        IsRestrictedEdit:
          type: boolean
          description: 'If true, this network restricts community edits for OCM data'
        ID:
          type: integer
          description: Id
        Title:
          type: string
          description: Title
          example: POD Point (UK)
          pattern: ^(.*)$
      required:
        - ID
    UsageType:
      type: object
      description: The Usage Type of a site indicates the general restrictions on usage.
      properties:
        IsPayAtLocation:
          type: boolean
          description: 'If true, usage requires paying at location'
        IsMembershipRequired:
          type: boolean
          description: 'If true, this usage type requires registration or membership with a service.'
        IsAccessKeyRequired:
          type: boolean
          description: If true this usage required a physical access key
          deprecated: true
        ID:
          type: integer
        Title:
          type: string
          example: Public - Membership Required
          pattern: ^(.*)$
      required:
        - IsPayAtLocation
        - IsMembershipRequired
        - IsAccessKeyRequired
        - ID
    StatusType:
      type: object
      description: The Status Type of a site or equipment item indicates whether it is generally operational.
      properties:
        IsOperational:
          type: boolean
          default: false
          example: true
        IsUserSelectable:
          type: boolean
          default: false
          example: true
        ID:
          type: integer
          example: 50
        Title:
          type: string
          example: Operational
      required:
        - IsOperational
        - IsUserSelectable
        - ID
    SubmissionStatusType:
      type: object
      description: 'Submission Status object, detailing the POI listing status'
      properties:
        ID:
          type: integer
          description: Submission Status Type reference ID
          default: 0
          example: 200
        Title:
          type: string
        IsLive:
          type: boolean
          description: 'If true, POI listing is live (not draft or de-listed)'
          default: false
      required:
        - ID
        - IsLive
    Country:
      type: object
      description: Country details
      properties:
        ID:
          type: integer
          description: The Id Schema
          default: 0
          example: 1
        ISOCode:
          type: string
          description: The Isocode Schema
          default: ''
          example: GB
          pattern: ^(.*)$
        ContinentCode:
          type: string
          description: The Continentcode Schema
          default: ''
          example: EU
          pattern: ^(.*)$
        Title:
          type: string
          description: The Title Schema
          default: ''
          example: United Kingdom
          pattern: ^(.*)$
      required:
        - ID
        - ISOCode
        - ContinentCode
    AddressInfo:
      type: object
      description: Geographic position for site and (nearest) address component information.
      properties:
        ID:
          type: integer
          description: ID
          default: 0
          example: 148879
        AddressLine1:
          type: string
          description: First line of nearby street address
          default: ''
          example: Buttsgrove Way
          pattern: ^(.*)$
        AddressLine2:
          type: string
          description: Second line of nearby street address
          default: null
        Town:
          type: string
          description: Town or City
          example: Huntingdon
          pattern: ^(.*)$
        StateOrProvince:
          type: string
          description: State or Province
        Postcode:
          type: string
          description: Postal code or Zipcode
          example: PE29 1PE
          pattern: ^(.*)$
        CountryID:
          type: integer
          description: The reference ID for the Country
          example: 1
        Country:
          $ref: '#/components/schemas/Country'
        Latitude:
          type: number
          description: Site latitude coordinate in decimal degrees
          default: 0
          example: 52.343197
        Longitude:
          type: number
          description: Site longitude coordinate in decimal degrees
          default: 0
          example: -0.170632
        ContactTelephone1:
          type: string
          description: Primary contact number
          default: null
        ContactTelephone2:
          type: string
          description: Secondary contact number
          default: null
        ContactEmail:
          type: string
          description: Primary contact email
        AccessComments:
          type: string
          description: Guidance for users to use or find the equipment
        RelatedURL:
          type: string
          description: Optional website for more information
          default: null
        Distance:
          type: number
          description: 'Distance from search location, if search is around a point'
          default: null
        DistanceUnit:
          type: integer
          description: 'Unit used for distance, 1= Miles, 2 = KM'
          default: 1
        Title:
          type: string
          description: General title for this location to aid user
      required:
        - ID
        - CountryID
        - Latitude
        - Longitude
    UserComment:
      type: object
      description: A user comment or check-in for a specific charging point (POI/Site)
      properties:
        ID:
          type: string
        ChargePointID:
          type: integer
        CommentTypeID:
          type: integer
        CommentType:
          $ref: '#/components/schemas/UserCommentType'
        UserName:
          type: string
        Comment:
          type: string
        RelatedURL:
          type: string
        DateCreated:
          type: string
          format: date-time
        User:
          $ref: '#/components/schemas/UserInfo'
        CheckinStatusTypeID:
          type: integer
        CheckinStatusType:
          $ref: '#/components/schemas/CheckinStatusType'
    MediaItem:
      type: object
      description: A user submitted media item related to a specific charge point or site. Currently always an image.
      properties:
        ID:
          type: string
        ChargePointID:
          type: string
        ItemURL:
          type: string
        ItemThumbnailURL:
          type: string
        Comment:
          type: string
        IsEnabled:
          type: boolean
        IsVideo:
          type: boolean
        IsFeaturedItem:
          type: boolean
        IsExternalResource:
          type: boolean
        User:
          $ref: '#/components/schemas/UserInfo'
        DateCreated:
          type: string
    ConnectionInfo:
      type: object
      description: |-
        Details on the equipment type and power capability.

        If calling the API in verbose mode related models are also included in the result (e.g. ConnectionType, Level, StatusType, CurrentType)
      properties:
        ID:
          type: integer
          example: 206241
        ConnectionTypeID:
          type: integer
          default: null
          example: 25
        ConnectionType:
          $ref: '#/components/schemas/ConnectionType'
        Reference:
          type: string
          description: Optional operators reference for this connection/port
          default: null
        StatusTypeID:
          type: integer
          description: Status Type reference ID. 0 = Unknown
          default: 0
          example: 50
        StatusType:
          $ref: '#/components/schemas/StatusType'
        LevelID:
          type: integer
          example: 2
          description: A general category for power capability. Depreceated in favour of documenting specific equipment power in kW.
          deprecated: true
        Level:
          $ref: '#/components/schemas/LevelType'
        Amps:
          type: integer
          description: EVSE supply max current in Amps
          default: null
          example: 32
        Voltage:
          type: number
          description: EVSE supply voltage
          default: null
          example: 230
        PowerKW:
          type: number
          description: Peak available power in kW
          default: null
          example: 7.4
        CurrentTypeID:
          description: The supply type reference ID (e.g. DC etc)
          default: null
          example: 10
          type: integer
        CurrentType:
          $ref: '#/components/schemas/SupplyType'
        Quantity:
          type: integer
          description: Optional summary number of equipment items available with this specification
          default: null
          example: 2
        Comments:
          type: string
    ConnectionType:
      type: object
      description: The type of end-user connection an EVSE supports.
      properties:
        FormalName:
          type: string
          description: Formal (standard) name for this connection type
          default: null
          example: IEC 62196-2 Type 2
          pattern: ^(.*)$
        IsDiscontinued:
          type: boolean
          description: 'If true, this is an discontinued but used connection type'
          default: false
          example: false
        IsObsolete:
          type: boolean
          description: 'If true, this is an obsolete connection type and is unlikely top be present in modern infrastructure'
          default: false
          example: false
        ID:
          type: integer
          example: 25
        Title:
          type: string
          example: Type 2 (Socket Only)
    LevelType:
      type: object
      description: A general category for equipment power capability. Deprecated for general use. Currently computed automatically based on equipment power.
      properties:
        ID:
          type: integer
          example: 2
        Title:
          type: string
          example: 'Level 2 : Medium (Over 2kW)'
        Comments:
          type: string
          example: 'Over 2 kW, usually non-domestic socket type'
        IsFastChargeCapable:
          type: boolean
          description: 'If true, this level is considered ''fast'' charging, relative to other levels.'
      required:
        - ID
        - Comments
        - IsFastChargeCapable
    SupplyType:
      type: object
      description: 'Indicates the EVSE power supply type e.g. DC (Direct Current), AC (Single Phase), AC (3 Phase).'
      properties:
        ID:
          type: integer
          example: 10
        Title:
          type: string
          example: AC (Single-Phase)
      required:
        - ID
    UserInfo:
      type: object
      description: Short public summary profile for a specific Open Charge Map user
      properties:
        ID:
          type: integer
        Username:
          type: string
        ReputationPoints:
          type: integer
        ProfileImageURL:
          type: string
    CheckinStatusType:
      type: object
      description: Classification for the users comment or experience using a specific charging location.
      properties:
        ID:
          type: integer
        Title:
          type: string
        IsAutomatedCheckin:
          type: boolean
          description: 'If true, checkin or comment was provided by an automated system.'
        IsPositive:
          type: boolean
          description: 'If true, this type of checkin/comment is considered positive.'
      required:
        - ID
        - IsAutomatedCheckin
    CoreReferenceData:
      type: object
      description: Set of core reference data used for other API results and UI
      properties:
        ChargerTypes:
          type: array
          items:
            $ref: '#/components/schemas/LevelType'
        ConnectionTypes:
          type: array
          items:
            $ref: '#/components/schemas/ConnectionType'
        CheckinStatusTypes:
          type: array
          items:
            $ref: '#/components/schemas/CheckinStatusType'
        Countries:
          type: array
          items:
            $ref: '#/components/schemas/Country'
        CurrentTypes:
          type: array
          items:
            $ref: '#/components/schemas/SupplyType'
        DataProviders:
          type: array
          items:
            $ref: '#/components/schemas/DataProvider'
        DataTypes: {}
        MetadataGroups:
          type: string
        Operators:
          type: array
          items:
            $ref: '#/components/schemas/OperatorInfo'
        StatusTypes:
          type: array
          items:
            $ref: '#/components/schemas/StatusType'
        SubmissionStatusTypes:
          type: array
          items:
            $ref: '#/components/schemas/SubmissionStatusType'
        UsageTypes:
          type: array
          items:
            $ref: '#/components/schemas/UsageType'
        UserCommentTypes:
          type: array
          items:
            $ref: '#/components/schemas/UserCommentType'
      x-examples:
        example-1:
          ChargerTypes:
            - ID: 2
              description: 'Level 2 : Medium (Over 2kW)'
              Comments: 'Over 2 kW, usually non-domestic socket type'
              IsFastChargeCapable: false
          ConnectionTypes:
            - FormalName: IEC 62196-2 Type 2
              IsDiscontinued: false
              IsObsolete: false
              ID: 25
              description: Type 2 (Socket Only)
          CheckinStatusTypes:
            - ID: 0
              description: string
              IsAutomatedCheckin: true
              IsPositive: true
          Countries:
            - ISOCode: GB
              ContinentCode: EU
              ID: 1
              description: United Kingdom
          CurrentTypes:
            - Description: Alternating Current - Single Phase
              ID: 10
              description: AC (Single-Phase)
          DataProviders:
            - WebsiteURL: 'https://openchargemap.org'
              Comments: string
              DataProviderStatusType:
                IsProviderEnabled: true
                ID:
                  - 1
                description:
                  - Manual Data Entry
              IsRestrictedEdit: false
              IsOpenDataLicensed: null - true
              IsApprovedImport: null - true
              License: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
              DateLastImported: 'null - ''2020-02-04T23:09:00Z'''
              ID: 1
              description: Open Charge Map Contributors
          DataTypes: null
          MetadataGroups: string
          Operators:
            - WebsiteURL: 'http://www.pod-point.com/'
              Comments: null
              PhonePrimaryContact: null
              PhoneSecondaryContact: null
              IsPrivateIndividual: false
              AddressInfo:
                ID: 148879
                description: Coneygear Centre
                AddressLine1: Buttsgrove Way
                AddressLine2: null
                Town: Huntingdon
                StateOrProvince: string
                Postcode: PE29 1PE
                CountryID: 1
                Country:
                  ISOCode: GB
                  ContinentCode: EU
                  ID: 1
                  description: United Kingdom
                Latitude: 52.343197
                Longitude: -0.170632
                ContactTelephone1: null
                ContactTelephone2: null
                ContactEmail: string
                AccessComments: string
                RelatedURL: null
                Distance: null
                DistanceUnit: 1
              BookingURL: string
              ContactEmail: enquiries@pod-point.com
              FaultReportEmail: enquiries@pod-point.com
              IsRestrictedEdit: true
              ID: 0
              description: POD Point (UK)
          StatusTypes:
            - IsOperational: true
              IsUserSelectable: true
              ID: 50
              description: Operational
          SubmissionStatusTypes:
            - IsLive: true
              ID: 200
              description: Submission Published
          UsageTypes:
            - IsPayAtLocation: true
              IsMembershipRequired: true
              IsAccessKeyRequired: true
              ID: 0
              description: Public - Membership Required
          UserCommentTypes:
            - ID: 0
              Title: string
    UserCommentType:
      title: UserCommentType
      type: object
      properties:
        ID:
          type: integer
        Title:
          type: string
      description: 'Category for a user comment, e.g. General Comment, Fault Report (Notice To Users And Operator)'
    AuthenticationResult:
      description: ''
      type: object
      x-examples:
        example-1:
          Data:
            UserProfile:
              ID: 1000
              Username: Joe Bloggs
              Profile: "Example person who uses open charge map \U0001F918"
              Location: 'San Francisco, US'
              WebsiteURL: 'https://openchargemap.org'
              ReputationPoints: 2008
              Permissions: '{"Permissions":[{"Level":100},{"Level":1000}],"LegacyPermissions":"[CountryLevel_Editor=All];[Administrator=true];"}'
              DateCreated: '2011-09-28T15:11:00'
              DateLastLogin: '2021-11-09T07:49:00'
              IsProfilePublic: true
              Latitude: -31
              Longitude: 115
              EmailAddress: example@example.com
              EmailHash: null
              ProfileImageURL: 'https://www.gravatar.com/avatar/e3e76940eb5e85220db216603ee6b00f?s=80&d=robohash'
            access_token: eXampleJwt.AccessTOKEN
          Metadata:
            StatusCode: 200
      properties:
        Data:
          type: object
          required:
            - UserProfile
            - access_token
          properties:
            UserProfile:
              type: object
              required:
                - ID
                - Username
                - Profile
                - Location
                - WebsiteURL
                - ReputationPoints
                - Permissions
                - DateCreated
                - DateLastLogin
                - IsProfilePublic
                - Latitude
                - Longitude
                - EmailAddress
                - ProfileImageURL
              properties:
                ID:
                  type: number
                Username:
                  type: string
                  minLength: 1
                Profile:
                  type: string
                  minLength: 1
                Location:
                  type: string
                  minLength: 1
                WebsiteURL:
                  type: string
                  minLength: 1
                ReputationPoints:
                  type: number
                Permissions:
                  type: string
                  minLength: 1
                DateCreated:
                  type: string
                  minLength: 1
                DateLastLogin:
                  type: string
                  minLength: 1
                IsProfilePublic:
                  type: boolean
                Latitude:
                  type: number
                Longitude:
                  type: number
                EmailAddress:
                  type: string
                  minLength: 1
                EmailHash: {}
                ProfileImageURL:
                  type: string
                  minLength: 1
            access_token:
              type: string
              minLength: 1
        Metadata:
          type: object
          required:
            - StatusCode
          properties:
            StatusCode:
              type: number
      required:
        - Data
        - Metadata
    UserProfile:
      description: 'Full user profile, including non-public fields such as Email Address'
      type: object
      x-examples:
        example-userprofile:
          ID: 1000
          Username: Joe Bloggs
          Profile: "Example Open Charge Map user. \U0001F918"
          Location: 'San Francisco, US'
          WebsiteURL: 'https://openchargemap.org'
          ReputationPoints: 2008
          Permissions: '{"Permissions":[{"Level":100},{"Level":1000}],"LegacyPermissions":"[CountryLevel_Editor=All];[Administrator=true];"}'
          DateCreated: '2011-09-28T15:11:00'
          DateLastLogin: '2021-11-09T07:49:00'
          IsProfilePublic: true
          Latitude: -31
          Longitude: 115
          EmailAddress: example@example.com
          ProfileImageURL: 'https://www.gravatar.com/avatar/examplef?s=80&d=robohash'
      properties:
        ID:
          type: number
        Username:
          type: string
          minLength: 1
        Profile:
          type: string
          minLength: 1
        Location:
          type: string
          minLength: 1
        WebsiteURL:
          type: string
          minLength: 1
        ReputationPoints:
          type: number
        Permissions:
          type: string
          minLength: 1
        DateCreated:
          type: string
          minLength: 1
        DateLastLogin:
          type: string
          minLength: 1
        IsProfilePublic:
          type: boolean
        Latitude:
          type: number
        Longitude:
          type: number
        EmailAddress:
          type: string
          minLength: 1
        ProfileImageURL:
          type: string
          minLength: 1
      required:
        - ID
        - Username
        - DateCreated
        - IsProfilePublic
  securitySchemes:
    APIKeyQueryString:
      name: key
      type: apiKey
      in: query
      description: API Key supplied as query string parameter
    APIKeyHeader:
      name: X-API-Key
      type: apiKey
      in: header
    UserAuthentication:
      type: http
      scheme: bearer
  responses:
    POI:
      description: List of POIs (sites) with associated equipment summary information.
      content:
        application/json:
          schema:
            type: array
            items:
              $ref: '#/components/schemas/POI'
          example:
            Example Results:
              - DataProvider:
                  WebsiteURL: 'http://openchargemap.org'
                  Comments: null
                  DataProviderStatusType:
                    IsProviderEnabled: true
                    ID: 1
                    description: Manual Data Entry
                  IsRestrictedEdit: false
                  IsOpenDataLicensed: true
                  IsApprovedImport: true
                  License: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
                  DateLastImported: null
                  ID: 1
                  description: Open Charge Map Contributors
                OperatorInfo:
                  WebsiteURL: 'https://www.afconev.co.il/'
                  Comments: null
                  PhonePrimaryContact: null
                  PhoneSecondaryContact: null
                  IsPrivateIndividual: false
                  AddressInfo: null
                  BookingURL: null
                  ContactEmail: null
                  FaultReportEmail: null
                  IsRestrictedEdit: false
                  ID: 3435
                  description: Afcon (Israel)
                UsageType:
                  IsPayAtLocation: false
                  IsMembershipRequired: true
                  IsAccessKeyRequired: true
                  ID: 4
                  description: Public - Membership Required
                StatusType:
                  IsOperational: true
                  IsUserSelectable: true
                  ID: 50
                  description: Operational
                SubmissionStatus:
                  IsLive: true
                  ID: 200
                  description: Submission Published
                UserComments: null
                PercentageSimilarity: null
                MediaItems: null
                IsRecentlyVerified: true
                DateLastVerified: '2021-11-07T16:36:00Z'
                ID: 189853
                UUID: 1686CE5C-95E8-450B-93C3-95D1B1AF98D4
                ParentChargePointID: null
                DataProviderID: 1
                DataProvidersReference: null
                OperatorID: 3435
                OperatorsReference: null
                UsageTypeID: 4
                UsageCost: null
                AddressInfo:
                  ID: 190212
                  description: בית משה
                  AddressLine1: כצנלסון 10
                  AddressLine2: null
                  Town: Ashkelon
                  StateOrProvince: South District
                  Postcode: '78100'
                  CountryID: 111
                  Country:
                    ISOCode: IL
                    ContinentCode: AS
                    ID: 111
                    description: Israel
                  Latitude: 31.66148706692408
                  Longitude: 34.587748089749425
                  ContactTelephone1: null
                  ContactTelephone2: null
                  ContactEmail: null
                  AccessComments: null
                  RelatedURL: 'https://account.afconev.co.il/findCharger?31.6615343,34.5873913,20z,%D7%9B%D7%A6%D7%A0%D7%9C%D7%A1%D7%95%D7%9F%2010%20%D7%90%D7%A9%D7%A7%D7%9C%D7%95%D7%9F,494si'
                  Distance: null
                  DistanceUnit: 0
                Connections:
                  - ID: 307235
                    ConnectionTypeID: 25
                    ConnectionType:
                      FormalName: IEC 62196-2 Type 2
                      IsDiscontinued: false
                      IsObsolete: false
                      ID: 25
                      description: Type 2 (Socket Only)
                    Reference: null
                    StatusTypeID: 50
                    StatusType:
                      IsOperational: true
                      IsUserSelectable: true
                      ID: 50
                      description: Operational
                    LevelID: 2
                    Level:
                      Comments: 'Over 2 kW, usually non-domestic socket type'
                      IsFastChargeCapable: false
                      ID: 2
                      description: 'Level 2 : Medium (Over 2kW)'
                    Amps: null
                    Voltage: null
                    PowerKW: 22
                    CurrentTypeID: 20
                    CurrentType:
                      Description: Alternating Current - Three Phase
                      ID: 20
                      description: AC (Three-Phase)
                    Quantity: 3
                    Comments: null
                  - ID: 307236
                    ConnectionTypeID: 33
                    ConnectionType:
                      FormalName: IEC 62196-3 Configuration FF
                      IsDiscontinued: false
                      IsObsolete: false
                      ID: 33
                      description: CCS (Type 2)
                    Reference: null
                    StatusTypeID: 50
                    StatusType:
                      IsOperational: true
                      IsUserSelectable: true
                      ID: 50
                      description: Operational
                    LevelID: 3
                    Level:
                      Comments: 40KW and Higher
                      IsFastChargeCapable: true
                      ID: 3
                      description: 'Level 3:  High (Over 40kW)'
                    Amps: null
                    Voltage: null
                    PowerKW: 50
                    CurrentTypeID: 30
                    CurrentType:
                      Description: Direct Current
                      ID: 30
                      description: DC
                    Quantity: 1
                    Comments: null
                NumberOfPoints: 4
                GeneralComments: null
                DatePlanned: null
                DateLastConfirmed: null
                StatusTypeID: 50
                DateLastStatusUpdate: '2021-11-07T16:36:00Z'
                MetadataValues: null
                DataQualityLevel: 1
                DateCreated: '2021-11-07T16:36:00Z'
                SubmissionStatusTypeID: 200
              - ID: 148527
                UUID: 4C524AA1-3413-4D56-804C-480304FEB0FB
                UserComments:
                  - ID: string
                    ChargePointID: 0
                    CommentTypeID: 0
                    CommentType:
                      ID: 0
                      Title: string
                    UserName: string
                    Comment: string
                    RelatedURL: string
                    DateCreated: '2019-08-24T14:15:22Z'
                    User:
                      ID: 0
                      Username: string
                      ReputationPoints: 0
                      ProfileImageURL: string
                    CheckinStatusTypeID: 0
                    CheckinStatusType:
                      ID: 0
                      Title: string
                      IsAutomatedCheckin: true
                      IsPositive: true
                MediaItems:
                  - ID: string
                    ChargePointID: string
                    ItemURL: string
                    ItemThumbnailURL: string
                    Comment: string
                    IsEnabled: true
                    IsVideo: true
                    IsFeaturedItem: true
                    IsExternalResource: true
                    User:
                      ID: 0
                      Username: string
                      ReputationPoints: 0
                      ProfileImageURL: string
                    DateCreated: string
                IsRecentlyVerified: true
                DateLastVerified: '2020-02-04T06:33:00Z'
                ParentChargePointID: 0
                DataProviderID: 1
                DataProvidersReference: string
                OperatorID: 3
                OperatorsReference: PG-84306
                UsageTypeID: 4
                UsageCost: See network operators app for current charges
                AddressInfo:
                  ID: 148879
                  AddressLine1: Buttsgrove Way
                  AddressLine2: null
                  Town: Huntingdon
                  StateOrProvince: string
                  Postcode: PE29 1PE
                  CountryID: 1
                  Country:
                    ID: 1
                    ISOCode: GB
                    ContinentCode: EU
                    Title: United Kingdom
                  Latitude: 52.343197
                  Longitude: -0.170632
                  ContactTelephone1: null
                  ContactTelephone2: null
                  ContactEmail: string
                  AccessComments: string
                  RelatedURL: null
                  Distance: null
                  DistanceUnit: 1
                  Title: string
                Connections:
                  - ID: 206241
                    ConnectionTypeID: 25
                    ConnectionType:
                      FormalName: IEC 62196-2 Type 2
                      IsDiscontinued: false
                      IsObsolete: false
                      ID: 25
                      Title: Type 2 (Socket Only)
                    Reference: null
                    StatusTypeID: 50
                    StatusType:
                      IsOperational: true
                      IsUserSelectable: true
                      ID: 50
                      Title: Operational
                    LevelID: 2
                    Level:
                      ID: 2
                      Title: 'Level 2 : Medium (Over 2kW)'
                      Comments: 'Over 2 kW, usually non-domestic socket type'
                      IsFastChargeCapable: true
                    Amps: 32
                    Voltage: 230
                    PowerKW: 7.4
                    CurrentTypeID: 10
                    CurrentType:
                      ID: 10
                      Title: AC (Single-Phase)
                    Quantity: 2
                    Comments: string
                NumberOfPoints: 2
                GeneralComments: 'This is an open charge unit installed at the Coneygear Centre at Buttsgrove Way, Huntingdon'
                DatePlanned: '2020-02-04T06:33:00Z'
                DateLastConfirmed: '2020-02-04T06:33:00Z'
                StatusTypeID: 50
                DateLastStatusUpdate: '2020-02-04T06:33:00Z'
                MetadataValues:
                  - null
                DataQualityLevel: 5
                DateCreated: '2020-02-04T06:33:00Z'
                SubmissionStatusTypeID: 200
                DataProvider:
                  WebsiteURL: 'https://openchargemap.org'
                  Comments: string
                  DataProviderStatusType:
                    IsProviderEnabled: true
                    ID:
                      - 1
                    description:
                      - Manual Data Entry
                  IsRestrictedEdit: false
                  IsOpenDataLicensed: null - true
                  IsApprovedImport: null - true
                  License: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
                  DateLastImported: 'null - ''2020-02-04T23:09:00Z'''
                  ID: 1
                  Title: Open Charge Map Contributors
                OperatorInfo:
                  WebsiteURL: 'http://www.pod-point.com/'
                  Comments: null
                  PhonePrimaryContact: null
                  PhoneSecondaryContact: null
                  IsPrivateIndividual: false
                  AddressInfo:
                    ID: 148879
                    AddressLine1: Buttsgrove Way
                    AddressLine2: null
                    Town: Huntingdon
                    StateOrProvince: string
                    Postcode: PE29 1PE
                    CountryID: 1
                    Country:
                      ID: 1
                      ISOCode: GB
                      ContinentCode: EU
                      Title: United Kingdom
                    Latitude: 52.343197
                    Longitude: -0.170632
                    ContactTelephone1: null
                    ContactTelephone2: null
                    ContactEmail: string
                    AccessComments: string
                    RelatedURL: null
                    Distance: null
                    DistanceUnit: 1
                    Title: string
                  BookingURL: string
                  ContactEmail: enquiries@pod-point.com
                  FaultReportEmail: enquiries@pod-point.com
                  IsRestrictedEdit: true
                  ID: 0
                  Title: POD Point (UK)
                UsageType:
                  IsPayAtLocation: true
                  IsMembershipRequired: true
                  IsAccessKeyRequired: true
                  ID: 0
                  Title: Public - Membership Required
                StatusType:
                  IsOperational: true
                  IsUserSelectable: true
                  ID: 50
                  Title: Operational
                SubmissionStatus:
                  ID: 200
                  Title: string
                  IsLive: false
      headers: {}
security:
  - APIKeyQueryString: []
  - APIKeyHeader: []
"""

TEST_AUTH_RESPONSE = {
    "Data": {
        "UserProfile": {
            "ID": 52757,
            "IdentityProvider": "OCM",
            "Identifier": "charlesbrown@test.com",
            "CurrentSessionToken": "01234567-89ab-cdef-0123-456789abcdef",
            "Username": "cbrown",
            "Profile": None,
            "Location": None,
            "WebsiteURL": None,
            "ReputationPoints": 0,
            "Permissions": None,
            "PermissionsRequested": None,
            "DateCreated": "",
            "DateLastLogin": "2024-06-14T01:59:00",
            "IsProfilePublic": True,
            "IsEmergencyChargingProvider": False,
            "IsPublicChargingProvider": False,
            "Latitude": None,
            "Longitude": None,
            "EmailAddress": "charlesbrown@test.com",
            "EmailHash": None,
            "ProfileImageURL": "",
            "IsCurrentSessionTokenValid": None,
            "APIKey": None,
            "SyncedSettings": None
        },
        "access_token": "Whentryingtoexpressoneself,it'sfranklyquiteabsurdToleafthroughlengthylexiconstofindtheperfectwordAlittlespontaneitykeepsconversationkeenYouneedtofindawaytosay,preciselywhatyoumeanSupercalifragilisticexpialidocious!EventhoughthesoundofitissomethingquiteatrociousIfyousayitloudenough,you'llalwayssoundprecocious!Supercalifragilisticexpialidocious"
    },
    "Metadata": {
        "StatusCode": 200
    }
}

TEST_COMMENT_CHECKIN_RESPONSE = {
  "status": "OK",
  "description": "OK"
}
