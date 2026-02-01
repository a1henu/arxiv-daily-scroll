---
layout: default
title: On Forgetting and Stability of Score-based Generative models
---

# On Forgetting and Stability of Score-based Generative models
**arXiv**：[2601.21868v1](https://arxiv.org/abs/2601.21868) · [PDF](https://arxiv.org/pdf/2601.21868.pdf)  
**作者**：Stanislas Strasman, Gabriel Cardoso, Sylvain Le Corff, Vincent Lemaire, Antonio Ocello  

**一句话要点**：基于马尔可夫链稳定性与遗忘性，量化基于分数的生成模型的采样误差边界。

**关键词**：基于分数的生成模型, 马尔可夫链稳定性, 采样误差分析, 反向扩散动力学, Lyapunov条件, Doeblin条件

## 3 点简述
- 研究基于分数的生成模型的稳定性与长期行为，分析采样误差传播。
- 利用反向时间动力学的Lyapunov漂移条件和Doeblin型小化条件，确保误差传播可控。
- 结果表明反向扩散动力学在采样轨迹上诱导收缩机制，提供量化稳定性框架。

## 摘要（原文）

> Understanding the stability and long-time behavior of generative models is a fundamental problem in modern machine learning. This paper provides quantitative bounds on the sampling error of score-based generative models by leveraging stability and forgetting properties of the Markov chain associated with the reverse-time dynamics. Under weak assumptions, we provide the two structural properties to ensure the propagation of initialization and discretization errors of the backward process: a Lyapunov drift condition and a Doeblin-type minorization condition. A practical consequence is quantitative stability of the sampling procedure, as the reverse diffusion dynamics induces a contraction mechanism along the sampling trajectory. Our results clarify the role of stochastic dynamics in score-based models and provide a principled framework for analyzing propagation of errors in such approaches.

