---
layout: default
title: SAVeD: A First-Person Social Media Video Dataset for ADAS-equipped vehicle Near-Miss and Crash Event Analyses
---

# SAVeD: A First-Person Social Media Video Dataset for ADAS-equipped vehicle Near-Miss and Crash Event Analyses
**arXiv**：[2512.17724v1](https://arxiv.org/abs/2512.17724) · [PDF](https://arxiv.org/pdf/2512.17724.pdf)  
**作者**：Shaoyan Zhai, Mohamed Abdel-Aty, Chenzhu Wang, Rodrigo Vena Garcia  

**一句话要点**：提出SAVeD数据集以解决ADAS车辆高风险事件分析中真实数据缺乏的问题

**关键词**：ADAS车辆数据集, 高风险事件分析, 第一人称视频, 时间到碰撞计算, 极端风险建模, 视频大语言模型基准

## 3 点简述
- 核心问题：现有数据集缺乏ADAS车辆在真实风险条件下的行为数据，限制安全研究。
- 方法要点：从社交媒体收集2,119个第一人称视频，标注碰撞、规避和系统失效事件。
- 实验或效果：通过TTC计算、风险建模和VLLM基准测试，验证数据集在复杂场景中的实用性。

## 摘要（原文）

> The advancement of safety-critical research in driving behavior in ADAS-equipped vehicles require real-world datasets that not only include diverse traffic scenarios but also capture high-risk edge cases such as near-miss events and system failures. However, existing datasets are largely limited to either simulated environments or human-driven vehicle data, lacking authentic ADAS (Advanced Driver Assistance System) vehicle behavior under risk conditions. To address this gap, this paper introduces SAVeD, a large-scale video dataset curated from publicly available social media content, explicitly focused on ADAS vehicle-related crashes, near-miss incidents, and disengagements. SAVeD features 2,119 first-person videos, capturing ADAS vehicle operations in diverse locations, lighting conditions, and weather scenarios. The dataset includes video frame-level annotations for collisions, evasive maneuvers, and disengagements, enabling analysis of both perception and decision-making failures. We demonstrate SAVeD's utility through multiple analyses and contributions: (1) We propose a novel framework integrating semantic segmentation and monocular depth estimation to compute real-time Time-to-Collision (TTC) for dynamic objects. (2) We utilize the Generalized Extreme Value (GEV) distribution to model and quantify the extreme risk in crash and near-miss events across different roadway types. (3) We establish benchmarks for state-of-the-art VLLMs (VideoLLaMA2 and InternVL2.5 HiCo R16), showing that SAVeD's detailed annotations significantly enhance model performance through domain adaptation in complex near-miss scenarios.

