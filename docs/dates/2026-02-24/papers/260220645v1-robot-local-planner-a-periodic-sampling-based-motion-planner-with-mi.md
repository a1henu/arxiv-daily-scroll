---
layout: default
title: Robot Local Planner: A Periodic Sampling-Based Motion Planner with Minimal Waypoints for Home Environments
---

# Robot Local Planner: A Periodic Sampling-Based Motion Planner with Minimal Waypoints for Home Environments
**arXiv**：[2602.20645v1](https://arxiv.org/abs/2602.20645) · [PDF](https://arxiv.org/pdf/2602.20645.pdf)  
**作者**：Keisuke Takeshita, Takahiro Yamazaki, Tomohiro Ono, Takashi Yamamoto  

**一句话要点**：提出周期性采样运动规划器，以最小化路径点实现家庭环境快速安全操作

**关键词**：机器人运动规划, 家庭环境操作, 周期性采样, 最小路径点, 逆运动学鲁棒性

## 3 点简述
- 核心问题：家庭环境中需快速安全执行操作任务，同时处理识别与控制误差
- 方法要点：周期性采样规划结合最小路径点，增强计算效率与运动最优性
- 实验或效果：评估显示优于现有方法，整理任务成功率高且操作时间短

## 摘要（原文）

> The objective of this study is to enable fast and safe manipulation tasks in home environments. Specifically, we aim to develop a system that can recognize its surroundings and identify target objects while in motion, enabling it to plan and execute actions accordingly. We propose a periodic sampling-based whole-body trajectory planning method, called the "Robot Local Planner (RLP)." This method leverages unique features of home environments to enhance computational efficiency, motion optimality, and robustness against recognition and control errors, all while ensuring safety. The RLP minimizes computation time by planning with minimal waypoints and generating safe trajectories. Furthermore, overall motion optimality is improved by periodically executing trajectory planning to select more optimal motions. This approach incorporates inverse kinematics that are robust to base position errors, further enhancing robustness. Evaluation experiments demonstrated that the RLP outperformed existing methods in terms of motion planning time, motion duration, and robustness, confirming its effectiveness in home environments. Moreover, application experiments using a tidy-up task achieved high success rates and short operation times, thereby underscoring its practical feasibility.

