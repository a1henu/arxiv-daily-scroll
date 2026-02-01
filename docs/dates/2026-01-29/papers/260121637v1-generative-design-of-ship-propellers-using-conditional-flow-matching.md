---
layout: default
title: Generative Design of Ship Propellers using Conditional Flow Matching
---

# Generative Design of Ship Propellers using Conditional Flow Matching
**arXiv**：[2601.21637v1](https://arxiv.org/abs/2601.21637) · [PDF](https://arxiv.org/pdf/2601.21637.pdf)  
**作者**：Patrick Kruger, Rafael Diaz, Simon Hauschulz, Stefan Harries, Hanno Gottschalk  

**一句话要点**：提出基于条件流匹配的生成式AI方法，用于船舶螺旋桨设计以实现指定性能目标。

**关键词**：生成式人工智能, 条件流匹配, 船舶螺旋桨设计, 数值模拟, 数据增强, 工程生成设计

## 3 点简述
- 核心问题：传统前向机器学习模型预测设计参数性能，但生成式AI旨在生成满足性能目标的设计。
- 方法要点：使用条件流匹配建立设计参数与模拟噪声间的双向映射，基于性能标签生成多样设计。
- 实验或效果：通过涡格法生成数据训练模型，提出伪标签数据增强，展示性能相近的螺旋桨几何多样性。

## 摘要（原文）

> In this paper, we explore the use of generative artificial intelligence (GenAI) for ship propeller design. While traditional forward machine learning models predict the performance of mechanical components based on given design parameters, GenAI models aim to generate designs that achieve specified performance targets. In particular, we employ conditional flow matching to establish a bidirectional mapping between design parameters and simulated noise that is conditioned on performance labels. This approach enables the generation of multiple valid designs corresponding to the same performance targets by sampling over the noise vector.
>   To support model training, we generate data using a vortex lattice method for numerical simulation and analyze the trade-off between model accuracy and the amount of available data. We further propose data augmentation using pseudo-labels derived from less data-intensive forward surrogate models, which can often improve overall model performance. Finally, we present examples of distinct propeller geometries that exhibit nearly identical performance characteristics, illustrating the versatility and potential of GenAI in engineering design.

