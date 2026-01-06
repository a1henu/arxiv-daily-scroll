---
layout: default
title: FMVP: Masked Flow Matching for Adversarial Video Purification
---

# FMVP: Masked Flow Matching for Adversarial Video Purification
**arXiv**：[2601.02228v1](https://arxiv.org/abs/2601.02228) · [PDF](https://arxiv.org/pdf/2601.02228.pdf)  
**作者**：Duoxun Tang, Xueyi Zhang, Chak Hin Wang, Xi Xiao, Dasen Dai, Xinhang Jiang, Wentao Shi, Rui Li, Qing Li  

**一句话要点**：提出FMVP方法，通过掩码流匹配对抗视频净化，提升视频识别模型的鲁棒性。

**关键词**：对抗视频净化, 流匹配, 掩码策略, 频率门控损失, 鲁棒性评估, 零样本检测

## 3 点简述
- 视频识别模型易受对抗攻击，现有扩散净化方法采样效率低且轨迹弯曲。
- FMVP使用掩码策略破坏对抗结构，结合条件流匹配和修复目标重建干净视频动态。
- 实验显示FMVP在UCF-101和HMDB-51上优于现有方法，对PGD和CW攻击鲁棒性高。

## 摘要（原文）

> Video recognition models remain vulnerable to adversarial attacks, while existing diffusion-based purification methods suffer from inefficient sampling and curved trajectories. Directly regressing clean videos from adversarial inputs often fails to recover faithful content due to the subtle nature of perturbations; this necessitates physically shattering the adversarial structure. Therefore, we propose Flow Matching for Adversarial Video Purification FMVP. FMVP physically shatters global adversarial structures via a masking strategy and reconstructs clean video dynamics using Conditional Flow Matching (CFM) with an inpainting objective. To further decouple semantic content from adversarial noise, we design a Frequency-Gated Loss (FGL) that explicitly suppresses high-frequency adversarial residuals while preserving low-frequency fidelity. We design Attack-Aware and Generalist training paradigms to handle known and unknown threats, respectively. Extensive experiments on UCF-101 and HMDB-51 demonstrate that FMVP outperforms state-of-the-art methods (DiffPure, Defense Patterns (DP), Temporal Shuffling (TS) and FlowPure), achieving robust accuracy exceeding 87% against PGD and 89% against CW attacks. Furthermore, FMVP demonstrates superior robustness against adaptive attacks (DiffHammer) and functions as a zero-shot adversarial detector, attaining detection accuracies of 98% for PGD and 79% for highly imperceptible CW attacks.

