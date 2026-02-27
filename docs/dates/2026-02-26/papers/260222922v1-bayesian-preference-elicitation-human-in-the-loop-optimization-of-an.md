---
layout: default
title: Bayesian Preference Elicitation: Human-In-The-Loop Optimization of An Active Prosthesis
---

# Bayesian Preference Elicitation: Human-In-The-Loop Optimization of An Active Prosthesis
**arXiv**：[2602.22922v1](https://arxiv.org/abs/2602.22922) · [PDF](https://arxiv.org/pdf/2602.22922.pdf)  
**作者**：Sophia Taddei, Wouter Koppen, Eligia Alfio, Stefano Nuzzo, Louis Flynn, Maria Alejandra Diaz, Sebastian Rojas Gonzalez, Tom Dhaene, Kevin De Pauw, Ivo Couckuyt, Tom Verstraten  

**一句话要点**：提出基于贝叶斯优化的偏好驱动人机交互方法，以高效个性化主动假肢控制器。

**关键词**：偏好学习, 贝叶斯优化, 人机交互, 假肢控制, 多目标优化

## 3 点简述
- 核心问题：主动假肢调参耗时且依赖指标，可能无法充分反映用户需求。
- 方法要点：采用偏好学习专用采集函数的多目标贝叶斯优化，包括离散和连续两种算法变体。
- 实验或效果：在基准函数和实际应用试验中展示高效收敛、鲁棒偏好获取及可测量的生物力学改进。

## 摘要（原文）

> Tuning active prostheses for people with amputation is time-consuming and relies on metrics that may not fully reflect user needs. We introduce a human-in-the-loop optimization (HILO) approach that leverages direct user preferences to personalize a standard four-parameter prosthesis controller efficiently. Our method employs preference-based Multiobjective Bayesian Optimization that uses a state-or-the-art acquisition function especially designed for preference learning, and includes two algorithmic variants: a discrete version (\textit{EUBO-LineCoSpar}), and a continuous version (\textit{BPE4Prost}). Simulation results on benchmark functions and real-application trials demonstrate efficient convergence, robust preference elicitation, and measurable biomechanical improvements, illustrating the potential of preference-driven tuning for user-centered prosthesis control.

