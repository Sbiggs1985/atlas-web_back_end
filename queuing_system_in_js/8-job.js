export default function createPushNotificationsJobs(jobs, queue) {
    // Check if jobs is an array
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    // Iterate over the array of jobs
    jobs.forEach((jobData) => {
      // Create a new job in the queue with the name 'push_notification_code_3'
      const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
          if (!err) {
            console.log(`Notification job created: ${job.id}`);
          }
        });
  
      // Listen for job completion
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
  
      // Listen for job failure
      job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
  
      // Listen for job progress
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  }  