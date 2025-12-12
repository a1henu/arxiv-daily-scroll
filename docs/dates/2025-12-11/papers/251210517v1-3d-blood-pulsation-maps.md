---
layout: default
title: 3D Blood Pulsation Maps
---

# 3D Blood Pulsation Maps
**arXiv**：[2512.10517v1](https://arxiv.org/abs/2512.10517) · [PDF](https://arxiv.org/pdf/2512.10517.pdf)  
**作者**：Maurice Rohr, Tobias Reinhardt, Tizian Dege, Justus Thies, Christoph Hoog Antink  

**一句话要点**：提出Pulse3DFace数据集以估计三维血流搏动图，用于改进远程脉搏估计方法。

**关键词**：三维血流搏动图, 光电容积描记成像, 多视角视频, FLAME模型, 远程脉搏估计

## 3 点简述
- 核心问题：缺乏三维血流搏动数据，影响远程光电容积描记成像方法的验证与改进。
- 方法要点：采集15名受试者的多视角视频和3D扫描，生成与FLAME模型兼容的3D搏动图。
- 实验或效果：评估数据集的光照条件、图一致性和生理特征捕获能力，支持多视图方法研究。

## 摘要（原文）

> We present Pulse3DFace, the first dataset of its kind for estimating 3D blood pulsation maps. These maps can be used to develop models of dynamic facial blood pulsation, enabling the creation of synthetic video data to improve and validate remote pulse estimation methods via photoplethysmography imaging. Additionally, the dataset facilitates research into novel multi-view-based approaches for mitigating illumination effects in blood pulsation analysis. Pulse3DFace consists of raw videos from 15 subjects recorded at 30 Hz with an RGB camera from 23 viewpoints, blood pulse reference measurements, and facial 3D scans generated using monocular structure-from-motion techniques. It also includes processed 3D pulsation maps compatible with the texture space of the 3D head model FLAME. These maps provide signal-to-noise ratio, local pulse amplitude, phase information, and supplementary data. We offer a comprehensive evaluation of the dataset's illumination conditions, map consistency, and its ability to capture physiologically meaningful features in the facial and neck skin regions.

