import redis from 'redis';

// Create a Redis client for publisher
const publisherClient = redis.createClient();

// Event listner for successful connection
publisherClient.on('connect', () => console.log('Redis client connected to the server'));

// Event listener for connection error
publisherClient.on('error', (error) => console.log('Redis client not connected to the server:', error));

// Function to publish a message after a specified time
const publishMessage = (message, time) => setTimeout(() => {
  console.log('About to send', message);
  publisherClient.publish('holberton school channel', message);
}, time);

// Call the function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
