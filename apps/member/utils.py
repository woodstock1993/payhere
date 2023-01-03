from django.core.validators import RegexValidator
from drf_yasg import openapi
from rest_framework import status
from rest_framework.exceptions import APIException

# PW : 비밀번호는 영문,숫자 조합으로 8자 이상으로 입력해주세요.
password_validator = RegexValidator(
    "^(?=.*[A-Za-z])(?=[~`!@#$%^&*()\-_+={[}\]|\\;:'\"<,>.?\/]*)(?=.*\d)[A-Za-z\d~`!@#$%^&*()\-_+={[}\]|\\;:'\"<,>.?\/]{8,20}$",
    "check your pw",
)


class MemberCreated(APIException):    
    status_code = status.HTTP_201_CREATED
    default_code = 'MEMBER_CREATED'
    default_detail = 'member is created'

    @classmethod
    def response(cls, data=None):
        res = openapi.Response(
            description=MemberCreated.default_detail,
            examples={
                "application/json": {
                    "data": data,
                    "meta": {                        
                        "code": MemberCreated.status_code,
                        "systemCode": MemberCreated.default_code,                        
                        "systemMessage": MemberCreated.default_detail,
                    },
                }
            },
        )
        return res    