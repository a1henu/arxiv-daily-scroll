---
layout: default
title: Strategizing at Speed: A Learned Model Predictive Game for Multi-Agent Drone Racing
---

# Strategizing at Speed: A Learned Model Predictive Game for Multi-Agent Drone Racing
**arXiv**：[2602.06925v1](https://arxiv.org/abs/2602.06925) · [PDF](https://arxiv.org/pdf/2602.06925.pdf)  
**作者**：Andrei-Carlo Papuc, Lasse Peters, Sihao Sun, Laura Ferranti, Javier Alonso-Mora  

**一句话要点**：提出学习型模型预测博弈以解决多智能体无人机竞速中的策略深度与延迟权衡问题。

**关键词**：多智能体无人机竞速, 模型预测博弈, 学习型规划, 策略决策, 延迟优化

## 3 点简述
- 核心问题：智能体在行动前应进行多深度的策略规划，涉及计算延迟与交互推理的权衡。
- 方法要点：比较模型预测博弈与轮廓模型预测控制，并引入学习型模型预测博弈以摊销计算降低延迟。
- 实验或效果：在仿真和硬件实验中，学习型模型预测博弈在头对头竞速中优于两种基线方法。

## 摘要（原文）

> Autonomous drone racing pushes the boundaries of high-speed motion planning and multi-agent strategic decision-making. Success in this domain requires drones not only to navigate at their limits but also to anticipate and counteract competitors' actions. In this paper, we study a fundamental question that arises in this domain: how deeply should an agent strategize before taking an action? To this end, we compare two planning paradigms: the Model Predictive Game (MPG), which finds interaction-aware strategies at the expense of longer computation times, and contouring Model Predictive Control (MPC), which computes strategies rapidly but does not reason about interactions. We perform extensive experiments to study this trade-off, revealing that MPG outperforms MPC at moderate velocities but loses its advantage at higher speeds due to latency. To address this shortcoming, we propose a Learned Model Predictive Game (LMPG) approach that amortizes model predictive gameplay to reduce latency. In both simulation and hardware experiments, we benchmark our approach against MPG and MPC in head-to-head races, finding that LMPG outperforms both baselines.

