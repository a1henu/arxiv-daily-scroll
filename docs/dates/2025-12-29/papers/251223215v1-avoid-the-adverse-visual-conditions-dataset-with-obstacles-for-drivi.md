---
layout: default
title: AVOID: The Adverse Visual Conditions Dataset with Obstacles for Driving Scene Understanding
---

# AVOID: The Adverse Visual Conditions Dataset with Obstacles for Driving Scene Understanding
**arXiv**：[2512.23215v1](https://arxiv.org/abs/2512.23215) · [PDF](https://arxiv.org/pdf/2512.23215.pdf)  
**作者**：Jongoh Jeong, Taek-Jin Song, Jong-Hwan Kim, Kuk-Jin Yoon  

**一句话要点**：提出AVOID数据集以解决恶劣视觉条件下实时障碍物检测的挑战

**关键词**：驾驶场景理解, 障碍物检测, 恶劣视觉条件, 多模态数据集, 实时网络, 模拟环境

## 3 点简述
- 核心问题：现有驾驶数据集缺乏恶劣条件下的小型道路障碍物数据，影响实时检测可靠性。
- 方法要点：在模拟环境中构建大规模数据集，包含多种天气和时间条件下的障碍物图像及多模态标注。
- 实验或效果：基准测试实时网络进行障碍物检测，并设计多任务网络进行消融研究，支持多种视觉感知任务。

## 摘要（原文）

> Understanding road scenes for visual perception remains crucial for intelligent self-driving cars. In particular, it is desirable to detect unexpected small road hazards reliably in real-time, especially under varying adverse conditions (e.g., weather and daylight). However, existing road driving datasets provide large-scale images acquired in either normal or adverse scenarios only, and often do not contain the road obstacles captured in the same visual domain as for the other classes. To address this, we introduce a new dataset called AVOID, the Adverse Visual Conditions Dataset, for real-time obstacle detection collected in a simulated environment. AVOID consists of a large set of unexpected road obstacles located along each path captured under various weather and time conditions. Each image is coupled with the corresponding semantic and depth maps, raw and semantic LiDAR data, and waypoints, thereby supporting most visual perception tasks. We benchmark the results on high-performing real-time networks for the obstacle detection task, and also propose and conduct ablation studies using a comprehensive multi-task network for semantic segmentation, depth and waypoint prediction tasks.

