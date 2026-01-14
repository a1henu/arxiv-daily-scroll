---
layout: default
title: MemRec: Collaborative Memory-Augmented Agentic Recommender System
---

# MemRec: Collaborative Memory-Augmented Agentic Recommender System
**arXiv**：[2601.08816v1](https://arxiv.org/abs/2601.08816) · [PDF](https://arxiv.org/pdf/2601.08816.pdf)  
**作者**：Weixin Chen, Yuhan Zhao, Jingyuan Huang, Zihe Ye, Clark Mingxuan Ju, Tong Zhao, Neil Shah, Li Chen, Yongfeng Zhang  

**一句话要点**：提出MemRec框架以解决推荐系统中协作记忆增强的效率和认知负载问题

**关键词**：协作记忆增强, 推荐系统, 图上下文蒸馏, 异步图传播, 智能体架构, 本地开源模型

## 3 点简述
- 核心问题：现有智能体依赖孤立记忆，忽略协作信号，且处理图上下文时面临认知负载和计算成本挑战
- 方法要点：通过架构解耦，引入LM_Mem管理动态协作记忆图，为下游LLM_Rec提供高信号上下文，支持异步图传播
- 实验或效果：在四个基准测试中实现最先进性能，架构分析显示其灵活性，平衡推理质量、成本和隐私

## 摘要（原文）

> The evolution of recommender systems has shifted preference storage from rating matrices and dense embeddings to semantic memory in the agentic era. Yet existing agents rely on isolated memory, overlooking crucial collaborative signals. Bridging this gap is hindered by the dual challenges of distilling vast graph contexts without overwhelming reasoning agents with cognitive load, and evolving the collaborative memory efficiently without incurring prohibitive computational costs. To address this, we propose MemRec, a framework that architecturally decouples reasoning from memory management to enable efficient collaborative augmentation. MemRec introduces a dedicated, cost-effective LM_Mem to manage a dynamic collaborative memory graph, serving synthesized, high-signal context to a downstream LLM_Rec. The framework operates via a practical pipeline featuring efficient retrieval and cost-effective asynchronous graph propagation that evolves memory in the background. Extensive experiments on four benchmarks demonstrate that MemRec achieves state-of-the-art performance. Furthermore, architectural analysis confirms its flexibility, establishing a new Pareto frontier that balances reasoning quality, cost, and privacy through support for diverse deployments, including local open-source models. Code:https://github.com/rutgerswiselab/memrec and Homepage: https://memrec.weixinchen.com

