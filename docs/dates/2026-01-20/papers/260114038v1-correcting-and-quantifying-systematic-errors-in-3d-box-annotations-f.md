---
layout: default
title: Correcting and Quantifying Systematic Errors in 3D Box Annotations for Autonomous Driving
---

# Correcting and Quantifying Systematic Errors in 3D Box Annotations for Autonomous Driving
**arXiv**：[2601.14038v1](https://arxiv.org/abs/2601.14038) · [PDF](https://arxiv.org/pdf/2601.14038.pdf)  
**作者**：Alexandre Justo Miro, Ludvig af Klinteberg, Bogdan Timus, Aron Asefaw, Ajinkya Khoche, Thomas Gustafsson, Sina Sharif Mansouri, Masoud Daneshtalab  

**一句话要点**：提出离线估计方法以纠正自动驾驶3D框标注中的系统误差

**关键词**：3D框标注, 自动驾驶, LiDAR数据, 系统误差校正, 时空一致性, 基准测试评估

## 3 点简述
- 核心问题：动态场景下基于LiDAR的3D框标注存在系统误差，影响数据集质量。
- 方法要点：通过物理可行轨迹和时空一致性校正标注，首次定义相关评估指标。
- 实验或效果：在多个数据集上提升标注质量超17%，量化误差达2.5米，并验证误差对基准测试的影响。

## 摘要（原文）

> Accurate ground truth annotations are critical to supervised learning and evaluating the performance of autonomous vehicle systems. These vehicles are typically equipped with active sensors, such as LiDAR, which scan the environment in predefined patterns. 3D box annotation based on data from such sensors is challenging in dynamic scenarios, where objects are observed at different timestamps, hence different positions. Without proper handling of this phenomenon, systematic errors are prone to being introduced in the box annotations. Our work is the first to discover such annotation errors in widely used, publicly available datasets. Through our novel offline estimation method, we correct the annotations so that they follow physically feasible trajectories and achieve spatial and temporal consistency with the sensor data. For the first time, we define metrics for this problem; and we evaluate our method on the Argoverse 2, MAN TruckScenes, and our proprietary datasets. Our approach increases the quality of box annotations by more than 17% in these datasets. Furthermore, we quantify the annotation errors in them and find that the original annotations are misplaced by up to 2.5 m, with highly dynamic objects being the most affected. Finally, we test the impact of the errors in benchmarking and find that the impact is larger than the improvements that state-of-the-art methods typically achieve with respect to the previous state-of-the-art methods; showing that accurate annotations are essential for correct interpretation of performance. Our code is available at https://github.com/alexandre-justo-miro/annotation-correction-3D-boxes.

