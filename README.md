# Todo Console App - Phase 2

This is a full-stack todo application with:
- Backend: FastAPI server
- Frontend: Next.js application

## Deployments

- **Frontend**: Deployed on GitHub Pages at: https://ash-codiology.github.io/todo-console-phase2/
- **Backend**: Deployed on Vercel (instructions below)

## Overview

This is a modern web application featuring user authentication and todo management capabilities. The application consists of a backend API built with FastAPI and a frontend built with Next.js.

## Features

- **Authentication**: Sign up and sign in functionality
- **Todo Management**: Create, read, update, and delete todos
- **Responsive UI**: Modern UI built with React and Tailwind CSS
- **API Integration**: Full integration with backend API

## Architecture

The application follows a modern full-stack architecture:
- **Backend**: FastAPI with SQLModel and PostgreSQL
- **Frontend**: Next.js with TypeScript and Tailwind CSS
- **Deployment**: Backend on Vercel, Frontend on GitHub Pages

## Backend Deployment to Vercel

To deploy the backend to Vercel:

1. Navigate to the backend directory: `cd backend`
2. Install the Vercel CLI: `npm i -g vercel`
3. Login to Vercel: `vercel login`
4. Deploy the backend: `vercel --cwd backend`

The backend will be deployed with the proper configuration for FastAPI.

## Frontend Deployment to GitHub Pages

The frontend is built and ready for GitHub Pages deployment:

1. Go to your GitHub repository settings
2. Click on "Pages" in the sidebar
3. Select "Deploy from a branch"
4. Choose "gh-pages" branch and "/" folder
5. Click "Save"

The frontend will then be accessible at: https://ash-codiology.github.io/todo-console-phase2/