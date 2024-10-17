// 4-payment.test.js
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { expect } = require('chai');

describe('sendPaymentRequestToApi', () => {
    let stub, spy;

    beforeEach(() => {
        // Stub the Utils.calculateNumber function to always return 10
        stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        // Spy on console.log to verify the output message
        spy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the stub and spy after each test
        stub.restore();
        spy.restore();
    });

    it('stubs Utils.calculateNumber to return 10', () => {
        sendPaymentRequestToApi(100, 20);

        // Verify that the stub was called with the correct arguments
        expect(stub.calledOnce).to.be.true;
        expect(stub.calledWith('SUM', 100, 20)).to.be.true;

        // Verify that console.log was called with the correct message
        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWith('The total is: 10')).to.be.true;
    });
});