---
layout: default
title: Keyframe-Based Feed-Forward Visual Odometry
---

# Keyframe-Based Feed-Forward Visual Odometry
**arXiv**：[2601.16020v1](https://arxiv.org/abs/2601.16020) · [PDF](https://arxiv.org/pdf/2601.16020.pdf)  
**作者**：Weichen Dai, Wenhan Su, Da Kong, Yuhang Ming, Wanzeng Kong  

**一句话要点**：提出基于关键帧的强化学习视觉里程计，以提升前馈网络效率与精度

**关键词**：视觉里程计, 关键帧选择, 强化学习, 前馈网络, 视觉基础模型

## 3 点简述
- 问题：现有视觉基础模型处理图像序列时忽略关键帧，导致计算冗余和性能下降
- 方法：使用强化学习自适应选择关键帧，替代手工规则，适应模型内在特征
- 效果：在多个真实数据集上评估，相比先进方法实现一致且显著的改进

## 摘要（原文）

> The emergence of visual foundation models has revolutionized visual odometry~(VO) and SLAM, enabling pose estimation and dense reconstruction within a single feed-forward network. However, unlike traditional pipelines that leverage keyframe methods to enhance efficiency and accuracy, current foundation model based methods, such as VGGT-Long, typically process raw image sequences indiscriminately. This leads to computational redundancy and degraded performance caused by low inter-frame parallax, which provides limited contextual stereo information. Integrating traditional geometric heuristics into these methods is non-trivial, as their performance depends on high-dimensional latent representations rather than explicit geometric metrics. To bridge this gap, we propose a novel keyframe-based feed-forward VO. Instead of relying on hand-crafted rules, our approach employs reinforcement learning to derive an adaptive keyframe policy in a data-driven manner, aligning selection with the intrinsic characteristics of the underlying foundation model. We train our agent on TartanAir dataset and conduct extensive evaluations across several real-world datasets. Experimental results demonstrate that the proposed method achieves consistent and substantial improvements over state-of-the-art feed-forward VO methods.

