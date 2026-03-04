# REST API Documentation

## Base URL

```
http://localhost:5000/api
```

## Authentication

Currently no authentication is required. **Do not expose this API to the public without adding authentication.**

## API Endpoints

### Statistics

#### Get Overall Statistics
```http
GET /api/stats
```

**Response:**
```json
{
  "papers": {
    "total": 188,
    "by_category": {
      "Evaluation Datasets": 20,
      "Training Datasets": 15,
      "Single-Agent Systems": 12,
      ...
    },
    "by_year": {
      "2024": 45,
      "2025": 132,
      "2026": 11
    },
    "by_month": {
      "2024-01": 3,
      "2024-02": 5,
      ...
    }
  },
  "datasets": {
    "eval": 42,
    "training": 18
  },
  "methods": {
    "sft": 25,
    "rl": 30,
    "foundation": 15
  }
}
```

---

### Papers

#### List Papers
```http
GET /api/papers?page=1&per_page=10&search=&category=&year=&month=&sort=
```

**Query Parameters:**
- `page` (int, default: 1): Page number
- `per_page` (int, default: 10): Items per page
- `search` (string): Full-text search query
- `category` (string): Filter by category (e.g., "Evaluation Datasets")
- `year` (int): Filter by year (e.g., 2025)
- `month` (string): Filter by month (e.g., "2025-01")
- `sort` (string): Sort field (e.g., "year", "-year", "title", "month")
  - Prefix with `-` for descending order

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "title": "SWE-bench: Can Language Models Resolve Real-world Github Issues?",
      "authors": "Jimenez, Carlos E. and Yang, John and Wettig, Alexander and ...",
      "venue": "arXiv preprint arXiv:2310.06770",
      "year": 2024,
      "month": "2024-03",
      "category": "Evaluation Datasets",
      "arxiv_link": "https://arxiv.org/abs/2310.06770",
      "doi_link": null,
      "openreview_link": null,
      "website_link": null,
      "github_links": ["https://github.com/SWE-bench/SWE-bench"],
      "huggingface_links": ["https://huggingface.co/datasets/princeton-nlp/SWE-bench"]
    },
    ...
  ],
  "total": 188,
  "page": 1,
  "per_page": 10,
  "pages": 19
}
```

#### Get Paper by ID
```http
GET /api/papers/{id}
```

**Response:**
```json
{
  "id": 1,
  "title": "...",
  "authors": "...",
  ...
}
```

#### Create Paper
```http
POST /api/papers
Content-Type: application/json

{
  "title": "New Paper Title",
  "authors": "Author1, Author2",
  "venue": "Conference Name",
  "year": 2025,
  "month": "2025-06",
  "category": "Single-Agent Systems,Multi-Agent Systems",
  "arxiv_link": "https://arxiv.org/abs/2501.12345",
  "github_links": ["https://github.com/user/repo"],
  "huggingface_links": []
}
```

**Response:**
```json
{
  "id": 189,
  "title": "New Paper Title",
  ...
}
```

**Notes:**
- `month` format: `YYYY-MM`
- When `month` is provided, `year` is automatically extracted
- `category` can contain multiple categories separated by commas
- ArXiv venues are auto-formatted to: `arXiv preprint arXiv:XXXX.XXXXX`

#### Update Paper
```http
PUT /api/papers/{id}
Content-Type: application/json

{
  "title": "Updated Title",
  "year": 2026
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated Title",
  "year": 2026,
  ...
}
```

**Notes:**
- Only include fields you want to update
- Updating `month` automatically updates `year`

#### Delete Paper
```http
DELETE /api/papers/{id}
```

**Response:**
```json
{
  "message": "Paper deleted successfully"
}
```

---

### Datasets

#### List Evaluation Datasets
```http
GET /api/datasets?page=1&per_page=10&search=&language=&multimodal=&sort=
```

**Query Parameters:**
- `page`, `per_page`: Pagination
- `search`: Full-text search
- `language`: Filter by programming language (e.g., "Python")
- `multimodal`: Filter by multimodal support (true/false)
- `sort`: Sort field (e.g., "amount", "-year")

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "name": "SWE-bench",
      "language": "Python",
      "multimodal": false,
      "repos": 12,
      "amount": 2294,
      "environment": true,
      "github_links": ["https://github.com/SWE-bench/SWE-bench"],
      ...
    }
  ],
  "total": 42,
  "page": 1,
  "per_page": 10,
  "pages": 5
}
```

#### List Training Datasets
```http
GET /api/training-datasets?page=1&per_page=10&search=&language=&sort=
```

Similar to evaluation datasets.

---

### Methods

#### List SFT Methods
```http
GET /api/sft-methods?page=1&per_page=10&search=&sort=
```

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "name": "SWE-Lego-Qwen3-32B",
      "base_model": "Qwen3-32B",
      "size": "32B",
      "architecture": "Dense",
      "training_scaffold": "OpenHands",
      "resolution": 57.6,
      "github_links": ["https://github.com/SWE-Lego/SWE-Lego"],
      ...
    }
  ],
  ...
}
```

#### List RL Methods
```http
GET /api/rl-methods?page=1&per_page=10&search=&sort=
```

#### List Foundation Models
```http
GET /api/foundation-models?page=1&per_page=10&search=&sort=
```

---

### Data Synchronization

#### Export Database to YAML/CSV
```http
POST /api/sync-to-data
```

**Description**: Exports all database records back to YAML and CSV files in `data/` directory.

**Response:**
```json
{
  "message": "Data exported successfully",
  "details": {
    "papers": 188,
    "datasets": 42,
    "training_datasets": 18,
    ...
  }
}
```

#### Import YAML/CSV to Database
```http
POST /api/import-from-data
```

**Description**: Imports data from YAML/CSV files in `data/` directory to database. Existing records are updated, new records are added.

**Response:**
```json
{
  "message": "Data imported successfully",
  "details": {
    "papers_added": 5,
    "papers_updated": 183,
    ...
  }
}
```

---

## Error Responses

All endpoints return standard error responses:

```json
{
  "error": "Error message description"
}
```

**Common HTTP Status Codes:**
- `200 OK`: Request successful
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Rate Limiting

Currently no rate limiting is implemented. Consider adding rate limiting in production deployment.

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for all origins in development mode. In production, restrict CORS to specific trusted origins.

## API Usage Examples

### Using cURL

```bash
# Get statistics
curl http://localhost:5000/api/stats

# Search papers
curl "http://localhost:5000/api/papers?search=agent&category=Single-Agent%20Systems"

# Create a paper
curl -X POST http://localhost:5000/api/papers \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My New Paper",
    "authors": "Author Name",
    "venue": "Conference 2025",
    "year": 2025,
    "category": "Single-Agent Systems"
  }'

# Update a paper
curl -X PUT http://localhost:5000/api/papers/1 \
  -H "Content-Type: application/json" \
  -d '{"year": 2026}'

# Delete a paper
curl -X DELETE http://localhost:5000/api/papers/1
```

### Using Python

```python
import requests

BASE_URL = "http://localhost:5000/api"

# Get statistics
response = requests.get(f"{BASE_URL}/stats")
stats = response.json()
print(f"Total papers: {stats['papers']['total']}")

# Search papers
params = {
    "search": "agent",
    "category": "Single-Agent Systems",
    "year": 2025,
    "sort": "-month"
}
response = requests.get(f"{BASE_URL}/papers", params=params)
papers = response.json()

# Create a paper
paper_data = {
    "title": "My New Paper",
    "authors": "Author Name",
    "venue": "Conference 2025",
    "year": 2025,
    "category": "Single-Agent Systems",
    "arxiv_link": "https://arxiv.org/abs/2501.12345"
}
response = requests.post(f"{BASE_URL}/papers", json=paper_data)
new_paper = response.json()
print(f"Created paper with ID: {new_paper['id']}")

# Sync database to files
response = requests.post(f"{BASE_URL}/sync-to-data")
result = response.json()
print(result['message'])
```

### Using JavaScript (Fetch API)

```javascript
const BASE_URL = 'http://localhost:5000/api';

// Get statistics
fetch(`${BASE_URL}/stats`)
  .then(res => res.json())
  .then(stats => console.log('Total papers:', stats.papers.total));

// Search papers
const params = new URLSearchParams({
  search: 'agent',
  category: 'Single-Agent Systems',
  year: 2025,
  sort: '-month'
});
fetch(`${BASE_URL}/papers?${params}`)
  .then(res => res.json())
  .then(data => console.log('Found papers:', data.items));

// Create a paper
fetch(`${BASE_URL}/papers`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: 'My New Paper',
    authors: 'Author Name',
    venue: 'Conference 2025',
    year: 2025,
    category: 'Single-Agent Systems'
  })
})
  .then(res => res.json())
  .then(paper => console.log('Created paper:', paper));
```

## Websocket Support

Not currently implemented. Consider adding for real-time updates in the future.

## Versioning

Current API version: **v1** (no version prefix in URL)

Future versions will use URL versioning: `/api/v2/papers`
