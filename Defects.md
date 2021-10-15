## Defects

#### No1 When request is passed， the status_code is not 200，but 201
【Reproduction】
1.send a normal request
2.when the request is passed
3.check the response
【Results】
status_code of the response is "200"
【Expect】
status_code is "200"


#### No2 Defact Description
When account_name is moare than 10 characters, request is success
【Reproduction】
1.send a request for account_name is more than 10 characters
(eg. "account_name": "John Walker John Walker John Walker John",)
【Results】
request is success
【Expect】
the account_name length is from 2 to 10
(the requirement of account_name length maybe changed, account_name length is from 2 to 200. need to confirm.)

#### No3 Defect Description
When bank_country_code is AU or CN, payment_methods can not support LOCAL, request is failed
【Reproduction】
1.Send a request for payment_methods is LOCAL, bank_country_code is AU（or CN）
【Results】
1.400 Bad Request

    -Response when bank_country_code is AU:
{
  "code": "payment_schema_validation_failed",
  "message": "Should equal SWIFT",
  "source": "payment_methods.0"
}

    -Response when bank_country_code is CN:
{
  "code": "payment_schema_validation_failed",
  "message": "This field is required",
  "source": "beneficiary.additional_info.business_registration_number"
}
【Expect】
not for sure that LOCAL payment methods is support to AU or CN
need to confirm
![avatar](/Users/gaoyuhang/Downloads/1.png)

#### No4 Defect Description
when bank_country_code is AU, account_routing_type1 is not limited
【Reproduction】
1.Send a request for bank_country_code is AU and account_routing_type1 is aba
2.Check the response
【Results】
The request is passed
【Expect】
400 Bad Request
message should be "Should equal bsb"