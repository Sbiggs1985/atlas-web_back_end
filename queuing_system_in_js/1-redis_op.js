import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to display the value for a given key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}:`, err);
    } else {
      console.log(reply);
    }
  });
}

// Function to set a value for a given key
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Call functions as per the task
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');