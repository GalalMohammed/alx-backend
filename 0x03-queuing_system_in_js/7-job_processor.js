import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklisted = ['4153518780', '4153518781'];

// Create a function to send notifications
const sendNotification = (phoneNumber, message, job, done) => {
  // Track progress: 0%
  job.progress(0, 100);

  // Check if phoneNumber is blacklisted
  if (blacklisted.includes(phoneNumber)) {
    // Fail the job with an error message
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress: 50%
  job.progress(50, 100);

  // Log the notification message
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
};

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs in the 'push_notification_code_2' queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with the extracted data
  sendNotification(phoneNumber, message, job, done);
});
