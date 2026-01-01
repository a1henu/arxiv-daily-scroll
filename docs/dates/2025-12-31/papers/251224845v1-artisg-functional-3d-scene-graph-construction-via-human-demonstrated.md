---
layout: default
title: ArtiSG: Functional 3D Scene Graph Construction via Human-demonstrated Articulated Objects Manipulation
---

# ArtiSG: Functional 3D Scene Graph Construction via Human-demonstrated Articulated Objects Manipulation
**arXiv**：[2512.24845v1](https://arxiv.org/abs/2512.24845) · [PDF](https://arxiv.org/pdf/2512.24845.pdf)  
**作者**：Qiuyi Gu, Yuze Sheng, Jincheng Yu, Jiahao Tang, Xiaolong Shan, Zhaoyang Shen, Tinghao Yi, Xiaodan Liang, Xinlei Chen, Yu Wang  

**一句话要点**：提出ArtiSG框架，通过人类演示构建功能3D场景图以解决关节物体操作中的功能信息缺失问题。

**关键词**：3D场景图, 关节物体操作, 功能记忆, 人类演示, 机器人导航, 开放词汇图

## 3 点简述
- 核心问题：现有3D场景图缺乏关节物体的功能信息，且视觉感知易遗漏细粒度元素。
- 方法要点：利用便携式设置收集人类演示数据，编码关节轨迹和轴到层次化开放词汇图中。
- 实验或效果：在真实世界实验中，显著提升功能元素召回和关节估计精度，支持语言指导的机器人操作。

## 摘要（原文）

> 3D scene graphs have empowered robots with semantic understanding for navigation and planning, yet they often lack the functional information required for physical manipulation, particularly regarding articulated objects. Existing approaches for inferring articulation mechanisms from static observations are prone to visual ambiguity, while methods that estimate parameters from state changes typically rely on constrained settings such as fixed cameras and unobstructed views. Furthermore, fine-grained functional elements like small handles are frequently missed by general object detectors. To bridge this gap, we present ArtiSG, a framework that constructs functional 3D scene graphs by encoding human demonstrations into structured robotic memory. Our approach leverages a robust articulation data collection pipeline utilizing a portable setup to accurately estimate 6-DoF articulation trajectories and axes even under camera ego-motion. We integrate these kinematic priors into a hierarchical and open-vocabulary graph while utilizing interaction data to discover inconspicuous functional elements missed by visual perception. Extensive real-world experiments demonstrate that ArtiSG significantly outperforms baselines in functional element recall and articulation estimation precision. Moreover, we show that the constructed graph serves as a reliable functional memory that effectively guides robots to perform language-directed manipulation tasks in real-world environments containing diverse articulated objects.

