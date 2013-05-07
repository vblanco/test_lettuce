Feature: Static pages with Django

    Scenario: Static page /help
        Given I navigate to "/help"
        Then I see the header "Help"

    Scenario: Static page /about
        Given I navigate to "/about"
        Then I see the header "About"

