---
layout: default
title: Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems
---

# Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems
**arXiv**：[2601.10681v1](https://arxiv.org/abs/2601.10681) · [PDF](https://arxiv.org/pdf/2601.10681.pdf)  
**作者**：Amir Khurshid, Abhishek Sehgal  

**一句话要点**：提出结构感知与多样性约束的上下文气泡构建框架，以优化企业检索增强系统中的上下文生成。

**关键词**：检索增强生成, 上下文构建, 文档结构, 多样性约束, 企业检索, 可审计性

## 3 点简述
- 核心问题：传统RAG的top-k检索导致信息图碎片化、内容冗余和查询上下文不足。
- 方法要点：基于文档结构组织多粒度跨度，通过约束选择平衡相关性、覆盖度和冗余惩罚。
- 实验或效果：在企业文档上减少冗余上下文，提升次要方面覆盖和答案质量，支持可审计性。

## 摘要（原文）

> Large language model (LLM) contexts are typically constructed using retrieval-augmented generation (RAG), which involves ranking and selecting the top-k passages. The approach causes fragmentation in information graphs in document structures, over-retrieval, and duplication of content alongside insufficient query context, including 2nd and 3rd order facets. In this paper, a structure-informed and diversity-constrained context bubble construction framework is proposed that assembles coherent, citable bundles of spans under a strict token budget. The method preserves and exploits inherent document structure by organising multi-granular spans (e.g., sections and rows) and using task-conditioned structural priors to guide retrieval. Starting from high-relevance anchor spans, a context bubble is constructed through constrained selection that balances query relevance, marginal coverage, and redundancy penalties. It will explicitly constrain diversity and budget, producing compact and informative context sets, unlike top-k retrieval. Moreover, a full retrieval is emitted that traces the scoring and selection choices of the records, thus providing auditability and deterministic tuning. Experiments on enterprise documents demonstrate the efficiency of context bubble as it significantly reduces redundant context, is better able to cover secondary facets and has a better answer quality and citation faithfulness within a limited context window. Ablation studies demonstrate that both structural priors as well as diversity constraint selection are necessary; removing either component results in a decline in coverage and an increase in redundant or incomplete context.

