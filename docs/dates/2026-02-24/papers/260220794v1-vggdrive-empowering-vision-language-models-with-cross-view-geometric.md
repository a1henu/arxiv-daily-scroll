---
layout: default
title: VGGDrive: Empowering Vision-Language Models with Cross-View Geometric Grounding for Autonomous Driving
---

# VGGDrive: Empowering Vision-Language Models with Cross-View Geometric Grounding for Autonomous Driving
**arXiv**：[2602.20794v1](https://arxiv.org/abs/2602.20794) · [PDF](https://arxiv.org/pdf/2602.20794.pdf)  
**作者**：Jie Wang, Guang Li, Zhijian Huang, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen  

**一句话要点**：提出VGGDrive架构，通过跨视图几何基础增强视觉语言模型，以提升自动驾驶任务性能。

**关键词**：自动驾驶, 视觉语言模型, 跨视图几何, 3D基础模型, 特征注入

## 3 点简述
- 现有视觉语言模型缺乏跨视图3D几何建模能力，导致自动驾驶任务表现不佳。
- 引入可插拔跨视图3D几何使能器，将冻结3D模型特征自适应注入VLM的2D特征中。
- 实验表明VGGDrive在五个自动驾驶基准上提升性能，包括风险感知和轨迹规划任务。

## 摘要（原文）

> The significance of cross-view 3D geometric modeling capabilities for autonomous driving is self-evident, yet existing Vision-Language Models (VLMs) inherently lack this capability, resulting in their mediocre performance. While some promising approaches attempt to mitigate this by constructing Q&A data for auxiliary training, they still fail to fundamentally equip VLMs with the ability to comprehensively handle diverse evaluation protocols. We thus chart a new course, advocating for the infusion of VLMs with the cross-view geometric grounding of mature 3D foundation models, closing this critical capability gap in autonomous driving. In this spirit, we propose a novel architecture, VGGDrive, which empowers Vision-language models with cross-view Geometric Grounding for autonomous Driving. Concretely, to bridge the cross-view 3D geometric features from the frozen visual 3D model with the VLM's 2D visual features, we introduce a plug-and-play Cross-View 3D Geometric Enabler (CVGE). The CVGE decouples the base VLM architecture and effectively empowers the VLM with 3D features through a hierarchical adaptive injection mechanism. Extensive experiments show that VGGDrive enhances base VLM performance across five autonomous driving benchmarks, including tasks like cross-view risk perception, motion prediction, and trajectory planning. It's our belief that mature 3D foundation models can empower autonomous driving tasks through effective integration, and we hope our initial exploration demonstrates the potential of this paradigm to the autonomous driving community.

