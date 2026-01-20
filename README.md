# Flight Routes System

A Django-based web application for managing airport flight routes with advanced tree-based operations. The system allows users to add flight routes between airports, query for specific routes, and find the longest and shortest routes in the network.

## Features

- **Add Routes**: Create new flight routes between airports with distance and duration information
- **Find Nth Node**: Navigate through the airport network tree structure and find airports at specific levels (left or right direction)
- **Longest Path From Airport**: Find the longest path traversal from a selected airport by calculating total duration
- **Shortest Path From Airport**: Find the shortest path traversal from a selected airport by calculating total duration
- **Airport Management**: Manage a network of airports with binary tree-based relationships

## Project Structure

```
Noviindus_Technology/
├── venv/                            # Virtual environment
└── src/
    └── Flight_Routes_System/
        ├── Flight_Routes_System/      # Main Django project settings
        │   ├── __init__.py
        │   ├── settings.py            # Django configuration
        │   ├── urls.py                # Main URL router
        │   ├── asgi.py                # ASGI configuration
        │   └── wsgi.py                # WSGI configuration
        ├── routes/                    # Main application
        │   ├── models.py              # Database models (Airport, AirportRoute)
        │   ├── views.py               # View handlers
        │   ├── forms.py               # Django forms
        │   ├── urls.py                # App-specific URL routes
        │   ├── services.py            # Business logic (find_nth_node)
        │   ├── admin.py               # Django admin configuration
        │   ├── apps.py                # App configuration
        │   ├── tests.py               # Unit tests
        │   └── migrations/            # Database migrations
        ├── templates/                 # HTML templates
        │   ├── base/
        │   │   └── base.html          # Base template
        │   └── routes/
        │       ├── add_route.html     # Add route form page
        │       ├── nth_node.html      # Nth node finder page
        │       ├── longest.html       # Longest route display
        │       └── shortest.html      # Shortest route display
        ├── static/                    # Static files
        │   └── css/
        │       └── style.css
        ├── manage.py                  # Django management script
        ├── requirements.txt           # Python dependencies
        ├── db.sqlite3                 # SQLite database
        └── .env                       # Environment variables (not in repo)
```

## System Architecture

### Data Models

#### Airport
- Stores airport information with unique airport codes
- Acts as a node in a binary tree network

#### AirportRoute
- Represents a flight route between airports
- Maintains binary tree relationships (left and right child airports)
- Stores distance (km) and duration (minutes) information
- One-to-one relationship with Airport (each airport has one route configuration)

### Core Functionality

1. **Route Addition**: Add new airports and their routes with left/right child relationships
2. **Tree Traversal**: Use BFS (Breadth-First Search) to find the nth-level node in either direction
3. **Path Analysis**: 
   - **Longest Path**: Uses DFS to find the node with maximum total duration from selected airport
   - **Shortest Path**: Uses Dijkstra's algorithm to find the node with minimum total duration from selected airport

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to project directory**
   ```bash
   cd "Noviindus_Technology\src\Flight_Routes_System"
   ```

2. **Activate the virtual environment**
   
   The virtual environment is located at the parent directory level (Noviindus_Technology/.venv)
   
   - On Windows:
   ```bash
   ..\..\venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source ../../.venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   
   Create a `.env` file in the Flight_Routes_System directory:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`

## Usage

### Access the Application

- **Main Page (Add Route)**: `http://127.0.0.1:8000/`
- **Find Nth Node**: `http://127.0.0.1:8000/nth/`
- **Find Longest Path From Airport**: `http://127.0.0.1:8000/longest/`
- **Find Shortest Path From Airport**: `http://127.0.0.1:8000/shortest/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET/POST | Add new flight route |
| `/nth/` | GET/POST | Find nth node in tree from root |
| `/longest/` | GET/POST | Find longest path from selected airport |
| `/shortest/` | GET/POST | Find shortest path from selected airport |

## Dependencies

- **Django** 5.2.10 - Web framework
- **psycopg2-binary** 2.9.11 - PostgreSQL adapter (included for future database migration)
- **python-dotenv** 1.2.1 - Environment variable management
- **asgiref** 3.11.0 - ASGI utilities
- **sqlparse** 0.5.5 - SQL parser

See `requirements.txt` for the complete list.

## Database

Currently uses SQLite (`db.sqlite3`) for development. The project is configured to support PostgreSQL migration with `psycopg2-binary` already included.

### Models & Fields

**Airport**
- `code` (CharField, unique, max_length=10) - Unique airport code
- `__str__()` - Returns airport code

**AirportRoute**
- `airport` (OneToOneField) - Reference to Airport
- `left` (ForeignKey) - Left child airport
- `right` (ForeignKey) - Right child airport
- `distance_km` (PositiveIntegerField) - Distance between airports
- `duration_min` (PositiveIntegerField) - Flight duration in minutes

## Configuration

### Settings.py Key Configurations
- `DEBUG` - Set via `.env` (recommended: False in production)
- `SECRET_KEY` - Set via `.env` for security
- `INSTALLED_APPS` - Includes: admin, auth, contenttypes, sessions, messages, staticfiles, routes
- `TEMPLATES` - Uses Django template engine

### Creating .env File

```bash

echo DEBUG=True >> .env
echo SECRET_KEY=your-random-secret-key >> .env
```

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
```

### Applying Migrations
```bash
python manage.py migrate
```

### Django Shell (for debugging)
```bash
python manage.py shell
```

## File Descriptions

| File | Purpose |
|------|---------|
| `manage.py` | Django management script for commands |
| `requirements.txt` | Lists all Python package dependencies |
| `db.sqlite3` | SQLite database file (auto-generated) |
| `routes/models.py` | Defines Airport and AirportRoute data models |
| `routes/views.py` | View functions handling requests/responses |
| `routes/forms.py` | Django form classes for user input |
| `routes/urls.py` | URL routing for the routes app |
| `routes/services.py` | Business logic for tree traversal |
| `templates/routes/` | HTML templates for different pages |
| `static/css/style.css` | Stylesheet for the application |

## Key Algorithms

### Find Nth Node
Located in `routes/services.py`:
- Uses Breadth-First Search (BFS) to traverse the airport network tree
- Starts from a root airport and finds the node at level n
- Supports both left and right direction navigation
- Returns the airport at the specified level or None if not found

### Find Longest Path
Located in `routes/services.py` - `find_longest_path()`:
- Uses Depth-First Search (DFS) with backtracking
- Traverses both forward (child nodes) and backward (parent nodes) paths
- Calculates cumulative duration for each path
- Returns the node with maximum total duration and its duration value

### Find Shortest Path
Located in `routes/services.py` - `find_shortest_path_from_airport()`:
- Uses Dijkstra's Algorithm with min-heap priority queue
- Explores both forward (child nodes) and backward (parent nodes) connections
- Calculates shortest cumulative duration to each reachable node
- Returns the node with minimum total duration (excluding root) and its duration value

## Testing & Verification

### Data Setup 

- **Airports Added**: Successfully added via Django Admin panel
- **Airport Routes Added**: Successfully configured via Django Admin panel
- **Route Relationships**: Left/Right child airports configured correctly
- **Data Persistence**: All data persistently stored in PostgreSQL database

### Functional Testing 

#### Nth Left/Right Node Feature
- **URL**: `/nth/`
- **Status**:  Fully Functional
- **Test Results**:
  - Search form works correctly
  - Returns correct node based on specified direction (left/right)
  - Accurately finds nodes at specified levels in the tree structure

#### Longest Path From Airport
- **URL**: `/longest/`
- **Method**: GET/POST with airport selection form
- **Status**:  Fully Functional
- **Test Results**:
  - Airport selection form works correctly
  - Calculates longest path from selected airport using DFS
  - Returns the node with maximum total duration
  - Displays Longest Node code and Total Duration in minutes

#### Shortest Path From Airport
- **URL**: `/shortest/`
- **Method**: GET/POST with airport selection form
- **Status**: ✅ Fully Functional
- **Test Results**:
  - Airport selection form works correctly
  - Calculates shortest path from selected airport using Dijkstra's algorithm
  - Returns the node with minimum total duration
  - Displays Shortest Node code and Total Duration in minutes

### Database Verification 

#### PostgreSQL Integration
- **Status**:  Fully Operational
- **Verification Methods**:
  - All airport and route data verified through **pgAdmin**
  - Data integrity confirmed through **Django Admin panel**
  - Persistent storage validated across application restarts

#### Data Integrity
- Airport codes unique and properly indexed
- Route relationships (left/right) correctly established
- Distance and duration values accurately stored and retrieved

## Troubleshooting

### Issue: Port 8000 already in use
```bash
python manage.py runserver 8001
```

### Issue: Database locked
Delete `db.sqlite3` and run migrations again:
```bash
rm db.sqlite3
python manage.py migrate
```

### Issue: Static files not loading
```bash
python manage.py collectstatic
```

## Future Enhancements

- Migration to PostgreSQL for production
- Authentication and user roles
- Advanced route analytics and reporting
- Real-time flight tracking
- API endpoints for mobile applications
- Docker containerization

## License

This project is developed by Noviindus Technology.

## Support

For issues or questions, please contact the development team.

---

**Last Updated**: January 2026
**Version**: 1.0
