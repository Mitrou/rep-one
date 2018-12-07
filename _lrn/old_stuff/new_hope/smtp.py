__author__ = 'Owner'
# content of ./test_smtpsimple.py
import pytest

# @pytest.fixture
# def smtp():
#     import smtplib
#     return smtplib.SMTP("smtp.gmail.com")

@pytest.fixture
def lol():
    # import selenium
    from selenium import webdriver
    dr = webdriver.Chrome()
    return dr.get("https://www.google.com.ua/")

# def test_ehlo(smtp):
#     response, msg = smtp.ehlo()
#     assert response == 250
#     assert 0 # for demo purposes


# def test_lol(lol):
#     lol.assertIn("Google", lol.title)
#     # assert 0

def test_lol(lol):
    a = 1
    b = 1
    assert a == b