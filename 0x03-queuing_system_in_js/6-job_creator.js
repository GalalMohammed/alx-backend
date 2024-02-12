const kue = require('kue');

// Create a queue with Kue
const queue = kue.createQueue();

// Object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'notification message'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log('Notification job created:', job.id);
  }
});

// Event listener for job completion
job.on('complete', () => console.log('Notification job completed'));

// Event listener for job failure
job.on('failed', () => console.log('Notification job failed'));
