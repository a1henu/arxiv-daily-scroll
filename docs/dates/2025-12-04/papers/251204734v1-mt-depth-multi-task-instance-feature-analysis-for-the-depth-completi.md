---
layout: default
title: MT-Depth: Multi-task Instance feature analysis for the Depth Completion
---

# MT-Depth: Multi-task Instance feature analysis for the Depth Completion
**arXiv**：[2512.04734v1](https://arxiv.org/abs/2512.04734) · [PDF](https://arxiv.org/pdf/2512.04734.pdf)  
**作者**：Abdul Haseeb Nizamani, Dandi Zhou, Xinhai Sun  

**一句话要点**：提出实例感知深度补全框架，通过实例掩码空间先验提升稀疏深度数据补全精度

**关键词**：深度补全, 实例感知, 跨注意力融合, 稀疏深度数据, 3D感知系统

## 3 点简述
- 核心问题：现有深度补全方法依赖语义分割，忽略对象级理解，影响边界和遮挡区域精度
- 方法要点：结合YOLO V11实例分割、U-Net深度补全、跨注意力融合和注意力引导预测头
- 实验或效果：在Virtual KITTI 2数据集上验证，降低RMSE，提升对象边界和薄结构深度准确性

## 摘要（原文）

> Depth completion plays a vital role in 3D perception systems, especially in scenarios where sparse depth data must be densified for tasks such as autonomous driving, robotics, and augmented reality. While many existing approaches rely on semantic segmentation to guide depth completion, they often overlook the benefits of object-level understanding. In this work, we introduce an instance-aware depth completion framework that explicitly integrates binary instance masks as spatial priors to refine depth predictions. Our model combines four main components: a frozen YOLO V11 instance segmentation branch, a U-Net-based depth completion backbone, a cross-attention fusion module, and an attention-guided prediction head. The instance segmentation branch generates per-image foreground masks that guide the depth branch via cross-attention, allowing the network to focus on object-centric regions during refinement. We validate our method on the Virtual KITTI 2 dataset, showing that it achieves lower RMSE compared to both a U-Net-only baseline and previous semantic-guided methods, while maintaining competitive MAE. Qualitative and quantitative results demonstrate that the proposed model effectively enhances depth accuracy near object boundaries, occlusions, and thin structures. Our findings suggest that incorporating instance-aware cues offers a promising direction for improving depth completion without relying on dense semantic labels.

