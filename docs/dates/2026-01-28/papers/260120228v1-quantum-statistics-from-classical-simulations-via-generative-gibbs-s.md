---
layout: default
title: Quantum statistics from classical simulations via generative Gibbs sampling
---

# Quantum statistics from classical simulations via generative Gibbs sampling
**arXiv**：[2601.20228v1](https://arxiv.org/abs/2601.20228) · [PDF](https://arxiv.org/pdf/2601.20228.pdf)  
**作者**：Weizhou Wang, Xuanxi Zhang, Jonathan Weare, Aaron R. Dinner  

**一句话要点**：提出GG-PI框架，通过生成式吉布斯采样从经典模拟数据恢复量子统计，以高效模拟核量子效应。

**关键词**：核量子效应模拟, 生成式建模, 吉布斯采样, 路径积分方法, 经典模拟数据利用, 温度迁移学习

## 3 点简述
- 核心问题：路径积分分子动力学模拟核量子效应计算成本高，需高效替代方法。
- 方法要点：结合单珠条件密度的生成建模与吉布斯采样，利用经典模拟数据训练，无需重新训练即可跨温度迁移。
- 实验或效果：在标准测试系统中，相比路径积分分子动力学显著减少壁钟时间，框架可扩展至类似马尔可夫结构问题。

## 摘要（原文）

> Accurate simulation of nuclear quantum effects is essential for molecular modeling but expensive using path integral molecular dynamics (PIMD). We present GG-PI, a ring-polymer-based framework that combines generative modeling of the single-bead conditional density with Gibbs sampling to recover quantum statistics from classical simulation data. GG-PI uses inexpensive standard classical simulations or existing data for training and allows transfer across temperatures without retraining. On standard test systems, GG-PI significantly reduces wall clock time compared to PIMD. Our approach extends easily to a wide range of problems with similar Markov structure.

