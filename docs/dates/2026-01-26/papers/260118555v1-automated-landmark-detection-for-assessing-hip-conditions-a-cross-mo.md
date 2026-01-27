---
layout: default
title: Automated Landmark Detection for assessing hip conditions: A Cross-Modality Validation of MRI versus X-ray
---

# Automated Landmark Detection for assessing hip conditions: A Cross-Modality Validation of MRI versus X-ray
**arXiv**：[2601.18555v1](https://arxiv.org/abs/2601.18555) · [PDF](https://arxiv.org/pdf/2601.18555.pdf)  
**作者**：Roberto Di Via, Vito Paolo Pastore, Francesca Odone, Siôn Glyn-Jones, Irina Voiculescu  

**一句话要点**：提出基于热图回归的自动化地标检测方法，验证MRI与X射线在髋关节撞击症评估中的跨模态临床等效性。

**关键词**：地标检测, 跨模态验证, 热图回归, 髋关节撞击症, 医学影像分析, 自动化评估

## 3 点简述
- 核心问题：髋关节撞击症筛查依赖X射线角度测量，但MRI提供3D视图，需验证两种模态在自动化评估中的临床等效性。
- 方法要点：使用标准热图回归架构，在配对MRI/X射线数据集上进行匹配队列验证研究，评估地标检测的定位和诊断准确性。
- 实验或效果：在89名患者数据中，MRI在冠状面视图上实现与X射线等效的定位精度，支持将自动化评估整合到常规MRI工作流。

## 摘要（原文）

> Many clinical screening decisions are based on angle measurements. In particular, FemoroAcetabular Impingement (FAI) screening relies on angles traditionally measured on X-rays. However, assessing the height and span of the impingement area requires also a 3D view through an MRI scan. The two modalities inform the surgeon on different aspects of the condition. In this work, we conduct a matched-cohort validation study (89 patients, paired MRI/X-ray) using standard heatmap regression architectures to assess cross-modality clinical equivalence. Seen that landmark detection has been proven effective on X-rays, we show that MRI also achieves equivalent localisation and diagnostic accuracy for cam-type impingement. Our method demonstrates clinical feasibility for FAI assessment in coronal views of 3D MRI volumes, opening the possibility for volumetric analysis through placing further landmarks. These results support integrating automated FAI assessment into routine MRI workflows. Code is released at https://github.com/Malga-Vision/Landmarks-Hip-Conditions

