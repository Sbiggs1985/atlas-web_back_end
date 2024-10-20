import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the client.get function
const getAsync = promisify(client.get).bind(client);

// Function to display the value for a given key using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}:`, err);
  }
}

// Function to set a value for a given key
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Call functions as per the task
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
