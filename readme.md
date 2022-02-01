The application has been built using django rest-framework.
API endpoints have been provided for displaying list of questions, adding and editing questions and answering questions. 
The UserAnswer model has a many-to-one relationship with the Questions model, so each question can have several answers, and deleting a question will not delete the corresponding solution codes from the database.

No API endpoint has been provided for accessing the answers individually. The entries in the UserAnswer data table can only be accessed via admin.

The user is displayed a list of questions, with each question having the option to expand and show details about it. On expanding, user also gets the option to be taken to where the solution needs to be typed. On posting the solution, the code output, correct output and user score is shown(1 if correct else 0) and the solution gets stored in the db.

For editing the questions, user has to know the question_id, and enter the url accordingly.

All dependencies are specified in requirements.txt.
