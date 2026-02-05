---
layout: default
title: A labeled dataset of simulated phlebotomy procedures for medical AI: polygon annotations for object detection and human-object interaction
---

# A labeled dataset of simulated phlebotomy procedures for medical AI: polygon annotations for object detection and human-object interaction
**arXiv**：[2602.04624v1](https://arxiv.org/abs/2602.04624) · [PDF](https://arxiv.org/pdf/2602.04624.pdf)  
**作者**：Raúl Jiménez Cruz, César Torres-Huitzil, Marco Franceschetti, Ronny Seiger, Luciano García-Bañuelos, Barbara Weber  

**一句话要点**：提出带多边形标注的模拟抽血数据集，用于医疗AI中的物体检测与人机交互研究。

**关键词**：医疗数据集, 物体检测, 人机交互, 多边形标注, 抽血模拟, 医疗培训

## 3 点简述
- 核心问题：医疗培训自动化中缺乏高质量标注的抽血程序数据集。
- 方法要点：从高清视频提取图像，应用SSIM过滤和面部匿名化，提供多边形标注。
- 实验或效果：数据集包含11,884张图像，划分为训练、验证和测试子集，支持多种应用。

## 摘要（原文）

> This data article presents a dataset of 11,884 labeled images documenting a simulated blood extraction (phlebotomy) procedure performed on a training arm. Images were extracted from high-definition videos recorded under controlled conditions and curated to reduce redundancy using Structural Similarity Index Measure (SSIM) filtering. An automated face-anonymization step was applied to all videos prior to frame selection. Each image contains polygon annotations for five medically relevant classes: syringe, rubber band, disinfectant wipe, gloves, and training arm. The annotations were exported in a segmentation format compatible with modern object detection frameworks (e.g., YOLOv8), ensuring broad usability. This dataset is partitioned into training (70%), validation (15%), and test (15%) subsets and is designed to advance research in medical training automation and human-object interaction. It enables multiple applications, including phlebotomy tool detection, procedural step recognition, workflow analysis, conformance checking, and the development of educational systems that provide structured feedback to medical trainees. The data and accompanying label files are publicly available on Zenodo.

