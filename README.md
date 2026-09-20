
# Flashcards

 **Project Title:** Flashcards **Name:** Ahmed Omer Yagoub Aldai **GitHub Username:** ahmed-1956 **edX Username:** ahmed249alhaj **City and Country:** Khartoum, Sudan **Video Recorded on:** September 18, 2026

  ## Video Demo

   https://youtube.com/shorts/ZAD77mu8gQk?si=BLvo6mncdrUKCV_2

    ## Description

     Flashcards is a web-based study application that allows users to create, manage, and study flashcards. The application is designed to provide a simple way to store questions and answers in one place and review them using an active-recall style workflow.

      The application allows the user to create a flashcard by entering a question, an answer, and a category. After a card is added, it is stored in the application's SQLite database and can be accessed from the **My Flashcards** section. From there, the user can view the cards that have been created and manage them when necessary.

       Existing flashcards can be edited or deleted. Editing allows the user to correct or update the question, answer, or category of a card, while deleting removes a card that is no longer needed. These functions make it possible to maintain a personal collection of study material over time.

        The application also includes a **Study** section. When studying, the user is shown a flashcard question first and can reveal the answer afterward. This separates the question from its answer and allows the user to attempt to recall the information before checking the answer.

         The application uses **Python and Flask** for the web application and routing, **SQLite** for persistent storage, and **HTML, CSS, and Jinja** for the user interface and dynamic pages. The project is organized so that the Flask application handles the application logic and database operations, while the templates provide the different pages and the static files provide the styling.

          The main application file is `app.py`, which contains the Flask application, routes, and logic for creating, displaying, editing, deleting, and studying flashcards. `flashcards.db` is the SQLite database that stores the flashcard data, while `schema.sql` defines the database structure. `requirements.txt` contains the Python dependencies required to run the application.

           The `templates/` directory contains the HTML/Jinja templates used by the different pages of the application, including the shared layout, home page, card creation and editing pages, My Flashcards page, and Study page. The `static/` directory contains the CSS and other static resources used for the application's interface.

            To use the application, the user starts the Flask application and opens it in a web browser. From the navigation menu, a new flashcard can be added, existing cards can be viewed and managed, or the Study section can be used to review the stored questions and answers.

             The application was developed as a CS50 final project to apply concepts from the course, including Python, Flask, SQL, HTML, CSS, database operations, routing, forms, and server-side templating. Its primary purpose is to provide a focused and straightforward tool for creating and reviewing study flashcards.
