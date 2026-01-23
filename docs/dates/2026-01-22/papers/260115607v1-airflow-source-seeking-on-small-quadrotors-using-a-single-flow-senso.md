---
layout: default
title: Airflow Source Seeking on Small Quadrotors Using a Single Flow Sensor
---

# Airflow Source Seeking on Small Quadrotors Using a Single Flow Sensor
**arXiv**：[2601.15607v1](https://arxiv.org/abs/2601.15607) · [PDF](https://arxiv.org/pdf/2601.15607.pdf)  
**作者**：Lenworth Thomas, Tjaden Bridges, Sarah Bergbreiter  

**一句话要点**：提出基于单气流传感器的小型四旋翼气流源追踪方法，以辅助化学羽流追踪。

**关键词**：气流源追踪, 小型四旋翼, 气流传感器, 羽流追踪, 算法改进

## 3 点简述
- 核心问题：小型四旋翼化学羽流追踪因气体传感器灵敏度低、响应慢而受限。
- 方法要点：使用定制气流传感器感知气流大小和方向，改进'Cast and Surge'算法。
- 实验或效果：验证系统能飞行中检测气流并朝向气流源，算法可靠找到气流源。

## 摘要（原文）

> As environmental disasters happen more frequently and severely, seeking the source of pollutants or harmful particulates using plume tracking becomes even more important. Plume tracking on small quadrotors would allow these systems to operate around humans and fly in more confined spaces, but can be challenging due to poor sensitivity and long response times from gas sensors that fit on small quadrotors. In this work, we present an approach to complement chemical plume tracking with airflow source-seeking behavior using a custom flow sensor that can sense both airflow magnitude and direction on small quadrotors < 100 g. We use this sensor to implement a modified version of the `Cast and Surge' algorithm that takes advantage of flow direction sensing to find and navigate towards flow sources. A series of characterization experiments verified that the system can detect airflow while in flight and reorient the quadrotor toward the airflow. Several trials with random starting locations and orientations were used to show that our source-seeking algorithm can reliably find a flow source. This work aims to provide a foundation for future platforms that can use flow sensors in concert with other sensors to enable richer plume tracking data collection and source-seeking.

