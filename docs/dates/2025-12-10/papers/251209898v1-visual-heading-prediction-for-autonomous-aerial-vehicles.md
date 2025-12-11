---
layout: default
title: Visual Heading Prediction for Autonomous Aerial Vehicles
---

# Visual Heading Prediction for Autonomous Aerial Vehicles
**arXiv**：[2512.09898v1](https://arxiv.org/abs/2512.09898) · [PDF](https://arxiv.org/pdf/2512.09898.pdf)  
**作者**：Reza Ahmari, Ahmad Mohammadi, Vahid Hemmati, Mohammed Mynuddin, Parham Kebria, Mahmoud Nabil Mahmoud, Xiaohong Yuan, Abdollah Homaifar  

**一句话要点**：提出基于视觉的无人机-无人车集成框架，用于GPS缺失环境下的实时导航与协调。

**关键词**：无人机-无人车集成, 视觉航向预测, YOLOv5检测, 轻量神经网络, GPS缺失环境, 实时协调

## 3 点简述
- 核心问题：无人机与无人车在GPS不可用或降级时实时协调困难，需精确检测与航向预测。
- 方法要点：使用微调YOLOv5检测无人车并提取特征，轻量ANN预测无人机航向角，仅需单目相机输入。
- 实验或效果：在受控实验室环境中收集超13,000张标注图像，ANN预测误差小，检测准确率达95%。

## 摘要（原文）

> The integration of Unmanned Aerial Vehicles (UAVs) and Unmanned Ground Vehicles (UGVs) is increasingly central to the development of intelligent autonomous systems for applications such as search and rescue, environmental monitoring, and logistics. However, precise coordination between these platforms in real-time scenarios presents major challenges, particularly when external localization infrastructure such as GPS or GNSS is unavailable or degraded [1]. This paper proposes a vision-based, data-driven framework for real-time UAV-UGV integration, with a focus on robust UGV detection and heading angle prediction for navigation and coordination. The system employs a fine-tuned YOLOv5 model to detect UGVs and extract bounding box features, which are then used by a lightweight artificial neural network (ANN) to estimate the UAV's required heading angle. A VICON motion capture system was used to generate ground-truth data during training, resulting in a dataset of over 13,000 annotated images collected in a controlled lab environment. The trained ANN achieves a mean absolute error of 0.1506° and a root mean squared error of 0.1957°, offering accurate heading angle predictions using only monocular camera inputs. Experimental evaluations achieve 95% accuracy in UGV detection. This work contributes a vision-based, infrastructure- independent solution that demonstrates strong potential for deployment in GPS/GNSS-denied environments, supporting reliable multi-agent coordination under realistic dynamic conditions. A demonstration video showcasing the system's real-time performance, including UGV detection, heading angle prediction, and UAV alignment under dynamic conditions, is available at: https://github.com/Kooroshraf/UAV-UGV-Integration

