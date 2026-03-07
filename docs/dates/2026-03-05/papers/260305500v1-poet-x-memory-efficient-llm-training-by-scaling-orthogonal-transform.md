---
layout: default
title: POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
---

# POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation
**arXiv**：[2603.05500v1](https://arxiv.org/abs/2603.05500) · [PDF](https://arxiv.org/pdf/2603.05500.pdf)  
**作者**：Zeju Qiu, Lixin Liu, Adrian Weller, Han Shi, Weiyang Liu  

**一句话要点**：提出POET-X以解决大语言模型训练中的内存效率问题

**关键词**：大语言模型训练, 内存效率优化, 正交等价变换, 计算开销降低, 单GPU预训练

## 3 点简述
- 核心问题：大语言模型训练内存消耗高，标准优化器如AdamW在单GPU上易内存不足
- 方法要点：基于正交等价变换的POET-X，通过可扩展设计显著降低计算开销和内存使用
- 实验或效果：POET-X能在单Nvidia H100 GPU上预训练十亿参数模型，提升吞吐量和内存效率

## 摘要（原文）

> Efficient and stable training of large language models (LLMs) remains a core challenge in modern machine learning systems. To address this challenge, Reparameterized Orthogonal Equivalence Training (POET), a spectrum-preserving framework that optimizes each weight matrix through orthogonal equivalence transformation, has been proposed. Although POET provides strong training stability, its original implementation incurs high memory consumption and computational overhead due to intensive matrix multiplications. To overcome these limitations, we introduce POET-X, a scalable and memory-efficient variant that performs orthogonal equivalence transformations with significantly reduced computational cost. POET-X maintains the generalization and stability benefits of POET while achieving substantial improvements in throughput and memory efficiency. In our experiments, POET-X enables the pretraining of billion-parameter LLMs on a single Nvidia H100 GPU, and in contrast, standard optimizers such as AdamW run out of memory under the same settings.

