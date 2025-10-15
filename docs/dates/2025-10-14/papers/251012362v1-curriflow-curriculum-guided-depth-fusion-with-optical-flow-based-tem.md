---
layout: default
title: CurriFlow: Curriculum-Guided Depth Fusion with Optical Flow-Based Temporal Alignment for 3D Semantic Scene Completion
---

# CurriFlow: Curriculum-Guided Depth Fusion with Optical Flow-Based Temporal Alignment for 3D Semantic Scene Completion
**arXiv**：[2510.12362v1](https://arxiv.org/abs/2510.12362) · [PDF](https://arxiv.org/pdf/2510.12362.pdf)  
**作者**：Jinzhou Lin, Jie Zhou, Wenhao Xu, Rongtao Xu, Changwei Wang, Shunpeng Chen, Kexue Fu, Yihua Shao, Li Guo, Shibiao Xu  

**一句话要点**：提出CurriFlow框架，通过光流时序对齐和课程深度融合解决自动驾驶中3D语义场景补全问题

**关键词**：3D语义场景补全, 光流时序对齐, 课程学习, 深度融合, 自动驾驶感知, 语义占用预测

## 3 点简述
- 核心问题：现有方法缺乏显式运动推理，难以处理遮挡和噪声深度监督
- 方法要点：集成光流时序对齐与课程学习，从稀疏LiDAR深度过渡到密集立体深度
- 实验效果：在SemanticKITTI基准上达到16.9 mIoU，验证运动引导和课程感知设计的有效性

## 摘要（原文）

> Semantic Scene Completion (SSC) aims to infer complete 3D geometry and
> semantics from monocular images, serving as a crucial capability for
> camera-based perception in autonomous driving. However, existing SSC methods
> relying on temporal stacking or depth projection often lack explicit motion
> reasoning and struggle with occlusions and noisy depth supervision. We propose
> CurriFlow, a novel semantic occupancy prediction framework that integrates
> optical flow-based temporal alignment with curriculum-guided depth fusion.
> CurriFlow employs a multi-level fusion strategy to align segmentation, visual,
> and depth features across frames using pre-trained optical flow, thereby
> improving temporal consistency and dynamic object understanding. To enhance
> geometric robustness, a curriculum learning mechanism progressively transitions
> from sparse yet accurate LiDAR depth to dense but noisy stereo depth during
> training, ensuring stable optimization and seamless adaptation to real-world
> deployment. Furthermore, semantic priors from the Segment Anything Model (SAM)
> provide category-agnostic supervision, strengthening voxel-level semantic
> learning and spatial consistency. Experiments on the SemanticKITTI benchmark
> demonstrate that CurriFlow achieves state-of-the-art performance with a mean
> IoU of 16.9, validating the effectiveness of our motion-guided and
> curriculum-aware design for camera-based 3D semantic scene completion.

