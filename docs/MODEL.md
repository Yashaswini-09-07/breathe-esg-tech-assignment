# Data Model

## Core Entities

### Company
- company_id
- name
- industry
- country

### DataSource
- source_id
- company_id
- source_type (SAP, PDF, Excel, API)
- upload_date
- status

### RawRecord
- record_id
- source_id
- raw_data
- ingestion_timestamp

### NormalizedRecord
- record_id
- company_id
- activity_type
- quantity
- unit
- date

### ReviewTask
- review_id
- record_id
- reviewer
- status
- comments

## Relationships

Company → DataSource → RawRecord → NormalizedRecord

NormalizedRecord → ReviewTask
