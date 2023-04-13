# SentimentWatch

SentimentWatch is a web application built using Python and Flask for the server-side, and React.js for the client-side. This application requires two environment variables to be set: `DATABASE_URL` and `OPENAI_KEY`.

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/app_image_1.png">
  </a>
</div>

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Setting Up Environment Variables](#setting-up-environment-variables)
4. [Running the Application](#running-the-application)
5. [Contributing](#contributing)
6. [License](#license)

## Prerequisites

Before you begin, make sure you have the following software installed on your system:

- Python 3.8 or higher
- Node.js 14.x or higher
- npm 6.x or higher
- Git (for cloning the repository)

## Installation

Follow these steps to set up the application on your local machine:

1. Clone the repository:
   ```
   git clone https://github.com/artsaraiva/SentimentWatch.git
   ```
2. Change to the `server` directory:
   ```
    cd SentimentWatch\server
   ```
3. Install the required Python packages using pip:
   ```
    pip install -r requirements.txt
   ```
4. Change to the `client` directory and install the required npm packages:
   ```
    cd ..\client
    npm install
   ```

## Setting Up Environment Variables

To run the application, you need to set up the following environment variables:

1. `DATABASE_URL`: This variable should contain the connection string for your database.

2. `OPENAI_KEY`: This variable should contain the API key for the OpenAI service you are using.

Create a `.env` file in the `server` directory and add the following lines:

   ```
    DATABASE_URL=your_database_connection_string
    OPENAI_KEY=your_openai_api_key
   ```

Replace `your_database_connection_string` and `your_openai_api_key` with the appropriate values.

## Running the Application

To run the server-side (Flask) application, execute the following command from the `server` directory:
   ```
   flask app.py
   ```

To run the client-side (React.js) application, execute the following command from the `client` directory:
   ```
    npm start
   ```
   
Now, open your web browser and navigate to `http://localhost:3000` to view the application.

## Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Commit your changes
4. Push your changes to your fork
5. Submit a pull request to the main repository

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
