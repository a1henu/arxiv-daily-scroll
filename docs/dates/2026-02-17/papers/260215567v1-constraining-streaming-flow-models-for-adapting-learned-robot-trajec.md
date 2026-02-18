---
layout: default
title: Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions
---

# Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions
**arXiv**：[2602.15567v1](https://arxiv.org/abs/2602.15567) · [PDF](https://arxiv.org/pdf/2602.15567.pdf)  
**作者**：Jieting Long, Dechuan Liu, Weidong Cai, Ian Manchester, Weiming Zhi  

**一句话要点**：提出约束感知流策略以增强机器人轨迹生成的安全性和适应性

**关键词**：机器人轨迹生成, 流策略, 约束适应, 安全控制, 多模态分布, 实时调整

## 3 点简述
- 机器人运动分布多模态，现有流策略缺乏训练后约束适应机制
- CASF通过可微距离函数将约束转化为局部度量，实时重塑速度场
- 在模拟和真实任务中验证，优于后处理投影基线，保持平滑和动态一致性

## 摘要（原文）

> Robot motion distributions often exhibit multi-modality and require flexible generative models for accurate representation. Streaming Flow Policies (SFPs) have recently emerged as a powerful paradigm for generating robot trajectories by integrating learned velocity fields directly in action space, enabling smooth and reactive control. However, existing formulations lack mechanisms for adapting trajectories post-training to enforce safety and task-specific constraints. We propose Constraint-Aware Streaming Flow (CASF), a framework that augments streaming flow policies with constraint-dependent metrics that reshape the learned velocity field during execution. CASF models each constraint, defined in either the robot's workspace or configuration space, as a differentiable distance function that is converted into a local metric and pulled back into the robot's control space. Far from restricted regions, the resulting metric reduces to the identity; near constraint boundaries, it smoothly attenuates or redirects motion, effectively deforming the underlying flow to maintain safety. This allows trajectories to be adapted in real time, ensuring that robot actions respect joint limits, avoid collisions, and remain within feasible workspaces, while preserving the multi-modal and reactive properties of streaming flow policies. We demonstrate CASF in simulated and real-world manipulation tasks, showing that it produces constraint-satisfying trajectories that remain smooth, feasible, and dynamically consistent, outperforming standard post-hoc projection baselines.

