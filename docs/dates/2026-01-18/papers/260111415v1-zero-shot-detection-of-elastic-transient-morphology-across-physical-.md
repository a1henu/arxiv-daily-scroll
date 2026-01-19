---
layout: default
title: Zero-Shot Detection of Elastic Transient Morphology Across Physical Systems
---

# Zero-Shot Detection of Elastic Transient Morphology Across Physical Systems
**arXiv**：[2601.11415v1](https://arxiv.org/abs/2601.11415) · [PDF](https://arxiv.org/pdf/2601.11415.pdf)  
**作者**：Jose Sánchez Andreu  

**一句话要点**：提出基于引力波干涉仪瞬态形态的零样本检测方法，用于跨物理系统的弹性瞬态异常监测。

**关键词**：零样本检测, 弹性瞬态形态, 跨物理系统, 异常监测, 神经编码器, 引力波干涉仪

## 3 点简述
- 核心问题：如何实现跨传感器零样本检测弹性瞬态异常，无需目标域标签或再训练。
- 方法要点：使用引力波干涉仪非高斯噪声训练的神经编码器作为冻结形态敏感算子。
- 实验效果：在轴承故障数据集上实现高精度异常检测，在电气振动信号中表现弱，界定物理转移边界。

## 摘要（原文）

> We test whether a representation learned from interferometric strain transients in gravitational-wave observatories can act as a frozen morphology-sensitive operator for unseen sensors, provided the target signals preserve coherent elastic transient structure. Using a neural encoder trained exclusively on non-Gaussian instrumental glitches, we perform strict zero-shot anomaly analysis on rolling-element bearings without retraining, fine-tuning, or target-domain labels.
>   On the IMS-NASA run-to-failure dataset, the operator yields a monotonic health index HI(t) = s0.99(t)/tau normalized to an early-life reference distribution, enabling fixed false-alarm monitoring at 1-q = 1e-3 with tau = Q0.999(P0). In discrete fault regimes (CWRU), it achieves strong window-level discrimination (AUC_win about 0.90) and file-level separability approaching unity (AUC_file about 0.99). Electrically dominated vibration signals (VSB) show weak, non-selective behavior, delineating a physical boundary for transfer.
>   Under a matched IMS controlled-split protocol, a generic EfficientNet-B0 encoder pretrained on ImageNet collapses in the intermittent regime (Lambda_tail about 2), while the interferometric operator retains strong extreme-event selectivity (Lambda_tail about 860), indicating that the effect is not a generic property of CNN features. Controlled morphology-destruction transformations selectively degrade performance despite per-window normalization, consistent with sensitivity to coherent time-frequency organization rather than marginal amplitude statistics.

