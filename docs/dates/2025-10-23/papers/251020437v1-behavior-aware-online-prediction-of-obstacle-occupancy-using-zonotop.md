---
layout: default
title: Behavior-Aware Online Prediction of Obstacle Occupancy using Zonotopes
---

# Behavior-Aware Online Prediction of Obstacle Occupancy using Zonotopes
**arXiv**：[2510.20437v1](https://arxiv.org/abs/2510.20437) · [PDF](https://arxiv.org/pdf/2510.20437.pdf)  
**作者**：Alvaro Carrizosa-Rendon, Jian Zhou, Erik Frisk, Vicenc Puig, Fatiha Nejjari  

**一句话要点**：提出基于Zonotopes的行为感知在线方法，以预测无结构环境中车辆占用区域。

**关键词**：自动驾驶预测, Zonotopes方法, 在线占用预测, 可达性分析, 扩展卡尔曼滤波, 线性规划

## 3 点简述
- 核心问题：在无先验信息的无结构环境中，准确预测周围车辆运动以确保自动驾驶安全。
- 方法要点：使用扩展卡尔曼滤波和线性规划估计控制动作，再通过可达性分析预测未来占用。
- 实验或效果：城市环境模拟验证方法准确紧凑，无需先验假设或训练数据。

## 摘要（原文）

> Predicting the motion of surrounding vehicles is key to safe autonomous
> driving, especially in unstructured environments without prior information.
> This paper proposes a novel online method to accurately predict the occupancy
> sets of surrounding vehicles based solely on motion observations. The approach
> is divided into two stages: first, an Extended Kalman Filter and a Linear
> Programming (LP) problem are used to estimate a compact zonotopic set of
> control actions; then, a reachability analysis propagates this set to predict
> future occupancy. The effectiveness of the method has been validated through
> simulations in an urban environment, showing accurate and compact predictions
> without relying on prior assumptions or prior training data.

