---
layout: default
title: SCENE OTA-FD: Self-Centering Noncoherent Estimator for Over-the-Air Federated Distillation
---

# SCENE OTA-FD: Self-Centering Noncoherent Estimator for Over-the-Air Federated Distillation
**arXiv**：[2602.15326v1](https://arxiv.org/abs/2602.15326) · [PDF](https://arxiv.org/pdf/2602.15326.pdf)  
**作者**：Hao Chen, Zavareh Bozorgasl  

**一句话要点**：提出SCENE方法，用于免导频、相位不变的空中联邦蒸馏聚合，适用于短相干和硬件受限场景。

**关键词**：空中联邦蒸馏, 非相干估计, 免导频聚合, 硬件友好传输, 短相干场景

## 3 点简述
- 核心问题：在短相干和硬件受限场景中，避免每轮信道状态信息开销，实现高效联邦蒸馏聚合。
- 方法要点：设备将软标签向量映射为非负发射能量，服务器通过自中心能量估计器去除噪声偏移，获得无偏加权平均估计。
- 实验或效果：方差随接收天线数和重复因子衰减，在导频开销显著时优于相干设计，提供收敛界和开销比较。

## 摘要（原文）

> We propose SCENE (Self-Centering Noncoherent Estimator), a pilot-free and phase-invariant aggregation primitive for over-the-air federated distillation (OTA-FD). Each device maps its soft-label (class-probability) vector to nonnegative transmit energies under constant per-round power and constant-envelope signaling (PAPR near 1). At the server, a self-centering energy estimator removes the noise-energy offset and yields an unbiased estimate of the weighted soft-label average, with variance decaying on the order of 1/(SM) in the number of receive antennas M and repetition factor S. We also develop a pilot-free ratio-normalized variant that cancels unknown large-scale gains, provide a convergence bound consistent with coherent OTA-FD analyses, and present an overhead-based crossover comparison. SCENE targets short-coherence and hardware-constrained regimes, where avoiding per-round CSI is essential: it trades a modest noncoherent variance constant for zero uplink pilots, unbiased aggregation, and hardware-friendly transmission, and can outperform coherent designs when pilot overhead is non-negligible.

