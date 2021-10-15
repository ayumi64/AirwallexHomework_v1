# NOTE: Generated By HttpRunner v3.1.4
# FROM: ./testcases/testcase_payment_method.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTestcasePaymentMethod(HttpRunner):

    config = (
        Config("/api/v1/beneficiaries/create")
        .base_url("https://api-demo.airwallex.com")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("get_Token")
            .post("/api/v1/authentication/login")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "Content-Type": "application/json",
                    "x-api-key": "2308e2dd300f6b959b7f4e0a52ba9181186fc92f075f7e64ee9fa0b6b1ada094c39c9a9f39f06693d06b17067f78d4e7",
                    "x-client-id": "KJbr_Xs5TLmhY03JWSi3NQ",
                }
            )
            .with_data("")
            .extract()
            .with_jmespath("body.token", "token")
            .validate()
            .assert_equal("status_code", 201)
        ),
        Step(
            RunRequest("payment_methods_abnormal")
            .post("/api/v1/beneficiaries/create")
            .with_headers(
                **{"Content-Type": "application/json", "Authorization": "Bearer $token"}
            )
            .with_json(
                {
                    "beneficiary": {
                        "additional_info": {"personal_email": "john.walker@gmail.com"},
                        "address": {
                            "city": "Seattle",
                            "country_code": "US",
                            "postcode": "98104",
                            "state": "Washington",
                            "street_address": "412 5th Avenue",
                        },
                        "bank_details": {
                            "account_currency": "USD",
                            "account_name": "John Walker",
                            "account_number": "50001121",
                            "account_routing_type1": "aba",
                            "account_routing_value1": "021000021",
                            "bank_country_code": "US",
                            "bank_name": "JP Morgan Chase Bank",
                            "local_clearing_system": "ACH",
                        },
                        "company_name": "ABC University",
                        "entity_type": "COMPANY",
                    },
                    "nickname": "ABC University",
                    "payment_methods": ["LOCAL1"],
                }
            )
            .validate()
            .assert_equal("status_code", 400)
            .assert_equal(
                "body.message",
                "No enum constant com.airwallex.domain.transaction.payment.PaymentMethod.LOCAL1",
            )
            .assert_equal("body.source", "payment_methods")
        ),
        Step(
            RunRequest("payment_methods_LOCAL")
            .post("/api/v1/beneficiaries/create")
            .with_headers(
                **{"Content-Type": "application/json", "Authorization": "Bearer $token"}
            )
            .with_json(
                {
                    "beneficiary": {
                        "additional_info": {"personal_email": "john.walker@gmail.com"},
                        "address": {
                            "city": "Seattle",
                            "country_code": "US",
                            "postcode": "98104",
                            "state": "Washington",
                            "street_address": "412 5th Avenue",
                        },
                        "bank_details": {
                            "account_currency": "USD",
                            "account_name": "John Walker",
                            "account_number": "50001121",
                            "account_routing_type1": "aba",
                            "account_routing_value1": "021000021",
                            "bank_country_code": "US",
                            "bank_name": "JP Morgan Chase Bank",
                            "local_clearing_system": "ACH",
                        },
                        "company_name": "ABC University",
                        "entity_type": "COMPANY",
                    },
                    "nickname": "ABC University",
                    "payment_methods": ["LOCAL"],
                }
            )
            .validate()
            .assert_equal("status_code", 201)
            .assert_equal("body.payment_methods[0]", "LOCAL")
        ),
        Step(
            RunRequest("payment_methods_SWIFT")
            .post("/api/v1/beneficiaries/create")
            .with_headers(
                **{"Content-Type": "application/json", "Authorization": "Bearer $token"}
            )
            .with_json(
                {
                    "beneficiary": {
                        "additional_info": {"personal_email": "john.walker@gmail.com"},
                        "address": {
                            "city": "Seattle",
                            "country_code": "US",
                            "postcode": "98104",
                            "state": "Washington",
                            "street_address": "412 5th Avenue",
                        },
                        "bank_details": {
                            "account_currency": "USD",
                            "account_name": "John Walker",
                            "account_number": "50001121",
                            "account_routing_type1": "aba",
                            "bank_country_code": "US",
                            "bank_name": "JP Morgan Chase Bank",
                            "swift_code": "CHASUS33",
                        },
                        "company_name": "ABC University",
                        "entity_type": "COMPANY",
                    },
                    "nickname": "ABC University",
                    "payment_methods": ["SWIFT"],
                }
            )
            .validate()
            .assert_equal("status_code", 201)
            .assert_equal("body.payment_methods[0]", "SWIFT")
        ),
    ]


if __name__ == "__main__":
    TestCaseTestcasePaymentMethod().test_start()
