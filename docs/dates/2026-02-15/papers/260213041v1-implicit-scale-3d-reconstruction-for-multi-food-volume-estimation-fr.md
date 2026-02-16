---
layout: default
title: Implicit-Scale 3D Reconstruction for Multi-Food Volume Estimation from Monocular Images
---

# Implicit-Scale 3D Reconstruction for Multi-Food Volume Estimation from Monocular Images
**arXiv**：[2602.13041v1](https://arxiv.org/abs/2602.13041) · [PDF](https://arxiv.org/pdf/2602.13041.pdf)  
**作者**：Yuhao Chen, Gautham Vinod, Siddeshwar Raghavan, Talha Ibn Mahmud, Bruce Coburn, Jinge Ma, Fengqing Zhu, Jiangpeng He  

**一句话要点**：提出隐式尺度三维重建基准数据集，用于单目多食物图像体积估计

**关键词**：隐式尺度三维重建, 食物体积估计, 单目图像, 几何推理, 基准数据集, 多食物场景

## 3 点简述
- 核心问题：现有饮食评估方法依赖单图分析或外观推理，缺乏几何推理且对尺度模糊敏感。
- 方法要点：将食物体积估计重构为单目观测下的隐式尺度三维重建问题，移除显式物理参考，依赖上下文对象推断尺度。
- 实验或效果：几何重建方法在体积估计和几何精度上优于视觉语言基线，最佳方法体积估计MAPE为0.21，L1 Chamfer距离为5.7。

## 摘要（原文）

> We present Implicit-Scale 3D Reconstruction from Monocular Multi-Food Images, a benchmark dataset designed to advance geometry-based food portion estimation in realistic dining scenarios. Existing dietary assessment methods largely rely on single-image analysis or appearance-based inference, including recent vision-language models, which lack explicit geometric reasoning and are sensitive to scale ambiguity. This benchmark reframes food portion estimation as an implicit-scale 3D reconstruction problem under monocular observations. To reflect real-world conditions, explicit physical references and metric annotations are removed; instead, contextual objects such as plates and utensils are provided, requiring algorithms to infer scale from implicit cues and prior knowledge. The dataset emphasizes multi-food scenes with diverse object geometries, frequent occlusions, and complex spatial arrangements. The benchmark was adopted as a challenge at the MetaFood 2025 Workshop, where multiple teams proposed reconstruction-based solutions. Experimental results show that while strong vision--language baselines achieve competitive performance, geometry-based reconstruction methods provide both improved accuracy and greater robustness, with the top-performing approach achieving 0.21 MAPE in volume estimation and 5.7 L1 Chamfer Distance in geometric accuracy.

