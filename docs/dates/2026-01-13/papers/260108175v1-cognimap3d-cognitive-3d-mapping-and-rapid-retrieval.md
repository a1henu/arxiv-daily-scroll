---
layout: default
title: CogniMap3D: Cognitive 3D Mapping and Rapid Retrieval
---

# CogniMap3D: Cognitive 3D Mapping and Rapid Retrieval
**arXiv**：[2601.08175v1](https://arxiv.org/abs/2601.08175) · [PDF](https://arxiv.org/pdf/2601.08175.pdf)  
**作者**：Feiran Wang, Junyi Wu, Dawen Cai, Yuan Hong, Yan Yan  

**一句话要点**：提出CogniMap3D框架，模拟人类认知过程实现动态3D场景理解与重建。

**关键词**：3D场景理解, 动态对象检测, 认知映射, 因子图优化, 多访场景重建

## 3 点简述
- 核心问题：动态3D场景理解与重建，需处理动态对象和静态场景的持续更新。
- 方法要点：集成多阶段运动线索、认知映射系统和因子图优化，支持场景存储与快速检索。
- 实验或效果：在视频深度估计、相机姿态重建和3D映射任务中表现先进，支持多访连续理解。

## 摘要（原文）

> We present CogniMap3D, a bioinspired framework for dynamic 3D scene understanding and reconstruction that emulates human cognitive processes. Our approach maintains a persistent memory bank of static scenes, enabling efficient spatial knowledge storage and rapid retrieval. CogniMap3D integrates three core capabilities: a multi-stage motion cue framework for identifying dynamic objects, a cognitive mapping system for storing, recalling, and updating static scenes across multiple visits, and a factor graph optimization strategy for refining camera poses. Given an image stream, our model identifies dynamic regions through motion cues with depth and camera pose priors, then matches static elements against its memory bank. When revisiting familiar locations, CogniMap3D retrieves stored scenes, relocates cameras, and updates memory with new observations. Evaluations on video depth estimation, camera pose reconstruction, and 3D mapping tasks demonstrate its state-of-the-art performance, while effectively supporting continuous scene understanding across extended sequences and multiple visits.

