# Entity Relationship Diagram (ERD)

## Database Schema

Aplikasi Twitter Clone menggunakan 2 tabel utama dengan struktur sebagai berikut:

```
┌─────────────────────────────────────────┐
│                  USER                   │
├─────────────────────────────────────────┤
│ PK: id (AutoField)                      │
│    username (CharField, unique, 150)     │
│    email (EmailField, unique)           │
│    password (CharField, 128)            │
│    first_name (CharField, 150)          │
│    last_name (CharField, 150)           │
│    is_staff (BooleanField)              │
│    is_active (BooleanField)             │
│    date_joined (DateTimeField)          │
│    last_login (DateTimeField)           │
│ +  bio (TextField, 160, blank=True)     │
│ +  location (CharField, 30, blank=True) │
│ +  birth_date (DateField, null=True)    │
│ +  avatar (ImageField, null=True)       │
│ +  created_at (DateTimeField)           │
└─────────────────────────────────────────┘
                    │
                    │ 1:N
                    │
                    ▼
┌─────────────────────────────────────────┐
│                 TWEET                   │
├─────────────────────────────────────────┤
│ PK: id (AutoField)                      │
│ FK: user_id → User.id                   │
│    content (TextField, 140)             │
│    location (CharField, 255)            │
│    latitude (DecimalField, 15,10)       │
│    longitude (DecimalField, 16,10)      │
│    image (ImageField, null=True)        │
│    created_at (DateTimeField)           │
│    updated_at (DateTimeField)           │
└─────────────────────────────────────────┘
```

## Relationships

### User → Tweet (One-to-Many)

- **Relationship Type**: One-to-Many (1:N)
- **Foreign Key**: `Tweet.user_id` → `User.id`
- **Related Name**: `tweets`
- **On Delete**: CASCADE (jika user dihapus, semua tweet ikut terhapus)
- **Description**: Satu user dapat memiliki banyak tweet

## Field Descriptions

### User Model Fields

| Field Name  | Type          | Max Length | Constraints      | Description                    |
| ----------- | ------------- | ---------- | ---------------- | ------------------------------ |
| id          | AutoField     | -          | PRIMARY KEY      | Primary key auto-increment     |
| username    | CharField     | 150        | UNIQUE, NOT NULL | Username unik untuk login      |
| email       | EmailField    | 254        | UNIQUE, NOT NULL | Email address untuk registrasi |
| password    | CharField     | 128        | NOT NULL         | Password ter-hash              |
| first_name  | CharField     | 150        | BLANK            | Nama depan pengguna            |
| last_name   | CharField     | 150        | BLANK            | Nama belakang pengguna         |
| is_staff    | BooleanField  | -          | DEFAULT: False   | Status admin                   |
| is_active   | BooleanField  | -          | DEFAULT: True    | Status aktif user              |
| date_joined | DateTimeField | -          | AUTO_NOW_ADD     | Tanggal registrasi             |
| last_login  | DateTimeField | -          | NULL             | Tanggal login terakhir         |
| bio         | TextField     | 160        | BLANK            | Bio singkat pengguna           |
| location    | CharField     | 30         | BLANK            | Lokasi pengguna                |
| birth_date  | DateField     | -          | NULL, BLANK      | Tanggal lahir                  |
| avatar      | ImageField    | -          | NULL, BLANK      | Foto profil                    |
| created_at  | DateTimeField | -          | AUTO_NOW_ADD     | Timestamp pembuatan            |

### Tweet Model Fields

| Field Name | Type          | Max Length | Constraints       | Description                  |
| ---------- | ------------- | ---------- | ----------------- | ---------------------------- |
| id         | AutoField     | -          | PRIMARY KEY       | Primary key auto-increment   |
| user_id    | ForeignKey    | -          | NOT NULL, CASCADE | Reference ke User            |
| content    | TextField     | 140        | NOT NULL          | Isi tweet (max 140 karakter) |
| location   | CharField     | 255        | NOT NULL          | Nama lokasi tweet            |
| latitude   | DecimalField  | 15,10      | NULL, BLANK       | Koordinat lintang            |
| longitude  | DecimalField  | 16,10      | NULL, BLANK       | Koordinat bujur              |
| image      | ImageField    | -          | NULL, BLANK       | Foto tweet                   |
| created_at | DateTimeField | -          | AUTO_NOW_ADD      | Timestamp pembuatan          |
| updated_at | DateTimeField | -          | AUTO_NOW          | Timestamp update             |

## Database Indexes

### Automatic Indexes

- `User.id` (PRIMARY KEY)
- `User.username` (UNIQUE)
- `User.email` (UNIQUE)
- `Tweet.id` (PRIMARY KEY)
- `Tweet.user_id` (FOREIGN KEY)

### Custom Indexes (untuk optimasi)

- `Tweet.created_at` (untuk ordering timeline)
- `Tweet.latitude, Tweet.longitude` (untuk query geografis)

## Query Patterns

### Common Queries

1. **Get all tweets for timeline**:

   ```sql
   SELECT * FROM tweet
   JOIN user ON tweet.user_id = user.id
   ORDER BY tweet.created_at DESC;
   ```

2. **Get tweets by specific user**:

   ```sql
   SELECT * FROM tweet
   WHERE user_id = ?
   ORDER BY created_at DESC;
   ```

3. **Get tweets with location data**:

   ```sql
   SELECT * FROM tweet
   WHERE latitude IS NOT NULL AND longitude IS NOT NULL;
   ```

4. **Search tweets by content or location**:
   ```sql
   SELECT * FROM tweet
   WHERE content LIKE ? OR location LIKE ?;
   ```

## Database Size Estimates

Berdasarkan struktur tabel dan field types:

- **User record**: ~500 bytes per record
- **Tweet record**: ~800 bytes per record
- **Image files**: Variable (0-5MB per image)

### Scalability Considerations

1. **Pagination**: Implemented untuk menghindari load semua data
2. **Image Storage**: Menggunakan Django ImageField dengan proper upload path
3. **Geographic Queries**: Decimal fields untuk koordinat GPS
4. **Indexing**: Otomatis untuk FK dan unique fields

## Migration History

1. **0001_initial.py**: Create User dan Tweet models
2. **0002_tweet_latitude_tweet_location_tweet_longitude_and_more.py**: Add location fields
3. **0003_tweet_image.py**: Add image field
4. **0004_alter_tweet_latitude_alter_tweet_location_and_more.py**: Adjust field types
5. **0005_alter_tweet_latitude_alter_tweet_longitude.py**: Final coordinate field adjustments
