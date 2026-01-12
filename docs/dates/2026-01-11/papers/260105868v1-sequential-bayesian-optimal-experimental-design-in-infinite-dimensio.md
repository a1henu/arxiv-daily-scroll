---
layout: default
title: Sequential Bayesian Optimal Experimental Design in Infinite Dimensions via Policy Gradient Reinforcement Learning
---

# Sequential Bayesian Optimal Experimental Design in Infinite Dimensions via Policy Gradient Reinforcement Learning
**arXiv**：[2601.05868v1](https://arxiv.org/abs/2601.05868) · [PDF](https://arxiv.org/pdf/2601.05868.pdf)  
**作者**：Kaichen Shen, Peng Chen  

**一句话要点**：提出基于策略梯度强化学习的无限维序贯贝叶斯最优实验设计方法，用于偏微分方程反问题。

**关键词**：序贯贝叶斯最优实验设计, 策略梯度强化学习, 偏微分方程反问题, 无限维随机场, 神经算子代理, 传感器放置

## 3 点简述
- 针对无限维随机场参数的序贯贝叶斯最优实验设计计算挑战，将问题建模为有限时域马尔可夫决策过程。
- 通过策略梯度强化学习学习摊销设计策略，结合双降维和调整的导数信息潜在注意力神经算子代理，实现高效在线设计选择。
- 在污染物源追踪的序贯多传感器放置实验中，相比高保真有限元方法加速约100倍，性能优于随机放置，并发现物理可解释策略。

## 摘要（原文）

> Sequential Bayesian optimal experimental design (SBOED) for PDE-governed inverse problems is computationally challenging, especially for infinite-dimensional random field parameters. High-fidelity approaches require repeated forward and adjoint PDE solves inside nested Bayesian inversion and design loops. We formulate SBOED as a finite-horizon Markov decision process and learn an amortized design policy via policy-gradient reinforcement learning (PGRL), enabling online design selection from the experiment history without repeatedly solving an SBOED optimization problem. To make policy training and reward evaluation scalable, we combine dual dimension reduction -- active subspace projection for the parameter and principal component analysis for the state -- with an adjusted derivative-informed latent attention neural operator (LANO) surrogate that predicts both the parameter-to-solution map and its Jacobian. We use a Laplace-based D-optimality reward while noting that, in general, other expected-information-gain utilities such as KL divergence can also be used within the same framework. We further introduce an eigenvalue-based evaluation strategy that uses prior samples as proxies for maximum a posteriori (MAP) points, avoiding repeated MAP solves while retaining accurate information-gain estimates. Numerical experiments on sequential multi-sensor placement for contaminant source tracking demonstrate approximately $100\times$ speedup over high-fidelity finite element methods, improved performance over random sensor placements, and physically interpretable policies that discover an ``upstream'' tracking strategy.

