---
layout: default
title: Visual Cooperative Drone Tracking for Open-Path Gas Measurements
---

# Visual Cooperative Drone Tracking for Open-Path Gas Measurements
**arXiv**：[2602.20768v1](https://arxiv.org/abs/2602.20768) · [PDF](https://arxiv.org/pdf/2602.20768.pdf)  
**作者**：Marius Schaab, Alisha Kiefer, Thomas Wiedemann, Patrick Hinsen, Achim J. Lilienthal  

**一句话要点**：提出基于视觉协同无人机跟踪的机器人系统，用于自动化开放路径气体测量

**关键词**：开放路径气体测量, 视觉跟踪, 无人机协同, 激光对准, 气体层析成像

## 3 点简述
- 核心问题：开放路径激光气体测量需专用反射面，自动化空间采样困难
- 方法要点：地面单元通过变焦相机视觉跟踪无人机LED标记，结合GNSS信息对准激光束
- 实验或效果：户外实验验证系统在60米距离内成功自主跟踪并有效测量CO2

## 摘要（原文）

> Open-path Tunable Diode Laser Absorption Spectroscopy offers an effective method for measuring, mapping, and monitoring gas concentrations, such as leaking CO2 or methane. Compared to spatial sampling of gas distributions using in-situ sensors, open-path sensors in combination with gas tomography algorithms can cover large outdoor environments faster in a non-invasive way. However, the requirement of a dedicated reflection surface for the open-path laser makes automating the spatial sampling process challenging. This publication presents a robotic system for collecting open-path measurements, making use of a sensor mounted on a ground-based pan-tilt unit and a small drone carrying a reflector. By means of a zoom camera, the ground unit visually tracks red LED markers mounted on the drone and aligns the sensor's laser beam with the reflector. Incorporating GNSS position information provided by the drone's flight controller further improves the tracking approach. Outdoor experiments validated the system's performance, demonstrating successful autonomous tracking and valid CO2 measurements at distances up to 60 meters. Furthermore, the system successfully measured a CO2 plume without interference from the drone's propulsion system, demonstrating its superiority compared to flying in-situ sensors.

