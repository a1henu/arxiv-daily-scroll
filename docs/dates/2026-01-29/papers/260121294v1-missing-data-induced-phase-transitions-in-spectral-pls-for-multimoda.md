---
layout: default
title: Missing-Data-Induced Phase Transitions in Spectral PLS for Multimodal Learning
---

# Missing-Data-Induced Phase Transitions in Spectral PLS for Multimodal Learning
**arXiv**：[2601.21294v1](https://arxiv.org/abs/2601.21294) · [PDF](https://arxiv.org/pdf/2601.21294.pdf)  
**作者**：Anders Gjølbye, Ida Kargaard, Emma Kargaard, Lars Kai Hansen  

**一句话要点**：分析缺失数据下PLS-SVD的相变行为，揭示模态学习中信号恢复的临界阈值。

**关键词**：缺失数据处理, 偏最小二乘, 多模态学习, 相变分析, 高维统计

## 3 点简述
- 研究PLS-SVD在独立随机缺失数据下的性能，基于高维尖峰模型。
- 发现归一化后掩码交叉协方差信号强度衰减，导致BBP型相变。
- 通过模拟和半合成实验验证相变图和恢复曲线，支持理论预测。

## 摘要（原文）

> Partial Least Squares (PLS) learns shared structure from paired data via the top singular vectors of the empirical cross-covariance (PLS-SVD), but multimodal datasets often have missing entries in both views. We study PLS-SVD under independent entry-wise missing-completely-at-random masking in a proportional high-dimensional spiked model. After appropriate normalization, the masked cross-covariance behaves like a spiked rectangular random matrix whose effective signal strength is attenuated by $\sqrtρ$, where $ρ$ is the joint entry retention probability. As a result, PLS-SVD exhibits a sharp BBP-type phase transition: below a critical signal-to-noise threshold the leading singular vectors are asymptotically uninformative, while above it they achieve nontrivial alignment with the latent shared directions, with closed-form asymptotic overlap formulas. Simulations and semi-synthetic multimodal experiments corroborate the predicted phase diagram and recovery curves across aspect ratios, signal strengths, and missingness levels.

