---
layout: default
title: Learning-Based Safety-Aware Task Scheduling for Efficient Human-Robot Collaboration
---

# Learning-Based Safety-Aware Task Scheduling for Efficient Human-Robot Collaboration
**arXiv**：[2512.17560v1](https://arxiv.org/abs/2512.17560) · [PDF](https://arxiv.org/pdf/2512.17560.pdf)  
**作者**：M. Faroni, A. Spano, A. M. Zanchettin, P. Rocco  

**一句话要点**：提出基于学习的任务调度方法，以在协作机器人中平衡安全与效率

**关键词**：协作机器人, 安全感知调度, 深度学习, 人机交互, 效率优化

## 3 点简述
- 核心问题：传统安全措施在频繁人机交互时降低机器人效率
- 方法要点：使用深度学习模型直接从执行数据学习安全逻辑对速度的影响
- 实验或效果：在拣选包装场景中显著减少循环时间

## 摘要（原文）

> Ensuring human safety in collaborative robotics can compromise efficiency because traditional safety measures increase robot cycle time when human interaction is frequent. This paper proposes a safety-aware approach to mitigate efficiency losses without assuming prior knowledge of safety logic. Using a deep-learning model, the robot learns the relationship between system state and safety-induced speed reductions based on execution data. Our framework does not explicitly predict human motions but directly models the interaction effects on robot speed, simplifying implementation and enhancing generalizability to different safety logics. At runtime, the learned model optimizes task selection to minimize cycle time while adhering to safety requirements. Experiments on a pick-and-packaging scenario demonstrated significant reductions in cycle times.

