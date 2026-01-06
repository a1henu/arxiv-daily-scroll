---
layout: default
title: Differential Barometric Altimetry for Submeter Vertical Localization and Floor Recognition Indoors
---

# Differential Barometric Altimetry for Submeter Vertical Localization and Floor Recognition Indoors
**arXiv**：[2601.02184v1](https://arxiv.org/abs/2601.02184) · [PDF](https://arxiv.org/pdf/2601.02184.pdf)  
**作者**：Yuhang Zhang, Sören Schwertfeger  

**一句话要点**：提出差分气压测高框架，实现室内亚米级垂直定位与楼层识别

**关键词**：差分气压测高, 垂直定位, 楼层识别, 移动机器人, ROS集成, 低成本传感

## 3 点简述
- 核心问题：移动机器人在多层复杂环境中需精确高度估计与可靠楼层识别，视觉或激光SLAM单独不足。
- 方法要点：利用差分气压传感，结合固定基站与移动传感器，发布实时无漂移高度数据，集成ROS软件包。
- 实验或效果：在封闭楼梯和电梯等挑战场景中，垂直精度达亚米级（RMSE 0.29米），楼层识别准确率100%。

## 摘要（原文）

> Accurate altitude estimation and reliable floor recognition are critical for mobile robot localization and navigation within complex multi-storey environments. In this paper, we present a robust, low-cost vertical estimation framework leveraging differential barometric sensing integrated within a fully ROS-compliant software package. Our system simultaneously publishes real-time altitude data from both a stationary base station and a mobile sensor, enabling precise and drift-free vertical localization. Empirical evaluations conducted in challenging scenarios -- such as fully enclosed stairwells and elevators, demonstrate that our proposed barometric pipeline achieves sub-meter vertical accuracy (RMSE: 0.29 m) and perfect (100%) floor-level identification. In contrast, our results confirm that standalone height estimates, obtained solely from visual- or LiDAR-based SLAM odometry, are insufficient for reliable vertical localization. The proposed ROS-compatible barometric module thus provides a practical and cost-effective solution for robust vertical awareness in real-world robotic deployments. The implementation of our method is released as open source at https://github.com/witsir/differential-barometric.

