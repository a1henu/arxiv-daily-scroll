---
layout: default
title: OMCL: Open-vocabulary Monte Carlo Localization
---

# OMCL: Open-vocabulary Monte Carlo Localization
**arXiv**：[2512.15557v1](https://arxiv.org/abs/2512.15557) · [PDF](https://arxiv.org/pdf/2512.15557.pdf)  
**作者**：Evgenii Kruzhkov, Raphael Memmesheimer, Sven Behnke  

**一句话要点**：提出OMCL方法，利用视觉-语言特征增强蒙特卡洛定位，实现跨模态鲁棒定位。

**关键词**：机器人定位, 蒙特卡洛定位, 视觉-语言特征, 开放词汇学习, 跨模态关联

## 3 点简述
- 核心问题：机器人定位需在传感器差异下鲁棒关联观测与地图特征。
- 方法要点：扩展蒙特卡洛定位，引入开放词汇视觉-语言特征计算观测似然。
- 实验或效果：在室内外场景评估，展示泛化能力，支持自然语言初始化全局定位。

## 摘要（原文）

> Robust robot localization is an important prerequisite for navigation planning. If the environment map was created from different sensors, robot measurements must be robustly associated with map features. In this work, we extend Monte Carlo Localization using vision-language features. These open-vocabulary features enable to robustly compute the likelihood of visual observations, given a camera pose and a 3D map created from posed RGB-D images or aligned point clouds. The abstract vision-language features enable to associate observations and map elements from different modalities. Global localization can be initialized by natural language descriptions of the objects present in the vicinity of locations. We evaluate our approach using Matterport3D and Replica for indoor scenes and demonstrate generalization on SemanticKITTI for outdoor scenes.

