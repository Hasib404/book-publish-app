from api.user.controller import are_you_darth_vader
from utils.security import create_access_token, get_password_hash, verify_password


def test_darth_vader_invasion():
    name = "Darth Vader"
    author_pseudonym = "Darth Vader"
    res = are_you_darth_vader(name, author_pseudonym)
    assert res


def test_access_token_creation():
    subject = ["username", "test@testmail.com"]
    res = create_access_token(subject)
    assert len(res) > 1


def test_password_hash():
    password = "darthvader"
    res = get_password_hash(password)
    assert len(res) > 1


def test_varify_password():
    plain_pass = "darthvader"
    hashed_pass = get_password_hash(plain_pass)
    res = verify_password(plain_pass, hashed_pass)
    assert res
