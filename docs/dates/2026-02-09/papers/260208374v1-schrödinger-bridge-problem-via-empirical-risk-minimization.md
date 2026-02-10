---
layout: default
title: Schrödinger bridge problem via empirical risk minimization
---

# Schrödinger bridge problem via empirical risk minimization
**arXiv**：[2602.08374v1](https://arxiv.org/abs/2602.08374) · [PDF](https://arxiv.org/pdf/2602.08374.pdf)  
**作者**：Denis Belomestny, Alexey Naumov, Nikita Puchkin, Denis Suchkov  

**一句话要点**：提出基于经验风险最小化的学习理论方法，以样本数据求解薛定谔桥问题。

**关键词**：薛定谔桥问题, 经验风险最小化, 样本数据, 随机控制, 非线性不动点方程, 学习理论

## 3 点简述
- 研究薛定谔桥问题，其中端点分布仅通过样本可得。
- 将薛定谔系统重写为单一正变换势的非线性不动点方程，通过函数类上的经验风险最小化估计该势。
- 在数值实验中展示所提方法的性能，并基于随机控制表示生成桥样本。

## 摘要（原文）

> We study the Schrödinger bridge problem when the endpoint distributions are available only through samples. Classical computational approaches estimate Schrödinger potentials via Sinkhorn iterations on empirical measures and then construct a time-inhomogeneous drift by differentiating a kernel-smoothed dual solution. In contrast, we propose a learning-theoretic route: we rewrite the Schrödinger system in terms of a single positive transformed potential that satisfies a nonlinear fixed-point equation and estimate this potential by empirical risk minimization over a function class. We establish uniform concentration of the empirical risk around its population counterpart under sub-Gaussian assumptions on the reference kernel and terminal density. We plug the learned potential into a stochastic control representation of the bridge to generate samples. We illustrate performance of the suggested approach with numerical experiments.

