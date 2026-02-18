---
layout: default
title: An Industrial Dataset for Scene Acquisitions and Functional Schematics Alignment
---

# An Industrial Dataset for Scene Acquisitions and Functional Schematics Alignment
**arXiv**：[2602.15584v1](https://arxiv.org/abs/2602.15584) · [PDF](https://arxiv.org/pdf/2602.15584.pdf)  
**作者**：Flavien Armangeon, Thibaud Ehret, Enric Meinhardt-Llopis, Rafael Grompone von Gioi, Guillaume Thibault, Marc Petit, Gabriele Facciolo  

**一句话要点**：提出IRIS-v2数据集以解决工业场景中功能示意图与采集数据对齐的挑战

**关键词**：工业数据集, 数字孪生, 功能示意图对齐, 分割与图匹配, 点云处理

## 3 点简述
- 核心问题：工业设施功能示意图与2D/3D采集数据对齐困难，缺乏公开数据集，手动方法效率低。
- 方法要点：提供包含图像、点云、标注、CAD模型和P&ID的综合数据集，支持分割与图匹配结合的研究。
- 实验或效果：通过案例研究展示对齐方法，旨在减少任务时间，具体效果未知。

## 摘要（原文）

> Aligning functional schematics with 2D and 3D scene acquisitions is crucial for building digital twins, especially for old industrial facilities that lack native digital models. Current manual alignment using images and LiDAR data does not scale due to tediousness and complexity of industrial sites. Inconsistencies between schematics and reality, and the scarcity of public industrial datasets, make the problem both challenging and underexplored. This paper introduces IRIS-v2, a comprehensive dataset to support further research. It includes images, point clouds, 2D annotated boxes and segmentation masks, a CAD model, 3D pipe routing information, and the P&ID (Piping and Instrumentation Diagram). The alignment is experimented on a practical case study, aiming at reducing the time required for this task by combining segmentation and graph matching.

