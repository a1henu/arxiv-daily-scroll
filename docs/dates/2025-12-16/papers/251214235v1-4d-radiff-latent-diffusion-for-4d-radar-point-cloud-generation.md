---
layout: default
title: 4D-RaDiff: Latent Diffusion for 4D Radar Point Cloud Generation
---

# 4D-RaDiff: Latent Diffusion for 4D Radar Point Cloud Generation
**arXiv**：[2512.14235v1](https://arxiv.org/abs/2512.14235) · [PDF](https://arxiv.org/pdf/2512.14235.pdf)  
**作者**：Jimmie Kwok, Holger Caesar, Andras Palffy  

**一句话要点**：提出4D-RaDiff框架，通过潜在扩散生成4D雷达点云以解决标注数据不足问题

**关键词**：4D雷达点云生成, 潜在扩散模型, 自动驾驶感知, 数据增强, 对象检测

## 3 点简述
- 核心问题：自动驾驶雷达感知系统因标注雷达数据有限而面临挑战
- 方法要点：在潜在点云表示上应用扩散模型，考虑雷达点云的稀疏性和特性，支持对象或场景级条件控制
- 实验或效果：合成数据作为增强方法提升检测性能，预训练可减少90%标注数据需求

## 摘要（原文）

> Automotive radar has shown promising developments in environment perception due to its cost-effectiveness and robustness in adverse weather conditions. However, the limited availability of annotated radar data poses a significant challenge for advancing radar-based perception systems. To address this limitation, we propose a novel framework to generate 4D radar point clouds for training and evaluating object detectors. Unlike image-based diffusion, our method is designed to consider the sparsity and unique characteristics of radar point clouds by applying diffusion to a latent point cloud representation. Within this latent space, generation is controlled via conditioning at either the object or scene level. The proposed 4D-RaDiff converts unlabeled bounding boxes into high-quality radar annotations and transforms existing LiDAR point cloud data into realistic radar scenes. Experiments demonstrate that incorporating synthetic radar data of 4D-RaDiff as data augmentation method during training consistently improves object detection performance compared to training on real data only. In addition, pre-training on our synthetic data reduces the amount of required annotated radar data by up to 90% while achieving comparable object detection performance.

