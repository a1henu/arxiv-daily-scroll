---
layout: default
title: Live Knowledge Tracing: Real-Time Adaptation using Tabular Foundation Models
---

# Live Knowledge Tracing: Real-Time Adaptation using Tabular Foundation Models
**arXiv**：[2602.06542v1](https://arxiv.org/abs/2602.06542) · [PDF](https://arxiv.org/pdf/2602.06542.pdf)  
**作者**：Mounir Lbath, Alexandre Paresy, Abdelkayoum Kaddouri, Alan André, Alexandre Ittah, Jill-Jênn Vie  

**一句话要点**：提出基于表格基础模型的实时知识追踪方法，以解决传统模型训练慢和过拟合问题。

**关键词**：知识追踪, 表格基础模型, 实时学习, 双向注意力, 在线推理

## 3 点简述
- 核心问题：传统深度知识追踪模型训练时间长，易在短序列数据集上过拟合。
- 方法要点：利用表格基础模型，通过双向注意力机制实时对齐测试与训练序列，无需离线训练。
- 实验或效果：在多个数据集上实现竞争性预测性能，速度提升高达273倍。

## 摘要（原文）

> Deep knowledge tracing models have achieved significant breakthroughs in modeling student learning trajectories. However, these architectures require substantial training time and are prone to overfitting on datasets with short sequences. In this paper, we explore a new paradigm for knowledge tracing by leveraging tabular foundation models (TFMs). Unlike traditional methods that require offline training on a fixed training set, our approach performs real-time ''live'' knowledge tracing in an online way. The core of our method lies in a two-way attention mechanism: while attention knowledge tracing models only attend across earlier time steps, TFMs simultaneously attend across both time steps and interactions of other students in the training set. They align testing sequences with relevant training sequences at inference time, therefore skipping the training step entirely. We demonstrate, using several datasets of increasing size, that our method achieves competitive predictive performance with up to 273x speedups, in a setting where more student interactions are observed over time.

