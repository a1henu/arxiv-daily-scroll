---
layout: default
title: Variational inference via radial transport
---

# Variational inference via radial transport
**arXiv**：[2602.17525v1](https://arxiv.org/abs/2602.17525) · [PDF](https://arxiv.org/pdf/2602.17525.pdf)  
**作者**：Luca Ghafourpour, Sinho Chewi, Alessio Figalli, Aram-Alexandre Pooladian  

**一句话要点**：提出radVI算法以优化径向轮廓，提升变分推断在高维分布近似中的覆盖效果。

**关键词**：变分推断, 径向传输, Wasserstein距离, 高斯近似, 优化算法, 理论保证

## 3 点简述
- 变分推断中高斯分布可能无法准确捕获目标分布的径向轮廓，导致覆盖不足。
- radVI算法通过优化径向轮廓，作为现有变分推断方案的廉价有效附加组件。
- 基于Wasserstein空间优化和径向传输映射的规律性，提供理论收敛保证。

## 摘要（原文）

> In variational inference (VI), the practitioner approximates a high-dimensional distribution $π$ with a simple surrogate one, often a (product) Gaussian distribution. However, in many cases of practical interest, Gaussian distributions might not capture the correct radial profile of $π$, resulting in poor coverage. In this work, we approach the VI problem from the perspective of optimizing over these radial profiles. Our algorithm radVI is a cheap, effective add-on to many existing VI schemes, such as Gaussian (mean-field) VI and Laplace approximation. We provide theoretical convergence guarantees for our algorithm, owing to recent developments in optimization over the Wasserstein space--the space of probability distributions endowed with the Wasserstein distance--and new regularity properties of radial transport maps in the style of Caffarelli (2000).

