---
layout: default
title: Self-Improvement as Coherence Optimization: A Theoretical Account
---

# Self-Improvement as Coherence Optimization: A Theoretical Account
**arXiv**：[2601.13566v1](https://arxiv.org/abs/2601.13566) · [PDF](https://arxiv.org/pdf/2601.13566.pdf)  
**作者**：Tianyi Qiu, Ahmed Hani Ismail, Zhonghao He, Shi Feng  

**一句话要点**：提出一致性优化理论，解释语言模型无监督自提升机制

**关键词**：语言模型自提升, 一致性优化, 无监督学习, 描述长度正则化, 理论分析

## 3 点简述
- 核心问题：语言模型无外部监督下自提升的理论基础不明
- 方法要点：将辩论、自举等方法统一为一致性优化，即寻找最可压缩和联合可预测的映射
- 实验或效果：理论证明一致性优化等价于描述长度正则化，初步实验支持其有效性

## 摘要（原文）

> Can language models improve their accuracy without external supervision? Methods such as debate, bootstrap, and internal coherence maximization achieve this surprising feat, even matching golden finetuning performance. Yet why they work remains theoretically unclear. We show that they are all special cases of coherence optimization: finding a context-to-behavior mapping that's most compressible and jointly predictable. We prove that coherence optimization is equivalent to description-length regularization, and that among all such regularization schemes, it is optimal for semi-supervised learning when the regularizer is derived from a pretrained model. Our theory, supported by preliminary experiments, explains why feedback-free self-improvement works and predicts when it should succeed or fail.

