<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Development Checklists

Below is a detailed checklist of atomic tasks for each ticket.

- Each task begins with a blank checkbox `[ ]`.
- Each task has a unique identifier composed of the ticket ID plus a two-digit task number (e.g., **T-003-02**).
- Every functionality starts with writing unit tests and ends with executing them.


### T-001  Draft project glossary

- [x] **T-001-01** Write unit-test skeleton validating that generated glossary JSON has required keys (`term`, `definition`).
- [x] **T-001-02** Collect seed papers (5+) into `data/seeds/papers/`.
- [x] **T-001-03** Write script to extract candidate glossary terms.
- [x] **T-001-04** Generate initial glossary draft (`glossary_draft.json`).
- [x] **T-001-05** Run unit tests for glossary structure.


### T-002  Approve glossary

- [ ] **T-002-01** Write unit test: glossary entries flagged “approved” must have non-empty definitions.
- [ ] **T-002-02** Create review spreadsheet from `glossary_draft.json`.
- [ ] **T-002-03** Run CI checks with AI static analysis and review the generated report
- [ ] **T-002-04** Update glossary JSON with approvals.
- [ ] **T-002-05** Execute approval unit tests.


### T-003  Fetch external ontology metadata

- [ ] **T-003-01** Write unit test: downloader returns 200 status \& saves file to cache.
- [ ] **T-003-02** Implement HTTP/FTP download helper.
- [ ] **T-003-03** Download GO, PO, TO, PECO, ChemOnt, NPClassifier, PlantCyc.
- [ ] **T-003-04** Checksum \& version stamp each file.
- [ ] **T-003-05** Run downloader unit tests.


### T-004  Cache ontology snapshots

- [ ] **T-004-01** Unit test: cached path resolved correctly via `OntologyFetcher`.
- [ ] **T-004-02** Design directory scheme `data/ontologies/raw/<source>/<version>/`.
- [ ] **T-004-03** Move downloaded files into scheme.
- [ ] **T-004-04** Log manifest (`ontologies_manifest.csv`).
- [ ] **T-004-05** Run cache resolution tests.


### T-005  Implement `OntologyFetcher` class

- [ ] **T-005-01** Unit test: `OntologyFetcher.get("GO", "latest")` returns local path.
- [ ] **T-005-02** Code class with download, cache, update methods.
- [ ] **T-005-03** Add retry \& timeout logic.
- [ ] **T-005-04** Document public API in docstring.
- [ ] **T-005-05** Execute unit tests.


### T-006  Build vocabulary-trimming algorithm

- [ ] **T-006-01** Write unit test: trimming reduces PO to ≤293 terms.
- [ ] **T-006-02** Implement depth-based trimming.
- [ ] **T-006-03** Implement usage-frequency scoring.
- [ ] **T-006-04** Combine criteria; output CSV.
- [ ] **T-006-05** Run trimming unit tests.


### T-007  Export trimmed term CSVs

- [ ] **T-007-01** Unit test: CSV headers `id,label,parent` exist.
- [ ] **T-007-02** Write exporter utility.
- [ ] **T-007-03** Generate PO, PECO, TO subset files.
- [ ] **T-007-04** Validate row counts.
- [ ] **T-007-05** Execute exporter tests.


### T-008  Review borderline trimmed terms

- [ ] **T-008-01** Unit test: review file includes `confidence` column.
- [ ] **T-008-02** Auto-generate list of low-confidence terms.
- [ ] **T-008-03** Facilitate manual review (spreadsheet or Markdown).
- [ ] **T-008-04** Merge curator feedback into final CSV.
- [ ] **T-008-05** Run review-file unit tests.


### T-009  Design ontology YAML schema

- [ ] **T-009-01** Unit test: YAML validates against pydantic model.
- [ ] **T-009-02** Draft `configs/ontology.yaml` with three facets \& relations.
- [ ] **T-009-03** Add xref mapping rules.
- [ ] **T-009-04** Run AI code critique and enforce coverage gates
- [ ] **T-009-05** Execute YAML validation tests.


### T-010  Implement `OntologyBuilder`

- [ ] **T-010-01** Unit test: builder outputs non-empty OWL graph.
- [ ] **T-010-02** Code CSV→OWL conversion.
- [ ] **T-010-03** Integrate YAML schema for relations.
- [ ] **T-010-04** Serialize OWL, TTL, JSON-LD.
- [ ] **T-010-05** Run builder unit tests.


### T-011  Implement `RelationManager`

- [ ] **T-011-01** Unit test: created object property exists in graph.
- [ ] **T-011-02** Add create/update helpers.
- [ ] **T-011-03** Attach domain/range axioms.
- [ ] **T-011-04** Expose API to `OntologyBuilder`.
- [ ] **T-011-05** Execute relation tests.


### T-012  Ontology validation suite

- [ ] **T-012-01** Unit test: cycle detection flags circular subclass.
- [ ] **T-012-02** Implement hierarchy checks.
- [ ] **T-012-03** Implement xref verification.
- [ ] **T-012-04** Create validation report generator.
- [ ] **T-012-05** Run validation tests.


### T-013  Export ontology formats

- [ ] **T-013-01** Unit test: CSV export rows equal OWL classes.
- [ ] **T-013-02** Implement export helpers (CSV, JSON-LD).
- [ ] **T-013-03** Embed version info in filenames.
- [ ] **T-013-04** Write checksum manifest.
- [ ] **T-013-05** Run export tests.


### T-014  Generate synthetic ontology test data

- [ ] **T-014-01** Unit test: synthetic CSV has ≤20 rows.
- [ ] **T-014-02** Create generator script.
- [ ] **T-014-03** Store under `data/synthetic/ontology/`.
- [ ] **T-014-04** Document usage in README.
- [ ] **T-014-05** Execute generator tests.


### T-015  Unit tests: ontology build

- [ ] **T-015-01** Write pytest cases covering builder, relations, validator.
- [ ] **T-015-02** Mock synthetic data inputs.
- [ ] **T-015-03** Set up CI job for ontology tests.
- [ ] **T-015-04** Run test suite; ensure ≥90% coverage.


### T-016  Implement `Config` loader

- [ ] **T-016-01** Unit test: invalid YAML raises `ValidationError`.
- [ ] **T-016-02** Code pydantic models.
- [ ] **T-016-03** Add YAML merge logic.
- [ ] **T-016-04** Document default search order.
- [ ] **T-016-05** Run config loader tests.


### T-017  Implement `generate_stable_id` util

- [ ] **T-017-01** Unit test: identical input returns same ID.
- [ ] **T-017-02** Implement 32-bit hash with namespace.
- [ ] **T-017-03** Collision check on 10,000 random strings.
- [ ] **T-017-04** Expose via `utils.py`.
- [ ] **T-017-05** Run ID generator tests.


### T-018  Build `Compound` \& `OntologyTerm` models

- [ ] **T-018-01** Unit test: missing required field triggers validation error.
- [ ] **T-018-02** Define pydantic schemas.
- [ ] **T-018-03** Add `from_csv()` factory methods.
- [ ] **T-018-04** Create serialization to JSON.
- [ ] **T-018-05** Execute model tests.


### T-019  Script `build_ontology.py`

- [ ] **T-019-01** Unit test: CLI returns exit code 0 and writes OWL.
- [ ] **T-019-02** Set up `argparse` interface.
- [ ] **T-019-03** Wire to `OntologyBuilder` \& `Validator`.
- [ ] **T-019-04** Print summary stats (class count).
- [ ] **T-019-05** Run CLI unit tests.


### T-020  Fetch seed PMC papers

- [ ] **T-020-01** Unit test: fetcher downloads XML to disk.
- [ ] **T-020-02** Implement `PaperFetcher` for PMC IDs.
- [ ] **T-020-03** Add retry \& progress bar.
- [ ] **T-020-04** Store papers in `corpora/pmc_xml/`.
- [ ] **T-020-05** Run fetcher tests.


### T-021  Parse PMC XML to JSONL segments

- [ ] **T-021-01** Unit test: parser produces non-empty JSONL.
- [ ] **T-021-02** Implement `XMLParser`.
- [ ] **T-021-03** Chunk sections with citation anchors.
- [ ] **T-021-04** Output to `work/segments.jsonl`.
- [ ] **T-021-05** Execute parser tests.


### T-022  Implement `ChemNER` \& `BioNER`

- [ ] **T-022-01** Unit test: NER returns expected entity labels on mock text.
- [ ] **T-022-02** Load pretrained/fine-tuned models.
- [ ] **T-022-03** Wrap in `extract_entities()` API.
- [ ] **T-022-04** Add batch inference.
- [ ] **T-022-05** Run NER tests.


### T-023  Implement `RelationExtractor`

- [ ] **T-023-01** Unit test: RE returns relation type string.
- [ ] **T-023-02** Set up quantized Llama-70B wrapper.
- [ ] **T-023-03** Pairwise entity candidate generation.
- [ ] **T-023-04** Confidence thresholding.
- [ ] **T-023-05** Execute RE tests.


### T-024  Normalize literature entities

- [ ] **T-024-01** Unit test: best-match ID similarity ≥0.9.
- [ ] **T-024-02** Implement fuzzy matcher via rapidfuzz.
- [ ] **T-024-03** Map to trimmed vocab CSVs.
- [ ] **T-024-04** Flag unmatched entities.
- [ ] **T-024-05** Run normalization tests.


### T-025  Produce literature fact JSON

- [ ] **T-025-01** Unit test: JSON schema matches `Fact` model.
- [ ] **T-025-02** Merge NER + RE results.
- [ ] **T-025-03** Attach provenance (paper, sentence).
- [ ] **T-025-04** Write `facts_lit.jsonl`.
- [ ] **T-025-05** Execute fact-file tests.


### T-026  Gold-standard annotation set

- [ ] **T-026-01** Unit test: gold set ≥100 annotated sentences.
- [ ] **T-026-02** Select 5–25 papers for annotation.
- [ ] **T-026-03** Annotate entities \& relations (brat/spacy).
- [ ] **T-026-04** Export to JSONL.
- [ ] **T-026-05** Run gold-set tests.


### T-027  Metrics: precision, recall, F1

- [ ] **T-027-01** Unit test: metric function returns 1.0 on perfect match.
- [ ] **T-027-02** Implement scorer comparing predictions vs gold.
- [ ] **T-027-03** Aggregate per-relation metrics.
- [ ] **T-027-04** Plot results to console table.
- [ ] **T-027-05** Execute metric tests.


### T-028  GNPS dataset downloader

- [ ] **T-028-01** Unit test: GNPSClient saves `.mzML` meta files.
- [ ] **T-028-02** Implement API calls for dataset ID.
- [ ] **T-028-03** Validate checksum.
- [ ] **T-028-04** Store under `data/gnps/raw/`.
- [ ] **T-028-05** Run downloader tests.


### T-029  Compound classifier (NPClassifier)

- [ ] **T-029-01** Unit test: classifier returns NP class string.
- [ ] **T-029-02** Integrate remote NPClassifier API.
- [ ] **T-029-03** Fallback to local model if offline.
- [ ] **T-029-04** Batch classify compounds TSV.
- [ ] **T-029-05** Execute classifier tests.


### T-030  ChemOnt structural mapper

- [ ] **T-030-01** Unit test: InChIKey maps to ChemOnt ID.
- [ ] **T-030-02** Integrate ClassyFire look-up.
- [ ] **T-030-03** Cache results locally.
- [ ] **T-030-04** Merge with NPClassifier output.
- [ ] **T-030-05** Run mapper tests.


### T-031  Pathway mapper (PlantCyc)

- [ ] **T-031-01** Unit test: compound → ≥1 pathway ID.
- [ ] **T-031-02** Load PlantCyc tables.
- [ ] **T-031-03** Implement lookup \& mapping.
- [ ] **T-031-04** Attach evidence codes.
- [ ] **T-031-05** Execute pathway tests.


### T-032  Annotate sample metadata

- [ ] **T-032-01** Unit test: sample row adds PO/PECO IDs.
- [ ] **T-032-02** Parse GNPS sample JSON.
- [ ] **T-032-03** Fuzzy map tissues \& conditions.
- [ ] **T-032-04** Output annotations TSV.
- [ ] **T-032-05** Run metadata tests.


### T-033  Export metabolomics annotations

- [ ] **T-033-01** Unit test: TSV columns match spec.
- [ ] **T-033-02** Combine classifications, pathways, metadata.
- [ ] **T-033-03** Add confidence scores.
- [ ] **T-033-04** Write `metabolomics_annotations.tsv`.
- [ ] **T-033-05** Execute export tests.


### T-034  Cross-source linker

- [ ] **T-034-01** Unit test: merged record includes both literature \& MS evidence.
- [ ] **T-034-02** Join on `compound_id`.
- [ ] **T-034-03** Merge ontology term sets.
- [ ] **T-034-04** Write `linked_annotations.jsonl`.
- [ ] **T-034-05** Run linker tests.


### T-035  Conflict resolver

- [ ] **T-035-01** Unit test: conflicting relation flagged.
- [ ] **T-035-02** Detect contradictions by term/relation.
- [ ] **T-035-03** Score conflicts by confidence gap.
- [ ] **T-035-04** Output resolution suggestions.
- [ ] **T-035-05** Execute conflict tests.


### T-036  Enrichment statistical module

- [ ] **T-036-01** Unit test: Fisher p-value <0.05 for known enriched set.
- [ ] **T-036-02** Implement Fisher exact \& FDR methods.
- [ ] **T-036-03** Load background universe from annotations.
- [ ] **T-036-04** Return sorted enrichment table.
- [ ] **T-036-05** Run enrichment tests.


### T-037  Pathway \& trait enrichment scripts

- [ ] **T-037-01** Unit test: CLI writes TSV with p-values.
- [ ] **T-037-02** Create `run_enrichment.py` wrapper.
- [ ] **T-037-03** Add YAML config parsing.
- [ ] **T-037-04** Support Structural / Source / Functional facets.
- [ ] **T-037-05** Execute CLI tests.


### T-038  Synthetic data generator

- [ ] **T-038-01** Unit test: generator outputs ≥10 mock compounds.
- [ ] **T-038-02** Generate synthetic compounds CSV.
- [ ] **T-038-03** Generate mock literature facts.
- [ ] **T-038-04** Generate artificial MS annotations.
- [ ] **T-038-05** Run generator tests.


### T-039  Unit tests: literature NER/RE

- [ ] **T-039-01** Write pytest fixtures for mock sentences.
- [ ] **T-039-02** Test entity span correctness.
- [ ] **T-039-03** Test relation detection accuracy.
- [ ] **T-039-04** Achieve ≥85% F1 on synthetic data.
- [ ] **T-039-05** Commit test coverage reports.


### T-040  Unit tests: metabolomics pipeline

- [ ] **T-040-01** Create synthetic MS dataset fixture.
- [ ] **T-040-02** Test classification outputs (NP \& ChemOnt).
- [ ] **T-040-03** Test pathway mapping correctness.
- [ ] **T-040-04** Test metadata annotation integrity.
- [ ] **T-040-05** Publish coverage badge.


### T-041  Integration test: full pipeline

- [ ] **T-041-01** Unit test: end-to-end run produces linked \& enriched TSV.
- [ ] **T-041-02** Wire synthetic data through all scripts.
- [ ] **T-041-03** Assert no exceptions \& valid outputs.
- [ ] **T-041-04** Measure run-time performance.
- [ ] **T-041-05** Log integration report.


### T-042  Continuous Integration setup

- [ ] **T-042-01** Unit test: CI workflow YAML passes `act` dry-run.
- [ ] **T-042-02** Configure GitHub Actions for lint + tests.
- [ ] **T-042-03** Add coverage upload to Codecov.
- [ ] **T-042-04** Set branch protection rules.
- [ ] **T-042-05** Validate CI on pull request.


### T-043  Project documentation scaffold

- [ ] **T-043-01** Unit test: `mkdocs build` exits 0.
- [ ] **T-043-02** Create docs folder with `index.md`, `usage.md`.
- [ ] **T-043-03** Generate API docs via `pydoc-markdown`.
- [ ] **T-043-04** Add contribution guidelines.
- [ ] **T-043-05** Run documentation build tests.


### T-044  Release v0.1 bundle

- [ ] **T-044-01** Unit test: release script creates tarball with expected files.
- [ ] **T-044-02** Compile OWL, CSV subsets, synthetic data.
- [ ] **T-044-03** Generate `CHANGELOG.md`.
- [ ] **T-044-04** Tag Git commit `v0.1.0`.
- [ ] **T-044-05** Run release unit tests and publish artifact.

Total atomic tasks: **220** (5 tasks per ticket × 44 tickets).

<div style="text-align: center">⁂</div>

[^1]: C-spirit-ontology-overall-plan-by-GPT-03-Possible-Python-scripts.md
