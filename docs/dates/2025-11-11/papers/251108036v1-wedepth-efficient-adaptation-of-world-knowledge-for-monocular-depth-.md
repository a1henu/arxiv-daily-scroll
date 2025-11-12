---
layout: default
title: WEDepth: Efficient Adaptation of World Knowledge for Monocular Depth Estimation
---

# WEDepth: Efficient Adaptation of World Knowledge for Monocular Depth Estimation
**arXiv**：[2511.08036v1](https://arxiv.org/abs/2511.08036) · [PDF](https://arxiv.org/pdf/2511.08036.pdf)  
**作者**：Gongshu Wang, Zhirui Wang, Kan Yang  

**一句话要点**：提出WEDepth以高效适配世界知识用于单目深度估计

**关键词**：单目深度估计, 视觉基础模型, 特征增强, 零样本迁移, 世界知识适配

## 3 点简述
- 单目深度估计因从单张2D图像重建3D场景而具有挑战性
- 方法利用视觉基础模型作为多级特征增强器，不修改其结构或权重
- 在NYU-Depth v2和KITTI数据集上实现SOTA，并展示强零样本迁移能力

## 摘要（原文）

> Monocular depth estimation (MDE) has widely applicable but remains highly challenging due to the inherently ill-posed nature of reconstructing 3D scenes from single 2D images. Modern Vision Foundation Models (VFMs), pre-trained on large-scale diverse datasets, exhibit remarkable world understanding capabilities that benefit for various vision tasks. Recent studies have demonstrated significant improvements in MDE through fine-tuning these VFMs. Inspired by these developments, we propose WEDepth, a novel approach that adapts VFMs for MDE without modi-fying their structures and pretrained weights, while effec-tively eliciting and leveraging their inherent priors. Our method employs the VFM as a multi-level feature en-hancer, systematically injecting prior knowledge at differ-ent representation levels. Experiments on NYU-Depth v2 and KITTI datasets show that WEDepth establishes new state-of-the-art (SOTA) performance, achieving competi-tive results compared to both diffusion-based approaches (which require multiple forward passes) and methods pre-trained on relative depth. Furthermore, we demonstrate our method exhibits strong zero-shot transfer capability across diverse scenarios.

