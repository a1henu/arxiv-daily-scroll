---
layout: default
title: HELP: HyperNode Expansion and Logical Path-Guided Evidence Localization for Accurate and Efficient GraphRAG
---

# HELP: HyperNode Expansion and Logical Path-Guided Evidence Localization for Accurate and Efficient GraphRAG
**arXiv**：[2602.20926v1](https://arxiv.org/abs/2602.20926) · [PDF](https://arxiv.org/pdf/2602.20926.pdf)  
**作者**：Yuqi Huang, Ning Liao, Kai Yang, Anning Hu, Shengchao Hu, Xiaoxing Wang, Junchi Yan  

**一句话要点**：提出HELP框架以平衡图增强检索生成中的准确性与效率

**关键词**：图增强检索生成, 多跳推理, 超节点扩展, 证据定位, 检索效率优化, 知识完整性

## 3 点简述
- 核心问题：图增强检索生成在准确性与效率间存在权衡，受限于图遍历成本和语义噪声
- 方法要点：采用超节点扩展构建推理路径，逻辑路径引导证据定位提升检索效率
- 实验或效果：在问答基准测试中表现竞争性，相比基线实现高达28.8倍加速

## 摘要（原文）

> Large Language Models (LLMs) often struggle with inherent knowledge boundaries and hallucinations, limiting their reliability in knowledge-intensive tasks. While Retrieval-Augmented Generation (RAG) mitigates these issues, it frequently overlooks structural interdependencies essential for multi-hop reasoning. Graph-based RAG approaches attempt to bridge this gap, yet they typically face trade-offs between accuracy and efficiency due to challenges such as costly graph traversals and semantic noise in LLM-generated summaries. In this paper, we propose HyperNode Expansion and Logical Path-Guided Evidence Localization strategies for GraphRAG (HELP), a novel framework designed to balance accuracy with practical efficiency through two core strategies: 1) HyperNode Expansion, which iteratively chains knowledge triplets into coherent reasoning paths abstracted as HyperNodes to capture complex structural dependencies and ensure retrieval accuracy; and 2) Logical Path-Guided Evidence Localization, which leverages precomputed graph-text correlations to map these paths directly to the corpus for superior efficiency. HELP avoids expensive random walks and semantic distortion, preserving knowledge integrity while drastically reducing retrieval latency. Extensive experiments demonstrate that HELP achieves competitive performance across multiple simple and multi-hop QA benchmarks and up to a 28.8$\times$ speedup over leading Graph-based RAG baselines.

