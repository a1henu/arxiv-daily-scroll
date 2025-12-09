---
layout: default
title: Online Segment Any 3D Thing as Instance Tracking
---

# Online Segment Any 3D Thing as Instance Tracking
**arXiv**：[2512.07599v1](https://arxiv.org/abs/2512.07599) · [PDF](https://arxiv.org/pdf/2512.07599.pdf)  
**作者**：Hanshi Wang, Zijian Cai, Jin Gao, Yiwei Zhang, Weiming Hu, Ke Wang, Zhipeng Zhang  

**一句话要点**：提出AutoSeg3D方法，将在线3D分割重构为实例跟踪问题，以增强具身智能体的动态环境感知能力。

**关键词**：在线3D分割, 实例跟踪, 时间信息传播, 空间一致性学习, 具身智能体, 点云处理

## 3 点简述
- 核心问题：现有基于查询的3D分割方法忽视时间维度，难以处理动态环境中的部分可见对象。
- 方法要点：利用对象查询进行时间信息传播，结合长期关联和短期更新，并引入空间一致性学习。
- 实验或效果：在ScanNet200等数据集上超越ESAM，达到新SOTA，提升分割精度和一致性。

## 摘要（原文）

> Online, real-time, and fine-grained 3D segmentation constitutes a fundamental capability for embodied intelligent agents to perceive and comprehend their operational environments. Recent advancements employ predefined object queries to aggregate semantic information from Vision Foundation Models (VFMs) outputs that are lifted into 3D point clouds, facilitating spatial information propagation through inter-query interactions. Nevertheless, perception is an inherently dynamic process, rendering temporal understanding a critical yet overlooked dimension within these prevailing query-based pipelines. Therefore, to further unlock the temporal environmental perception capabilities of embodied agents, our work reconceptualizes online 3D segmentation as an instance tracking problem (AutoSeg3D). Our core strategy involves utilizing object queries for temporal information propagation, where long-term instance association promotes the coherence of features and object identities, while short-term instance update enriches instant observations. Given that viewpoint variations in embodied robotics often lead to partial object visibility across frames, this mechanism aids the model in developing a holistic object understanding beyond incomplete instantaneous views. Furthermore, we introduce spatial consistency learning to mitigate the fragmentation problem inherent in VFMs, yielding more comprehensive instance information for enhancing the efficacy of both long-term and short-term temporal learning. The temporal information exchange and consistency learning facilitated by these sparse object queries not only enhance spatial comprehension but also circumvent the computational burden associated with dense temporal point cloud interactions. Our method establishes a new state-of-the-art, surpassing ESAM by 2.8 AP on ScanNet200 and delivering consistent gains on ScanNet, SceneNN, and 3RScan datasets.

