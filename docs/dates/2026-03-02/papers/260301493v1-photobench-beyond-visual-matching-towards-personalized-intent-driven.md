---
layout: default
title: PhotoBench: Beyond Visual Matching Towards Personalized Intent-Driven Photo Retrieval
---

# PhotoBench: Beyond Visual Matching Towards Personalized Intent-Driven Photo Retrieval
**arXiv**：[2603.01493v1](https://arxiv.org/abs/2603.01493) · [PDF](https://arxiv.org/pdf/2603.01493.pdf)  
**作者**：Tianyi Xu, Rong Shan, Junjie Wu, Jiadeng Huang, Teng Wang, Jiachen Zhu, Wenteng Chen, Minxin Tu, Quantao Dou, Zhaoxiang Wang, Changwang Zhang, Weinan Zhang, Jun Wang, Jianghao Lin  

**一句话要点**：提出PhotoBench基准以解决个性化意图驱动照片检索中的多源推理问题

**关键词**：个性化照片检索, 多源推理基准, 意图驱动查询, 模态鸿沟, 智能体系统, 照片相册分析

## 3 点简述
- 核心问题：现有检索基准依赖孤立网络快照，无法捕捉真实用户查询所需的多源推理
- 方法要点：基于真实个人相册构建基准，集成视觉语义、时空元数据、社交身份和事件进行多源分析
- 实验或效果：评估揭示模态鸿沟和源融合悖论，表明需超越统一嵌入的智能体推理系统

## 摘要（原文）

> Personal photo albums are not merely collections of static images but living, ecological archives defined by temporal continuity, social entanglement, and rich metadata, which makes the personalized photo retrieval non-trivial. However, existing retrieval benchmarks rely heavily on context-isolated web snapshots, failing to capture the multi-source reasoning required to resolve authentic, intent-driven user queries. To bridge this gap, we introduce PhotoBench, the first benchmark constructed from authentic, personal albums. It is designed to shift the paradigm from visual matching to personalized multi-source intent-driven reasoning. Based on a rigorous multi-source profiling framework, which integrates visual semantics, spatial-temporal metadata, social identity, and temporal events for each image, we synthesize complex intent-driven queries rooted in users' life trajectories. Extensive evaluation on PhotoBench exposes two critical limitations: the modality gap, where unified embedding models collapse on non-visual constraints, and the source fusion paradox, where agentic systems perform poor tool orchestration. These findings indicate that the next frontier in personal multimodal retrieval lies beyond unified embeddings, necessitating robust agentic reasoning systems capable of precise constraint satisfaction and multi-source fusion. Our PhotoBench is available.

