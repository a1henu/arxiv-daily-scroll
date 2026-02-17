---
layout: default
title: Extending Multi-Source Bayesian Optimization With Causality Principles
---

# Extending Multi-Source Bayesian Optimization With Causality Principles
**arXiv**：[2602.14791v1](https://arxiv.org/abs/2602.14791) · [PDF](https://arxiv.org/pdf/2602.14791.pdf)  
**作者**：Luuk Jacobs, Mohammad Ali Javidian  

**一句话要点**：提出多源因果贝叶斯优化算法，以提升高维多源场景下的优化效率与可扩展性。

**关键词**：多源贝叶斯优化, 因果贝叶斯优化, 高维优化, 计算效率, 算法融合, 可扩展性

## 3 点简述
- 传统多源贝叶斯优化假设变量独立，限制了因果信息可用场景的应用。
- 集成多源与因果贝叶斯优化原理，实现算法融合以降低计算复杂度。
- 在合成与真实数据集上验证算法，展示其鲁棒性、收敛速度与性能提升。

## 摘要（原文）

> Multi-Source Bayesian Optimization (MSBO) serves as a variant of the traditional Bayesian Optimization (BO) framework applicable to situations involving optimization of an objective black-box function over multiple information sources such as simulations, surrogate models, or real-world experiments. However, traditional MSBO assumes the input variables of the objective function to be independent and identically distributed, limiting its effectiveness in scenarios where causal information is available and interventions can be performed, such as clinical trials or policy-making. In the single-source domain, Causal Bayesian Optimization (CBO) extends standard BO with the principles of causality, enabling better modeling of variable dependencies. This leads to more accurate optimization, improved decision-making, and more efficient use of low-cost information sources. In this article, we propose a principled integration of the MSBO and CBO methodologies in the multi-source domain, leveraging the strengths of both to enhance optimization efficiency and reduce computational complexity in higher-dimensional problems. We present the theoretical foundations of both Causal and Multi-Source Bayesian Optimization, and demonstrate how their synergy informs our Multi-Source Causal Bayesian Optimization (MSCBO) algorithm. We compare the performance of MSCBO against its foundational counterparts for both synthetic and real-world datasets with varying levels of noise, highlighting the robustness and applicability of MSCBO. Based on our findings, we conclude that integrating MSBO with the causality principles of CBO facilitates dimensionality reduction and lowers operational costs, ultimately improving convergence speed, performance, and scalability.

