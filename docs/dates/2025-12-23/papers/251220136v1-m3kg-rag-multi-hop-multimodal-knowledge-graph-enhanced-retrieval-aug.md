---
layout: default
title: M$^3$KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation
---

# M$^3$KG-RAG: Multi-hop Multimodal Knowledge Graph-enhanced Retrieval-Augmented Generation
**arXiv**：[2512.20136v1](https://arxiv.org/abs/2512.20136) · [PDF](https://arxiv.org/pdf/2512.20136.pdf)  
**作者**：Hyeongcheol Park, Jiyoung Seo, Jaewon Mun, Hogun Park, Wonmin Byeon, Sung June Kim, Hyeonsoo Im, JeungSub Lee, Sangpil Kim  

**一句话要点**：提出M³KG-RAG以解决视听领域多模态检索增强生成中的模态覆盖不足与检索不精确问题。

**关键词**：多模态检索增强生成, 多跳知识图谱, 视听知识检索, 实体对齐, 冗余剪枝, 多模态推理

## 3 点简述
- 核心问题：现有多模态知识图谱在视听领域模态覆盖有限且多跳连接不足，检索仅依赖嵌入空间相似性易引入无关或冗余知识。
- 方法要点：设计轻量级多智能体管道构建多跳多模态知识图谱，并引入GRASP机制进行实体对齐、相关性评估与冗余剪枝。
- 实验或效果：在多样化多模态基准测试中显著提升多模态大语言模型的多模态推理与基础能力。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has recently been extended to multimodal settings, connecting multimodal large language models (MLLMs) with vast corpora of external knowledge such as multimodal knowledge graphs (MMKGs). Despite their recent success, multimodal RAG in the audio-visual domain remains challenging due to 1) limited modality coverage and multi-hop connectivity of existing MMKGs, and 2) retrieval based solely on similarity in a shared multimodal embedding space, which fails to filter out off-topic or redundant knowledge. To address these limitations, we propose M$^3$KG-RAG, a Multi-hop Multimodal Knowledge Graph-enhanced RAG that retrieves query-aligned audio-visual knowledge from MMKGs, improving reasoning depth and answer faithfulness in MLLMs. Specifically, we devise a lightweight multi-agent pipeline to construct multi-hop MMKG (M$^3$KG), which contains context-enriched triplets of multimodal entities, enabling modality-wise retrieval based on input queries. Furthermore, we introduce GRASP (Grounded Retrieval And Selective Pruning), which ensures precise entity grounding to the query, evaluates answer-supporting relevance, and prunes redundant context to retain only knowledge essential for response generation. Extensive experiments across diverse multimodal benchmarks demonstrate that M$^3$KG-RAG significantly enhances MLLMs' multimodal reasoning and grounding over existing approaches.

