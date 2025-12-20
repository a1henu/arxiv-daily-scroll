---
layout: default
title: AG-MPBS: a Mobility-Aware Prediction and Behavior-Based Scheduling Framework for Air-Ground Unmanned Systems
---

# AG-MPBS: a Mobility-Aware Prediction and Behavior-Based Scheduling Framework for Air-Ground Unmanned Systems
**arXiv**：[2512.16454v1](https://arxiv.org/abs/2512.16454) · [PDF](https://arxiv.org/pdf/2512.16454.pdf)  
**作者**：Tianhao Shao, Kaixing Zhao, Feng Liu, Lixin Yang, Bin Guo  

**一句话要点**：提出AG-MPBS框架，通过移动性预测与行为分类优化空地无人系统的实时任务调度

**关键词**：无人系统调度, 移动性预测, 行为分类, 动态优先级调度, 空地协同

## 3 点简述
- 核心问题：空地无人系统在时间敏感任务中高效招募设备的挑战
- 方法要点：集成行为分类、移动性预测和动态优先级调度模块
- 实验或效果：在GeoLife数据集上验证，提升任务完成效率和资源利用率

## 摘要（原文）

> As unmanned systems such as Unmanned Aerial Vehicles (UAVs) and Unmanned Ground Vehicles (UGVs) become increasingly important to applications like urban sensing and emergency response, efficiently recruiting these autonomous devices to perform time-sensitive tasks has become a critical challenge. This paper presents MPBS (Mobility-aware Prediction and Behavior-based Scheduling), a scalable task recruitment framework that treats each device as a recruitable "user". MPBS integrates three key modules: a behavior-aware KNN classifier, a time-varying Markov prediction model for forecasting device mobility, and a dynamic priority scheduling mechanism that considers task urgency and base station performance. By combining behavioral classification with spatiotemporal prediction, MPBS adaptively assigns tasks to the most suitable devices in real time. Experimental evaluations on the real-world GeoLife dataset show that MPBS significantly improves task completion efficiency and resource utilization. The proposed framework offers a predictive, behavior-aware solution for intelligent and collaborative scheduling in unmanned systems.

