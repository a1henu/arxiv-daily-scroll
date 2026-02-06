---
layout: default
title: Limitations of SGD for Multi-Index Models Beyond Statistical Queries
---

# Limitations of SGD for Multi-Index Models Beyond Statistical Queries
**arXiv**：[2602.05704v1](https://arxiv.org/abs/2602.05704) · [PDF](https://arxiv.org/pdf/2602.05704.pdf)  
**作者**：Daniel Barzilai, Ohad Shamir  

**一句话要点**：提出非统计查询框架以分析标准SGD在单索引与多索引模型中的局限性

**关键词**：随机梯度下降, 多索引模型, 学习理论, 神经网络, 统计查询框架

## 3 点简述
- 核心问题：现有统计查询框架与SGD关联薄弱，可能导致错误预测
- 方法要点：开发新非统计查询框架，适用于标准SGD，涵盖神经网络等架构
- 实验或效果：未知，论文未提及具体实验或效果

## 摘要（原文）

> Understanding the limitations of gradient methods, and stochastic gradient descent (SGD) in particular, is a central challenge in learning theory. To that end, a commonly used tool is the Statistical Queries (SQ) framework, which studies performance limits of algorithms based on noisy interaction with the data. However, it is known that the formal connection between the SQ framework and SGD is tenuous: Existing results typically rely on adversarial or specially-structured gradient noise that does not reflect the noise in standard SGD, and (as we point out here) can sometimes lead to incorrect predictions. Moreover, many analyses of SGD for challenging problems rely on non-trivial algorithmic modifications, such as restricting the SGD trajectory to the sphere or using very small learning rates. To address these shortcomings, we develop a new, non-SQ framework to study the limitations of standard vanilla SGD, for single-index and multi-index models (namely, when the target function depends on a low-dimensional projection of the inputs). Our results apply to a broad class of settings and architectures, including (potentially deep) neural networks.

