<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Software Development Plan: Plant Resilience Chemical Ontology Toolkit

## Project Overview

**Project Name**: Plant Resilience Chemical Ontology Toolkit
**Description**: A modular Python toolkit for building and managing a Plant Resilience Chemical Ontology that integrates structural, source, and functional facets of plant compounds related to stress resilience.

**Key Design Principles**:

- Modular architecture with standalone scripts and importable modules
- No GUI, API, or Docker requirements
- Comprehensive testing with synthetic data generation
- Focus on scientific reproducibility and data provenance


## Development Phases

### Phase 1: Foundation Setup (2-3 weeks)

**Modules**: ontology_builder, term_store, config_manager
**Deliverables**: OWL ontology skeleton, Trimmed vocabulary CSVs, Configuration system

### Phase 2: Data Processing Pipelines (4-6 weeks)

**Modules**: literature_processor, metabolomics_processor, nlp_extractors
**Deliverables**: Literature fact extraction, Metabolomics annotation, NER/RE models

### Phase 3: Integration \& Analysis (3-4 weeks)

**Modules**: data_linker, enrichment_analyzer, evaluator
**Deliverables**: Cross-source linking, Statistical analysis, Quality metrics

### Phase 4: Testing \& Documentation (2-3 weeks)

**Modules**: test_suite, synthetic_data_generator, documentation
**Deliverables**: Unit tests, Integration tests, Usage examples

## Project Structure

```
plant_resilience_ontology/
├── src/plant_resilience/
│   ├── core/                    # Core utilities and models
│   ├── ontology/               # OWL ontology building
│   ├── termstore/              # External ontology management
│   ├── literature/             # Literature processing pipeline
│   ├── metabolomics/           # Metabolomics data processing
│   ├── linking/                # Cross-source data integration
│   ├── enrichment/             # Statistical analysis
│   ├── data/                   # Data handling utilities
│   └── evaluation/             # Quality assessment
├── scripts/                    # Standalone execution scripts
├── tests/                      # Comprehensive test suite
├── configs/                    # YAML configuration files
├── data/                       # Data directories
└── requirements.txt            # Python dependencies
```


## Core Module Specifications

### Core Modules (`src/plant_resilience/core/`)

**config.py**: Configuration management system

- Classes: `Config`, `OntologyConfig`, `PipelineConfig`
- Functions: `load_config()`, `validate_config()`, `merge_configs()`
- Dependencies: pyyaml, pydantic

**models.py**: Core data models and schemas

- Classes: `Compound`, `OntologyTerm`, `Fact`, `Annotation`, `Evidence`
- Functions: `validate_compound()`, `serialize_fact()`, `merge_annotations()`
- Dependencies: pydantic, typing

**utils.py**: Common utility functions

- Functions: `normalize_text()`, `generate_stable_id()`, `safe_file_write()`, `batch_process()`
- Dependencies: pathlib, hashlib, logging


### Ontology Management (`src/plant_resilience/ontology/`)

**builder.py**

**builder_ai.md**: AI-assisted ontology construction guidelines

- Notes: `OntologyBuilder` consumes YAML/CSV without manual OWL editing; LLM-based helpers can propose relation patterns and detect conflicts for developer approval in CI-only mode.

: Build OWL ontologies from CSV/YAML configurations

- Classes: `OntologyBuilder`, `RelationManager`
- Functions: `build_owl_from_csv()`, `add_class_hierarchy()`, `add_relations()`, `validate_owl()`
- Dependencies: rdflib, pandas, owlready2

**validator.py**: Validate ontology structure and consistency

- Functions: `validate_hierarchy()`, `check_cycles()`, `validate_xrefs()`, `consistency_check()`
- Dependencies: rdflib, owlready2

**relations.py**: Manage ontology relations and properties

- Classes: `RelationBuilder`, `PropertyManager`
- Functions: `create_object_property()`, `create_data_property()`, `add_domain_range()`
- Dependencies: rdflib, owlready2


### Term Store Management (`src/plant_resilience/termstore/`)

**fetcher.py**: Fetch terms from external ontologies

- Classes: `OntologyFetcher`, `GOFetcher`, `POFetcher`, `ChemOntFetcher`
- Functions: `fetch_go_terms()`, `fetch_po_terms()`, `fetch_chemont_terms()`, `cache_ontology()`
- Dependencies: requests, pronto, oaklib

**trimmer.py**

**ai_qc.py**: AI-assisted quality control for trimmed vocabularies

- Functions: `score_borderline_terms()`, `llm_consistency_check()`, `auto_flag_mismatches()`
- Description: Replaces manual spreadsheet review (T-008) with rule-based thresholds and an LLM scoring pass to flag/remove low-confidence terms. Logs rationales; no human-in-the-loop is required for v0.1.
- Dependencies: pandas, scikit-learn, openai-compatible LLM client

: Trim large ontologies to manageable subsets

- Classes: `VocabularyTrimmer`
- Functions: `trim_by_depth()`, `trim_by_usage()`, `select_relevant_terms()`, `export_subset()`
- Dependencies: pandas, networkx


### Literature Processing (`src/plant_resilience/literature/`)

**fetcher.py**: Fetch scientific papers from various sources

- Classes: `PaperFetcher`, `PMCFetcher`, `PDFFetcher`
- Functions: `fetch_pmc_papers()`, `download_pdfs()`, `extract_metadata()`
- Dependencies: requests, lxml, beautifulsoup4

**ner.py**

**synthetic_lit.py**: Synthetic corpora & distant supervision

- Functions: `generate_ner_corpus()`, `template_relations()`, `augment_negatives()`
- Description: Avoids manual annotation by generating synthetic sentences and templated relation statements; uses distant supervision from the ontology to create labeled examples for NER/RE.
- Dependencies: transformers, spacy, faker

: Named Entity Recognition for chemical and biological entities

- Classes: `ChemNER`, `BioNER`, `EntityExtractor`
- Functions: `extract_compounds()`, `extract_species()`, `extract_tissues()`, `extract_conditions()`
- Dependencies: transformers, torch, spacy

**relation_extractor.py**: Extract relationships between entities

- Classes: `RelationExtractor`, `LLMExtractor`
- Functions: `extract_relations()`, `classify_relations()`, `validate_extractions()`
- Dependencies: transformers, torch


### Metabolomics Processing (`src/plant_resilience/metabolomics/`)

**gnps_client.py**: Interface with GNPS databases and APIs

- Classes: `GNPSClient`, `PlantMASTClient`
- Functions: `fetch_gnps_data()`, `query_spectral_libraries()`, `download_datasets()`
- Dependencies: requests, pandas

**classifier.py**: Classify compounds using NPClassifier and ChemOnt

- Classes: `CompoundClassifier`, `NPClassifier`, `ChemOntClassifier`
- Functions: `classify_by_structure()`, `assign_np_class()`, `map_to_chemont()`
- Dependencies: requests, rdkit, pandas

**synthetic_ms.py**: Synthetic MS/MS generation for testing

- Functions: `simulate_spectra()`, `inject_noise()`, `compose_batches()`
- Description: Replaces real instrument data with simulated spectra and batch effects for end-to-end testing and evaluation.
- Dependencies: numpy, scipy

## Standalone Scripts

### Primary Execution Scripts (`scripts/`)

**build_ontology.py**: Main script to build the Plant Resilience Ontology

- Usage: `python scripts/build_ontology.py --config configs/ontology.yaml --output data/ontology/`
- Functions: `load_term_subsets()`, `build_three_facet_ontology()`, `validate_ontology_structure()`, `export_formats()`
- Inputs: Term CSV files, Ontology configuration YAML, Relation definitions
- Outputs: OWL file, CSV export, JSON-LD export, Validation report

**process_literature.py**: Extract facts from scientific literature

- Usage: `python scripts/process_literature.py --input data/papers/ --output data/facts/`
- Functions: `fetch_papers_from_pmids()`, `parse_paper_content()`, `extract_entities_and_relations()`, `normalize_to_ontology()`
- Inputs: PMID list, PDF files, XML files
- Outputs: Extracted facts JSON/CSV, Entity annotations, Confidence scores

**process_metabolomics.py**: Process metabolomics data and annotate with ontology terms

- Usage: `python scripts/process_metabolomics.py --gnps-id MSV000012345 --output data/metabolomics/`
- Functions: `fetch_gnps_dataset()`, `classify_compounds()`, `map_sample_metadata()`, `annotate_with_ontology()`
- Inputs: GNPS dataset IDs, Mass spectrometry data, Sample metadata
- Outputs: Compound classifications, Ontology annotations, Pathway mappings

**run_enrichment.py**: Perform statistical enrichment analysis

- Usage: `python scripts/run_enrichment.py --compounds data/compound_set.txt --method fisher`
- Functions: `load_compound_annotations()`, `run_statistical_tests()`, `apply_multiple_testing_correction()`
- Inputs: Compound ID lists, Background universe, Ontology annotations
- Outputs: Enrichment results, Statistical summaries, Visualization data

**generate_synthetic_data.py**: Generate synthetic test data for development and testing

- Usage: `python scripts/generate_synthetic_data.py --type all --output data/synthetic/`
- Functions: `generate_synthetic_compounds()`, `create_mock_literature_facts()`, `generate_test_metabolomics_data()`
- Outputs: Synthetic compounds, Mock facts, Test datasets, Gold standard data


## Three-Facet Ontology Architecture

The ontology follows the three-facet structure outlined in the original document:

### Structural Facet

- **Relations**: `has_structural_class`, `has_NP_class`, `participates_in_pathway`
- **Sources**: ChemOnt, NPClassifier, PMN/PlantCyc


### Source Facet

- **Relations**: `detected_in_anatomy`, `observed_in_species`, `under_condition`
- **Sources**: PO, NCBI Taxonomy, PECO


### Functional Facet

- **Relations**: `affects_process`, `associated_with_trait`, `increases_tolerance_to`, `decreases_sensitivity_to`
- **Sources**: GO, TO, ChemFOnt


## Testing Strategy

### Unit Tests

- **Coverage**: Each module and major function
- **Approach**: pytest with fixtures for mock data
- **Key Areas**: Ontology building, term normalization, NLP extraction, statistical calculations, data conversions


### Integration Tests

- **Coverage**: End-to-end workflows
- **Approach**: Test complete pipelines with synthetic data
- **Key Workflows**: Ontology building, literature processing, metabolomics annotation, data linking, enrichment analysis


### Synthetic Data Tests

- **Purpose**: Test with controlled, known-correct data
- **Data Types**: Synthetic compounds, mock literature, artificial metabolomics data, controlled ontology subsets


## Development Dependencies

```
pandas>=1.5.0
pydantic>=2.0.0
pyyaml>=6.0
rdflib>=6.2.0
owlready2>=0.40
pronto>=2.5.0
oaklib>=0.5.0
requests>=2.28.0
rapidfuzz>=3.0.0
phonetics>=1.0.5
networkx>=3.0
lxml>=4.9.0
beautifulsoup4>=4.11.0
trafilatura>=1.6.0
transformers>=4.25.0
torch>=1.13.0
spacy>=3.5.0
rdkit>=2022.9.0
pytest>=7.0.0
pytest-cov>=4.0.0
```


## Key Implementation Features

1. **Modular Design**: Each component can be used independently or as part of larger workflows
2. **Configuration-Driven**: YAML configuration files control all pipeline behavior
3. **Synthetic Data Generation**: Built-in capability to generate test data for development and validation
4. **Comprehensive Testing**: Unit, integration, and synthetic data tests ensure reliability
5. **Data Provenance**: All extractions and annotations maintain full traceability to sources
6. **Extensible Architecture**: Easy to add new ontology sources, extraction methods, or analysis techniques

This development plan provides a solid foundation for creating a robust, modular toolkit that can grow and adapt to evolving research needs while maintaining scientific rigor and reproducibility.

<div style="text-align: center">⁂</div>

[^1]: C-spirit-ontology-overall-plan-by-GPT-03-Possible-Python-scripts.md

