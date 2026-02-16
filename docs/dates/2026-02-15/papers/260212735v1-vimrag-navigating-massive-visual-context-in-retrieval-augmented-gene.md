---
layout: default
title: VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph
---

# VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph
**arXiv**：[2602.12735v1](https://arxiv.org/abs/2602.12735) · [PDF](https://arxiv.org/pdf/2602.12735.pdf)  
**作者**：Qiuchen Wang, Shihang Wang, Yu Zeng, Qiang Zhang, Fanrui Zhang, Zhuoning Guo, Bosi Zhang, Wenxuan Huang, Lin Chen, Zehui Chen, Pengjun Xie, Ruixue Ding  

**一句话要点**：提出VimRAG框架，通过多模态记忆图解决长上下文视觉检索增强生成中的推理挑战。

**关键词**：多模态检索增强生成, 视觉记忆图, 动态有向无环图, 图调制编码, 长上下文推理, 视觉数据压缩

## 3 点简述
- 核心问题：传统RAG方法依赖线性历史，难以处理信息稀疏但token密集的视觉数据在迭代推理中的长上下文任务。
- 方法要点：建模推理过程为动态有向无环图，引入图调制视觉记忆编码机制，基于拓扑位置动态分配高分辨率token至关键证据。
- 实验或效果：在多样化多模态RAG基准测试中实现最先进性能，代码已开源。

## 摘要（原文）

> Effectively retrieving, reasoning, and understanding multimodal information remains a critical challenge for agentic systems. Traditional Retrieval-augmented Generation (RAG) methods rely on linear interaction histories, which struggle to handle long-context tasks, especially those involving information-sparse yet token-heavy visual data in iterative reasoning scenarios. To bridge this gap, we introduce VimRAG, a framework tailored for multimodal Retrieval-augmented Reasoning across text, images, and videos. Inspired by our systematic study, we model the reasoning process as a dynamic directed acyclic graph that structures the agent states and retrieved multimodal evidence. Building upon this structured memory, we introduce a Graph-Modulated Visual Memory Encoding mechanism, with which the significance of memory nodes is evaluated via their topological position, allowing the model to dynamically allocate high-resolution tokens to pivotal evidence while compressing or discarding trivial clues. To implement this paradigm, we propose a Graph-Guided Policy Optimization strategy. This strategy disentangles step-wise validity from trajectory-level rewards by pruning memory nodes associated with redundant actions, thereby facilitating fine-grained credit assignment. Extensive experiments demonstrate that VimRAG consistently achieves state-of-the-art performance on diverse multimodal RAG benchmarks. The code is available at https://github.com/Alibaba-NLP/VRAG.

