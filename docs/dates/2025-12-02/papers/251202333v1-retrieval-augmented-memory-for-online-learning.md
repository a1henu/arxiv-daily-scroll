---
layout: default
title: Retrieval-Augmented Memory for Online Learning
---

# Retrieval-Augmented Memory for Online Learning
**arXiv**：[2512.02333v1](https://arxiv.org/abs/2512.02333) · [PDF](https://arxiv.org/pdf/2512.02333.pdf)  
**作者**：Wenzhang Du  

**一句话要点**：提出RAM-OL以增强在线学习在概念漂移环境下的性能

**关键词**：在线学习, 概念漂移, 检索增强记忆, 最近邻检索, 梯度下降扩展, 非平稳环境

## 3 点简述
- 研究在线分类在非平稳环境中的问题，概念漂移影响模型适应性
- 扩展SGD，维护小缓冲区，通过检索最近邻并联合更新模型来增强记忆
- 在强漂移数据流上提升预序准确率约7个百分点，减少方差，门控变体在噪声流中匹配基线

## 摘要（原文）

> Retrieval-augmented models couple parametric predictors with non-parametric memories, but their use in streaming supervised learning with concept drift is not well understood. We study online classification in non-stationary environments and propose Retrieval-Augmented Memory for Online Learning (RAM-OL), a simple extension of stochastic gradient descent that maintains a small buffer of past examples. At each time step, RAM-OL retrieves a few nearest neighbours of the current input in the hidden representation space and updates the model jointly on the current example and the retrieved neighbours. We compare a naive replay variant with a gated replay variant that constrains neighbours using a time window, similarity thresholds, and gradient reweighting, in order to balance fast reuse of relevant past data against robustness to outdated regimes. From a theoretical perspective, we interpret RAM-OL under a bounded drift model and discuss how retrieval can reduce adaptation cost and improve regret constants when patterns recur over time. Empirically, we instantiate RAM-OL on a simple online multilayer perceptron and evaluate it on three real-world data streams derived from electricity pricing, electricity load, and airline delay data. On strongly and periodically drifting streams, RAM-OL improves prequential accuracy by up to about seven percentage points and greatly reduces variance across random seeds, while on a noisy airline stream the gated variant closely matches the purely online baseline. These results show that retrieval-augmented memory is a practical and robust tool for online learning under concept drift.

