---
layout: default
title: Hybrid F' and ROS2 Architecture for Vision-Based Autonomous Flight: Design and Experimental Validation
---

# Hybrid F' and ROS2 Architecture for Vision-Based Autonomous Flight: Design and Experimental Validation
**arXiv**：[2602.15398v1](https://arxiv.org/abs/2602.15398) · [PDF](https://arxiv.org/pdf/2602.15398.pdf)  
**作者**：Abdelrahman Metwally, Monijesu James, Aleksey Fedoseev, Miguel Altamirano Cabrera, Dzmitry Tsetserukou, Andrey Somov  

**一句话要点**：提出结合F'与ROS2的混合架构，以支持视觉自主飞行的实时控制与感知需求。

**关键词**：自主飞行, 混合架构, 视觉导航, 实时系统, ROS2, F'框架

## 3 点简述
- 核心问题：自主航空系统需平衡确定性实时控制与先进感知能力。
- 方法要点：通过Protocol Buffers桥接NASA F'框架与ROS2中间件，实现混合架构。
- 实验或效果：室内四旋翼飞行测试验证了高频率位置估计、低延迟和稳健集成性能。

## 摘要（原文）

> Autonomous aerospace systems require architectures that balance deterministic real-time control with advanced perception capabilities. This paper presents an integrated system combining NASA's F' flight software framework with ROS2 middleware via Protocol Buffers bridging. We evaluate the architecture through a 32.25-minute indoor quadrotor flight test using vision-based navigation. The vision system achieved 87.19 Hz position estimation with 99.90\% data continuity and 11.47 ms mean latency, validating real-time performance requirements. All 15 ground commands executed successfully with 100 % success rate, demonstrating robust F'--PX4 integration. System resource utilization remained low (15.19 % CPU, 1,244 MB RAM) with zero stale telemetry messages, confirming efficient operation on embedded platforms. Results validate the feasibility of hybrid flight-software architectures combining certification-grade determinism with flexible autonomy for autonomous aerial vehicles.

