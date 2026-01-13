---
layout: default
title: Motion Focus Recognition in Fast-Moving Egocentric Video
---

# Motion Focus Recognition in Fast-Moving Egocentric Video
**arXiv**：[2601.07154v1](https://arxiv.org/abs/2601.07154) · [PDF](https://arxiv.org/pdf/2601.07154.pdf)  
**作者**：Daniel Hong, James Tribble, Hao Wang, Chaoyi Zhou, Ashish Bastola, Siyu Huang, Abolfazl Razi  

**一句话要点**：提出实时运动焦点识别方法，从快速移动的自我中心视频中估计主体运动意图。

**关键词**：自我中心视频, 运动焦点识别, 实时推理, 相机姿态估计, 系统优化

## 3 点简述
- 核心问题：现有自我中心数据集忽视运动分析在体育等快速移动场景中的固有作用。
- 方法要点：利用基础模型进行相机姿态估计，并通过系统级优化实现高效可扩展推理。
- 实验或效果：在收集的数据集上实现实时性能，通过滑动批量推理策略控制内存消耗。

## 摘要（原文）

> From Vision-Language-Action (VLA) systems to robotics, existing egocentric datasets primarily focus on action recognition tasks, while largely overlooking the inherent role of motion analysis in sports and other fast-movement scenarios. To bridge this gap, we propose a real-time motion focus recognition method that estimates the subject's locomotion intention from any egocentric video. Our approach leverages the foundation model for camera pose estimation and introduces system-level optimizations to enable efficient and scalable inference. Evaluated on a collected egocentric action dataset, our method achieves real-time performance with manageable memory consumption through a sliding batch inference strategy. This work makes motion-centric analysis practical for edge deployment and offers a complementary perspective to existing egocentric studies on sports and fast-movement activities.

