---
layout: default
title: Path Tracking with Dynamic Control Point Blending for Autonomous Vehicles: An Experimental Study
---

# Path Tracking with Dynamic Control Point Blending for Autonomous Vehicles: An Experimental Study
**arXiv**：[2602.01892v1](https://arxiv.org/abs/2602.01892) · [PDF](https://arxiv.org/pdf/2602.01892.pdf)  
**作者**：Alexandre Lombard, Florent Perronnet, Nicolas Gaud, Abdeljalil Abbas-Turki  

**一句话要点**：提出动态控制点混合路径跟踪框架，提升自动驾驶车辆在多种驾驶场景下的轨迹精度与适应性。

**关键词**：自动驾驶, 路径跟踪, 动态控制点, 混合控制器, 轨迹精度, 实验验证

## 3 点简述
- 核心问题：传统路径跟踪方法使用固定控制点（如前轴或后轴）可能导致低速或倒车时跟踪不稳定。
- 方法要点：通过动态插值前后轴控制点，结合前轴Stanley和后轴几何控制器混合，实现平滑转向过渡。
- 实验或效果：在仿真和真实车辆实验中，相比基线方法，提高了轨迹精度、转向平滑性和适应性。

## 摘要（原文）

> This paper presents an experimental study of a path-tracking framework for autonomous vehicles in which the lateral control command is applied to a dynamic control point along the wheelbase. Instead of enforcing a fixed reference at either the front or rear axle, the proposed method continuously interpolates between both, enabling smooth adaptation across driving contexts, including low-speed maneuvers and reverse motion. The lateral steering command is obtained by barycentric blending of two complementary controllers: a front-axle Stanley formulation and a rear-axle curvature-based geometric controller, yielding continuous transitions in steering behavior and improved tracking stability. In addition, we introduce a curvature-aware longitudinal control strategy based on virtual track borders and ray-tracing, which converts upcoming geometric constraints into a virtual obstacle distance and regulates speed accordingly. The complete approach is implemented in a unified control stack and validated in simulation and on a real autonomous vehicle equipped with GPS-RTK, radar, odometry, and IMU. The results in closed-loop tracking and backward maneuvers show improved trajectory accuracy, smoother steering profiles, and increased adaptability compared to fixed control-point baselines.

