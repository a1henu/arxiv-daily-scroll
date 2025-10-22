---
layout: default
title: Descriptor: Occluded nuScenes: A Multi-Sensor Dataset for Evaluating Perception Robustness in Automated Driving
---

# Descriptor: Occluded nuScenes: A Multi-Sensor Dataset for Evaluating Perception Robustness in Automated Driving
**arXiv**：[2510.18552v1](https://arxiv.org/abs/2510.18552) · [PDF](https://arxiv.org/pdf/2510.18552.pdf)  
**作者**：Sanjay Kumar, Tim Brophy, Reenu Mohandas, Eoin Martino Grua, Ganesh Sistu, Valentina Donzella, Ciaran Eising  

**一句话要点**：提出Occluded nuScenes数据集以评估自动驾驶感知在传感器遮挡下的鲁棒性

**关键词**：自动驾驶感知, 多传感器数据集, 传感器遮挡, 鲁棒性评估, nuScenes扩展

## 3 点简述
- 核心问题：现有数据集缺乏可控多传感器退化，限制感知模型在不良条件下的系统评估
- 方法要点：扩展nuScenes，提供相机、雷达和LiDAR的参数化遮挡脚本，支持可重复数据生成
- 实验或效果：未知具体性能提升，但资源支持一致、可重复的感知模型评估

## 摘要（原文）

> Robust perception in automated driving requires reliable performance under
> adverse conditions, where sensors may be affected by partial failures or
> environmental occlusions. Although existing autonomous driving datasets
> inherently contain sensor noise and environmental variability, very few enable
> controlled, parameterised, and reproducible degradations across multiple
> sensing modalities. This gap limits the ability to systematically evaluate how
> perception and fusion architectures perform under well-defined adverse
> conditions. To address this limitation, we introduce the Occluded nuScenes
> Dataset, a novel extension of the widely used nuScenes benchmark. For the
> camera modality, we release both the full and mini versions with four types of
> occlusions, two adapted from public implementations and two newly designed. For
> radar and LiDAR, we provide parameterised occlusion scripts that implement
> three types of degradations each, enabling flexible and repeatable generation
> of occluded data. This resource supports consistent, reproducible evaluation of
> perception models under partial sensor failures and environmental interference.
> By releasing the first multi-sensor occlusion dataset with controlled and
> reproducible degradations, we aim to advance research on robust sensor fusion,
> resilience analysis, and safety-critical perception in automated driving.

