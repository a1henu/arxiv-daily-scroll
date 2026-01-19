---
layout: default
title: Learn Before Represent: Bridging Generative and Contrastive Learning for Domain-Specific LLM Embeddings
---

# Learn Before Represent: Bridging Generative and Contrastive Learning for Domain-Specific LLM Embeddings
**arXiv**：[2601.11124v1](https://arxiv.org/abs/2601.11124) · [PDF](https://arxiv.org/pdf/2601.11124.pdf)  
**作者**：Xiaoyu Liang, Yuchen Peng, Jiale Luo, Wenhao Wang, Haoji Hu, Xincheng Zhou  

**一句话要点**：提出Learn Before Represent框架，通过两阶段学习解决垂直领域LLM嵌入的知识获取与对齐问题。

**关键词**：领域特定嵌入, 生成学习, 对比学习, 信息瓶颈, 垂直领域检索, LLM优化

## 3 点简述
- 核心问题：LLM+对比学习范式在化学、法律等垂直领域因缺乏领域知识而表现不佳，无法处理专业术语。
- 方法要点：LBR采用两阶段框架，先通过信息瓶颈约束的生成学习注入知识，再在压缩表示上进行生成精炼的对比学习以实现对齐。
- 实验或效果：在医疗、化学和代码检索任务上，LBR显著超越基线，建立了垂直领域准确鲁棒表示的新范式。

## 摘要（原文）

> Large Language Models (LLMs) adapted via contrastive learning excel in general representation learning but struggle in vertical domains like chemistry and law, primarily due to a lack of domain-specific knowledge. This work identifies a core bottleneck: the prevailing ``LLM+CL'' paradigm focuses on semantic alignment but cannot perform knowledge acquisition, leading to failures on specialized terminology. To bridge this gap, we propose Learn Before Represent (LBR), a novel two-stage framework. LBR first injects domain knowledge via an Information Bottleneck-Constrained Generative Learning stage, preserving the LLM's causal attention to maximize knowledge acquisition while compressing semantics. It then performs Generative-Refined Contrastive Learning on the compressed representations for alignment. This approach maintains architectural consistency and resolves the objective conflict between generative and contrastive learning. Extensive experiments on medical, chemistry, and code retrieval tasks show that LBR significantly outperforms strong baselines. Our work establishes a new paradigm for building accurate and robust representations in vertical domains.

