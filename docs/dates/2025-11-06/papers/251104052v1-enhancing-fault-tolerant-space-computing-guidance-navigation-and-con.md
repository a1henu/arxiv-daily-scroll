---
layout: default
title: Enhancing Fault-Tolerant Space Computing: Guidance Navigation and Control (GNC) and Landing Vision System (LVS) Implementations on Next-Gen Multi-Core Processors
---

# Enhancing Fault-Tolerant Space Computing: Guidance Navigation and Control (GNC) and Landing Vision System (LVS) Implementations on Next-Gen Multi-Core Processors
**arXiv**：[2511.04052v1](https://arxiv.org/abs/2511.04052) · [PDF](https://arxiv.org/pdf/2511.04052.pdf)  
**作者**：Kyongsik Yun, David Bayard, Gerik Kubiak, Austin Owens, Andrew Johnson, Ryan Johnson, Dan Scharf, Thomas Lu  

**一句话要点**：提出ARBITER机制以增强行星探索任务中多核处理器的容错计算能力

**关键词**：容错计算, 多核处理器, GNC算法, LVS系统, 故障检测, 轨迹优化

## 3 点简述
- 核心问题：行星探索任务需高性能容错计算支持自主GNC和LVS操作
- 方法要点：部署GNC和LVS算法于多核处理器，并引入ARBITER进行实时故障检测与纠正
- 实验或效果：LVS图像处理加速15倍，GFOLD轨迹优化加速超250倍，并通过故障注入验证

## 摘要（原文）

> Future planetary exploration missions demand high-performance, fault-tolerant
> computing to enable autonomous Guidance, Navigation, and Control (GNC) and
> Lander Vision System (LVS) operations during Entry, Descent, and Landing (EDL).
> This paper evaluates the deployment of GNC and LVS algorithms on
> next-generation multi-core processors--HPSC, Snapdragon VOXL2, and AMD Xilinx
> Versal--demonstrating up to 15x speedup for LVS image processing and over 250x
> speedup for Guidance for Fuel-Optimal Large Divert (GFOLD) trajectory
> optimization compared to legacy spaceflight hardware. To ensure computational
> reliability, we present ARBITER (Asynchronous Redundant Behavior Inspection for
> Trusted Execution and Recovery), a Multi-Core Voting (MV) mechanism that
> performs real-time fault detection and correction across redundant cores.
> ARBITER is validated in both static optimization tasks (GFOLD) and dynamic
> closed-loop control (Attitude Control System). A fault injection study further
> identifies the gradient computation stage in GFOLD as the most sensitive to
> bit-level errors, motivating selective protection strategies and vector-based
> output arbitration. This work establishes a scalable and energy-efficient
> architecture for future missions, including Mars Sample Return, Enceladus
> Orbilander, and Ceres Sample Return, where onboard autonomy, low latency, and
> fault resilience are critical.

