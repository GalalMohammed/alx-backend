import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Event listener for connection error
client.on('error', err => console.log('Redis client not connected to the server:', err));

// Event listener for successful connection
client.on('connect', () => console.log('Redis client connected to the server'));

// Create Hash using hset
client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

// Display Hash using hgetall
client.hgetall('HolbertonSchools', (_err, result) => console.log(result));
