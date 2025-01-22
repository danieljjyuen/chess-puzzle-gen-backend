# chess-puzzle-gen-backend

## Overview

This backend application is built using FastAPI and integrates with the Lichess Puzzle API. It fetches chess puzzles, converts Portable Game Notation (PGN) into Forsyth–Edwards Notation (FEN), and serves the processed data via API endpoints.

## Features

Fetches chess puzzles from the Lichess Puzzle API.

Converts PGN to FEN format for easier board state representation.

Provides an API endpoint to serve processed FEN data.

## Technologies Used

FastAPI: Python web framework for building APIs.

Requests: Python library for making HTTP requests.

Chess: Python library to parse and manipulate PGN and FEN.

JSON: For API responses.

### steps

pip install -r requirements.txt

uvicorn main:app --reload