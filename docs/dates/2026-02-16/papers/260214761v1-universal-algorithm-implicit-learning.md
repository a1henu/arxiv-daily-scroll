---
layout: default
title: Universal Algorithm-Implicit Learning
---

# Universal Algorithm-Implicit Learning
**arXiv**：[2602.14761v1](https://arxiv.org/abs/2602.14761) · [PDF](https://arxiv.org/pdf/2602.14761.pdf)  
**作者**：Stefano Woerner, Seong Joon Oh, Christian F. Baumgartner  

**一句话要点**：提出TAIL算法隐式元学习框架，解决元学习任务分布窄和术语不一致问题，实现跨域跨模态泛化。

**关键词**：元学习框架, 算法隐式学习, 跨模态泛化, Transformer元学习, 少样本学习, 计算效率优化

## 3 点简述
- 核心问题：当前元学习方法局限于固定特征和标签空间，且术语定义不精确，影响应用和比较。
- 方法要点：引入理论框架定义实用通用性，区分算法显式和隐式学习，并基于Transformer设计TAIL，采用随机投影和标签嵌入等创新。
- 实验或效果：TAIL在少样本基准上达到SOTA，能泛化到未见域和模态，处理更多类别，计算效率大幅提升。

## 摘要（原文）

> Current meta-learning methods are constrained to narrow task distributions with fixed feature and label spaces, limiting applicability. Moreover, the current meta-learning literature uses key terms like "universal" and "general-purpose" inconsistently and lacks precise definitions, hindering comparability. We introduce a theoretical framework for meta-learning which formally defines practical universality and introduces a distinction between algorithm-explicit and algorithm-implicit learning, providing a principled vocabulary for reasoning about universal meta-learning methods. Guided by this framework, we present TAIL, a transformer-based algorithm-implicit meta-learner that functions across tasks with varying domains, modalities, and label configurations. TAIL features three innovations over prior transformer-based meta-learners: random projections for cross-modal feature encoding, random injection label embeddings that extrapolate to larger label spaces, and efficient inline query processing. TAIL achieves state-of-the-art performance on standard few-shot benchmarks while generalizing to unseen domains. Unlike other meta-learning methods, it also generalizes to unseen modalities, solving text classification tasks despite training exclusively on images, handles tasks with up to 20$\times$ more classes than seen during training, and provides orders-of-magnitude computational savings over prior transformer-based approaches.

