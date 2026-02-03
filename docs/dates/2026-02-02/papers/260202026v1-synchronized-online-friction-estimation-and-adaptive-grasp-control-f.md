---
layout: default
title: Synchronized Online Friction Estimation and Adaptive Grasp Control for Robust Gentle Grasp
---

# Synchronized Online Friction Estimation and Adaptive Grasp Control for Robust Gentle Grasp
**arXiv**：[2602.02026v1](https://arxiv.org/abs/2602.02026) · [PDF](https://arxiv.org/pdf/2602.02026.pdf)  
**作者**：Zhenwei Niu, Xiaoyi Chen, Jiayu Hu, Zhaoyang Liu, Xiaozu Ju  

**一句话要点**：提出同步在线摩擦估计与自适应抓取控制框架，实现稳健轻柔抓取

**关键词**：机器人抓取, 摩擦估计, 自适应控制, 触觉传感器, 粒子滤波, 闭环控制

## 3 点简述
- 核心问题：机器人轻柔抓取中摩擦系数未知导致抓取不稳定或损伤物体
- 方法要点：基于粒子滤波实时估计摩擦系数，并集成到反应式控制器动态调节抓取力
- 实验或效果：通过广泛机器人实验验证了框架的可靠性和效率

## 摘要（原文）

> We introduce a unified framework for gentle robotic grasping that synergistically couples real-time friction estimation with adaptive grasp control. We propose a new particle filter-based method for real-time estimation of the friction coefficient using vision-based tactile sensors. This estimate is seamlessly integrated into a reactive controller that dynamically modulates grasp force to maintain a stable grip. The two processes operate synchronously in a closed-loop: the controller uses the current best estimate to adjust the force, while new tactile feedback from this action continuously refines the estimation. This creates a highly responsive and robust sensorimotor cycle. The reliability and efficiency of the complete framework are validated through extensive robotic experiments.

