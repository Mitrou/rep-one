*** Settings ***
Documentation  qwe
Library  Selenium2Library


*** Variables ***


*** Test Cases ***
User must sign in to check out
    [Documentation]  Basic info
    [Tags]  Smoke
    Open Browser  http://www.amazon.com  Chrome
    Close Browser

*** Keywords ***
