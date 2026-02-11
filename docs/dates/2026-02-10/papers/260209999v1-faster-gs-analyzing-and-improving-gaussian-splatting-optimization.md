---
layout: default
title: Faster-GS: Analyzing and Improving Gaussian Splatting Optimization
---

# Faster-GS: Analyzing and Improving Gaussian Splatting Optimization
**arXiv**：[2602.09999v1](https://arxiv.org/abs/2602.09999) · [PDF](https://arxiv.org/pdf/2602.09999.pdf)  
**作者**：Florian Hahlbohm, Linus Franke, Martin Eisemann, Marcus Magnor  

**一句话要点**：提出Faster-GS以加速3D高斯泼溅优化，保持视觉质量并扩展至4D重建。

**关键词**：3D高斯泼溅, 优化算法, 训练加速, 数值稳定性, 4D重建, 非刚性场景

## 3 点简述
- 核心问题：现有3DGS方法常混淆实现改进与算法修改，导致性能与保真度权衡，难以公平比较。
- 方法要点：整合并评估先前有效策略，加入数值稳定性、高斯截断和梯度近似等新优化，形成Faster-GS系统。
- 实验或效果：在综合基准测试中，Faster-GS实现高达5倍训练加速，视觉质量不变，并应用于4D非刚性场景优化。

## 摘要（原文）

> Recent advances in 3D Gaussian Splatting (3DGS) have focused on accelerating optimization while preserving reconstruction quality. However, many proposed methods entangle implementation-level improvements with fundamental algorithmic modifications or trade performance for fidelity, leading to a fragmented research landscape that complicates fair comparison. In this work, we consolidate and evaluate the most effective and broadly applicable strategies from prior 3DGS research and augment them with several novel optimizations. We further investigate underexplored aspects of the framework, including numerical stability, Gaussian truncation, and gradient approximation. The resulting system, Faster-GS, provides a rigorously optimized algorithm that we evaluate across a comprehensive suite of benchmarks. Our experiments demonstrate that Faster-GS achieves up to 5$\times$ faster training while maintaining visual quality, establishing a new cost-effective and resource efficient baseline for 3DGS optimization. Furthermore, we demonstrate that optimizations can be applied to 4D Gaussian reconstruction, leading to efficient non-rigid scene optimization.

