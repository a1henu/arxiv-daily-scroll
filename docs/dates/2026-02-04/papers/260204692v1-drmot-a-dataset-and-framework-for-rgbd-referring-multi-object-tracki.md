---
layout: default
title: DRMOT: A Dataset and Framework for RGBD Referring Multi-Object Tracking
---

# DRMOT: A Dataset and Framework for RGBD Referring Multi-Object Tracking
**arXiv**：[2602.04692v1](https://arxiv.org/abs/2602.04692) · [PDF](https://arxiv.org/pdf/2602.04692.pdf)  
**作者**：Sijia Chen, Lijuan Ma, Yanqiu Yu, En Yu, Liman Liu, Wenbing Tao  

**一句话要点**：提出DRMOT任务与DRTrack框架，融合RGB-D-L模态以解决3D感知的指代多目标跟踪问题。

**关键词**：RGBD指代多目标跟踪, 多模态融合, 3D感知跟踪, 深度信息, 数据集构建, 轨迹关联

## 3 点简述
- 现有RMOT模型仅依赖2D RGB数据，难以处理复杂空间语义和严重遮挡下的目标跟踪。
- 提出DRMOT任务，要求模型融合RGB、深度和语言模态，实现3D感知的跟踪。
- 构建DRSet数据集并开发DRTrack框架，实验验证其在空间语义定位和轨迹关联上的有效性。

## 摘要（原文）

> Referring Multi-Object Tracking (RMOT) aims to track specific targets based on language descriptions and is vital for interactive AI systems such as robotics and autonomous driving. However, existing RMOT models rely solely on 2D RGB data, making it challenging to accurately detect and associate targets characterized by complex spatial semantics (e.g., ``the person closest to the camera'') and to maintain reliable identities under severe occlusion, due to the absence of explicit 3D spatial information. In this work, we propose a novel task, RGBD Referring Multi-Object Tracking (DRMOT), which explicitly requires models to fuse RGB, Depth (D), and Language (L) modalities to achieve 3D-aware tracking. To advance research on the DRMOT task, we construct a tailored RGBD referring multi-object tracking dataset, named DRSet, designed to evaluate models' spatial-semantic grounding and tracking capabilities. Specifically, DRSet contains RGB images and depth maps from 187 scenes, along with 240 language descriptions, among which 56 descriptions incorporate depth-related information. Furthermore, we propose DRTrack, a MLLM-guided depth-referring tracking framework. DRTrack performs depth-aware target grounding from joint RGB-D-L inputs and enforces robust trajectory association by incorporating depth cues. Extensive experiments on the DRSet dataset demonstrate the effectiveness of our framework.

