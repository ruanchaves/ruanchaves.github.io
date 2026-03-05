# Source content workflow

This directory stores raw exports and working source material used to curate the public website.

## Principles

- `files/` is reserved for intentional public downloads only.
- Raw profile exports, scraped data, generated summaries, and archived HTML stay under `sources/`.
- The website should render curated content from `_data/` and page files instead of exposing raw dumps directly.

## Current source inputs

- LinkedIn profile export
- GitHub profile and repository summaries
- Google Scholar summaries and article metadata
- Medium archive exports
- local scripts used to extract or summarize profile data

## Refresh process

1. Put new raw exports in `sources/profile/`.
2. Update `_data/candidate.yml` with any new facts worth surfacing publicly.
3. Review homepage, experience, projects, research, writing, and resume pages for needed edits.
4. Keep `files/` limited to assets that a recruiter should download directly, such as the PDF resume.
