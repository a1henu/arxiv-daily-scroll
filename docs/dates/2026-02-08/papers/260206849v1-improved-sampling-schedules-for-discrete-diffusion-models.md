---
layout: default
title: Improved Sampling Schedules for Discrete Diffusion Models
---

# Improved Sampling Schedules for Discrete Diffusion Models
**arXiv**：[2602.06849v1](https://arxiv.org/abs/2602.06849) · [PDF](https://arxiv.org/pdf/2602.06849.pdf)  
**作者**：Alberto Foresti, Mustapha Bounoua, Giulio Franzese, Luca Ambrogioni, Pietro Michiardi  

**一句话要点**：提出基于熵产生率的离散扩散模型采样调度，提升序列数据生成效率

**关键词**：离散扩散模型, 采样调度, 熵产生率, Wasserstein距离, 序列数据生成, 信息论分析

## 3 点简述
- 分析离散扩散模型反向过程的信息论原理，引入熵产生率量化信息生成
- 设计两种均匀采样调度：EDS保持信息增益恒定，WDS基于Wasserstein距离等步长
- 实验验证新调度在合成数据、音乐、视觉和语言任务中优于现有方法，计算成本更低

## 摘要（原文）

> Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

