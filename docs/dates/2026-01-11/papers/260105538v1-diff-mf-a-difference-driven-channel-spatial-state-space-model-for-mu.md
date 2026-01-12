---
layout: default
title: DIFF-MF: A Difference-Driven Channel-Spatial State Space Model for Multi-Modal Image Fusion
---

# DIFF-MF: A Difference-Driven Channel-Spatial State Space Model for Multi-Modal Image Fusion
**arXiv**：[2601.05538v1](https://arxiv.org/abs/2601.05538) · [PDF](https://arxiv.org/pdf/2601.05538.pdf)  
**作者**：Yiming Sun, Zifan Ye, Qinghua Hu, Pengfei Zhu  

**一句话要点**：提出DIFF-MF模型，通过差异驱动通道空间状态空间建模解决多模态图像融合中红外与可见光信息失衡问题。

**关键词**：多模态图像融合, 状态空间模型, 通道空间建模, 差异驱动, 红外可见光融合, 计算效率

## 3 点简述
- 核心问题：现有状态空间模型在多模态图像融合中易过度偏重红外强度或可见细节，导致互补信息整合不足。
- 方法要点：利用模态间特征差异图引导特征提取，结合通道交换和空间交换模块实现自适应通道重加权与全局空间融合。
- 实验或效果：在驾驶场景和低空无人机数据集上，DIFF-MF在视觉质量和定量评估上优于现有方法，保持线性计算复杂度。

## 摘要（原文）

> Multi-modal image fusion aims to integrate complementary information from multiple source images to produce high-quality fused images with enriched content. Although existing approaches based on state space model have achieved satisfied performance with high computational efficiency, they tend to either over-prioritize infrared intensity at the cost of visible details, or conversely, preserve visible structure while diminishing thermal target salience. To overcome these challenges, we propose DIFF-MF, a novel difference-driven channel-spatial state space model for multi-modal image fusion. Our approach leverages feature discrepancy maps between modalities to guide feature extraction, followed by a fusion process across both channel and spatial dimensions. In the channel dimension, a channel-exchange module enhances channel-wise interaction through cross-attention dual state space modeling, enabling adaptive feature reweighting. In the spatial dimension, a spatial-exchange module employs cross-modal state space scanning to achieve comprehensive spatial fusion. By efficiently capturing global dependencies while maintaining linear computational complexity, DIFF-MF effectively integrates complementary multi-modal features. Experimental results on the driving scenarios and low-altitude UAV datasets demonstrate that our method outperforms existing approaches in both visual quality and quantitative evaluation.

