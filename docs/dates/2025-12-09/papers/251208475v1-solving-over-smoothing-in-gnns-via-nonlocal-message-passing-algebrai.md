---
layout: default
title: Solving Over-Smoothing in GNNs via Nonlocal Message Passing: Algebraic Smoothing and Depth Scalability
---

# Solving Over-Smoothing in GNNs via Nonlocal Message Passing: Algebraic Smoothing and Depth Scalability
**arXiv**：[2512.08475v1](https://arxiv.org/abs/2512.08475) · [PDF](https://arxiv.org/pdf/2512.08475.pdf)  
**作者**：Weiqi Guan, Junlin He  

**一句话要点**：提出基于Post-LN的非局部消息传递方法，通过代数平滑解决GNN中的过平滑问题，避免深度诅咒。

**关键词**：图神经网络, 过平滑问题, 层归一化, 深度可扩展性, 代数平滑

## 3 点简述
- 核心问题：层归一化位置选择导致过平滑与深度诅咒的困境，Post-LN架构易过平滑，Pre-LN架构受深度诅咒影响。
- 方法要点：基于Post-LN引入代数平滑机制，无需额外参数，防止过平滑同时避免深度诅咒。
- 实验或效果：在五个基准测试中验证，支持高达256层的深层网络，性能提升。

## 摘要（原文）

> The relationship between Layer Normalization (LN) placement and the over-smoothing phenomenon remains underexplored. We identify a critical dilemma: Pre-LN architectures avoid over-smoothing but suffer from the curse of depth, while Post-LN architectures bypass the curse of depth but experience over-smoothing.
>   To resolve this, we propose a new method based on Post-LN that induces algebraic smoothing, preventing over-smoothing without the curse of depth. Empirical results across five benchmarks demonstrate that our approach supports deeper networks (up to 256 layers) and improves performance, requiring no additional parameters.
>   Key contributions:
>   Theoretical Characterization: Analysis of LN dynamics and their impact on over-smoothing and the curse of depth.
>   A Principled Solution: A parameter-efficient method that induces algebraic smoothing and avoids over-smoothing and the curse of depth.
>   Empirical Validation: Extensive experiments showing the effectiveness of the method in deeper GNNs.

