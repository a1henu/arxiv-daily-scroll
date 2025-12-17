---
layout: default
title: Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field
---

# Interactive Motion Planning for Human-Robot Collaboration Based on Human-Centric Configuration Space Ergonomic Field
**arXiv**：[2512.14111v1](https://arxiv.org/abs/2512.14111) · [PDF](https://arxiv.org/pdf/2512.14111.pdf)  
**作者**：Chenzui Li, Yiming Chen, Xi Wu, Tao Teng, Sylvain Calinon, Darwin Caldwell, Fei Chen  

**一句话要点**：提出基于人机配置空间人机工程场的交互式运动规划方法，以提升工业人机协作的实时性和人机工程安全性。

**关键词**：人机协作, 运动规划, 人机工程学, 配置空间, 梯度优化, 实时控制

## 3 点简述
- 工业人机协作需兼顾无碰撞、响应快和人机工程安全，以减少疲劳和肌肉骨骼风险。
- 提出配置空间人机工程场，作为连续可微场量化人机工程质量并提供梯度，支持实时规划。
- 在基准测试和硬件实验中，该方法提高了成功率、降低了人机工程成本和肌肉激活，验证了实际效益。

## 摘要（原文）

> Industrial human-robot collaboration requires motion planning that is collision-free, responsive, and ergonomically safe to reduce fatigue and musculoskeletal risk. We propose the Configuration Space Ergonomic Field (CSEF), a continuous and differentiable field over the human joint space that quantifies ergonomic quality and provides gradients for real-time ergonomics-aware planning. An efficient algorithm constructs CSEF from established metrics with joint-wise weighting and task conditioning, and we integrate it into a gradient-based planner compatible with impedance-controlled robots. In a 2-DoF benchmark, CSEF-based planning achieves higher success rates, lower ergonomic cost, and faster computation than a task-space ergonomic planner. Hardware experiments with a dual-arm robot in unimanual guidance, collaborative drilling, and bimanual cocarrying show faster ergonomic cost reduction, closer tracking to optimized joint targets, and lower muscle activation than a point-to-point baseline. CSEF-based planning method reduces average ergonomic scores by up to 10.31% for collaborative drilling tasks and 5.60% for bimanual co-carrying tasks while decreasing activation in key muscle groups, indicating practical benefits for real-world deployment.

