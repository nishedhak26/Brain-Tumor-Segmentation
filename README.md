# React Firebase App

A React application integrated with Firebase for authentication and real-time messaging.

## Features

- User authentication (sign up/sign in/sign out)
- Real-time messaging with Firestore
- Responsive design
- Firebase Analytics integration

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Start the development server:
   ```
   npm start
   ```

3. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Firebase Services Used

- **Authentication**: Email/password authentication
- **Firestore**: Real-time database for messages
- **Analytics**: User behavior tracking
- **Storage**: Available for file uploads (configured but not used in this example)

## Project Structure

```
src/
  ├── firebase.js      # Firebase configuration and initialization
  ├── App.js          # Main application component
  ├── App.css         # Application styles
  ├── index.js        # React entry point
  └── index.css       # Global styles
```

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm eject` - Ejects from Create React App (one-way operation)