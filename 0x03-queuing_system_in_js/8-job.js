const createPushNotificationsJobs = (jobs, queue) => {
  if (Array.isArray(jobs)) {
    jobs.forEach((jobData) => {
      // Create a job and add it to the queue
      const job = queue.create('push_notification_code_3', jobData).save((err) => {
        if (!err) {
          console.log('Notification job created:', job.id);
        }
      });

      // Event listener for job completion
      job.on('complete', () => console.log(`Notification job ${job.id} completed`));

      // Event listener for job failure
      job.on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`));

      // Event listener for job progress
      job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
  } else {
    throw new Error('Jobs is not an array');
  }
};

module.exports = createPushNotificationsJobs;
