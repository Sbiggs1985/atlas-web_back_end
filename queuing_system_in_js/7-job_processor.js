import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function that will send a notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the job progress from 0 out of 100
  job.progress(0, 100);

  // Check if the phoneNumber is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // If blacklisted, fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track the job progress to 50%
  job.progress(50, 100);

  // Log the message that is being sent
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Track the job completion progress to 100% and mark the job as done
  job.progress(100, 100);
  done();
};

// Create the queue
const queue = kue.createQueue();

// Process the queue for jobs of type 'push_notification_code_2' with a concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call sendNotification with the job's data
  sendNotification(phoneNumber, message, job, done);
});