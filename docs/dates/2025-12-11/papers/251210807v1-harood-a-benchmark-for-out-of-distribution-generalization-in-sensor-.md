---
layout: default
title: HAROOD: A Benchmark for Out-of-distribution Generalization in Sensor-based Human Activity Recognition
---

# HAROOD: A Benchmark for Out-of-distribution Generalization in Sensor-based Human Activity Recognition
**arXiv**：[2512.10807v1](https://arxiv.org/abs/2512.10807) · [PDF](https://arxiv.org/pdf/2512.10807.pdf)  
**作者**：Wang Lu, Yao Zhu, Jindong Wang  

**一句话要点**：提出HAROOD基准以全面评估传感器人类活动识别中的分布外泛化能力

**关键词**：传感器人类活动识别, 分布外泛化, 基准测试, 跨场景评估, 深度学习

## 3 点简述
- 核心问题：传感器人类活动识别中个体、设备、环境和时间变化导致分布偏移，现有OOD算法缺乏全面评估
- 方法要点：定义跨人、跨位置、跨数据集和跨时间4种OOD场景，构建包含6个数据集和16种方法的测试平台
- 实验或效果：实验表明无单一方法始终最优，基准代码模块化易于扩展，促进OOD-HAR研究

## 摘要（原文）

> Sensor-based human activity recognition (HAR) mines activity patterns from the time-series sensory data. In realistic scenarios, variations across individuals, devices, environments, and time introduce significant distributional shifts for the same activities. Recent efforts attempt to solve this challenge by applying or adapting existing out-of-distribution (OOD) algorithms, but only in certain distribution shift scenarios (e.g., cross-device or cross-position), lacking comprehensive insights on the effectiveness of these algorithms. For instance, is OOD necessary to HAR? Which OOD algorithm performs the best? In this paper, we fill this gap by proposing HAROOD, a comprehensive benchmark for HAR in OOD settings. We define 4 OOD scenarios: cross-person, cross-position, cross-dataset, and cross-time, and build a testbed covering 6 datasets, 16 comparative methods (implemented with CNN-based and Transformer-based architectures), and two model selection protocols. Then, we conduct extensive experiments and present several findings for future research, e.g., no single method consistently outperforms others, highlighting substantial opportunity for advancement. Our codebase is highly modular and easy to extend for new datasets, algorithms, comparisons, and analysis, with the hope to facilitate the research in OOD-based HAR. Our implementation is released and can be found at https://github.com/AIFrontierLab/HAROOD.

