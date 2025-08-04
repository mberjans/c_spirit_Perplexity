<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Development Tickets for Plant Resilience Chemical Ontology Toolkit

| ID | Title | Description | Module / Area | Phase | Prerequisites |
| :-- | :-- | :-- | :-- | :-- | :-- |
| T-001 | Draft project glossary | Generate draft definitions of “plant resilience,” stressors, and outcomes from seed papers | Documentation | 1 | – |
| T-002 | Auto-glossary adjudication (no-HITL) | Multi-agent LLM consensus + NLI entailment + ontology constraints to generate/validate glossary; emit JSON change-log. **Acceptance:** F1≥0.95 on duplicate/ambiguity detection (synthetic), zero OWL validation errors. | Documentation | 1 | T-001 |
| T-003 | Fetch external ontology metadata | Download GO, PO, TO, PECO, ChemOnt, NPClassifier, PlantCyc term dumps (latest versions) | termstore ∙ fetcher | 1 | – |
| T-004 | Cache ontology snapshots | Store raw ontology files in `data/ontologies/raw/` with version hashes | termstore ∙ fetcher | 1 | T-003 |
| T-005 | Implement `OntologyFetcher` class | Generic downloader / local-cache wrapper supporting HTTP, FTP, and BioPortal APIs | termstore ∙ fetcher | 1 | T-004 |
| T-006 | Build vocabulary-trimming algorithm | Depth- \& usage-based trimming to target sizes (PO 293, PECO 127, TO 188) | termstore ∙ trimmer | 1 | T-005 |
| T-007 | Export trimmed term CSVs | Write curated subsets to `data/terms/` with headers `id,label,parent` | termstore ∙ trimmer | 1 | T-006 |
| T-008 | Automated borderline triage & policy learner | Score terms (info content, depth, usage, ambiguity, centrality); learn keep/drop policy to hit target sizes (PO 293 / PECO 127 / TO 188); self-consistency loop resolves defers; full constraint checks. **Acceptance:** counts within ±1%; no cycles; trimmed CSVs pass validator. | Curation | 1 | T-007 |
| T-009 | Design ontology YAML schema | Draft `configs/ontology.yaml` defining three facets, relations, and xrefs | ontology ∙ builder | 1 | T-002 |
| T-010 | Implement `OntologyBuilder` | Convert YAML + CSV term sets into OWL graph using rdflib | ontology ∙ builder | 1 | T-007, T-009 |
| T-011 | Implement `RelationManager` | Create object/data properties and domain/range axioms | ontology ∙ relations | 1 | T-009 |
| T-012 | Ontology validation suite | Consistency, cycle check, and xref verification | ontology ∙ validator | 1 | T-010, T-011 |
| T-013 | Export ontology formats | Write OWL, CSV, and JSON-LD plus validation report | ontology ∙ export | 1 | T-012 |
| T-014 | Generate synthetic ontology test data | Tiny CSVs (≤20 terms) for CI unit tests | tests | 1 | T-010 |
| T-015 | Unit tests: ontology build | pytest cases for `OntologyBuilder`, `RelationManager`, validation | tests | 1 | T-010, T-012, T-014 |
| T-016 | Implement `Config` loader | Typed pydantic classes + YAML merge logic | core | 1 | – |
| T-017 | Implement `generate_stable_id` util | 32-bit hash-based ID generator with namespace prefix | core ∙ utils | 1 | – |
| T-018 | Build `Compound` \& `OntologyTerm` models | pydantic schemas with validation rules | core ∙ models | 1 | T-017 |
| T-019 | Script `build_ontology.py` | CLI wrapper (argparse) to run build \& validation end-to-end | scripts | 1 | T-010, T-013, T-016 |
| T-020 | Fetch seed PMC papers | Download 25 open-access XML articles by PMID list | literature ∙ fetcher | 2 | – |
| T-021 | Parse PMC XML to JSONL segments | Implement `XMLParser` + `segment_content()` | literature ∙ parser | 2 | T-020 |
| T-022 | Implement `ChemNER` \& `BioNER` | Fine-tune or load pretrained models; expose `extract_entities()` | literature ∙ ner | 2 | T-021 |
| T-023 | Implement `RelationExtractor` | Llama-70B (quantized) wrapper for pairwise relation prediction | literature ∙ relation_extractor | 2 | T-022 |
| T-024 | Normalize literature entities | Map raw spans to trimmed term IDs using `rapidfuzz` | linking ∙ canonicalizer | 2 | T-022 |
| T-025 | Produce literature fact JSON | Combine NER + RE + normalization + provenance | literature ∙ pipeline | 2 | T-023, T-024 |
| T-026 | Programmatic silver→gold dataset builder | Build evaluation set via (1) synthetic templated+generative sentences, (2) distant supervision from PlantCyc/GO/PO/PECO, (3) model-agreement filters; include spans, normalized IDs, relation types, provenance. **Acceptance:** ≥2,000 labeled sentences; est. label error ≤5% (agreement+NLI); train/dev/test splits reproducible. | evaluation | 2 | T-020 |
| T-027 | Metrics: precision, recall, F1 | Compute extraction quality against gold set | evaluation ∙ metrics | 2 | T-025, T-026 |
| T-028 | GNPS dataset downloader | Implement `GNPSClient.fetch_dataset()` | metabolomics ∙ gnps_client | 2 | – |
| T-029 | Compound classifier (NPClassifier) | Wrap API or local model to assign NP classes | metabolomics ∙ classifier | 2 | T-028 |
| T-030 | ChemOnt structural mapper | Map InChIKey → ChemOnt via ClassyFire or local mapping | metabolomics ∙ classifier | 2 | T-028 |
| T-031 | Pathway mapper (PlantCyc) | Map compounds to pathways via PMN tables | metabolomics ∙ pathway_mapper | 2 | T-029 |
| T-032 | Annotate sample metadata | Map GNPS sample JSON to PO/PECO/species IDs | metabolomics ∙ annotator | 2 | T-028 |
| T-033 | Export metabolomics annotations | TSV with compound_id, term_id, relation, evidence | metabolomics ∙ pipeline | 2 | T-029–T-032 |
| T-034 | Cross-source linker | Merge metabolomics and literature facts on compound_id | linking ∙ merger | 3 | T-025, T-033 |
| T-035 | Conflict resolver | Detect \& flag contradictory annotations | linking ∙ conflict_resolver | 3 | T-034 |
| T-036 | Enrichment statistical module | Fisher test + FDR for GO/TO/Pathway enrichment | enrichment ∙ statistical | 3 | T-034 |
| T-037 | Pathway \& trait enrichment scripts | CLI `run_enrichment.py` with YAML-driven params | scripts | 3 | T-036 |
| T-038 | Synthetic data generator | `generate_synthetic_data.py` for compounds, facts, MS data | scripts | 4 | T-018 |
| T-039 | Unit tests: literature NER/RE | Mock sentences → expected entities/relations | tests | 4 | T-022, T-023, T-038 |
| T-040 | Unit tests: metabolomics pipeline | Synthetic MS data → expected annotations | tests | 4 | T-033, T-038 |
| T-041 | Integration test: full pipeline | Build ontology → extract facts → enrich set (synthetic data) | tests | 4 | T-019, T-025, T-033, T-037, T-038 |
| T-042 | Continuous Integration setup | GitHub Actions: lint, unit, integration, coverage | DevOps | 4 | T-015, T-039, T-040, T-041 |
| T-043 | Project documentation (auto-generated) scaffold | `docs/` with usage, module API, contribution guide | Documentation | 4 | T-019-T-037 |
| T-044 | Release v0.1 bundle | Publish OWL, CSV subsets, synthetic datasets, tarball of scripts | Release | 4 | T-013, T-033, T-038, T-042, T-043 |

Total tickets: **44**.

<div style="text-align: center">⁂</div>

[^1]: C-spirit-ontology-overall-plan-by-GPT-03-Possible-Python-scripts.md
