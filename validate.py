# import os
# import pathlib
# import pytest
# import subprocess
# import sys
#
#
# def cypress_exeuction():
#     result = subprocess.run(['npx','cypress','run','--spec', 'cypress/e2e/spec.cy.ts', '--config-file', '/home/alister/B/Code/cypress/cypress-ts-config/cypress.config.ts'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#     print(result.returncode)
#     if result.returncode!=0:
#         print(result.stdout.decode())
#     assert (result.returncode ==0)
#
# cypress_exeuction()


import subprocess

# Define the command to run Cypress script
cypress_command = "npx cypress run --spec cypress/e2e/spec.cy.ts --config-file /home/alister/B/Code/cypress/cypress-ts-config/cypress.config.ts"


# Run the Cypress script using subprocess.run
result = subprocess.run(cypress_command, shell=True, capture_output=True, text=True)

# Print the result
print("Exit code:", result.returncode)
print("Standard output:\n", result.stdout)
print("Standard error:\n", result.stderr)
