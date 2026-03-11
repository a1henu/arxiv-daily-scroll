---
layout: default
title: From Ideal to Real: Stable Video Object Removal under Imperfect Conditions
---

# From Ideal to Real: Stable Video Object Removal under Imperfect Conditions
**arXiv**：[2603.09283v1](https://arxiv.org/abs/2603.09283) · [PDF](https://arxiv.org/pdf/2603.09283.pdf)  
**作者**：Jiagao Hu, Yuxuan Chen, Fuhao Li, Zepeng Wang, Fei Wang, Daiguo Zhou, Jian Luan  

**一句话要点**：提出SVOR框架以解决视频对象移除在阴影、突变运动等不完美条件下的稳定性问题

**关键词**：视频对象移除, 扩散模型, 时间稳定性, 掩码处理, 鲁棒性训练, 跨域应用

## 3 点简述
- 核心问题：现有扩散模型在真实世界缺陷下难以保持视频修复的时间稳定性和视觉一致性
- 方法要点：通过MUSE、DA-Seg和课程两阶段训练实现鲁棒移除，处理阴影、闪烁和掩码缺陷
- 实验或效果：在多个数据集和退化掩码基准测试中达到新SOTA，提升跨域鲁棒性

## 摘要（原文）

> Removing objects from videos remains difficult in the presence of real-world imperfections such as shadows, abrupt motion, and defective masks. Existing diffusion-based video inpainting models often struggle to maintain temporal stability and visual consistency under these challenges. We propose Stable Video Object Removal (SVOR), a robust framework that achieves shadow-free, flicker-free, and mask-defect-tolerant removal through three key designs: (1) Mask Union for Stable Erasure (MUSE), a windowed union strategy applied during temporal mask downsampling to preserve all target regions observed within each window, effectively handling abrupt motion and reducing missed removals; (2) Denoising-Aware Segmentation (DA-Seg), a lightweight segmentation head on a decoupled side branch equipped with Denoising-Aware AdaLN and trained with mask degradation to provide an internal diffusion-aware localization prior without affecting content generation; and (3) Curriculum Two-Stage Training: where Stage I performs self-supervised pretraining on unpaired real-background videos with online random masks to learn realistic background and temporal priors, and Stage II refines on synthetic pairs using mask degradation and side-effect-weighted losses, jointly removing objects and their associated shadows/reflections while improving cross-domain robustness. Extensive experiments show that SVOR attains new state-of-the-art results across multiple datasets and degraded-mask benchmarks, advancing video object removal from ideal settings toward real-world applications.

