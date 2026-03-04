---
layout: default
title: Specificity-aware reinforcement learning for fine-grained open-world classification
---

# Specificity-aware reinforcement learning for fine-grained open-world classification
**arXiv**：[2603.03197v1](https://arxiv.org/abs/2603.03197) · [PDF](https://arxiv.org/pdf/2603.03197.pdf)  
**作者**：Samuele Angheben, Davide Berasi, Alessandro Conti, Elisa Ricci, Yiming Wang  

**一句话要点**：提出SpeciaRL强化学习框架以优化开放世界细粒度图像分类中的预测特异性

**关键词**：开放世界分类, 细粒度视觉识别, 强化学习, 多模态模型, 特异性优化

## 3 点简述
- 核心问题：大型多模态模型在细粒度分类中预测过于泛化，需平衡正确性与特异性。
- 方法要点：引入基于验证器的动态奖励信号，通过在线rollouts引导模型生成更具体预测。
- 实验或效果：在开放世界细粒度基准测试中实现正确性与特异性的最佳权衡，超越现有方法。

## 摘要（原文）

> Classifying fine-grained visual concepts under open-world settings, i.e., without a predefined label set, demands models to be both accurate and specific. Recent reasoning Large Multimodal Models (LMMs) exhibit strong visual understanding capability but tend to produce overly generic predictions when performing fine-grained image classification. Our preliminary analysis reveals that models do possess the intrinsic fine-grained domain knowledge. However, promoting more specific predictions (specificity) without compromising correct ones (correctness) remains a non-trivial and understudied challenge. In this work, we investigate how to steer reasoning LMMs toward predictions that are both correct and specific. We propose a novel specificity-aware reinforcement learning framework, SpeciaRL, to fine-tune reasoning LMMs on fine-grained image classification under the open-world setting. SpeciaRL introduces a dynamic, verifier-based reward signal anchored to the best predictions within online rollouts, promoting specificity while respecting the model's capabilities to prevent incorrect predictions. Our out-of-domain experiments show that SpeciaRL delivers the best trade-off between correctness and specificity across extensive fine-grained benchmarks, surpassing existing methods and advancing open-world fine-grained image classification. Code and model are publicly available at https://github.com/s-angheben/SpeciaRL.

