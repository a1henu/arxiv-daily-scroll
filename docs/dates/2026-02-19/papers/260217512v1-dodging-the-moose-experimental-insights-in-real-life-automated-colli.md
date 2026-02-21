---
layout: default
title: Dodging the Moose: Experimental Insights in Real-Life Automated Collision Avoidance
---

# Dodging the Moose: Experimental Insights in Real-Life Automated Collision Avoidance
**arXiv**：[2602.17512v1](https://arxiv.org/abs/2602.17512) · [PDF](https://arxiv.org/pdf/2602.17512.pdf)  
**作者**：Leila Gharavi, Simone Baldi, Yuki Hosomi, Tona Sato, Bart De Schutter, Binh-Minh Nguyen, Hiroshi Fujimoto  

**一句话要点**：提出人机协同规划策略以解决紧急避障场景中非线性MPC实时性不足的问题

**关键词**：模型预测控制, 紧急避障, 前馈规划, 实时规划, 自动驾驶, 实车实验

## 3 点简述
- 核心问题：非线性MPC在紧急避障场景中因计算需求高而难以实时提供可行解
- 方法要点：引入前馈规划器模仿人类反应，辅助MPC在优化失败时生成避障轨迹
- 实验或效果：通过实车实验验证策略在不同速度和紧急程度下的有效性

## 摘要（原文）

> The sudden appearance of a static obstacle on the road, i.e. the moose test, is a well-known emergency scenario in collision avoidance for automated driving. Model Predictive Control (MPC) has long been employed for planning and control of automated vehicles in the state of the art. However, real-time implementation of automated collision avoidance in emergency scenarios such as the moose test remains unaddressed due to the high computational demand of MPC for evasive action in such hazardous scenarios. This paper offers new insights into real-time collision avoidance via the experimental imple- mentation of MPC for motion planning after a sudden and unexpected appearance of a static obstacle. As the state-of-the-art nonlinear MPC shows limited capability to provide an acceptable solution in real-time, we propose a human-like feed-forward planner to assist when the MPC optimization problem is either infeasible or unable to find a suitable solution due to the poor quality of its initial guess. We introduce the concept of maximum steering maneuver to design the feed-forward planner and mimic a human-like reaction after detecting the static obstacle on the road. Real-life experiments are conducted across various speeds and level of emergency using FPEV2-Kanon electric vehicle. Moreover, we demonstrate the effectiveness of our planning strategy via comparison with the state-of- the-art MPC motion planner.

