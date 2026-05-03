# HippoRAG Implementation Project - Context File

## Project Overview

**Goal**: Faithful technical implementation of HippoRAG, a retrieval-augmented generation system grounded in a knowledge graph (KG) architecture.

**Scope**: Both HippoRAG v1 (NeurIPS 2024) and v2 (ICML 2025), with attention to how v2 addressed v1's weaknesses in factual QA performance.

**Success Criteria**: Correctly reproducing the core pipeline components and achieving expected benchmark-range behavior.

---

## Project Status

### Current State
Actively working through the methodology details of HippoRAG, having focused on:
- KG construction
- Personalized PageRank (PPR)
- Node/passage linking

### Completed Analysis
- Understanding of pipeline phases: Offline indexing → Online retrieval
- KG construction methodology (Two-step NER → OpenIE prompting structure)
- PPR configuration and implementation details
- Synonym edge threshold determination
- Passage-node weight factor identification
- Top-k triple retrieval configuration
- v2-specific query-to-triple linking mechanism

---

## Implementation Details Established

### Core Parameters
- **Damping factor (PPR)**: 0.5
- **PPR Implementation**: `python-igraph` (used in v2)
- **Synonym edge threshold (τ)**: 0.8
- **Passage-node weight factor**: 0.05
- **Top-k triple retrieval**: 5

### Pipeline Architecture

#### Offline Indexing Phase
1. **NER (Named Entity Recognition)**
   - Two-step process
   - Entity extraction from corpus

2. **OpenIE (Open Information Extraction)**
   - Prompting structure for triple extraction
   - Knowledge graph construction

3. **Knowledge Graph Construction**
   - Nodes: Named entities
   - Edges: Relations between entities
   - Synonym edges with threshold τ = 0.8

#### Online Retrieval Phase
1. **Query Processing**
   - Query-to-triple linking (v2-specific)
   - Entity and relation extraction from query

2. **PPR (Personalized PageRank)**
   - Damping factor: 0.5
   - Graph traversal starting from query entities

3. **Triple Retrieval**
   - Top-k = 5 triples
   - Passage-node weighting: 0.05

4. **LLM-based Filtering (v2)**
   - Triple filtering via "recognition memory"
   - Prompt located in v2 Appendix A (Figure 4)

---

## Key Differences: v1 vs v2

### v2 Improvements Over v1
1. **Query-to-triple linking mechanism**
   - Better handles complex queries
   - Improved entity grounding

2. **LLM-based triple filtering**
   - "Recognition memory" component
   - Reduces noise in retrieved triples
   - Improves factual QA performance

3. **Enhanced prompting structure**
   - Specific prompt in Appendix A, Figure 4
   - More structured filtering logic

---

## Technical Resources

### Source Papers
- **HippoRAG v1**: Gutiérrez et al., NeurIPS 2024
- **HippoRAG v2**: Jiménez Gutiérrez et al., ICML 2025

### Key Sections to Reference
- **v2 Appendix A, Figure 4**: Triple filter prompt (NOT in main paper)
- **Methodology sections**: Both v1 and v2 for comparison

### Implementation Tools
- `python-igraph` for PPR implementation
- Standard NER tools (to be determined)
- OpenIE framework (to be determined)
- LLM API for triple filtering (to be determined)

---

## Open Questions & Next Steps

### Follow-up Directions
1. **Extract exact triple-filter prompt**
   - Location: v2 Appendix A, Figure 4
   - Needed for faithful v2 implementation

2. **Formalize PPR mathematics**
   - Mathematical formulation
   - Implementation pseudocode
   - Edge case handling

3. **Module-by-module code structure**
   - Sketch overall architecture
   - Define interfaces between components
   - Plan data flow

4. **Compute and cost analysis**
   - Compare v1 vs v2 resource requirements
   - Estimate API costs for LLM components
   - Benchmark compute requirements

### Validation Checkpoints
- **KG scale benchmarks**: Needed for sanity-checking implementation correctness
- **Retrieval quality metrics**: Compare against paper baselines
- **End-to-end QA performance**: Verify benchmark-range behavior

---

## Implementation Roadmap (Proposed)

### Phase 1: Offline Indexing Pipeline
1. Set up corpus processing
2. Implement NER component
3. Implement OpenIE prompting
4. Build KG construction module
5. Validate KG against expected scale/structure

### Phase 2: Online Retrieval Pipeline
1. Implement query processing
2. Build PPR module with `python-igraph`
3. Implement triple retrieval
4. Add passage-node linking
5. Test retrieval quality

### Phase 3: v2 Enhancements
1. Add query-to-triple linking
2. Implement LLM-based triple filtering
3. Integrate filter prompt from Appendix A
4. Validate improvements over v1 baseline

### Phase 4: Evaluation & Optimization
1. Run benchmark datasets
2. Compare performance to paper results
3. Profile compute and cost
4. Optimize bottlenecks

---

## Notes for Claude Code Implementation

### Development Environment Setup
- Python environment with `python-igraph`
- LLM API access for triple filtering
- Access to benchmark datasets
- Sufficient storage for knowledge graphs

### Code Organization Suggestions
```
hipporag/
├── offline/
│   ├── ner.py
│   ├── openie.py
│   └── kg_builder.py
├── online/
│   ├── query_processor.py
│   ├── ppr.py
│   ├── triple_retriever.py
│   └── llm_filter.py (v2)
├── utils/
│   ├── graph_utils.py
│   └── prompts.py
├── config/
│   └── params.yaml
└── evaluation/
    ├── benchmarks.py
    └── metrics.py
```

### Testing Strategy
- Unit tests for each module
- Integration tests for pipeline
- Benchmark comparison tests
- Performance profiling

---

## Important Reminders

1. **Triple filter prompt location**: v2 Appendix A, Figure 4 (NOT in main paper body)
2. **PPR damping factor**: Must be exactly 0.5 for faithful reproduction
3. **Synonym threshold**: τ = 0.8 is critical for edge formation
4. **v2 is the target**: Focus on v2 implementation with v1 understanding as foundation
5. **Validation is key**: KG scale benchmarks needed to confirm correctness

---

## Research Assistant Guidelines

When working in Claude Code, remember to:
- Ask clarifying questions about implementation choices
- Provide balanced perspectives on architectural decisions
- Suggest evidence-based approaches from the papers
- Guide through debugging rather than just providing solutions
- Help develop critical thinking about design tradeoffs
- Maintain focus on faithful reproduction while noting opportunities for improvements

---

## Document Version
**Created**: 2026-05-02  
**Last Updated**: 2026-05-02  
**Status**: Initial transfer to Claude Code environment

---

## Additional Resources Needed

### From Papers
- [ ] Extract complete triple filter prompt (v2 Appendix A, Figure 4)
- [ ] Document complete PPR formulation
- [ ] List all hyperparameters with justifications
- [ ] Identify benchmark datasets used in evaluation

### For Implementation
- [ ] Choose specific NER library/model
- [ ] Choose specific OpenIE approach
- [ ] Determine LLM API provider for filtering
- [ ] Set up development environment
- [ ] Acquire benchmark datasets

### For Validation
- [ ] Define expected KG scale metrics
- [ ] Set retrieval quality thresholds
- [ ] Establish performance baselines
- [ ] Plan ablation studies

---

*This context file provides a comprehensive snapshot of the HippoRAG implementation project. Use it to maintain consistency across development sessions and to quickly onboard into the technical details when working in Claude Code on VS Code.*
