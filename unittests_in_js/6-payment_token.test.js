// 6-payment_token.test.js

const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', function () {
  it('should return a resolved promise with correct data when success is true', function (done) {
    // Call the async function and wait for its resolution
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Assert that the response contains the expected data
        expect(response).to.include({ data: 'Successful response from the API' });
        // Call done to signify the test is complete
        done();
      })
      .catch((err) => done(err)); // Handle any unexpected error in the promise
  });
});