# Database Schema - Osland Global Network

---

## User (Django Default)
Used for dashboard authentication.

---

## SiteSettings
- id
- company_name
- email
- phone
- whatsapp_number
- address
- business_hours
- logo
- created_at
- updated_at

---

## HomePage
- id
- hero_title
- hero_subtitle
- short_intro
- updated_at

---

## AboutPage
- id
- company_overview
- mission
- vision
- updated_at

---

## ProductCategory
- id
- name
- description
- slug
- created_at

---

## Product
- id
- category (FK → ProductCategory)
- name
- description
- grade
- sizes_available
- packaging_type
- minimum_order_quantity
- export_availability
- featured (Boolean)
- slug
- created_at
- updated_at

---

## ProductImage
- id
- product (FK → Product)
- image
- alt_text
- created_at

---

## GalleryImage
- id
- image
- title
- category (Raw Horns, Processed, Hide, Warehouse, etc.)
- uploaded_at

---

## ExportService
- id
- title
- description

---

## ExportMarket
- id
- country_name

---

## FAQ
- id
- question
- answer
- created_at

---

## Inquiry
- id
- full_name
- company_name
- country
- email
- phone
- product_needed
- quantity
- message
- status (New, Contacted, Closed)
- created_at

---

Relationships Summary

ProductCategory → Product (1-to-many)
Product → ProductImage (1-to-many)
