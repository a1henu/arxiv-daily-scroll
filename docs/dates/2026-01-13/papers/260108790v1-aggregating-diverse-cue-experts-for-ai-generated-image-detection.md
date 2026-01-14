---
layout: default
title: Aggregating Diverse Cue Experts for AI-Generated Image Detection
---

# Aggregating Diverse Cue Experts for AI-Generated Image Detection
**arXiv**：[2601.08790v1](https://arxiv.org/abs/2601.08790) · [PDF](https://arxiv.org/pdf/2601.08790.pdf)  
**作者**：Lei Tan, Shuwei Li, Mohan Kankanhalli, Robby T. Tan  

**一句话要点**：提出多线索聚合网络以提升AI生成图像检测的跨模型泛化能力

**关键词**：AI生成图像检测, 多线索聚合, 跨模型泛化, 频率域分析, 色度不一致性, 混合编码器

## 3 点简述
- 核心问题：现有检测器依赖模型特定特征，导致过拟合和泛化差
- 方法要点：集成空间、频域和色度线索，通过混合编码器适配器动态处理
- 实验或效果：在GenImage等基准上验证，平均准确率最高提升7.4%

## 摘要（原文）

> The rapid emergence of image synthesis models poses challenges to the generalization of AI-generated image detectors. However, existing methods often rely on model-specific features, leading to overfitting and poor generalization. In this paper, we introduce the Multi-Cue Aggregation Network (MCAN), a novel framework that integrates different yet complementary cues in a unified network. MCAN employs a mixture-of-encoders adapter to dynamically process these cues, enabling more adaptive and robust feature representation. Our cues include the input image itself, which represents the overall content, and high-frequency components that emphasize edge details. Additionally, we introduce a Chromatic Inconsistency (CI) cue, which normalizes intensity values and captures noise information introduced during the image acquisition process in real images, making these noise patterns more distinguishable from those in AI-generated content. Unlike prior methods, MCAN's novelty lies in its unified multi-cue aggregation framework, which integrates spatial, frequency-domain, and chromaticity-based information for enhanced representation learning. These cues are intrinsically more indicative of real images, enhancing cross-model generalization. Extensive experiments on the GenImage, Chameleon, and UniversalFakeDetect benchmark validate the state-of-the-art performance of MCAN. In the GenImage dataset, MCAN outperforms the best state-of-the-art method by up to 7.4% in average ACC across eight different image generators.

