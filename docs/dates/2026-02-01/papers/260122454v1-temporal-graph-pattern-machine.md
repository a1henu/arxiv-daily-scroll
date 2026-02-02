---
layout: default
title: Temporal Graph Pattern Machine
---

# Temporal Graph Pattern Machine
**arXiv**：[2601.22454v1](https://arxiv.org/abs/2601.22454) · [PDF](https://arxiv.org/pdf/2601.22454.pdf)  
**作者**：Yijun Ma, Zehong Wang, Weixiang Sun, Yanfang Ye  

**一句话要点**：提出Temporal Graph Pattern Machine以解决动态图学习中可迁移演化模式建模问题

**关键词**：时序图学习, 演化模式建模, 自监督预训练, 链接预测, 跨域迁移

## 3 点简述
- 核心问题：现有方法依赖短期依赖、静态邻域语义等限制性假设，阻碍可迁移演化机制的发现。
- 方法要点：通过时间偏置随机游走合成交互补丁，捕获多尺度结构和长程依赖，使用Transformer骨干学习全局时间规律。
- 实验或效果：在转导和归纳链接预测中实现最先进性能，展示卓越的跨域可迁移性。

## 摘要（原文）

> Temporal graph learning is pivotal for deciphering dynamic systems, where the core challenge lies in explicitly modeling the underlying evolving patterns that govern network transformation. However, prevailing methods are predominantly task-centric and rely on restrictive assumptions -- such as short-term dependency modeling, static neighborhood semantics, and retrospective time usage. These constraints hinder the discovery of transferable temporal evolution mechanisms. To address this, we propose the Temporal Graph Pattern Machine (TGPM), a foundation framework that shifts the focus toward directly learning generalized evolving patterns. TGPM conceptualizes each interaction as an interaction patch synthesized via temporally-biased random walks, thereby capturing multi-scale structural semantics and long-range dependencies that extend beyond immediate neighborhoods. These patches are processed by a Transformer-based backbone designed to capture global temporal regularities while adapting to context-specific interaction dynamics. To further empower the model, we introduce a suite of self-supervised pre-training tasks -- specifically masked token modeling and next-time prediction -- to explicitly encode the fundamental laws of network evolution. Extensive experiments show that TGPM consistently achieves state-of-the-art performance in both transductive and inductive link prediction, demonstrating exceptional cross-domain transferability.

