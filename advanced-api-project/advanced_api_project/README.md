# Book API Documentation

## Endpoints

### List/Create Books
- **URL**: `/api/books/`
- **Methods**: 
  - GET: List books (with filtering, searching, ordering)
  - POST: Create new book (requires authentication)

### Retrieve/Update/Delete Book
- **URL**: `/api/books/<id>/`
- **Methods**:
  - GET: Retrieve book details
  - PUT/PATCH: Update book (owner only)
  - DELETE: Delete book (owner only)

## Query Capabilities

### Filtering
- `?title=Example` - Exact title match
- `?title__icontains=example` - Case-insensitive partial match
- `?author=Smith` - Exact author match
- `?publication_year__gte=2000` - Books published after 2000
- `?owner__username=johndoe` - Books by specific owner

### Searching
`?search=query` - Searches title, author, and description

### Ordering
- `?ordering=title` - Sort by title (ascending)
- `?ordering=-publication_year` - Sort by publication year (descending)
- `?ordering=author,title` - Sort by author then title

## Authentication
Use Django REST Framework's session authentication or token authentication.

## Examples

1. Get all fantasy books published after 2010:
