---
layout: default
title: On the Convergence of Stochastic Gradient Descent with Perturbed Forward-Backward Passes
---

# On the Convergence of Stochastic Gradient Descent with Perturbed Forward-Backward Passes
**arXiv**：[2602.20646v1](https://arxiv.org/abs/2602.20646) · [PDF](https://arxiv.org/pdf/2602.20646.pdf)  
**作者**：Boao Kong, Hengrui Zhang, Kun Yuan  

**一句话要点**：分析SGD在前后向扰动下的收敛性，解释深度学习梯度尖峰现象。

**关键词**：随机梯度下降, 扰动分析, 复合优化, 梯度尖峰, 深度学习理论

## 3 点简述
- 研究SGD在复合优化中前后向扰动传播与放大问题。
- 推导非凸和Polyak–Łojasiewicz条件下的收敛保证。
- 实验验证扰动敏感性和梯度尖峰行为。

## 摘要（原文）

> We study stochastic gradient descent (SGD) for composite optimization problems with $N$ sequential operators subject to perturbations in both the forward and backward passes. Unlike classical analyses that treat gradient noise as additive and localized, perturbations to intermediate outputs and gradients cascade through the computational graph, compounding geometrically with the number of operators. We present the first comprehensive theoretical analysis of this setting. Specifically, we characterize how forward and backward perturbations propagate and amplify within a single gradient step, derive convergence guarantees for both general non-convex objectives and functions satisfying the Polyak--Łojasiewicz condition, and identify conditions under which perturbations do not deteriorate the asymptotic convergence order. As a byproduct, our analysis furnishes a theoretical explanation for the gradient spiking phenomenon widely observed in deep learning, precisely characterizing the conditions under which training recovers from spikes or diverges. Experiments on logistic regression with convex and non-convex regularization validate our theories, illustrating the predicted spike behavior and the asymmetric sensitivity to forward versus backward perturbations.

