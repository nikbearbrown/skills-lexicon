# Field notes from the 25-credential check

**Usually filled (25 of 25 or close):** verdict, official name, issuer, description, credential type, field of work, requirements, jurisdiction, draft check. Level: 22.

**Often empty:**
- `official_url`: 11 of 25. Degrees, state-issued endorsements and generic college certificates have many issuers, so no single issuer domain exists. SACA and UK SC had no issuer-domain link in the results.
- `wikipedia_url`: 6 of 25. I counted only pages about the credential itself. Broader articles went into `other_sources`.
- `renewal`: 11 of 25. Results rarely stated it.
- `acronym`: empty for 7.

**Fields I wished I had:**
1. **Status** (active, retired, closed to new candidates). Mobility+ is retired, the ABMLI exam is closed, and DoD 8570 is being replaced. `notes` is the wrong place for it.
2. **Issuer scope** (single body, many institutions, or state by state). This separates a degree or endorsement from a certification, and would make a null `official_url` self-explanatory.
3. **Accreditor or standard-setter**, separate from the issuer: CAPTE, CEPH, FMCSA (49 CFR 383.93), ABSNC.
4. **Related credentials with the relationship**: P is a prerequisite for S; T needs a Class A CDL; Security+ satisfies IAM Level I; CPEN differs from CPN; STS versus STSC; a college certificate versus the state licence it prepares for.
5. **Stable identifier or code**: C-101, T, P, RR (the FCC's current code, versus RP in older listings), O*NET certification IDs seen in results (10047-C, 12826-A, 10937-B).
6. **Kind of entry** (specific credential, requirement level, generic programme type, occupation). IAM Level I and the four legacy certificates are not single credentials.
7. **Evidence type per claim.** The snippets here come from the search tool's own result summaries, not page text. A per-claim flag (issuer, third-party, Wikipedia, memory) would beat one `confidence` value.
