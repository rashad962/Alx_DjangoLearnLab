## Advanced Query Capabilities

The Book API supports powerful filtering, searching, and ordering options:

### Filtering
- Filter by exact or partial matches:
  - `title`: `?title=Example` or `?title__icontains=example`
  - `author`: `?author=Smith` or `?author__icontains=smi`
  - `publication_year`: `?publication_year=2020` or range with `?publication_year__gte=2000&publication_year__lte=2010`
  - `owner`: `?owner__username=johndoe`

### Searching
Search across multiple fields with a single query:
`?search=query` searches in title, author, description, and owner username.

### Ordering
Sort results by any field:
- `?ordering=title` (ascending)
- `?ordering=-publication_year` (descending)
- Multiple fields: `?ordering=author,title`

### Examples
1. Get fantasy books published after 2010:
   `GET /api/books/?search=fantasy&publication_year__gte=2011`

2. Get books by Tolkien ordered by publication year:
   `GET /api/books/?author__icontains=tolkien&ordering=publication_year`
