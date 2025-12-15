---
layout: default
title: Softmax as Linear Attention in the Large-Prompt Regime: a Measure-based Perspective
---

# Softmax as Linear Attention in the Large-Prompt Regime: a Measure-based Perspective
**arXiv**：[2512.11784v1](https://arxiv.org/abs/2512.11784) · [PDF](https://arxiv.org/pdf/2512.11784.pdf)  
**作者**：Etienne Boursier, Claire Boyer  

**一句话要点**：提出基于测度的框架，证明长提示下Softmax注意力收敛为线性算子，便于理论分析。

**关键词**：Softmax注意力, 线性注意力, 测度理论, 长提示分析, 上下文学习, 训练动态

## 3 点简述
- 核心问题：Softmax注意力的非线性结构导致理论分析困难，尤其在长提示场景下。
- 方法要点：基于测度框架，证明在无限提示极限下Softmax收敛为线性算子，并建立非渐近浓度界。
- 实验或效果：在上下文线性回归中，利用无限提示动态分析有限提示训练，展示长提示下Softmax继承线性结构。

## 摘要（原文）

> Softmax attention is a central component of transformer architectures, yet its nonlinear structure poses significant challenges for theoretical analysis. We develop a unified, measure-based framework for studying single-layer softmax attention under both finite and infinite prompts. For i.i.d. Gaussian inputs, we lean on the fact that the softmax operator converges in the infinite-prompt limit to a linear operator acting on the underlying input-token measure. Building on this insight, we establish non-asymptotic concentration bounds for the output and gradient of softmax attention, quantifying how rapidly the finite-prompt model approaches its infinite-prompt counterpart, and prove that this concentration remains stable along the entire training trajectory in general in-context learning settings with sub-Gaussian tokens. In the case of in-context linear regression, we use the tractable infinite-prompt dynamics to analyze training at finite prompt length. Our results allow optimization analyses developed for linear attention to transfer directly to softmax attention when prompts are sufficiently long, showing that large-prompt softmax attention inherits the analytical structure of its linear counterpart. This, in turn, provides a principled and broadly applicable toolkit for studying the training dynamics and statistical behavior of softmax attention layers in large prompt regimes.

