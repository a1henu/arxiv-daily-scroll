---
layout: default
title: High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle
---

# High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle
**arXiv**：[2512.09798v1](https://arxiv.org/abs/2512.09798) · [PDF](https://arxiv.org/pdf/2512.09798.pdf)  
**作者**：Misael Mamani, Mariel Fernandez, Grace Luna, Steffani Limachi, Leonel Apaza, Carolina Montes-Dávalos, Marcelo Herrera, Edwin Salcedo  

**一句话要点**：提出太阳能自主水面无人艇，通过注射器采样架构实现高分辨率水质监测。

**关键词**：自主水面无人艇, 水质采样, ROS 2, 行为树架构, 模块化系统, 太阳能供电

## 3 点简述
- 问题：现有无人艇采样点少或传感器代表性差，难以满足水质评估的空间分辨率需求。
- 方法：集成ROS 2自主栈、行为树架构和模块化6x12注射器采样系统，支持GPS-RTK导航与障碍检测。
- 效果：在玻利维亚Achocalla Lagoon试验中，达到87%航点精度，测量结果与手动采样可比。

## 摘要（原文）

> Accurate water quality assessment requires spatially resolved sampling, yet most unmanned surface vehicles (USVs) can collect only a limited number of samples or rely on single-point sensors with poor representativeness. This work presents a solar-powered, fully autonomous USV featuring a novel syringe-based sampling architecture capable of acquiring 72 discrete, contamination-minimized water samples per mission. The vehicle incorporates a ROS 2 autonomy stack with GPS-RTK navigation, LiDAR and stereo-vision obstacle detection, Nav2-based mission planning, and long-range LoRa supervision, enabling dependable execution of sampling routes in unstructured environments. The platform integrates a behavior-tree autonomy architecture adapted from Nav2, enabling mission-level reasoning and perception-aware navigation. A modular 6x12 sampling system, controlled by distributed micro-ROS nodes, provides deterministic actuation, fault isolation, and rapid module replacement, achieving spatial coverage beyond previously reported USV-based samplers. Field trials in Achocalla Lagoon (La Paz, Bolivia) demonstrated 87% waypoint accuracy, stable autonomous navigation, and accurate physicochemical measurements (temperature, pH, conductivity, total dissolved solids) comparable to manually collected references. These results demonstrate that the platform enables reliable high-resolution sampling and autonomous mission execution, providing a scalable solution for aquatic monitoring in remote environments.

