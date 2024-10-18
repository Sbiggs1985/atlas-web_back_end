const request = require('supertest');
const app = require('./api');

describe('API Endpoints', () => {

  describe('GET /available_payments', () => {
    it('should return available payment methods', async () => {
      const res = await request(app)
        .get('/available_payments');
      expect(res.statusCode).toEqual(200);
      expect(res.body).toEqual({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
    });
  });

  describe('POST /login', () => {
    it('should welcome the user with username', async () => {
      const res = await request(app)
        .post('/login')
        .send({ userName: 'Betty' })
        .set('Content-Type', 'application/json');
      expect(res.statusCode).toEqual(200);
      expect(res.text).toBe('Welcome Betty');
    });

    it('should return 400 if userName is not provided', async () => {
      const res = await request(app)
        .post('/login')
        .send({})
        .set('Content-Type', 'application/json');
      expect(res.statusCode).toEqual(400);
      expect(res.text).toBe('UserName is required');
    });
  });

});