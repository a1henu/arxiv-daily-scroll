---
layout: default
title: Barron-Wiener-Laguerre models
---

# Barron-Wiener-Laguerre models
**arXiv**：[2602.13098v1](https://arxiv.org/abs/2602.13098) · [PDF](https://arxiv.org/pdf/2602.13098.pdf)  
**作者**：Rahul Manavalan, Filip Tronarp  

**一句话要点**：提出Barron-Wiener-Laguerre模型以增强因果算子学习的不确定性量化

**关键词**：因果算子学习, 不确定性量化, Wiener-Laguerre模型, Barron函数逼近, 系统辨识, 时间序列建模

## 3 点简述
- 核心问题：经典Wiener-Laguerre模型仅提供确定性点估计，缺乏概率性不确定性量化。
- 方法要点：结合Laguerre基参数化线性动态与Barron函数逼近，通过参数测度积分表示实现贝叶斯推断。
- 实验或效果：未知，但框架为时间序列建模和非线性系统辨识提供了结构化且可解释的方法。

## 摘要（原文）

> We propose a probabilistic extension of Wiener-Laguerre models for causal operator learning. Classical Wiener-Laguerre models parameterize stable linear dynamics using orthonormal Laguerre bases and apply a static nonlinear map to the resulting features. While structurally efficient and interpretable, they provide only deterministic point estimates. We reinterpret the nonlinear component through the lens of Barron function approximation, viewing two-layer networks, random Fourier features, and extreme learning machines as discretizations of integral representations over parameter measures. This perspective naturally admits Bayesian inference on the nonlinear map and yields posterior predictive uncertainty. By combining Laguerre-parameterized causal dynamics with probabilistic Barron-type nonlinear approximators, we obtain a structured yet expressive class of causal operators equipped with uncertainty quantification. The resulting framework bridges classical system identification and modern measure-based function approximation, providing a principled approach to time-series modeling and nonlinear systems identification.

