import redis from 'redis';

// Create a Redis client for subscriber
const subscriberClient = redis.createClient();

// Event listener for successful connection
subscriberClient.on('connect', () => console.log('Redis client connected to the server'));

// Event listener for connection error
subscriberClient.on('error', (error) => console.log('Redis client not connected to the server:', error));

// Subscribe to th echannel
subscriberClient.subscribe('holberton school channel');

// Event listener for incoming messages
subscriberClient.on('message', (_channel, message) => {
  console.log(message);

  // Unsubscribe and quit if the message is KILL_SERVER
  if (message === 'KILL_SERVER') {
    subscriberClient.unsubscribe();
    subscriberClient.quit();
  }
});
