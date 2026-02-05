---
layout: default
title: A Unified Complementarity-based Approach for Rigid-Body Manipulation and Motion Prediction
---

# A Unified Complementarity-based Approach for Rigid-Body Manipulation and Motion Prediction
**arXiv**：[2602.04522v1](https://arxiv.org/abs/2602.04522) · [PDF](https://arxiv.org/pdf/2602.04522.pdf)  
**作者**：Bingkun Huang, Xin Ma, Nilanjan Chakraborty, Riddhiman Laha  

**一句话要点**：提出基于互补性的统一框架Unicomp，用于刚体操作和运动预测，以解决非结构化环境中接触建模的挑战。

**关键词**：刚体操作, 互补性建模, 摩擦接触, 运动预测, 实时规划, 非结构化环境

## 3 点简述
- 核心问题：现有规划框架在非结构化环境中分离自由运动和接触，简化接触表示，限制接触模式转换的保真度和实时鲁棒性。
- 方法要点：基于互补性刚体动力学，将自由运动和摩擦接触建模为耦合线性和非线性互补问题，支持无固定接触假设的接触模式转换。
- 实验或效果：实验显示，该方法在交互速度下实现稳定、物理一致的行为，适用于从平面推送到全身接触的多种任务。

## 摘要（原文）

> Robotic manipulation in unstructured environments requires planners to reason jointly about free-space motion and sustained, frictional contact with the environment. Existing (local) planning and simulation frameworks typically separate these regimes or rely on simplified contact representations, particularly when modeling non-convex or distributed contact patches. Such approximations limit the fidelity of contact-mode transitions and hinder the robust execution of contact-rich behaviors in real time. This paper presents a unified discrete-time modeling framework for robotic manipulation that consistently captures both free motion and frictional contact within a single mathematical formalism (Unicomp). Building on complementarity-based rigid-body dynamics, we formulate free-space motion and contact interactions as coupled linear and nonlinear complementarity problems, enabling principled transitions between contact modes without enforcing fixed-contact assumptions. For planar patch contact, we derive a frictional contact model from the maximum power dissipation principle in which the set of admissible contact wrenches is represented by an ellipsoidal limit surface. This representation captures coupled force-moment effects, including torsional friction, while remaining agnostic to the underlying pressure distribution across the contact patch. The resulting formulation yields a discrete-time predictive model that relates generalized velocities and contact wrenches through quadratic constraints and is suitable for real-time optimization-based planning. Experimental results show that the proposed approach enables stable, physically consistent behavior at interactive speeds across tasks, from planar pushing to contact-rich whole-body maneuvers.

