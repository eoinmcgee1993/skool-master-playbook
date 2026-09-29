# Architecture

## Responsibilities

### Ingestion
Accept authorised transcripts, lesson exports, PDFs, notes and resource metadata.

### Normalisation
Convert heterogeneous inputs into a stable lesson schema.

### Provenance
Every extracted claim keeps source, lesson, section and ingestion timestamp metadata.

### Handoff
Produce deterministic JSONL/Markdown bundles for the playbook engine.

### Publication
Generate versioned Markdown/HTML/PDF artefacts without mutating source material.

## Non-goals
- credential capture
- session-cookie harvesting
- CAPTCHA bypass
- access-control bypass
- unauthorised scraping
