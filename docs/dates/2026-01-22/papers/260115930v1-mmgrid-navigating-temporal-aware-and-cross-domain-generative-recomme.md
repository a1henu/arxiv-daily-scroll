---
layout: default
title: MMGRid: Navigating Temporal-aware and Cross-domain Generative Recommendation via Model Merging
---

# MMGRid: Navigating Temporal-aware and Cross-domain Generative Recommendation via Model Merging
**arXiv**：[2601.15930v1](https://arxiv.org/abs/2601.15930) · [PDF](https://arxiv.org/pdf/2601.15930.pdf)  
**作者**：Tianjun Wei, Enneng Yang, Yingpeng Du, Huizhong Guo, Jie Zhang, Zhu Sun  

**一句话要点**：提出MMGRid框架，通过模型合并解决生成式推荐中跨时间和跨领域的上下文适应问题。

**关键词**：生成式推荐, 模型合并, 上下文适应, 时间演化, 跨领域推荐, 参数冲突

## 3 点简述
- 核心问题：生成式推荐模型在时间演化和领域异构的上下文下难以高效合并，存在参数冲突和近期偏差。
- 方法要点：构建结构化上下文网格组织模型检查点，通过基础模型替换和加权合并来缓解冲突和平衡偏差。
- 实验或效果：发现合并权重与上下文交互特征相关，为实际部署提供权重选择指导，提升成本敏感场景的部署效率。

## 摘要（原文）

> Model merging (MM) offers an efficient mechanism for integrating multiple specialized models without access to original training data or costly retraining. While MM has demonstrated success in domains like computer vision, its role in recommender systems (RSs) remains largely unexplored. Recently, Generative Recommendation (GR) has emerged as a new paradigm in RSs, characterized by rapidly growing model scales and substantial computational costs, making MM particularly appealing for cost-sensitive deployment scenarios. In this work, we present the first systematic study of MM in GR through a contextual lens. We focus on a fundamental yet underexplored challenge in real-world: how to merge generative recommenders specialized to different real-world contexts, arising from temporal evolving user behaviors and heterogeneous application domains. To this end, we propose a unified framework MMGRid, a structured contextual grid of GR checkpoints that organizes models trained under diverse contexts induced by temporal evolution and domain diversity. All checkpoints are derived from a shared base LLM but fine-tuned on context-specific data, forming a realistic and controlled model space for systematically analyzing MM across GR paradigms and merging algorithms. Our investigation reveals several key insights. First, training GR models from LLMs can introduce parameter conflicts during merging due to token distribution shifts and objective disparities; such conflicts can be alleviated by disentangling task-aware and context-specific parameter changes via base model replacement. Second, incremental training across contexts induces recency bias, which can be effectively balanced through weighted contextual merging. Notably, we observe that optimal merging weights correlate with context-dependent interaction characteristics, offering practical guidance for weight selection in real-world deployments.

