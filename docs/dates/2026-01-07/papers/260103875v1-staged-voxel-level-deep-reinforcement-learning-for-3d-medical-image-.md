---
layout: default
title: Staged Voxel-Level Deep Reinforcement Learning for 3D Medical Image Segmentation with Noisy Annotations
---

# Staged Voxel-Level Deep Reinforcement Learning for 3D Medical Image Segmentation with Noisy Annotations
**arXiv**：[2601.03875v1](https://arxiv.org/abs/2601.03875) · [PDF](https://arxiv.org/pdf/2601.03875.pdf)  
**作者**：Yuyang Fu, Xiuzhen Guo, Ji Shi  

**一句话要点**：提出SVL-DRL框架以解决带噪声标注的3D医学图像分割问题

**关键词**：医学图像分割, 噪声标注, 强化学习, 体素级处理, 3D图像分析

## 3 点简述
- 核心问题：医学图像分割中噪声标注因器官形态复杂和标注者差异而普遍存在，限制模型性能。
- 方法要点：采用分阶段强化学习框架，将每个体素视为自主代理，通过vA3C模块和复合奖励函数动态修正标签错误。
- 实验或效果：在三个公开数据集上实现SOTA性能，Dice和IoU分数平均提升超过3%。

## 摘要（原文）

> Deep learning has achieved significant advancements in medical image segmentation. Currently, obtaining accurate segmentation outcomes is critically reliant on large-scale datasets with high-quality annotations. However, noisy annotations are frequently encountered owing to the complex morphological structures of organs in medical images and variations among different annotators, which can substantially limit the efficacy of segmentation models. Motivated by the fact that medical imaging annotator can correct labeling errors during segmentation based on prior knowledge, we propose an end-to-end Staged Voxel-Level Deep Reinforcement Learning (SVL-DRL) framework for robust medical image segmentation under noisy annotations. This framework employs a dynamic iterative update strategy to automatically mitigate the impact of erroneous labels without requiring manual intervention. The key advancements of SVL-DRL over existing works include: i) formulating noisy annotations as a voxel-dependent problem and addressing it through a novel staged reinforcement learning framework which guarantees robust model convergence; ii) incorporating a voxel-level asynchronous advantage actor-critic (vA3C) module that conceptualizes each voxel as an autonomous agent, which allows each agent to dynamically refine its own state representation during training, thereby directly mitigating the influence of erroneous labels; iii) designing a novel action space for the agents, along with a composite reward function that strategically combines the Dice value and a spatial continuity metric to significantly boost segmentation accuracy while maintain semantic integrity. Experiments on three public medical image datasets demonstrates State-of-The-Art (SoTA) performance under various experimental settings, with an average improvement of over 3\% in both Dice and IoU scores.

