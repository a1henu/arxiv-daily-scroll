---
layout: default
title: E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory
---

# E-mem: Multi-agent based Episodic Context Reconstruction for LLM Agent Memory
**arXiv**：[2601.21714v1](https://arxiv.org/abs/2601.21714) · [PDF](https://arxiv.org/pdf/2601.21714.pdf)  
**作者**：Kaixiang Wang, Yidan Lin, Jiong Lou, Zhaojiacheng Zhou, Bunyod Suvonov, Jie Li  

**一句话要点**：提出E-mem框架，通过多智能体情景重建解决LLM智能体记忆中的上下文破坏问题。

**关键词**：LLM智能体记忆, 情景重建, 多智能体系统, 长序列推理, 记忆预处理

## 3 点简述
- 核心问题：现有记忆预处理方法压缩序列依赖，破坏上下文完整性，影响深度推理。
- 方法要点：采用异构分层架构，多助理智能体维护未压缩记忆，主智能体协调全局规划。
- 实验或效果：在LoCoMo基准上F1超过54%，优于GAM 7.75%，令牌成本降低超70%。

## 摘要（原文）

> The evolution of Large Language Model (LLM) agents towards System~2 reasoning, characterized by deliberative, high-precision problem-solving, requires maintaining rigorous logical integrity over extended horizons. However, prevalent memory preprocessing paradigms suffer from destructive de-contextualization. By compressing complex sequential dependencies into pre-defined structures (e.g., embeddings or graphs), these methods sever the contextual integrity essential for deep reasoning. To address this, we propose E-mem, a framework shifting from Memory Preprocessing to Episodic Context Reconstruction. Inspired by biological engrams, E-mem employs a heterogeneous hierarchical architecture where multiple assistant agents maintain uncompressed memory contexts, while a central master agent orchestrates global planning. Unlike passive retrieval, our mechanism empowers assistants to locally reason within activated segments, extracting context-aware evidence before aggregation. Evaluations on the LoCoMo benchmark demonstrate that E-mem achieves over 54\% F1, surpassing the state-of-the-art GAM by 7.75\%, while reducing token cost by over 70\%.

