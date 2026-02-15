---
layout: default
title: SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization
---

# SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization
**arXiv**：[2602.12187v1](https://arxiv.org/abs/2602.12187) · [PDF](https://arxiv.org/pdf/2602.12187.pdf)  
**作者**：Sunghwan Kim, Wooseok Jeong, Serin Kim, Sangam Lee, Dongha Lee  

**一句话要点**：提出SAGEO Arena以解决搜索增强生成引擎优化缺乏现实评估环境的问题

**关键词**：搜索增强生成引擎优化, 评估环境, 文档结构信息, 端到端可见性, 生成搜索管道, 阶段级分析

## 3 点简述
- 核心问题：现有基准无法全面评估SAGEO，缺乏端到端可见性分析和真实文档结构信息。
- 方法要点：集成大规模网络文档和结构信息的完整生成搜索管道，支持阶段级SAGEO分析。
- 实验或效果：发现现有方法在现实条件下不实用，结构信息有助于缓解限制，需针对各阶段优化。

## 摘要（原文）

> Search-Augmented Generative Engines (SAGE) have emerged as a new paradigm for information access, bridging web-scale retrieval with generative capabilities to deliver synthesized answers. This shift has fundamentally reshaped how web content gains exposure online, giving rise to Search-Augmented Generative Engine Optimization (SAGEO), the practice of optimizing web documents to improve their visibility in AI-generated responses. Despite growing interest, no evaluation environment currently supports comprehensive investigation of SAGEO. Specifically, existing benchmarks lack end-to-end visibility evaluation of optimization strategies, operating on pre-determined candidate documents that abstract away retrieval and reranking preceding generation. Moreover, existing benchmarks discard structural information (e.g., schema markup) present in real web documents, overlooking the rich signals that search systems actively leverage in practice. Motivated by these gaps, we introduce SAGEO Arena, a realistic and reproducible environment for stage-level SAGEO analysis. Our objective is to jointly target search-oriented optimization (SEO) and generation-centric optimization (GEO). To achieve this, we integrate a full generative search pipeline over a large-scale corpus of web documents with rich structural information. Our findings reveal that existing approaches remain largely impractical under realistic conditions and often degrade performance in retrieval and reranking. We also find that structural information helps mitigate these limitations, and that effective SAGEO requires tailoring optimization to each pipeline stage. Overall, our benchmark paves the way for realistic SAGEO evaluation and optimization beyond simplified settings.

