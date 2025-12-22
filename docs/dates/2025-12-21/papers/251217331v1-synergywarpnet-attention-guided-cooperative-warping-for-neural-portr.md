---
layout: default
title: SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation
---

# SynergyWarpNet: Attention-Guided Cooperative Warping for Neural Portrait Animation
**arXiv**：[2512.17331v1](https://arxiv.org/abs/2512.17331) · [PDF](https://arxiv.org/pdf/2512.17331.pdf)  
**作者**：Shihang Li, Zhiqiang Gong, Minming Ye, Yue Gao, Wen Yao  

**一句话要点**：提出SynergyWarpNet，通过注意力引导的协同扭曲框架解决神经肖像动画中运动转移不准确和区域缺失问题。

**关键词**：神经肖像动画, 注意力引导扭曲, 3D光流, 跨注意力机制, 说话头部合成, 高保真度动画

## 3 点简述
- 核心问题：传统显式扭曲方法在运动转移和区域恢复上表现不佳，而基于注意力的方法复杂度高且几何基础弱。
- 方法要点：采用三阶段渐进式框架，包括显式扭曲、参考增强校正和置信度引导融合，结合3D光流和跨注意力机制。
- 实验或效果：在基准数据集上评估，展示了最先进的性能，实现高保真度的说话头部合成。

## 摘要（原文）

> Recent advances in neural portrait animation have demonstrated remarked potential for applications in virtual avatars, telepresence, and digital content creation. However, traditional explicit warping approaches often struggle with accurate motion transfer or recovering missing regions, while recent attention-based warping methods, though effective, frequently suffer from high complexity and weak geometric grounding. To address these issues, we propose SynergyWarpNet, an attention-guided cooperative warping framework designed for high-fidelity talking head synthesis. Given a source portrait, a driving image, and a set of reference images, our model progressively refines the animation in three stages. First, an explicit warping module performs coarse spatial alignment between the source and driving image using 3D dense optical flow. Next, a reference-augmented correction module leverages cross-attention across 3D keypoints and texture features from multiple reference images to semantically complete occluded or distorted regions. Finally, a confidence-guided fusion module integrates the warped outputs with spatially-adaptive fusing, using a learned confidence map to balance structural alignment and visual consistency. Comprehensive evaluations on benchmark datasets demonstrate state-of-the-art performance.

