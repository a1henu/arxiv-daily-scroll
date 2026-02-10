---
layout: default
title: Personalized Autonomous Driving via Optimal Control with Clearance Constraints from Questionnaires
---

# Personalized Autonomous Driving via Optimal Control with Clearance Constraints from Questionnaires
**arXiv**：[2602.08326v1](https://arxiv.org/abs/2602.08326) · [PDF](https://arxiv.org/pdf/2602.08326.pdf)  
**作者**：Yongjae Lim, Dabin Kim, H. Jin Kim  

**一句话要点**：提出基于问卷和最优控制的个性化自动驾驶规划框架，以解决用户偏好安全间距问题。

**关键词**：个性化自动驾驶, 最优控制, 安全间距约束, 问卷设计, 实时规划, 用户偏好建模

## 3 点简述
- 核心问题：传统自动驾驶规划忽略用户对周围车辆安全间距的偏好，可能导致驾驶不适。
- 方法要点：设计问卷捕获用户偏好，将其作为最优控制问题的约束，并通过问题分解实现实时计算。
- 实验或效果：通过模拟验证，该框架能有效反映用户偏好，优于无偏好基线规划器。

## 摘要（原文）

> Driving without considering the preferred separation distance from surrounding vehicles may cause discomfort for users. To address this limitation, we propose a planning framework that explicitly incorporates user preferences regarding the desired level of safe clearance from surrounding vehicles. We design a questionnaire purposefully tailored to capture user preferences relevant to our framework, while minimizing unnecessary questions. Specifically, the questionnaire considers various interaction-relevant factors, including the surrounding vehicle's size, speed, position, and maneuvers of surrounding vehicles, as well as the maneuvers of the ego vehicle. The response indicates the user-preferred clearance for the scenario defined by the question and is incorporated as constraints in the optimal control problem. However, it is impractical to account for all possible scenarios that may arise in a driving environment within a single optimal control problem, as the resulting computational complexity renders real-time implementation infeasible. To overcome this limitation, we approximate the original problem by decomposing it into multiple subproblems, each dealing with one fixed scenario. We then solve these subproblems in parallel and select one using the cost function from the original problem. To validate our work, we conduct simulations using different user responses to the questionnaire. We assess how effectively our planner reflects user preferences compared to preference-agnostic baseline planners by measuring preference alignment.

