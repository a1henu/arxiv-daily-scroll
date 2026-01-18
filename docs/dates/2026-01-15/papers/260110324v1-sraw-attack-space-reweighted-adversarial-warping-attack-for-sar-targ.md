---
layout: default
title: SRAW-Attack: Space-Reweighted Adversarial Warping Attack for SAR Target Recognition
---

# SRAW-Attack: Space-Reweighted Adversarial Warping Attack for SAR Target Recognition
**arXiv**：[2601.10324v1](https://arxiv.org/abs/2601.10324) · [PDF](https://arxiv.org/pdf/2601.10324.pdf)  
**作者**：Yiming Zhang, Weibo Qin, Yuntian Liu, Feng Wang  

**一句话要点**：提出空间重加权对抗扭曲攻击方法，以提升合成孔径雷达目标识别中的对抗攻击隐蔽性与效果。

**关键词**：合成孔径雷达目标识别, 对抗攻击, 空间变形, 信息稀疏, 对抗迁移性

## 3 点简述
- 核心问题：SAR图像信息稀疏，现有对抗攻击需明显失真，且模型易过度依赖背景区域。
- 方法要点：通过优化空间变形，在前景和背景区域分配重加权预算，生成对抗样本。
- 实验或效果：显著降低SAR-ATR模型性能，在隐蔽性和对抗迁移性上优于现有方法。

## 摘要（原文）

> Synthetic aperture radar (SAR) imagery exhibits intrinsic information sparsity due to its unique electromagnetic scattering mechanism. Despite the widespread adoption of deep neural network (DNN)-based SAR automatic target recognition (SAR-ATR) systems, they remain vulnerable to adversarial examples and tend to over-rely on background regions, leading to degraded adversarial robustness. Existing adversarial attacks for SAR-ATR often require visually perceptible distortions to achieve effective performance, thereby necessitating an attack method that balances effectiveness and stealthiness. In this paper, a novel attack method termed Space-Reweighted Adversarial Warping (SRAW) is proposed, which generates adversarial examples through optimized spatial deformation with reweighted budgets across foreground and background regions. Extensive experiments demonstrate that SRAW significantly degrades the performance of state-of-the-art SAR-ATR models and consistently outperforms existing methods in terms of imperceptibility and adversarial transferability. Code is made available at https://github.com/boremycin/SAR-ATR-TransAttack.

