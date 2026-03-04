---
layout: default
title: Retrievit: In-context Retrieval Capabilities of Transformers, State Space Models, and Hybrid Architectures
---

# Retrievit: In-context Retrieval Capabilities of Transformers, State Space Models, and Hybrid Architectures
**arXiv**：[2603.02874v1](https://arxiv.org/abs/2603.02874) · [PDF](https://arxiv.org/pdf/2603.02874.pdf)  
**作者**：Georgios Pantazopoulos, Malvina Nikandrou, Ioannis Konstas, Alessandro Suglia  

**一句话要点**：研究Transformer、SSM及混合架构在上下文检索任务中的性能差异与表示特性

**关键词**：上下文检索, Transformer架构, 状态空间模型, 混合模型, 表示分析, 位置关联学习

## 3 点简述
- 核心问题：Transformer二次复杂度高，SSM检索能力有限，混合架构能否结合优势
- 方法要点：在n-gram检索和位置检索任务上评估数据效率、长度泛化及表示学习
- 实验或效果：混合模型在信息密集检索中优于SSM，匹配或超越Transformer，但Transformer在位置检索中仍占优

## 摘要（原文）

> Transformers excel at in-context retrieval but suffer from quadratic complexity with sequence length, while State Space Models (SSMs) offer efficient linear-time processing but have limited retrieval capabilities. We investigate whether hybrid architectures combining Transformers and SSMs can achieve the best of both worlds on two synthetic in-context retrieval tasks. The first task, n-gram retrieval, requires the model to identify and reproduce an n-gram that succeeds the query within the input sequence. The second task, position retrieval, presents the model with a single query token and requires it to perform a two-hop associative lookup: first locating the corresponding element in the sequence, and then outputting its positional index. Under controlled experimental conditions, we assess data efficiency, length generalization, robustness to out of domain training examples, and learned representations across Transformers, SSMs, and hybrid architectures. We find that hybrid models outperform SSMs and match or exceed Transformers in data efficiency and extrapolation for information-dense context retrieval. However, Transformers maintain superiority in position retrieval tasks. Through representation analysis, we discover that SSM-based models develop locality-aware embeddings where tokens representing adjacent positions become neighbors in embedding space, forming interpretable structures. This emergent property, absent in Transformers, explains both the strengths and limitations of SSMs and hybrids for different retrieval tasks. Our findings provide principled guidance for architecture selection based on task requirements and reveal fundamental differences in how Transformers and SSMs, and hybrid models learn positional associations.

