---
layout: default
title: Neural Network-Based Parameter Estimation of a Labour Market Agent-Based Model
---

# Neural Network-Based Parameter Estimation of a Labour Market Agent-Based Model
**arXiv**：[2602.15572v1](https://arxiv.org/abs/2602.15572) · [PDF](https://arxiv.org/pdf/2602.15572.pdf)  
**作者**：M Lopes Alves, Joel Dyer, Doyne Farmer, Michael Wooldridge, Anisoara Calinescu  

**一句话要点**：提出基于神经网络的模拟推断框架，以解决大规模劳动力市场基于代理模型参数估计的计算效率问题。

**关键词**：基于代理模型, 参数估计, 模拟推断, 神经网络, 劳动力市场

## 3 点简述
- 核心问题：大规模基于代理模型参数估计因计算限制难以探索参数空间，影响决策支持应用。
- 方法要点：应用基于神经网络的模拟推断框架，结合统计量摘要与神经网络学习，进行参数估计。
- 实验或效果：在合成和真实美国劳动力市场数据上验证，神经网络方法能恢复原始参数并提升效率。

## 摘要（原文）

> Agent-based modelling (ABM) is a widespread approach to simulate complex systems. Advancements in computational processing and storage have facilitated the adoption of ABMs across many fields; however, ABMs face challenges that limit their use as decision-support tools. A significant issue is parameter estimation in large-scale ABMs, particularly due to computational constraints on exploring the parameter space. This study evaluates a state-of-the-art simulation-based inference (SBI) framework that uses neural networks (NN) for parameter estimation. This framework is applied to an established labour market ABM based on job transition networks. The ABM is initiated with synthetic datasets and the real U.S. labour market. Next, we compare the effectiveness of summary statistics derived from a list of statistical measures with that learned by an embedded NN. The results demonstrate that the NN-based approach recovers the original parameters when evaluating posterior distributions across various dataset scales and improves efficiency compared to traditional Bayesian methods.

