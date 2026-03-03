---
layout: default
title: SCATR: Mitigating New Instance Suppression in LiDAR-based Tracking-by-Attention via Second Chance Assignment and Track Query Dropout
---

# SCATR: Mitigating New Instance Suppression in LiDAR-based Tracking-by-Attention via Second Chance Assignment and Track Query Dropout
**arXiv**：[2603.01485v1](https://arxiv.org/abs/2603.01485) · [PDF](https://arxiv.org/pdf/2603.01485.pdf)  
**作者**：Brian Cheong, Letian Wang, Sandro Papais, Steven L. Waslander  

**一句话要点**：提出SCATR模型，通过第二机会分配和轨迹查询丢弃解决LiDAR跟踪中注意力框架的新实例抑制问题。

**关键词**：LiDAR跟踪, 注意力机制, 第二机会分配, 轨迹查询丢弃, nuScenes基准, 假阴性缓解

## 3 点简述
- 核心问题：LiDAR基于注意力的跟踪框架存在高假阴性错误，导致性能低于传统检测跟踪方法。
- 方法要点：引入第二机会分配和轨迹查询丢弃两种训练策略，优化跟踪查询分配和增强模型鲁棒性。
- 实验效果：在nuScenes基准测试中实现最先进性能，缩小了注意力与检测跟踪方法的性能差距。

## 摘要（原文）

> LiDAR-based tracking-by-attention (TBA) frameworks inherently suffer from high false negative errors, leading to a significant performance gap compared to traditional LiDAR-based tracking-by-detection (TBD) methods. This paper introduces SCATR, a novel LiDAR-based TBA model designed to address this fundamental challenge systematically. SCATR leverages recent progress in vision-based tracking and incorporates targeted training strategies specifically adapted for LiDAR.
>   Our work's core innovations are two architecture-agnostic training strategies for TBA methods: Second Chance Assignment and Track Query Dropout.
>   Second Chance Assignment is a novel ground truth assignment that concatenates unassigned track queries to the proposal queries before bipartite matching, giving these track queries a second chance to be assigned to a ground truth object and effectively mitigating the conflict between detection and tracking tasks inherent in tracking-by-attention.
>   Track Query Dropout is a training method that diversifies supervised object query configurations to efficiently train the decoder to handle different track query sets, enhancing robustness to missing or newborn tracks.
>   Experiments on the nuScenes tracking benchmark demonstrate that SCATR achieves state-of-the-art performance among LiDAR-based TBA methods, outperforming previous works by 7.6\% AMOTA and successfully bridging the long-standing performance gap between LiDAR-based TBA and TBD methods.
>   Ablation studies further validate the effectiveness and generalization of Second Chance Assignment and Track Query Dropout.
>   Code can be found at the following link: \href{https://github.com/TRAILab/SCATR}{https://github.com/TRAILab/SCATR}

