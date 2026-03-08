---
layout: default
title: VinePT-Map: Pole-Trunk Semantic Mapping for Resilient Autonomous Robotics in Vineyards
---

# VinePT-Map: Pole-Trunk Semantic Mapping for Resilient Autonomous Robotics in Vineyards
**arXiv**：[2603.05070v1](https://arxiv.org/abs/2603.05070) · [PDF](https://arxiv.org/pdf/2603.05070.pdf)  
**作者**：Giorgio Audrito, Mauro Martini, Alessandro Navone, Giorgia Galluzzo, Marcello Chiaberge  

**一句话要点**：提出VinePT-Map语义建图框架，利用葡萄藤干和支撑杆作为持久地标，实现葡萄园中季节无关的机器人定位。

**关键词**：语义建图, 机器人定位, 葡萄园自主机器人, 因子图优化, 实例分割, 多季节数据集

## 3 点简述
- 核心问题：葡萄园环境因感知混淆、季节变化和作物动态，导致传统基于特征的定位与建图方法鲁棒性不足。
- 方法要点：基于因子图整合GPS、IMU和RGB-D观测，通过实例分割与跟踪的感知流程，结合聚类滤波进行异常值剔除和位姿优化。
- 实验或效果：使用多季节数据集验证，跨季节实地实验显示方法具有鲁棒性和准确性，适合农业环境长期自主操作。

## 摘要（原文）

> Reliable long-term deployment of autonomous robots in agricultural environments remains challenging due to perceptual aliasing, seasonal variability, and the dynamic nature of crop canopies. Vineyards, characterized by repetitive row structures and significant visual changes across phenological stages, represent a pivotal field challenge, limiting the robustness of conventional feature-based localization and mapping approaches. This paper introduces VinePT-Map, a semantic mapping framework that leverages vine trunks and support poles as persistent structural landmarks to enable season-agnostic and resilient robot localization. The proposed method formulates the mapping problem as a factor graph, integrating GPS, IMU, and RGB-D observations through robust geometrical constraints that exploit vineyard structure. An efficient perception pipeline based on instance segmentation and tracking, combined with a clustering filter for outlier rejection and pose refinement, enables accurate landmark detection using low-cost sensors and onboard computation. To validate the pipeline, we present a multi-season dataset for trunk and pole segmentation and tracking. Extensive field experiments conducted across diverse seasons demonstrate the robustness and accuracy of the proposed approach, highlighting its suitability for long-term autonomous operation in agricultural environments.

