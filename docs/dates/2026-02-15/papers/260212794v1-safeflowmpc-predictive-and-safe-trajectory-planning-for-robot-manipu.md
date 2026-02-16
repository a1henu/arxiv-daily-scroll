---
layout: default
title: SafeFlowMPC: Predictive and Safe Trajectory Planning for Robot Manipulators with Learning-based Policies
---

# SafeFlowMPC: Predictive and Safe Trajectory Planning for Robot Manipulators with Learning-based Policies
**arXiv**：[2602.12794v1](https://arxiv.org/abs/2602.12794) · [PDF](https://arxiv.org/pdf/2602.12794.pdf)  
**作者**：Thies Oelerich, Gerald Ebmer, Christian Hartl-Nesic, Andreas Kugi  

**一句话要点**：提出SafeFlowMPC结合流匹配与在线优化，实现机器人安全轨迹规划

**关键词**：机器人轨迹规划, 流匹配, 模型预测控制, 安全保证, 学习策略

## 3 点简述
- 核心问题：学习策略缺乏安全保证，优化方法灵活性不足
- 方法要点：融合流匹配与模型预测控制，确保实时安全
- 实验或效果：在KUKA 7-DoF机械臂上验证抓取和人机交接任务

## 摘要（原文）

> The emerging integration of robots into everyday life brings several major challenges. Compared to classical industrial applications, more flexibility is needed in combination with real-time reactivity. Learning-based methods can train powerful policies based on demonstrated trajectories, such that the robot generalizes a task to similar situations. However, these black-box models lack interpretability and rigorous safety guarantees. Optimization-based methods provide these guarantees but lack the required flexibility and generalization capabilities. This work proposes SafeFlowMPC, a combination of flow matching and online optimization to combine the strengths of learning and optimization. This method guarantees safety at all times and is designed to meet the demands of real-time execution by using a suboptimal model-predictive control formulation. SafeFlowMPC achieves strong performance in three real-world experiments on a KUKA 7-DoF manipulator, namely two grasping experiment and a dynamic human-robot object handover experiment. A video of the experiments is available at http://www.acin.tuwien.ac.at/42d6. The code is available at https://github.com/TU-Wien-ACIN-CDS/SafeFlowMPC.

