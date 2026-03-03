---
layout: default
title: GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation
---

# GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation
**arXiv**：[2603.01783v1](https://arxiv.org/abs/2603.01783) · [PDF](https://arxiv.org/pdf/2603.01783.pdf)  
**作者**：Yifan Wang, Mingxuan Jiang, Zhihao Sun, Yixin Cao, Yicun Liu, Keyang Chen, Guangnan Ye, Hongfeng Chai  

**一句话要点**：提出GAM-RAG框架，通过增益自适应记忆解决检索增强生成中静态索引导致的重复计算问题。

**关键词**：检索增强生成, 自适应记忆, 分层索引, 增益规则, 推理优化

## 3 点简述
- 核心问题：RAG依赖静态索引，相关查询重复多跳遍历，增加延迟和计算成本。
- 方法要点：构建轻量级无关系分层索引，基于检索反馈更新句子记忆，引入不确定性感知增益规则平衡稳定性和适应性。
- 实验或效果：平均性能提升3.95%，5轮记忆下提升8.19%，推理成本降低61%。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) grounds large language models with external evidence, but many implementations rely on pre-built indices that remain static after construction. Related queries therefore repeat similar multi-hop traversal, increasing latency and compute. Motivated by schema-based learning in cognitive neuroscience, we propose GAM-RAG, a training-free framework that accumulates retrieval experience from recurring or related queries and updates retrieval memory over time. GAM-RAG builds a lightweight, relation-free hierarchical index whose links capture potential co-occurrence rather than fixed semantic relations. During inference, successful retrieval episodes provide sentence-level feedback, updating sentence memories so evidence useful for similar reasoning types becomes easier to activate later. To balance stability and adaptability under noisy feedback, we introduce an uncertainty-aware, Kalman-inspired gain rule that jointly updates memory states and perplexity-based uncertainty estimates. It applies fast updates for reliable novel signals and conservative refinement for stable or noisy memories. We provide a theoretical analysis of the update dynamics, and empirically show that GAM-RAG improves average performance by 3.95% over the strongest baseline and by 8.19% with 5-turn memory, while reducing inference cost by 61%. Our code and datasets are available at: https://anonymous.4open.science/r/GAM_RAG-2EF6.

