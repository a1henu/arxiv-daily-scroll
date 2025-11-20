---
layout: default
title: MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation
---

# MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation
**arXiv**：[2511.15077v1](https://arxiv.org/abs/2511.15077) · [PDF](https://arxiv.org/pdf/2511.15077.pdf)  
**作者**：Shengjing Tian, Yinan Han, Xiantong Zhao, Xuehu Liu, Qi Lang  

**一句话要点**：提出MambaTrack3D框架，基于状态空间模型解决高时变LiDAR目标跟踪问题

**关键词**：3D目标跟踪, LiDAR点云, 状态空间模型, 高时变环境, 帧间传播, 特征增强

## 3 点简述
- 核心问题：高时变环境下，现有基于记忆的3D跟踪器存在计算复杂度高、时间冗余和几何先验利用不足
- 方法要点：设计Mamba模块实现帧间传播和分组特征增强，降低复杂度并减少冗余
- 实验或效果：在HTV基准上优于现有方法，标准数据集上保持竞争力，实现精度与效率平衡

## 摘要（原文）

> Dynamic outdoor environments with high temporal variation (HTV) pose significant challenges for 3D single object tracking in LiDAR point clouds. Existing memory-based trackers often suffer from quadratic computational complexity, temporal redundancy, and insufficient exploitation of geometric priors. To address these issues, we propose MambaTrack3D, a novel HTV-oriented tracking framework built upon the state space model Mamba. Specifically, we design a Mamba-based Inter-frame Propagation (MIP) module that replaces conventional single-frame feature extraction with efficient inter-frame propagation, achieving near-linear complexity while explicitly modeling spatial relations across historical frames. Furthermore, a Grouped Feature Enhancement Module (GFEM) is introduced to separate foreground and background semantics at the channel level, thereby mitigating temporal redundancy in the memory bank. Extensive experiments on KITTI-HTV and nuScenes-HTV benchmarks demonstrate that MambaTrack3D consistently outperforms both HTV-oriented and normal-scenario trackers, achieving improvements of up to 6.5 success and 9.5 precision over HVTrack under moderate temporal gaps. On the standard KITTI dataset, MambaTrack3D remains highly competitive with state-of-the-art normal-scenario trackers, confirming its strong generalization ability. Overall, MambaTrack3D achieves a superior accuracy-efficiency trade-off, delivering robust performance across both specialized HTV and conventional tracking scenarios.

