---
layout: default
title: Understanding Sensor Vulnerabilities in Industrial XR Tracking
---

# Understanding Sensor Vulnerabilities in Industrial XR Tracking
**arXiv**：[2602.14413v1](https://arxiv.org/abs/2602.14413) · [PDF](https://arxiv.org/pdf/2602.14413.pdf)  
**作者**：Sourya Saha, Md. Nurul Absur  

**一句话要点**：通过受控实验研究工业XR中传感器退化对VIO跟踪的影响

**关键词**：工业XR系统, 视觉-惯性里程计, 传感器退化, 故障注入, 姿态跟踪, 轨迹偏差

## 3 点简述
- 核心问题：工业XR系统在非理想传感条件下VIO性能退化未被充分理解
- 方法要点：采用系统故障注入方法，分析视觉和惯性传感器退化对VIO的影响
- 实验或效果：发现惯性传感器退化导致轨迹偏差可达数百至数千米，视觉退化误差则较小

## 摘要（原文）

> Extended Reality (XR) systems deployed in industrial and operational settings rely on Visual--Inertial Odometry (VIO) for continuous six-degree-of-freedom pose tracking, yet these environments often involve sensing conditions that deviate from ideal assumptions. Despite this, most VIO evaluations emphasize nominal sensor behavior, leaving the effects of sustained sensor degradation under operational conditions insufficiently understood. This paper presents a controlled empirical study of VIO behavior under degraded sensing, examining faults affecting visual and inertial modalities across a range of operating regimes. Through systematic fault injection and quantitative evaluation, we observe a pronounced asymmetry in fault impact where degradations affecting visual sensing typically lead to bounded pose errors on the order of centimeters, whereas degradations affecting inertial sensing can induce substantially larger trajectory deviations, in some cases reaching hundreds to thousands of meters. These observations motivate greater emphasis on inertial reliability in the evaluation and design of XR systems for real-life industrial settings.

