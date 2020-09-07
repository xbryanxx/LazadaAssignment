Feature: Add and Checkout Specific Items

  Scenario: Add one item from beverages
    Given We go to homepage and login
    When We navigate to the Beverages and Water
    Then Add one Item from Beverages and Water

  Scenario: Add one item from Spirits
    Given We go to homepage and login
    When We navigate to the Spirits
    Then Add one Item from Spirits

  Scenario: Update cart and check out
    Given We go to homepage and login
    When Update number of items
    Then Check out items