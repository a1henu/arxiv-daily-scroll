---
layout: default
title: A Faster and More Reliable Middleware for Autonomous Driving Systems
---

# A Faster and More Reliable Middleware for Autonomous Driving Systems
**arXiv**：[2510.11448v1](https://arxiv.org/abs/2510.11448) · [PDF](https://arxiv.org/pdf/2510.11448.pdf)  
**作者**：Yuankai He, Hanlin Chen, Weisong Shi  

**一句话要点**：提出Sensor-in-Memory共享内存传输以降低自动驾驶系统延迟

**关键词**：自动驾驶系统, 共享内存传输, ROS 2优化, 低延迟中间件, 数据新鲜度, 实时控制

## 3 点简述
- ROS 2中间件在单计算单元多节点时引入高延迟，影响自动驾驶安全控制循环
- SIM使用共享内存、原生数据布局和锁自由双缓冲，优先数据新鲜度，集成ROS 2
- 实验显示SIM显著降低延迟，提升定位频率，减少紧急制动距离

## 摘要（原文）

> Ensuring safety in high-speed autonomous vehicles requires rapid control
> loops and tightly bounded delays from perception to actuation. Many open-source
> autonomy systems rely on ROS 2 middleware; when multiple sensor and control
> nodes share one compute unit, ROS 2 and its DDS transports add significant
> (de)serialization, copying, and discovery overheads, shrinking the available
> time budget. We present Sensor-in-Memory (SIM), a shared-memory transport
> designed for intra-host pipelines in autonomous vehicles. SIM keeps sensor data
> in native memory layouts (e.g., cv::Mat, PCL), uses lock-free bounded double
> buffers that overwrite old data to prioritize freshness, and integrates into
> ROS 2 nodes with four lines of code. Unlike traditional middleware, SIM
> operates beside ROS 2 and is optimized for applications where data freshness
> and minimal latency outweigh guaranteed completeness. SIM provides sequence
> numbers, a writer heartbeat, and optional checksums to ensure ordering,
> liveness, and basic integrity. On an NVIDIA Jetson Orin Nano, SIM reduces
> data-transport latency by up to 98% compared to ROS 2 zero-copy transports such
> as FastRTPS and Zenoh, lowers mean latency by about 95%, and narrows
> 95th/99th-percentile tail latencies by around 96%. In tests on a
> production-ready Level 4 vehicle running Autoware.Universe, SIM increased
> localization frequency from 7.5 Hz to 9.5 Hz. Applied across all
> latency-critical modules, SIM cut average perception-to-decision latency from
> 521.91 ms to 290.26 ms, reducing emergency braking distance at 40 mph (64 km/h)
> on dry concrete by 13.6 ft (4.14 m).

