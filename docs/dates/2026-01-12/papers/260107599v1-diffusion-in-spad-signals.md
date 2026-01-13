---
layout: default
title: Diffusion in SPAD Signals
---

# Diffusion in SPAD Signals
**arXiv**：[2601.07599v1](https://arxiv.org/abs/2601.07599) · [PDF](https://arxiv.org/pdf/2601.07599.pdf)  
**作者**：Lior Dvir, Nadav Torem, Yoav Y. Schechner  

**一句话要点**：推导SPAD原始信号的似然与得分函数，以解决基于扩散模型的逆问题。

**关键词**：单光子雪崩二极管, 信号似然, 得分函数, 扩散模型, 逆问题, 光子计数

## 3 点简述
- 核心问题：SPAD原始信号（检测事件时间）与光子通量非线性且随机，需建模以解决逆问题。
- 方法要点：推导给定固定光子通量下信号的似然函数，并得出得分函数，作为扩散模型表达图像先验的关键。
- 实验或效果：分析低或高光子计数的影响，并展示利用检测事件时间的效果。

## 摘要（原文）

> We derive the likelihood of a raw signal in a single photon avalanche diode (SPAD), given a fixed photon flux. The raw signal comprises timing of detection events, which are nonlinearly related to the flux. Moreover, they are naturally stochastic. We then derive a score function of the signal. This is a key for solving inverse problems based on SPAD signals. We focus on deriving solutions involving a diffusion model, to express image priors. We demonstrate the effect of low or high photon counts, and the consequence of exploiting timing of detection events.

