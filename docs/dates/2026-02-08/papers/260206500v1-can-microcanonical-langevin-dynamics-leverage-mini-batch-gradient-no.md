---
layout: default
title: Can Microcanonical Langevin Dynamics Leverage Mini-Batch Gradient Noise?
---

# Can Microcanonical Langevin Dynamics Leverage Mini-Batch Gradient Noise?
**arXiv**：[2602.06500v1](https://arxiv.org/abs/2602.06500) · [PDF](https://arxiv.org/pdf/2602.06500.pdf)  
**作者**：Emanuel Sommer, Kangning Diao, Jakob Robnik, Uros Seljak, David Rügamer  

**一句话要点**：提出随机梯度微正则朗之万动力学，通过噪声预调节和自适应调谐器解决大规模贝叶斯推断问题。

**关键词**：微正则朗之万动力学, 随机梯度噪声, 贝叶斯深度学习, 蒙特卡洛采样, 自适应调谐器, 大规模推断

## 3 点简述
- 核心问题：微正则朗之万蒙特卡洛依赖全数据集梯度，在大规模问题中计算成本过高。
- 方法要点：引入随机梯度微正则动力学，分析其偏差和不稳定性，并提出噪声预调节和自适应步长选择。
- 实验或效果：算法在贝叶斯神经网络等高维推断任务中实现先进性能，并扩展为随机微正则朗之万集成采样器。

## 摘要（原文）

> Scaling inference methods such as Markov chain Monte Carlo to high-dimensional models remains a central challenge in Bayesian deep learning. A promising recent proposal, microcanonical Langevin Monte Carlo, has shown state-of-the-art performance across a wide range of problems. However, its reliance on full-dataset gradients makes it prohibitively expensive for large-scale problems. This paper addresses a fundamental question: Can microcanonical dynamics effectively leverage mini-batch gradient noise? We provide the first systematic study of this problem, establishing a novel continuous-time theoretical analysis of stochastic-gradient microcanonical dynamics. We reveal two critical failure modes: a theoretically derived bias due to anisotropic gradient noise and numerical instabilities in complex high-dimensional posteriors. To tackle these issues, we propose a principled gradient noise preconditioning scheme shown to significantly reduce this bias and develop a novel, energy-variance-based adaptive tuner that automates step size selection and dynamically informs numerical guardrails. The resulting algorithm is a robust and scalable microcanonical Monte Carlo sampler that achieves state-of-the-art performance on challenging high-dimensional inference tasks like Bayesian neural networks. Combined with recent ensemble techniques, our work unlocks a new class of stochastic microcanonical Langevin ensemble (SMILE) samplers for large-scale Bayesian inference.

