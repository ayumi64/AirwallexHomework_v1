# NOTE: Generated By HttpRunner v3.1.4
# FROM: ./testcases/testcase_bank_country_code_parametrize.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTestcaseBankCountryCodeParametrize(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "bank_country_code-swift_code": [
                    ["US", "CHASUS33"],
                    ["AU", "CITIAUSX"],
                    ["CN", "PCBCCNBJSZX"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

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
            RunRequest("bank_country_code_parametrize")
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
                            "account_routing_type1": "bsb",
                            "account_routing_value1": "021000022",
                            "bank_country_code": "$bank_country_code",
                            "bank_name": "JP Morgan Chase Bank",
                            "swift_code": "$swift_code",
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
            .assert_equal(
                "body.beneficiary.bank_details.bank_country_code", "$bank_country_code"
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseTestcaseBankCountryCodeParametrize().test_start()
