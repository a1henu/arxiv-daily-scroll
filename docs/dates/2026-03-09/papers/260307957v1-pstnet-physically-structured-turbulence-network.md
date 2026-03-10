---
layout: default
title: PSTNet: Physically-Structured Turbulence Network
---

# PSTNet: Physically-Structured Turbulence Network
**arXiv**：[2603.07957v1](https://arxiv.org/abs/2603.07957) · [PDF](https://arxiv.org/pdf/2603.07957.pdf)  
**作者**：Boris Kriuk, Fedor Kriuk  

**一句话要点**：提出PSTNet以解决资源受限系统中大气湍流强度的实时估计问题

**关键词**：大气湍流估计, 物理结构网络, 资源受限系统, 实时估计, 轻量级架构, 嵌入式应用

## 3 点简述
- 核心问题：缺乏实时基础设施区域的大气湍流强度估计，传统方法无法保证物理定律遵循
- 方法要点：嵌入物理结构，包括零参数主干、专家子网络、特征调制层和输出约束
- 实验或效果：在340次仿真中验证，平均脱靶距离改善2.8%，存储小于2.5kB，运行时间低于12秒

## 摘要（原文）

> Reliable real-time estimation of atmospheric turbulence intensity remains an open challenge for aircraft operating across diverse altitude bands, particularly over oceanic, polar, and data-sparse regions that lack operational nowcasting infrastructure. Classical spectral models encode climatological averages rather than the instantaneous atmospheric state, and generic ML regressors offer adaptivity but provide no guarantee that predictions respect fundamental scaling laws. This paper introduces the Physically-Structured Turbulence Network (PSTNet), a lightweight architecture that embeds physics directly into its structure. PSTNet couples four components: (i) a zero-parameter backbone derived from Monin-Obukhov theory, (ii) a regime-gated mixture of specialist sub-networks supervised by Richardson-number-derived soft targets, (iii) Feature-wise Linear Modulation layers conditioning hidden representations on local air-density ratio, and (iv) a Kolmogorov output layer enforcing inertial-subrange scaling as an architectural constraint. The entire model contains only 552 learnable parameters, requiring fewer than 2.5 kB of storage and executing in under 12s on a Cortex-M7 microcontroller. We validate PSTNet on 340 paired six-degree-of-freedom guidance simulations spanning three vehicle classes (Mach 2.8, 4.5, and 8.0) and six operational categories with real-time satellite weather ingestion. PSTNet achieves a mean miss-distance improvement of +2.8% with a 78% win rate and a statistically significant effect size. Our results demonstrate that encoding domain physics as architectural priors yields a more efficient and interpretable path to turbulence estimation accuracy than scaling model capacity, establishing PSTNet as a viable drop-in replacement for legacy look-up tables in resource-constrained, safety-critical on-board guidance systems.

