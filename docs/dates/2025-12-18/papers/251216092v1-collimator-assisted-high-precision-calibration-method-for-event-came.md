---
layout: default
title: Collimator-assisted high-precision calibration method for event cameras
---

# Collimator-assisted high-precision calibration method for event cameras
**arXiv**：[2512.16092v1](https://arxiv.org/abs/2512.16092) · [PDF](https://arxiv.org/pdf/2512.16092.pdf)  
**作者**：Zibin Liu, Shunkun Liang, Banglei Guan, Dongcai Tan, Yang Shang, Qifeng Yu  

**一句话要点**：提出基于准直器闪烁星点模式的事件相机高精度标定方法，以解决长距离测量场景下的几何标定挑战。

**关键词**：事件相机标定, 准直器辅助, 长距离测量, 高精度优化, 几何参数估计

## 3 点简述
- 核心问题：事件相机在长距离测量场景中的几何标定（内参和外参确定）仍具挑战性。
- 方法要点：使用准直器生成闪烁星点模式，先线性求解相机参数，再非线性优化提升精度。
- 实验或效果：真实世界实验表明，该方法在准确性和可靠性上优于现有事件相机标定方法。

## 摘要（原文）

> Event cameras are a new type of brain-inspired visual sensor with advantages such as high dynamic range and high temporal resolution. The geometric calibration of event cameras, which involves determining their intrinsic and extrinsic parameters, particularly in long-range measurement scenarios, remains a significant challenge. To address the dual requirements of long-distance and high-precision measurement, we propose an event camera calibration method utilizing a collimator with flickering star-based patterns. The proposed method first linearly solves camera parameters using the sphere motion model of the collimator, followed by nonlinear optimization to refine these parameters with high precision. Through comprehensive real-world experiments across varying conditions, we demonstrate that the proposed method consistently outperforms existing event camera calibration methods in terms of accuracy and reliability.

