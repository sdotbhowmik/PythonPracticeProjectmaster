*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${LOGIN URL}      https://sdotbhowmik.github.io/
${BROWSER}        Chrome

*** Keywords ***
Open Browser To Homepage Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Subrata Kumar Bhowmik's Portfolio

Clink on Read more
    click link      //*[@id="skills"]/div/div/div[1]/a


*** Test Cases ***
Valid Login
    Open Browser To Homepage Page
    Welcome Page Should Be Open
    [Teardown]    Close Browser





