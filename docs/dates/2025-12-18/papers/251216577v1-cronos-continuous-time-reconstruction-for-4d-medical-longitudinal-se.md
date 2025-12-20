---
layout: default
title: CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series
---

# CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series
**arXiv**：[2512.16577v1](https://arxiv.org/abs/2512.16577) · [PDF](https://arxiv.org/pdf/2512.16577.pdf)  
**作者**：Nico Albert Disch, Saikat Roy, Constantin Ulrich, Yannick Kirchhoff, Maximilian Rokuss, Robin Peretzke, David Zimmerer, Klaus Maier-Hein  

**一句话要点**：提出CRONOS框架，通过时空速度场实现多上下文连续时间3D医学序列预测

**关键词**：医学图像预测, 连续时间建模, 时空速度场, 多上下文学习, 3D体素处理

## 3 点简述
- 核心问题：现有模型依赖单次扫描或固定时间网格，限制不规则采样下的体素级预测。
- 方法要点：学习时空速度场，支持离散和连续时间戳，直接处理3D体素空间。
- 实验或效果：在三个公共数据集上超越基线，计算效率高，代码将开源。

## 摘要（原文）

> Forecasting how 3D medical scans evolve over time is important for disease progression, treatment planning, and developmental assessment. Yet existing models either rely on a single prior scan, fixed grid times, or target global labels, which limits voxel-level forecasting under irregular sampling. We present CRONOS, a unified framework for many-to-one prediction from multiple past scans that supports both discrete (grid-based) and continuous (real-valued) timestamps in one model, to the best of our knowledge the first to achieve continuous sequence-to-image forecasting for 3D medical data. CRONOS learns a spatio-temporal velocity field that transports context volumes toward a target volume at an arbitrary time, while operating directly in 3D voxel space. Across three public datasets spanning Cine-MRI, perfusion CT, and longitudinal MRI, CRONOS outperforms other baselines, while remaining computationally competitive. We will release code and evaluation protocols to enable reproducible, multi-dataset benchmarking of multi-context, continuous-time forecasting.

