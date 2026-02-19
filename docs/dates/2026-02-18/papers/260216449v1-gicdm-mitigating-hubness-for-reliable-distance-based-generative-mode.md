---
layout: default
title: GICDM: Mitigating Hubness for Reliable Distance-Based Generative Model Evaluation
---

# GICDM: Mitigating Hubness for Reliable Distance-Based Generative Model Evaluation
**arXiv**：[2602.16449v1](https://arxiv.org/abs/2602.16449) · [PDF](https://arxiv.org/pdf/2602.16449.pdf)  
**作者**：Nicolas Salvy, Hugues Talbot, Bertrand Thirion  

**一句话要点**：提出GICDM方法以解决生成模型评估中因hubness现象导致的距离度量偏差问题

**关键词**：生成模型评估, hubness现象, 距离度量, 邻域估计, 多尺度扩展

## 3 点简述
- 核心问题：高维嵌入空间中hubness现象扭曲最近邻关系，影响生成模型评估的可靠性
- 方法要点：基于ICDM提出GICDM，校正真实与生成数据的邻域估计，并引入多尺度扩展
- 实验或效果：在合成和真实基准测试中，GICDM缓解hubness失败，恢复度量可靠性，提升与人类判断的一致性

## 摘要（原文）

> Generative model evaluation commonly relies on high-dimensional embedding spaces to compute distances between samples. We show that dataset representations in these spaces are affected by the hubness phenomenon, which distorts nearest neighbor relationships and biases distance-based metrics. Building on the classical Iterative Contextual Dissimilarity Measure (ICDM), we introduce Generative ICDM (GICDM), a method to correct neighborhood estimation for both real and generated data. We introduce a multi-scale extension to improve empirical behavior. Extensive experiments on synthetic and real benchmarks demonstrate that GICDM resolves hubness-induced failures, restores reliable metric behavior, and improves alignment with human judgment.

