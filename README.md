# Wiki Encyclopedia

This project is my submission for CS50W Course Project 1: Wiki.

## Overview

Design a Wikipedia-like online encyclopedia using Django, where each encyclopedia entry is represented by a Markdown file. This project includes features like viewing entries, creating new entries, editing existing entries, searching entries, and viewing a random entry.

## Project Structure

- `encyclopedia/`
  - `urls.py`: URL configuration.
  - `views.py`: View functions to handle requests.
  - `util.py`: Utility functions for interacting with encyclopedia entries.
  - `templates/encyclopedia/`
    - `index.html`: Main page listing all entries.
    - `layout.html`: Base layout for all pages.
    - `entry.html`: Template for displaying a single entry.
    - `create.html`: Template for creating a new entry.
    - `edit.html`: Template for editing an existing entry.
    - `search.html`: Template for search results.

## Features

### Entry Page

- **URL**: `/wiki/TITLE`
- **Functionality**: Displays the content of the requested encyclopedia entry.
- If the entry does not exist, an error page is shown.
- The title of the page includes the name of the entry.

### Index Page

- **URL**: `/`
- **Functionality**: Lists all encyclopedia entries. Users can click on any entry name to be taken directly to that entry page.

### Search

- **URL**: `/search`
- **Functionality**: 
  - Users can search for an encyclopedia entry using a search box in the sidebar.
  - If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
  - If the query does not match, a search results page is displayed with a list of all entries that have the query as a substring.
  - Clicking on any of the entry names on the search results page takes the user to that entry’s page.

### New Page

- **URL**: `/create`
- **Functionality**: 
  - Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
  - Users can enter a title and Markdown content for the new entry.
  - If an entry with the provided title already exists, an error message is shown.
  - Otherwise, the new entry is saved and the user is taken to the new entry’s page.

### Edit Page

- **URL**: `/edit/TITLE`
- **Functionality**: 
  - Each entry page includes a link to edit that entry.
  - The edit page contains a textarea pre-populated with the existing Markdown content.
  - Users can save their changes, which updates the entry and redirects back to the entry’s page.

### Random Page

- **URL**: `/random`
- **Functionality**: Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

- **Functionality**: 
  - Markdown content in the entry files is converted to HTML before being displayed to the user.
  - The `python-markdown2` package is used for this conversion.