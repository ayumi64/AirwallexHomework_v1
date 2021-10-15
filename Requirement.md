# API testing Requirements

#### Path: api/v1/beneficiaries/create

#### Payload fields:

payment_method: mandatory, value should be either LOCAL or SWIFT bank_country_code: mandatory, can be one of US, AU, CN
account name: mandatory, any character, length from 2 to 10
account number: mandatory
    for US, account number is 1-17 character long, can be any character for AU, account number is 6-9 character long, can be any character for CN, account number is 8-20 character long, can be any character
swift_code:
    mandatory when payment method is SWIFT
    the 5th and 6th character of swift code should match the bank country code, e.g. ICBKCNBJ is a valid swift code for CN swift code should be either 8 or 11 characters
bsb:
    mandatory when bank country is AU
    6 characters 
aba:
    mandatory when bank country is US 
    9 characters

If the request passes the field validation, 200 response will returned.
If the request failed the validation, we need to return 400 http response with proper error message, some sample messages as below:
    when account_number not given: "'account_number' is required"
    account_number length error: "Length of account_number should be between 7 and 11 when bank_country_code is 'US'" wrong swift code: "The swift code is not valid for the given bank country code: US"
    swift code length error: "Length of 'swift_code' should be either 8 or 11"
