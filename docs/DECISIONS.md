# Architecture Decisions

## 1. Human-in-the-Loop Review

Decision:
Data is reviewed before becoming final.

Reason:
Client ESG data often contains missing fields and inconsistencies.

---

## 2. Separate Raw and Normalized Data

Decision:
Store raw input separately from transformed data.

Reason:
Provides auditability and allows reprocessing if mapping logic changes.

---

## 3. Queue-Based Processing

Decision:
Use asynchronous ingestion workers.

Reason:
Large files should not block user uploads.

---

## 4. API-First Backend

Decision:
Backend exposes REST APIs.

Reason:
Allows frontend and future integrations to consume the same services.
