---
layout: default
title: ReScene4D: Temporally Consistent Semantic Instance Segmentation of Evolving Indoor 3D Scenes
---

# ReScene4D: Temporally Consistent Semantic Instance Segmentation of Evolving Indoor 3D Scenes
**arXiv**：[2601.11508v1](https://arxiv.org/abs/2601.11508) · [PDF](https://arxiv.org/pdf/2601.11508.pdf)  
**作者**：Emily Steiner, Jianhao Zheng, Henry Howard-Jenkins, Chris Xie, Iro Armeni  

**一句话要点**：提出ReScene4D方法，用于稀疏时间4D室内语义实例分割，以处理演化室内场景的时序一致性

**关键词**：4D语义实例分割, 时序一致性, 室内场景演化, 稀疏观测, 3RScan数据集, t-mAP指标

## 3 点简述
- 核心问题：室内环境随时间演化，现有3DSIS方法缺乏时序推理，4D LiDAR方法依赖高频测量，不适用于稀疏观测场景
- 方法要点：基于3DSIS架构，通过跨观测信息共享实现时序一致的实例跟踪，无需密集观测
- 实验或效果：在3RScan数据集上达到最先进性能，定义新指标t-mAP评估时序一致性

## 摘要（原文）

> Indoor environments evolve as objects move, appear, or disappear. Capturing these dynamics requires maintaining temporally consistent instance identities across intermittently captured 3D scans, even when changes are unobserved. We introduce and formalize the task of temporally sparse 4D indoor semantic instance segmentation (SIS), which jointly segments, identifies, and temporally associates object instances. This setting poses a challenge for existing 3DSIS methods, which require a discrete matching step due to their lack of temporal reasoning, and for 4D LiDAR approaches, which perform poorly due to their reliance on high-frequency temporal measurements that are uncommon in the longer-horizon evolution of indoor environments. We propose ReScene4D, a novel method that adapts 3DSIS architectures for 4DSIS without needing dense observations. It explores strategies to share information across observations, demonstrating that this shared context not only enables consistent instance tracking but also improves standard 3DSIS quality. To evaluate this task, we define a new metric, t-mAP, that extends mAP to reward temporal identity consistency. ReScene4D achieves state-of-the-art performance on the 3RScan dataset, establishing a new benchmark for understanding evolving indoor scenes.

