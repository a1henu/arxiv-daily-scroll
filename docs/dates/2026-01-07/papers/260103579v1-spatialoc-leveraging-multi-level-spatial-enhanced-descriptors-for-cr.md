---
layout: default
title: SpatiaLoc: Leveraging Multi-Level Spatial Enhanced Descriptors for Cross-Modal Localization
---

# SpatiaLoc: Leveraging Multi-Level Spatial Enhanced Descriptors for Cross-Modal Localization
**arXiv**：[2601.03579v1](https://arxiv.org/abs/2601.03579) · [PDF](https://arxiv.org/pdf/2601.03579.pdf)  
**作者**：Tianyi Shang, Pengjie Xu, Zhaojun Deng, Zhenyu Li, Zhicong Chen, Lijun Wu  

**一句话要点**：提出SpatiaLoc框架，利用多级空间增强描述符解决文本与点云跨模态定位问题。

**关键词**：跨模态定位, 空间关系建模, 点云处理, 文本描述, 机器人导航, 不确定性估计

## 3 点简述
- 核心问题：跨模态定位中，文本与点云间的空间关系是关键判别线索，用于机器人自主导航和人机交互。
- 方法要点：采用粗到细策略，粗阶段使用BEOSE和FAE编码实例级和全局级空间关系，细阶段用UGFL回归位置并建模不确定性。
- 实验或效果：在KITTI360Pose数据集上，SpatiaLoc显著优于现有最先进方法。

## 摘要（原文）

> Cross-modal localization using text and point clouds enables robots to localize themselves via natural language descriptions, with applications in autonomous navigation and interaction between humans and robots. In this task, objects often recur across text and point clouds, making spatial relationships the most discriminative cues for localization. Given this characteristic, we present SpatiaLoc, a framework utilizing a coarse-to-fine strategy that emphasizes spatial relationships at both the instance and global levels. In the coarse stage, we introduce a Bezier Enhanced Object Spatial Encoder (BEOSE) that models spatial relationships at the instance level using quadratic Bezier curves. Additionally, a Frequency Aware Encoder (FAE) generates spatial representations in the frequency domain at the global level. In the fine stage, an Uncertainty Aware Gaussian Fine Localizer (UGFL) regresses 2D positions by modeling predictions as Gaussian distributions with a loss function aware of uncertainty. Extensive experiments on KITTI360Pose demonstrate that SpatiaLoc significantly outperforms existing state-of-the-art (SOTA) methods.

