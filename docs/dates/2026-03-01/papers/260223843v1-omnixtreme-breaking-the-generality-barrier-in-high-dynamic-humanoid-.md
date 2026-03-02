---
layout: default
title: OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control
---

# OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control
**arXiv**：[2602.23843v1](https://arxiv.org/abs/2602.23843) · [PDF](https://arxiv.org/pdf/2602.23843.pdf)  
**作者**：Yunshen Wang, Shaohang Zhu, Peiyuan Zhi, Yuhan Li, Jiaxin Li, Yong-Lu Li, Yuchen Xiao, Xingxing Wang, Baoxiong Jia, Siyuan Huang  

**一句话要点**：提出OmniXtreme框架以解决高动态人形机器人控制中运动多样性扩展时的保真度下降问题

**关键词**：高动态人形控制, 流匹配策略, 仿真到现实精炼, 运动跟踪保真度, 通用运动技能

## 3 点简述
- 核心问题：运动库多样性扩展导致跟踪保真度崩溃，源于多运动优化瓶颈和物理执行约束
- 方法要点：使用流匹配策略和高容量架构解耦通用运动技能学习与仿真到现实的物理技能精炼
- 实验或效果：在多样高难度数据集上保持高保真度跟踪，并在真实机器人上成功执行多种极端运动

## 摘要（原文）

> High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

