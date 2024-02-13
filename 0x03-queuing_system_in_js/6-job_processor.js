import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Function to send notification
const sendNotification = (phoneNumber, message) => console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

// Process jobs in the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with the extracted data
  sendNotification(phoneNumber, message);

  // Mark the job as completed
  done();
});
