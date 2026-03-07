---
layout: default
title: ORMOT: A Dataset and Framework for Omnidirectional Referring Multi-Object Tracking
---

# ORMOT: A Dataset and Framework for Omnidirectional Referring Multi-Object Tracking
**arXiv**：[2603.05384v1](https://arxiv.org/abs/2603.05384) · [PDF](https://arxiv.org/pdf/2603.05384.pdf)  
**作者**：Sijia Chen, Zihan Zhou, Yanqiu Yu, En Yu, Wenbing Tao  

**一句话要点**：提出ORMOT任务与ORSet数据集及ORTrack框架，以解决全景图像中基于语言描述的多目标跟踪问题。

**关键词**：全景图像, 基于语言描述的多目标跟踪, 大视觉语言模型, 数据集构建, 视野扩展, 长序列语言理解

## 3 点简述
- 核心问题：现有基于语言描述的多目标跟踪方法在传统相机数据上视野受限，导致目标丢失和跟踪碎片化。
- 方法要点：引入全景图像扩展任务，构建ORSet数据集，并开发基于大视觉语言模型的ORTrack框架。
- 实验或效果：在ORSet数据集上实验验证了ORTrack框架的有效性，数据集和代码将开源。

## 摘要（原文）

> Multi-Object Tracking (MOT) is a fundamental task in computer vision, aiming to track targets across video frames. Existing MOT methods perform well in general visual scenes, but face significant challenges and limitations when extended to visual-language settings. To bridge this gap, the task of Referring Multi-Object Tracking (RMOT) has recently been proposed, which aims to track objects that correspond to language descriptions. However, current RMOT methods are primarily developed on datasets captured by conventional cameras, which suffer from limited field of view. This constraint often causes targets to move out of the frame, leading to fragmented tracking and loss of contextual information. In this work, we propose a novel task, called Omnidirectional Referring Multi-Object Tracking (ORMOT), which extends RMOT to omnidirectional imagery, aiming to overcome the field-of-view (FoV) limitation of conventional datasets and improve the model's ability to understand long-horizon language descriptions. To advance the ORMOT task, we construct ORSet, an Omnidirectional Referring Multi-Object Tracking dataset, which contains 27 diverse omnidirectional scenes, 848 language descriptions, and 3,401 annotated objects, providing rich visual, temporal, and language information. Furthermore, we propose ORTrack, a Large Vision-Language Model (LVLM)-driven framework tailored for Omnidirectional Referring Multi-Object Tracking. Extensive experiments on the ORSet dataset demonstrate the effectiveness of our ORTrack framework. The dataset and code will be open-sourced at https://github.com/chen-si-jia/ORMOT.

