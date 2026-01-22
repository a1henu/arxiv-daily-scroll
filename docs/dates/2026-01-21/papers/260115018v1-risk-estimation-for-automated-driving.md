---
layout: default
title: Risk Estimation for Automated Driving
---

# Risk Estimation for Automated Driving
**arXiv**：[2601.15018v1](https://arxiv.org/abs/2601.15018) · [PDF](https://arxiv.org/pdf/2601.15018.pdf)  
**作者**：Leon Tolksdorf, Arturo Tejada, Jonas Bauernfeind, Christian Birkner, Nathan van de Wouw  

**一句话要点**：提出结合碰撞概率与严重性的通用风险估计方法，以提升自动驾驶安全规划

**关键词**：自动驾驶风险估计, 碰撞概率, 碰撞严重性, 运动规划, 高斯不确定性, 实时计算

## 3 点简述
- 核心问题：自动驾驶风险估计缺乏通用性和准确性，现有方法依赖经验模型或近似。
- 方法要点：整合碰撞概率估计与碰撞严重性概念，支持为不同碰撞类型分配个体化严重性函数。
- 实验或效果：方法计算高效，适用于实时运动规划，并提供高斯不确定性示例代码。

## 摘要（原文）

> Safety is a central requirement for automated vehicles. As such, the assessment of risk in automated driving is key in supporting both motion planning technologies and safety evaluation. In automated driving, risk is characterized by two aspects. The first aspect is the uncertainty on the state estimates of other road participants by an automated vehicle. The second aspect is the severity of a collision event with said traffic participants. Here, the uncertainty aspect typically causes the risk to be non-zero for near-collision events. This makes risk particularly useful for automated vehicle motion planning. Namely, constraining or minimizing risk naturally navigates the automated vehicle around traffic participants while keeping a safety distance based on the level of uncertainty and the potential severity of the impending collision. Existing approaches to calculate the risk either resort to empirical modeling or severe approximations, and, hence, lack generalizability and accuracy. In this paper, we combine recent advances in collision probability estimation with the concept of collision severity to develop a general method for accurate risk estimation. The proposed method allows us to assign individual severity functions for different collision constellations, such as, e.g., frontal or side collisions. Furthermore, we show that the proposed approach is computationally efficient, which is beneficial, e.g., in real-time motion planning applications. The programming code for an exemplary implementation of Gaussian uncertainties is also provided.

