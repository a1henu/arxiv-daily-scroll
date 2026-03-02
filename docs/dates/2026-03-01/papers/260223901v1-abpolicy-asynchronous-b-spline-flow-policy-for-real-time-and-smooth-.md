---
layout: default
title: ABPolicy: Asynchronous B-Spline Flow Policy for Real-Time and Smooth Robotic Manipulation
---

# ABPolicy: Asynchronous B-Spline Flow Policy for Real-Time and Smooth Robotic Manipulation
**arXiv**：[2602.23901v1](https://arxiv.org/abs/2602.23901) · [PDF](https://arxiv.org/pdf/2602.23901.pdf)  
**作者**：Fan Yang, Peiguang Jing, Kaihua Qu, Ningyuan Zhao, Yuting Su  

**一句话要点**：提出ABPolicy异步B样条流策略，以解决机器人操作中动作不平滑和响应延迟问题。

**关键词**：机器人操作, 异步推理, B样条表示, 动作平滑, 实时控制, 流匹配策略

## 3 点简述
- 核心问题：同步推理导致动作抖动、不连续和停顿，影响机器人操作的平滑性和响应性。
- 方法要点：采用B样条控制点动作空间，结合双向动作预测和异步推理，确保动作平滑和实时更新。
- 实验或效果：在七项任务中评估，减少轨迹急动，提升运动平滑性和性能。

## 摘要（原文）

> Robotic manipulation requires policies that are smooth and responsive to evolving observations. However, synchronous inference in the raw action space introduces several challenges, including intra-chunk jitter, inter-chunk discontinuities, and stop-and-go execution. These issues undermine a policy's smoothness and its responsiveness to environmental changes. We propose ABPolicy, an asynchronous flow-matching policy that operates in a B-spline control-point action space. First, the B-spline representation ensures intra-chunk smoothness. Second, we introduce bidirectional action prediction coupled with refitting optimization to enforce inter-chunk continuity. Finally, by leveraging asynchronous inference, ABPolicy delivers real-time, continuous updates. We evaluate ABPolicy across seven tasks encompassing both static settings and dynamic settings with moving objects. Empirical results indicate that ABPolicy reduces trajectory jerk, leading to smoother motion and improved performance. Project website: https://teee000.github.io/ABPolicy/.

