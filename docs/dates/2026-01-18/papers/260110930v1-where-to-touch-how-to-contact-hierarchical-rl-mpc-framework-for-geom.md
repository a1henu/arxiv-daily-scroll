---
layout: default
title: Where to Touch, How to Contact: Hierarchical RL-MPC Framework for Geometry-Aware Long-Horizon Dexterous Manipulation
---

# Where to Touch, How to Contact: Hierarchical RL-MPC Framework for Geometry-Aware Long-Horizon Dexterous Manipulation
**arXiv**：[2601.10930v1](https://arxiv.org/abs/2601.10930) · [PDF](https://arxiv.org/pdf/2601.10930.pdf)  
**作者**：Zhixian Xie, Yu Xiang, Michael Posa, Wanxin Jin  

**一句话要点**：提出分层RL-MPC框架以解决几何感知长时程灵巧操作问题

**关键词**：灵巧操作, 分层强化学习, 模型预测控制, 几何感知, 接触动力学, 仿真到现实迁移

## 3 点简述
- 核心问题：灵巧操作需联合推理几何、运动学约束和非光滑接触动力学，端到端方法数据需求大、泛化弱。
- 方法要点：高层RL预测接触意图（接触位置和子目标位姿），低层MPC优化接触模式并规划动作以实现子目标。
- 实验效果：在非抓取任务中实现近100%成功率，数据需求减少10倍，鲁棒性强且零样本仿真到现实迁移。

## 摘要（原文）

> A key challenge in contact-rich dexterous manipulation is the need to jointly reason over geometry, kinematic constraints, and intricate, nonsmooth contact dynamics. End-to-end visuomotor policies bypass this structure, but often require large amounts of data, transfer poorly from simulation to reality, and generalize weakly across tasks/embodiments. We address those limitations by leveraging a simple insight: dexterous manipulation is inherently hierarchical - at a high level, a robot decides where to touch (geometry) and move the object (kinematics); at a low level it determines how to realize that plan through contact dynamics. Building on this insight, we propose a hierarchical RL--MPC framework in which a high-level reinforcement learning (RL) policy predicts a contact intention, a novel object-centric interface that specifies (i) an object-surface contact location and (ii) a post-contact object-level subgoal pose. Conditioned on this contact intention, a low-level contact-implicit model predictive control (MPC) optimizes local contact modes and replans with contact dynamics to generate robot actions that robustly drive the object toward each subgoal. We evaluate the framework on non-prehensile tasks, including geometry-generalized pushing and object 3D reorientation. It achieves near-100% success with substantially reduced data (10x less than end-to-end baselines), highly robust performance, and zero-shot sim-to-real transfer.

