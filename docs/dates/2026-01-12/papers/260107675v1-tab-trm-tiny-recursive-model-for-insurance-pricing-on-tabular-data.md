---
layout: default
title: Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data
---

# Tab-TRM: Tiny Recursive Model for Insurance Pricing on Tabular Data
**arXiv**：[2601.07675v1](https://arxiv.org/abs/2601.07675) · [PDF](https://arxiv.org/pdf/2601.07675.pdf)  
**作者**：Kishan Padayachy, Ronald Richman, Mario V. Wüthrich  

**一句话要点**：提出Tab-TRM模型，将递归潜在推理范式应用于保险定价的表格数据建模。

**关键词**：保险定价, 表格数据建模, 递归神经网络, 潜在推理, 精算工作流

## 3 点简述
- 核心问题：将现代机器学习方法融入传统保险定价工作流，以处理表格数据。
- 方法要点：采用紧凑递归网络迭代更新可学习的答案和推理状态令牌，模拟迭代定价方案。
- 实验或效果：未知，但模型旨在桥接经典精算方法和梯度提升机等现代技术。

## 摘要（原文）

> We introduce Tab-TRM (Tabular-Tiny Recursive Model), a network architecture that adapts the recursive latent reasoning paradigm of Tiny Recursive Models (TRMs) to insurance modeling. Drawing inspiration from both the Hierarchical Reasoning Model (HRM) and its simplified successor TRM, the Tab-TRM model makes predictions by reasoning over the input features. It maintains two learnable latent tokens - an answer token and a reasoning state - that are iteratively refined by a compact, parameter-efficient recursive network. The recursive processing layer repeatedly updates the reasoning state given the full token sequence and then refines the answer token, in close analogy with iterative insurance pricing schemes. Conceptually, Tab-TRM bridges classical actuarial workflows - iterative generalized linear model fitting and minimum-bias calibration - on the one hand, and modern machine learning, in terms of Gradient Boosting Machines, on the other.

