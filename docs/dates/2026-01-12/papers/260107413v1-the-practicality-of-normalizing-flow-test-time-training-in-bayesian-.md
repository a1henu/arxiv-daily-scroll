---
layout: default
title: The Practicality of Normalizing Flow Test-Time Training in Bayesian Inference for Agent-Based Models
---

# The Practicality of Normalizing Flow Test-Time Training in Bayesian Inference for Agent-Based Models
**arXiv**：[2601.07413v1](https://arxiv.org/abs/2601.07413) · [PDF](https://arxiv.org/pdf/2601.07413.pdf)  
**作者**：Junyao Zhang, Jinglai Li, Junqi Tang  

**一句话要点**：提出基于归一化流的测试时训练策略，以增强基于代理模型的贝叶斯参数推断实用性。

**关键词**：基于代理模型, 贝叶斯推断, 归一化流, 测试时训练, 参数估计, 分布偏移

## 3 点简述
- 核心问题：基于代理模型的参数后验估计面临分布偏移挑战，影响推断准确性。
- 方法要点：首次将归一化流的测试时训练应用于代理模型，设计多种策略进行微调。
- 实验或效果：数值研究表明测试时训练显著有效，支持实时调整推断过程。

## 摘要（原文）

> Agent-Based Models (ABMs) are gaining great popularity in economics and social science because of their strong flexibility to describe the realistic and heterogeneous decisions and interaction rules between individual agents. In this work, we investigate for the first time the practicality of test-time training (TTT) of deep models such as normalizing flows, in the parameters posterior estimations of ABMs. We propose several practical TTT strategies for fine-tuning the normalizing flow against distribution shifts. Our numerical study demonstrates that TTT schemes are remarkably effective, enabling real-time adjustment of flow-based inference for ABM parameters.

