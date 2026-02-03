---
layout: default
title: FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation
---

# FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation
**arXiv**：[2602.02142v1](https://arxiv.org/abs/2602.02142) · [PDF](https://arxiv.org/pdf/2602.02142.pdf)  
**作者**：Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis E. H. Tay, Marcelo H. Ang, Haiyue Zhu  

**一句话要点**：提出FD-VLA框架，通过力蒸馏模块在无物理力传感器下实现接触丰富操作的力感知VLA模型。

**关键词**：视觉-语言-动作模型, 力感知, 接触丰富操作, 蒸馏训练, 跨模态对齐, 机器人操作

## 3 点简述
- 核心问题：接触丰富操作中力感知对VLA框架至关重要，但依赖物理力传感器增加硬件成本与复杂性。
- 方法要点：设计力蒸馏模块，将视觉观察和机器人状态映射为预测力令牌，注入预训练VLM实现力感知推理。
- 实验或效果：物理实验显示蒸馏力令牌优于直接传感器测量，提升跨模态对齐和操作鲁棒性。

## 摘要（原文）

> Force sensing is a crucial modality for Vision-Language-Action (VLA) frameworks, as it enables fine-grained perception and dexterous manipulation in contact-rich tasks. We present Force-Distilled VLA (FD-VLA), a novel framework that integrates force awareness into contact-rich manipulation without relying on physical force sensors. The core of our approach is a Force Distillation Module (FDM), which distills force by mapping a learnable query token, conditioned on visual observations and robot states, into a predicted force token aligned with the latent representation of actual force signals. During inference, this distilled force token is injected into the pretrained VLM, enabling force-aware reasoning while preserving the integrity of its vision-language semantics. This design provides two key benefits: first, it allows practical deployment across a wide range of robots that lack expensive or fragile force-torque sensors, thereby reducing hardware cost and complexity; second, the FDM introduces an additional force-vision-state fusion prior to the VLM, which improves cross-modal alignment and enhances perception-action robustness in contact-rich scenarios. Surprisingly, our physical experiments show that the distilled force token outperforms direct sensor force measurements as well as other baselines, which highlights the effectiveness of this force-distilled VLA approach.

