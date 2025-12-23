---
layout: default
title: Zero-shot Reconstruction of In-Scene Object Manipulation from Video
---

# Zero-shot Reconstruction of In-Scene Object Manipulation from Video
**arXiv**：[2512.19684v1](https://arxiv.org/abs/2512.19684) · [PDF](https://arxiv.org/pdf/2512.19684.pdf)  
**作者**：Dixuan Lin, Tianyou Wang, Zhuoyang Pan, Yufu Wang, Lingjie Liu, Kostas Daniilidis  

**一句话要点**：提出首个系统以零样本重建单目视频中的场景内物体操作

**关键词**：零样本重建, 单目视频理解, 手-物体交互, 场景一致性优化, 物理交互建模

## 3 点简述
- 核心问题：从单目RGB视频重建场景内物体操作，面临病态场景重建、手-物体深度模糊和物理交互合理性挑战。
- 方法要点：使用数据驱动基础模型初始化物体网格、姿态、场景点云和手部姿态，然后通过两阶段优化恢复从抓取到交互的完整手-物体运动。
- 实验或效果：系统保持与输入视频中观察到的场景信息一致，提升度量准确性和实用性。

## 摘要（原文）

> We build the first system to address the problem of reconstructing in-scene object manipulation from a monocular RGB video. It is challenging due to ill-posed scene reconstruction, ambiguous hand-object depth, and the need for physically plausible interactions. Existing methods operate in hand centric coordinates and ignore the scene, hindering metric accuracy and practical use. In our method, we first use data-driven foundation models to initialize the core components, including the object mesh and poses, the scene point cloud, and the hand poses. We then apply a two-stage optimization that recovers a complete hand-object motion from grasping to interaction, which remains consistent with the scene information observed in the input video.

