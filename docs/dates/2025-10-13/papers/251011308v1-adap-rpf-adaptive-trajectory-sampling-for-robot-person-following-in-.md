---
layout: default
title: Adap-RPF: Adaptive Trajectory Sampling for Robot Person Following in Dynamic Crowded Environments
---

# Adap-RPF: Adaptive Trajectory Sampling for Robot Person Following in Dynamic Crowded Environments
**arXiv**：[2510.11308v1](https://arxiv.org/abs/2510.11308) · [PDF](https://arxiv.org/pdf/2510.11308.pdf)  
**作者**：Weixi Situ, Hanjing Ye, Jianwei Peng, Yu Zhan, Hong Zhang  

**一句话要点**：提出自适应轨迹采样方法以解决动态拥挤环境中机器人跟随的遮挡问题

**关键词**：机器人跟随, 轨迹采样, 遮挡处理, 模型预测控制, 动态环境

## 3 点简述
- 核心问题：动态拥挤环境中频繁遮挡导致机器人跟随困难
- 方法要点：生成密集候选点并评估，结合预测设计MPPI控制器
- 实验或效果：在平滑性、安全性、鲁棒性和人类舒适度上优于基线

## 摘要（原文）

> Robot person following (RPF) is a core capability in human-robot interaction,
> enabling robots to assist users in daily activities, collaborative work, and
> other service scenarios. However, achieving practical RPF remains challenging
> due to frequent occlusions, particularly in dynamic and crowded environments.
> Existing approaches often rely on fixed-point following or sparse
> candidate-point selection with oversimplified heuristics, which cannot
> adequately handle complex occlusions caused by moving obstacles such as
> pedestrians. To address these limitations, we propose an adaptive trajectory
> sampling method that generates dense candidate points within socially aware
> zones and evaluates them using a multi-objective cost function. Based on the
> optimal point, a person-following trajectory is estimated relative to the
> predicted motion of the target. We further design a prediction-aware model
> predictive path integral (MPPI) controller that simultaneously tracks this
> trajectory and proactively avoids collisions using predicted pedestrian
> motions. Extensive experiments show that our method outperforms
> state-of-the-art baselines in smoothness, safety, robustness, and human
> comfort, with its effectiveness further demonstrated on a mobile robot in
> real-world scenarios.

