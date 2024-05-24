/// <reference types="cypress" />

describe('Test checkout', () =>
    // click the butto nwhich contains To events
    it('Test checkout', () => {
        cy.visit('http://localhost:8080/')
        // cy.get('button').contains('To events').click()
        cy.contains('a', 'To events').click()
        cy.get('a').contains('View Details').click()
        cy.get('button').contains('Checkout').click()
        cy.get('input[name="userName"]').type('test')
        cy.get('input[name="userContact"]').type('1234567890')
        cy.get('input[name="billingAddressStreet"]').type('Raatuse 22')
        cy.get('input[name="billingAddressCity"]').type('Tartu')
        cy.get('input[name="billingAddressState"]').type('Estonia')
        cy.get('input[name="billingAddressCity"]').type('billingAddressZip')
        cy.get('input[name="billingAddressCity"]').type('51009')
        // from form-control billingAddressCountry select Estonia
        cy.get('select[name="billingAddressCountry"]').select('Estonia')
        cy.get('input[name="creditCardNumber"]').type('1111222233334444')
        cy.get('input[name="creditCardExpirationDate"]').type('05/21')
        cy.get('input[name="creditCardCVV"]').type('123')
        
        cy.get('button').contains('Submit').click()
    }
)

)