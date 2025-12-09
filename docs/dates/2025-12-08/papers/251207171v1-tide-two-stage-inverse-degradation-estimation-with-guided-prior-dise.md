---
layout: default
title: TIDE: Two-Stage Inverse Degradation Estimation with Guided Prior Disentanglement for Underwater Image Restoration
---

# TIDE: Two-Stage Inverse Degradation Estimation with Guided Prior Disentanglement for Underwater Image Restoration
**arXiv**：[2512.07171v1](https://arxiv.org/abs/2512.07171) · [PDF](https://arxiv.org/pdf/2512.07171.pdf)  
**作者**：Shravan Venkatraman, Rakesh Raj Madavan, Pavan Kumar S, Muthu Subash Kavitha  

**一句话要点**：提出TIDE框架，通过两阶段逆退化估计与先验解耦解决水下图像恢复问题

**关键词**：水下图像恢复, 逆退化估计, 先验解耦, 多退化处理, 自适应融合, 渐进细化

## 3 点简述
- 核心问题：水下图像退化复杂且空间变化，现有方法难以处理多退化共存。
- 方法要点：将退化分解为四因素，设计专家假设并自适应融合，再渐进细化。
- 实验或效果：在标准基准和浑浊条件下，在保真度和感知质量上表现优异。

## 摘要（原文）

> Underwater image restoration is essential for marine applications ranging from ecological monitoring to archaeological surveys, but effectively addressing the complex and spatially varying nature of underwater degradations remains a challenge. Existing methods typically apply uniform restoration strategies across the entire image, struggling to handle multiple co-occurring degradations that vary spatially and with water conditions. We introduce TIDE, a $\underline{t}$wo stage $\underline{i}$nverse $\underline{d}$egradation $\underline{e}$stimation framework that explicitly models degradation characteristics and applies targeted restoration through specialized prior decomposition. Our approach disentangles the restoration process into multiple specialized hypotheses that are adaptively fused based on local degradation patterns, followed by a progressive refinement stage that corrects residual artifacts. Specifically, TIDE decomposes underwater degradations into four key factors, namely color distortion, haze, detail loss, and noise, and designs restoration experts specialized for each. By generating specialized restoration hypotheses, TIDE balances competing degradation factors and produces natural results even in highly degraded regions. Extensive experiments across both standard benchmarks and challenging turbid water conditions show that TIDE achieves competitive performance on reference based fidelity metrics while outperforming state of the art methods on non reference perceptual quality metrics, with strong improvements in color correction and contrast enhancement. Our code is available at: https://rakesh-123-cryp.github.io/TIDE.

