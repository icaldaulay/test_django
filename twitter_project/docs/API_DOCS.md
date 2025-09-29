# API Documentation

## Overview

Twitter Clone Application menyediakan RESTful API untuk mengakses data tweet dan integrasi dengan aplikasi external. API menggunakan format JSON untuk request dan response.

## Base URL

```
Development: http://127.0.0.1:8000
Production: https://your-domain.com
```

## Authentication

API menggunakan session-based authentication. User harus login melalui web interface untuk mengakses protected endpoints.

### Authentication Flow

1. **Login via Web Interface**: `POST /login/`
2. **Session Cookie**: Automatically set after successful login
3. **API Access**: Use session cookie for authenticated requests

---

## Endpoints

### 1. Posts API

**Get all posts/tweets with detailed information**

```http
GET /api/posts/
```

#### Parameters

None required.

#### Response Format

```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "tanggal": "2025-09-29",
      "waktu": "14:30:25",
      "user": "john_doe",
      "pesan": "Hello from Jakarta! Beautiful weather today.",
      "lokasi": "Jakarta, Indonesia",
      "latitude": -6.2087634,
      "longitude": 106.845599,
      "foto": "/media/tweet_images/photo123.jpg"
    },
    {
      "id": 2,
      "tanggal": "2025-09-29",
      "waktu": "13:15:42",
      "user": "jane_smith",
      "pesan": "Working from Bali today! #digitalnomad",
      "lokasi": "Ubud, Bali, Indonesia",
      "latitude": -8.5069312,
      "longitude": 115.2625452,
      "foto": null
    }
  ],
  "total": 2,
  "description": "Data detail posted dari halaman dashboard"
}
```

#### Response Fields

| Field         | Type    | Description                            |
| ------------- | ------- | -------------------------------------- |
| `status`      | string  | Response status ("success" or "error") |
| `data`        | array   | Array of tweet objects                 |
| `total`       | integer | Total number of tweets returned        |
| `description` | string  | API endpoint description               |

#### Tweet Object Fields

| Field       | Type        | Description                   | Example                           |
| ----------- | ----------- | ----------------------------- | --------------------------------- |
| `id`        | integer     | Unique tweet identifier       | `1`                               |
| `tanggal`   | string      | Tweet date (YYYY-MM-DD)       | `"2025-09-29"`                    |
| `waktu`     | string      | Tweet time (HH:MM:SS)         | `"14:30:25"`                      |
| `user`      | string      | Username of tweet author      | `"john_doe"`                      |
| `pesan`     | string      | Tweet content (max 140 chars) | `"Hello world!"`                  |
| `lokasi`    | string      | Location name                 | `"Jakarta, Indonesia"`            |
| `latitude`  | float/null  | GPS latitude coordinate       | `-6.2087634`                      |
| `longitude` | float/null  | GPS longitude coordinate      | `106.845599`                      |
| `foto`      | string/null | Image URL if attached         | `"/media/tweet_images/photo.jpg"` |

#### Example Request

```bash
curl -X GET "http://127.0.0.1:8000/api/posts/" \
     -H "Content-Type: application/json"
```

#### Example Response

```json
{
  "status": "success",
  "data": [
    {
      "id": 15,
      "tanggal": "2025-09-29",
      "waktu": "20:45:12",
      "user": "travel_blogger",
      "pesan": "Amazing sunset at Tanah Lot! 🌅 #Bali #sunset",
      "lokasi": "Tanah Lot, Tabanan, Bali",
      "latitude": -8.6211934,
      "longitude": 115.0868536,
      "foto": "/media/tweet_images/sunset_tanah_lot.jpg"
    },
    {
      "id": 14,
      "tanggal": "2025-09-29",
      "waktu": "18:30:00",
      "user": "foodie_jakarta",
      "pesan": "Best nasi gudeg in Yogyakarta! Must try 😋",
      "lokasi": "Malioboro Street, Yogyakarta",
      "latitude": -7.7929465,
      "longitude": 110.3657136,
      "foto": "/media/tweet_images/nasi_gudeg.jpg"
    }
  ],
  "total": 25,
  "description": "Data detail posted dari halaman dashboard"
}
```

---

### 2. API Documentation Page

**Get API documentation interface**

```http
GET /api/
```

#### Authentication Required

✅ Yes - User must be logged in

#### Response

Returns HTML page with API documentation and interactive interface.

---

## Error Responses

### HTTP Status Codes

| Status Code | Description                          |
| ----------- | ------------------------------------ |
| `200`       | Success                              |
| `401`       | Unauthorized (not logged in)         |
| `403`       | Forbidden (insufficient permissions) |
| `404`       | Not Found                            |
| `500`       | Internal Server Error                |

### Error Response Format

```json
{
  "status": "error",
  "message": "Authentication required",
  "code": 401
}
```

---

## Usage Examples

### JavaScript/jQuery

```javascript
// Fetch all tweets
$.ajax({
  url: "/api/posts/",
  method: "GET",
  success: function (response) {
    if (response.status === "success") {
      console.log("Total tweets:", response.total);
      response.data.forEach(function (tweet) {
        console.log(`${tweet.user}: ${tweet.pesan}`);
      });
    }
  },
  error: function (xhr, status, error) {
    console.error("API Error:", error);
  },
});
```

### Python Requests

```python
import requests

# Make API request
response = requests.get('http://127.0.0.1:8000/api/posts/')

if response.status_code == 200:
    data = response.json()
    print(f"Total tweets: {data['total']}")

    for tweet in data['data']:
        print(f"{tweet['user']}: {tweet['pesan']}")
        if tweet['foto']:
            print(f"Photo: {tweet['foto']}")
        print(f"Location: {tweet['lokasi']}")
        print("---")
else:
    print(f"Error: {response.status_code}")
```

### cURL

```bash
# Get all tweets
curl -X GET "http://127.0.0.1:8000/api/posts/" \
     -H "Accept: application/json" \
     -H "User-Agent: MyApp/1.0"
```

### PHP

```php
<?php
$url = 'http://127.0.0.1:8000/api/posts/';
$response = file_get_contents($url);
$data = json_decode($response, true);

if ($data['status'] === 'success') {
    echo "Total tweets: " . $data['total'] . "\n";

    foreach ($data['data'] as $tweet) {
        echo $tweet['user'] . ": " . $tweet['pesan'] . "\n";
        echo "Location: " . $tweet['lokasi'] . "\n";
        echo "---\n";
    }
}
?>
```

---

## Data Filtering and Processing

### Filter Tweets with Location Data

```javascript
// Get only tweets with GPS coordinates
fetch("/api/posts/")
  .then((response) => response.json())
  .then((data) => {
    const tweetsWithGPS = data.data.filter(
      (tweet) => tweet.latitude !== null && tweet.longitude !== null
    );
    console.log(`${tweetsWithGPS.length} tweets have GPS data`);
  });
```

### Group Tweets by Location

```javascript
// Group tweets by city/location
fetch("/api/posts/")
  .then((response) => response.json())
  .then((data) => {
    const grouped = data.data.reduce((acc, tweet) => {
      const location = tweet.lokasi;
      if (!acc[location]) {
        acc[location] = [];
      }
      acc[location].push(tweet);
      return acc;
    }, {});

    console.log("Tweets by location:", grouped);
  });
```

### Search Tweets

```javascript
// Search tweets by content or user
function searchTweets(query) {
  return fetch("/api/posts/")
    .then((response) => response.json())
    .then((data) => {
      return data.data.filter(
        (tweet) =>
          tweet.pesan.toLowerCase().includes(query.toLowerCase()) ||
          tweet.user.toLowerCase().includes(query.toLowerCase()) ||
          tweet.lokasi.toLowerCase().includes(query.toLowerCase())
      );
    });
}

// Usage
searchTweets("jakarta").then((results) => {
  console.log(`Found ${results.length} tweets matching 'jakarta'`);
});
```

---

## Integration Examples

### Map Integration (Leaflet.js)

```javascript
// Load tweets and display on map
fetch("/api/posts/")
  .then((response) => response.json())
  .then((data) => {
    data.data.forEach((tweet) => {
      if (tweet.latitude && tweet.longitude) {
        const marker = L.marker([tweet.latitude, tweet.longitude])
          .bindPopup(
            `
                        <strong>${tweet.user}</strong><br>
                        ${tweet.pesan}<br>
                        <small>${tweet.lokasi}</small>
                    `
          )
          .addTo(map);
      }
    });
  });
```

### Dashboard Widget

```javascript
// Create dashboard statistics
fetch("/api/posts/")
  .then((response) => response.json())
  .then((data) => {
    const stats = {
      totalTweets: data.total,
      uniqueUsers: [...new Set(data.data.map((t) => t.user))].length,
      tweetsWithPhotos: data.data.filter((t) => t.foto).length,
      uniqueLocations: [...new Set(data.data.map((t) => t.lokasi))].length,
    };

    console.log("Dashboard Stats:", stats);
  });
```

---

## Rate Limiting

Currently, no rate limiting is implemented. For production use, consider implementing:

- **Requests per minute**: 60 requests per user per minute
- **Requests per hour**: 1000 requests per user per hour
- **Authentication required**: All API endpoints require user login

---

## Data Export

### CSV Export Example

```python
import requests
import csv

# Fetch data
response = requests.get('http://127.0.0.1:8000/api/posts/')
data = response.json()

# Export to CSV
with open('tweets_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'tanggal', 'waktu', 'user', 'pesan', 'lokasi', 'latitude', 'longitude', 'foto']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for tweet in data['data']:
        writer.writerow(tweet)

print(f"Exported {len(data['data'])} tweets to tweets_export.csv")
```

### JSON Export

```javascript
// Export to JSON file
fetch("/api/posts/")
  .then((response) => response.json())
  .then((data) => {
    const dataStr = JSON.stringify(data, null, 2);
    const dataBlob = new Blob([dataStr], { type: "application/json" });

    const link = document.createElement("a");
    link.href = URL.createObjectURL(dataBlob);
    link.download = "tweets_export.json";
    link.click();
  });
```

---

## API Versioning

Current API version: **v1**

Future versions will be available at:

- `/api/v1/posts/` (current)
- `/api/v2/posts/` (future)

---

## Support and Contact

For API support and questions:

- **Documentation**: Check this API documentation
- **Issues**: Create issues in project repository
- **Updates**: API changes will be documented in changelog

---

## Changelog

### Version 1.0 (Current)

- ✅ GET /api/posts/ - Retrieve all tweets with location data
- ✅ Session-based authentication
- ✅ JSON response format
- ✅ Complete tweet metadata (user, content, location, coordinates, photos)

### Planned Features (v1.1)

- 🔄 POST /api/posts/ - Create new tweets via API
- 🔄 GET /api/posts/{id}/ - Get specific tweet
- 🔄 API key authentication option
- 🔄 Pagination support
- 🔄 Rate limiting
