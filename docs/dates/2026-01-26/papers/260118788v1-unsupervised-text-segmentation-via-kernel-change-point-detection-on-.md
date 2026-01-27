---
layout: default
title: Unsupervised Text Segmentation via Kernel Change-Point Detection on Sentence Embeddings
---

# Unsupervised Text Segmentation via Kernel Change-Point Detection on Sentence Embeddings
**arXiv**：[2601.18788v1](https://arxiv.org/abs/2601.18788) · [PDF](https://arxiv.org/pdf/2601.18788.pdf)  
**作者**：Mumin Jia, Jairo Diaz-Rodriguez  

**一句话要点**：提出Embed-KCPD方法，通过核变化点检测句子嵌入实现无监督文本分割。

**关键词**：无监督文本分割, 核变化点检测, 句子嵌入, 有限记忆依赖, 理论保证, 模拟验证

## 3 点简述
- 无监督文本分割因边界标签昂贵、主观且跨域迁移难而具挑战性。
- 方法基于句子嵌入，最小化惩罚核变化点检测目标以估计边界，无需训练。
- 在标准基准测试中常优于强无监督基线，并通过案例验证实用性。

## 摘要（原文）

> Unsupervised text segmentation is crucial because boundary labels are expensive, subjective, and often fail to transfer across domains and granularity choices. We propose Embed-KCPD, a training-free method that represents sentences as embedding vectors and estimates boundaries by minimizing a penalized KCPD objective. Beyond the algorithmic instantiation, we develop, to our knowledge, the first dependence-aware theory for KCPD under $m$-dependent sequences, a finite-memory abstraction of short-range dependence common in language. We prove an oracle inequality for the population penalized risk and a localization guarantee showing that each true change point is recovered within a window that is small relative to segment length. To connect theory to practice, we introduce an LLM-based simulation framework that generates synthetic documents with controlled finite-memory dependence and known boundaries, validating the predicted scaling behavior. Across standard segmentation benchmarks, Embed-KCPD often outperforms strong unsupervised baselines. A case study on Taylor Swift's tweets illustrates that Embed-KCPD combines strong theoretical guarantees, simulated reliability, and practical effectiveness for text segmentation.

