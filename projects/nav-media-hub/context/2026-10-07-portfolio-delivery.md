# Portfolio delivery recommendation — 7 October 2026

## User statement

The user reports that the client has supplied real portfolio material and has Cloudflare R2,
and asks where to upload videos for the website. This establishes reported availability,
not inspected files, approved publication rights, a configured bucket, or upload authorization.

## Research and proposed approach

Skill used: workspace skills/research/SKILL.md. Official Cloudflare documentation checked
on 7 October 2026. Proposed approach: for a small curated portfolio of short videos, use
a dedicated R2 Standard bucket for approved compressed web exports and poster images,
served through a custom media subdomain. Keep original masters in a separate private bucket.
Laravel renders project metadata; the browser retrieves video directly from the media URL.
Prepare broadly compatible MP4/H.264/AAC exports, fast-start metadata, intentional poster
frames, restrained preload and explicit play/pause controls. Preserve portrait/wide framing.
Measure actual files/network playback before settling export settings.

Cloudflare facts: custom domains enable R2 caching; r2.dev is rate limited and intended for
development. Default caching depends on file type and cache rules. Free/Pro/Business cache
objects up to 512 MB, so large original files are inappropriate as the default web export.
R2 has no direct egress-bandwidth charge, but storage/operation charges can apply.
Stream provides automatic encoding and adaptive bitrate playback at 360p–1080p. Consider
Stream for longer/heavier videos when automatic quality adjustment is worth its separate
service cost. R2 direct-file delivery does not itself provide that encoding pipeline.

Sources:
- https://developers.cloudflare.com/r2/buckets/public-buckets/
- https://developers.cloudflare.com/cache/interaction-cloudflare-products/r2/
- https://developers.cloudflare.com/r2/pricing/
- https://developers.cloudflare.com/stream/

## Current application and next inputs

config/nav.php still has an empty project list; the current Blade template contains a native
MP4 video player with explicit controls and poster support. No runtime or cloud setting was
changed. R2 remains a proposed delivery decision, pending the user's selection and actual
video counts, durations, sizes, desired quality, public rights and custom-domain availability.
No files were uploaded, no credentials requested, and no bucket access was made public.
