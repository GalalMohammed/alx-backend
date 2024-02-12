import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener for connection error
client.on('error', err => console.log('Redis client not connected to the server:', err));

// Event listener for successful connection
client.on('connect', () => console.log('Redis client connected to the server'));

// Function to set a new value in Redis
const setNewSchool = (schoolName, value) => client.set(schoolName, value, print);

// Function to display the value for a given key
const displaySchoolValue = (schoolName) => client.get(schoolName, (_err, value) => console.log(value));

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
