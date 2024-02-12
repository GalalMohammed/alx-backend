import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();
const getAsync = promisify(client.get).bind(client);

// Event listener for connection error
client.on('error', err => console.log('Redis client not connected to the server:', err));

// Event listener for successful connection
client.on('connect', () => console.log('Redis client connected to the server'));

// Function to set a new value in Redis
const setNewSchool = (schoolName, value) => client.set(schoolName, value, print);

// Async function to display the value for a given key using async/await
const displaySchoolValue = async (schoolName) => console.log(await getAsync(schoolName));

// Call the functions
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
