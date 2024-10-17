// 5-payment.test.js
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', function () {
  let consoleSpy;

  // Before each test, create a spy on console.log
  beforeEach(function () {
    consoleSpy = sinon.spy(console, 'log');
  });

  // After each test, restore the original console.log function
  afterEach(function () {
    sinon.restore();
  });

  it('should log the correct total when called with 100 and 20', function () {
    sendPaymentRequestToApi(100, 20);
    
    // Verify the console logged the correct message
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    // Ensure console.log is only called once
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('should log the correct total when called with 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);
    
    // Verify the console logged the correct message
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    // Ensure console.log is only called once
    expect(consoleSpy.calledOnce).to.be.true;
  });
});