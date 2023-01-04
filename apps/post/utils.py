from django.core.validators import RegexValidator

# PW : 비밀번호는 영문,숫자 조합으로 8자 이상으로 입력해주세요.
password_validator = RegexValidator(
    "^(?=.*[A-Za-z])(?=[~`!@#$%^&*()\-_+={[}\]|\\;:'\"<,>.?\/]*)(?=.*\d)[A-Za-z\d~`!@#$%^&*()\-_+={[}\]|\\;:'\"<,>.?\/]{8,20}$",
    "check your pw",

)