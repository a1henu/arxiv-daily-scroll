---
layout: default
title: VBO-MI: A Fully Gradient-Based Bayesian Optimization Framework Using Variational Mutual Information Estimation
---

# VBO-MI: A Fully Gradient-Based Bayesian Optimization Framework Using Variational Mutual Information Estimation
**arXiv**：[2601.08172v1](https://arxiv.org/abs/2601.08172) · [PDF](https://arxiv.org/pdf/2601.08172.pdf)  
**作者**：Farhad Mirkarimi  

**一句话要点**：提出VBO-MI框架，利用变分互信息估计实现全梯度贝叶斯优化，以解决昂贵黑盒函数优化问题。

**关键词**：贝叶斯优化, 变分推断, 互信息估计, 梯度优化, 黑盒函数优化, 计算效率

## 3 点简述
- 核心问题：传统贝叶斯优化在贝叶斯神经网络中面临后验采样和采集函数优化的计算瓶颈。
- 方法要点：采用演员-评论家架构，通过动作网络和变分评论家实现端到端梯度流，消除内循环优化。
- 实验或效果：在合成和真实任务中，VBO-MI达到相同或更优性能，计算量减少高达10^2倍。

## 摘要（原文）

> Many real-world tasks require optimizing expensive black-box functions accessible only through noisy evaluations, a setting commonly addressed with Bayesian optimization (BO). While Bayesian neural networks (BNNs) have recently emerged as scalable alternatives to Gaussian Processes (GPs), traditional BNN-BO frameworks remain burdened by expensive posterior sampling and acquisition function optimization. In this work, we propose {VBO-MI} (Variational Bayesian Optimization with Mutual Information), a fully gradient-based BO framework that leverages recent advances in variational mutual information estimation. To enable end-to-end gradient flow, we employ an actor-critic architecture consisting of an {action-net} to navigate the input space and a {variational critic} to estimate information gain. This formulation effectively eliminates the traditional inner-loop acquisition optimization bottleneck, achieving up to a {$10^2 \times$ reduction in FLOPs} compared to BNN-BO baselines. We evaluate our method on a diverse suite of benchmarks, including high-dimensional synthetic functions and complex real-world tasks such as PDE optimization, the Lunar Lander control problem, and categorical Pest Control. Our experiments demonstrate that VBO-MI consistently provides the same or superior optimization performance and computational scalability over the baselines.

