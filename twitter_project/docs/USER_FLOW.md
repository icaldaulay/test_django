# User Flow Diagram

## Application User Flow

### 1. Authentication Flow

```
┌─────────────────┐
│   Landing Page  │
│   (Home URL)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐    No     ┌─────────────────┐
│  User Logged    │ ────────► │   Login Page    │
│     In?         │           │  (/login/)      │
└─────────────────┘           └─────────────────┘
         │ Yes                          │
         ▼                              ▼
┌─────────────────┐           ┌─────────────────┐
│   Dashboard     │           │  Enter Creds    │
│  (/dashboard/)  │           │ Username/Pass   │
└─────────────────┘           └─────────────────┘
                                       │
                              ┌────────┴────────┐
                              │                 │
                              ▼                 ▼
                    ┌─────────────────┐  ┌─────────────────┐
                    │   Valid Creds   │  │ Invalid Creds   │
                    │      Yes        │  │      No         │
                    └─────────────────┘  └─────────────────┘
                              │                 │
                              ▼                 ▼
                    ┌─────────────────┐  ┌─────────────────┐
                    │   Dashboard     │  │  Error Message  │
                    │  (Timeline)     │  │  Back to Login  │
                    └─────────────────┘  └─────────────────┘
```

### 2. Registration Flow

```
┌─────────────────┐
│   Login Page    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  "Register"     │
│    Link         │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ Registration    │
│     Form        │
│ (/register/)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Fill Form:     │
│ • Username      │
│ • Email         │
│ • Password      │
│ • Confirm Pass  │
└─────────────────┘
         │
         ▼
┌─────────────────┐    No     ┌─────────────────┐
│  Form Valid?    │ ────────► │  Show Errors    │
│                 │           │  Stay on Form   │
└─────────────────┘           └─────────────────┘
         │ Yes
         ▼
┌─────────────────┐
│  Create User    │
│  Auto Login     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Dashboard     │
│  (Redirect)     │
└─────────────────┘
```

### 3. Tweet Creation Flow

```
┌─────────────────┐
│   Dashboard     │
│   Timeline      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Tweet Form     │
│  (Top of page)  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Fill Content   │
│  (140 chars)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Search         │
│  Location       │
│  (Required)     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Type Location  │
│  (min 3 chars)  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  API Calls:     │
│ • Nominatim     │
│ • Photon        │
│ • GPS (opt)     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Show Location  │
│  Suggestions    │
│  Dropdown       │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Select         │
│  Location       │
│  + Coordinates  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Upload Photo   │
│   (Optional)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Submit Tweet   │
│   POST Form     │
└─────────────────┘
         │
         ▼
┌─────────────────┐    No     ┌─────────────────┐
│  Form Valid?    │ ────────► │  Show Errors    │
│                 │           │  Stay on Form   │
└─────────────────┘           └─────────────────┘
         │ Yes
         ▼
┌─────────────────┐
│  Save Tweet     │
│  to Database    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Success Msg    │
│  Refresh Page   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Updated        │
│  Timeline       │
│  (New Tweet)    │
└─────────────────┘
```

### 4. Map Exploration Flow

```
┌─────────────────┐
│   Dashboard     │
│   Timeline      │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Click "Map"   │
│   Navigation    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Map Page      │
│   (/map/)       │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Loading        │
│  Indicator      │
│  Spinner        │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Fetch Tweets   │
│  via AJAX       │
│  (/api/posts/)  │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Filter Tweets  │
│  with Location  │
│  Data           │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Display Map    │
│  with Markers   │
│  (Leaflet.js)   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Show Stats:    │
│ • Total Tweets  │
│ • Locations     │
│ • Active Users  │
│ • Current View  │
└─────────────────┘
```

### 5. Map Interaction Flow

```
┌─────────────────┐
│   Map Loaded    │
│  with Markers   │
└─────────────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌─────────────────┐  ┌─────────────────┐
│  Hover Marker   │  │  Click Marker   │
└─────────────────┘  └─────────────────┘
    │                    │
    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐
│  Show Preview   │  │  Show Detailed  │
│   Tooltip       │  │     Popup       │
└─────────────────┘  └─────────────────┘
                         │
                         ▼
                 ┌─────────────────┐
                 │  Popup Content: │
                 │ • User Avatar   │
                 │ • Username      │
                 │ • Tweet Text    │
                 │ • Location      │
                 │ • Timestamp     │
                 │ • Photo (opt)   │
                 └─────────────────┘
```

### 6. Search & Filter Flow

```
┌─────────────────┐
│   Map Page      │
│  All Markers    │
│   Visible       │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Type in        │
│  Search Box     │
│  (Real-time)    │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Filter Logic:  │
│ • Username      │
│ • Tweet Content │
│ • Location Name │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Hide Non-      │
│  Matching       │
│  Markers        │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Update Stats   │
│  Counter        │
│  (Filtered)     │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Show "Clear"   │
│   Button        │
└─────────────────┘
```

### 7. Profile & Navigation Flow

```
┌─────────────────┐
│   Any Page      │
│   (Logged In)   │
└─────────────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌─────────────────┐  ┌─────────────────┐
│  Click Username │  │  Click "Map"    │
│     Link        │  │   Button        │
└─────────────────┘  └─────────────────┘
    │                    │
    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐
│   Profile Page  │  │   Map Page      │
│ (/profile/user/)│  │   (/map/)       │
└─────────────────┘  └─────────────────┘
    │
    ▼
┌─────────────────┐
│  Show User:     │
│ • Profile Info  │
│ • User's Tweets │
│ • Pagination    │
└─────────────────┘
```

### 8. API Access Flow

```
┌─────────────────┐
│   Dashboard     │
│   (Logged In)   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Click "API"   │
│   Link          │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   API Doc Page  │
│  (/api/view/)   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Show:          │
│ • API Endpoint  │
│ • Response      │
│ • JSON Format   │
│ • Usage Guide   │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Direct Access  │
│  /api/posts/    │
│  (JSON Data)    │
└─────────────────┘
```

## User Journey Scenarios

### Scenario 1: New User Registration & First Tweet

1. **Start**: User visits application
2. **Register**: Creates new account
3. **Login**: Automatically logged in
4. **Dashboard**: Sees empty timeline
5. **Create Tweet**: Writes first tweet with location
6. **Result**: Tweet appears in timeline and map

### Scenario 2: Existing User Tweet & Map Exploration

1. **Start**: User logs in
2. **Dashboard**: Views timeline of all tweets
3. **Create Tweet**: Posts new tweet with photo
4. **Map**: Navigates to map page
5. **Explore**: Views all tweet locations
6. **Search**: Filters tweets by location
7. **Interact**: Clicks markers to see details

### Scenario 3: API Consumer

1. **Start**: Developer needs tweet data
2. **Login**: Accesses application
3. **API Docs**: Views API documentation
4. **Endpoint**: Makes GET request to /api/posts/
5. **Result**: Receives JSON data for integration

## Navigation Pattern

```
┌─────────────────┐
│      Base       │
│    Template     │
│   Navigation    │
└─────────────────┘
         │
    ┌────┼────┐
    │    │    │
    ▼    ▼    ▼
┌──────┐ ┌──────┐ ┌──────┐
│ Home │ │ Map  │ │ API  │
│  📏  │ │  🗺️  │ │  ⚙️  │
└──────┘ └──────┘ └──────┘
```

**Navigation is consistent across all pages:**

- **Home/Dashboard**: Main timeline and tweet creation
- **Map**: Geographic exploration of tweets
- **API**: Developer documentation and access
- **Profile**: User-specific tweet view
- **Logout**: Authentication management

## Error Handling Flows

### Form Validation Errors

```
User Input → Validation → Error? → Show Error → Stay on Form
                      → No Error → Process → Redirect
```

### API/Network Errors

```
Request → Network Error → Show Error Message → Retry Button
       → Success → Process Data → Update UI
```

### Authentication Errors

```
Protected Page → Not Logged In → Redirect to Login
              → Logged In → Show Page Content
```
