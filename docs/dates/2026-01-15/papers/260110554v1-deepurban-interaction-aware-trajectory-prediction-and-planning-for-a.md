---
layout: default
title: DeepUrban: Interaction-Aware Trajectory Prediction and Planning for Automated Driving by Aerial Imagery
---

# DeepUrban: Interaction-Aware Trajectory Prediction and Planning for Automated Driving by Aerial Imagery
**arXiv**：[2601.10554v1](https://arxiv.org/abs/2601.10554) · [PDF](https://arxiv.org/pdf/2601.10554.pdf)  
**作者**：Constantin Selzer, Fabian B. Flohr  

**一句话要点**：提出DeepUrban无人机数据集以增强密集城市交通场景下的轨迹预测与规划基准

**关键词**：轨迹预测, 自动驾驶规划, 无人机数据集, 密集交通场景, 交互建模

## 3 点简述
- 核心问题：现有自动驾驶基准缺乏密集交通场景，难以建模复杂交互。
- 方法要点：与工业伙伴合作，基于高分辨率航拍图像构建包含3D交通对象和地图信息的无人机数据集。
- 实验或效果：在nuScenes上评估SOTA方法，提升车辆预测和规划精度，ADE/FDE指标改进达44.1%/44.3%。

## 摘要（原文）

> The efficacy of autonomous driving systems hinges critically on robust prediction and planning capabilities. However, current benchmarks are impeded by a notable scarcity of scenarios featuring dense traffic, which is essential for understanding and modeling complex interactions among road users. To address this gap, we collaborated with our industrial partner, DeepScenario, to develop DeepUrban-a new drone dataset designed to enhance trajectory prediction and planning benchmarks focusing on dense urban settings. DeepUrban provides a rich collection of 3D traffic objects, extracted from high-resolution images captured over urban intersections at approximately 100 meters altitude. The dataset is further enriched with comprehensive map and scene information to support advanced modeling and simulation tasks. We evaluate state-of-the-art (SOTA) prediction and planning methods, and conducted experiments on generalization capabilities. Our findings demonstrate that adding DeepUrban to nuScenes can boost the accuracy of vehicle predictions and planning, achieving improvements up to 44.1 % / 44.3% on the ADE / FDE metrics. Website: https://iv.ee.hm.edu/deepurban

