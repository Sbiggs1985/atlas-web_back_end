#   // Connect to the database and update the documents
db = db.getSiblingDB('<database_name>');

#   // Define the update operation
db.school.updateMany(
  { name: "Holberton school" },     #   // Query to match documents
  { $set: { address: "972 Mission street" } }  // Update operation
);