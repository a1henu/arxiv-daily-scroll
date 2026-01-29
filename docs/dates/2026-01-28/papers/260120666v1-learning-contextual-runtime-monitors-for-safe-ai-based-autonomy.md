---
layout: default
title: Learning Contextual Runtime Monitors for Safe AI-Based Autonomy
---

# Learning Contextual Runtime Monitors for Safe AI-Based Autonomy
**arXiv**：[2601.20666v1](https://arxiv.org/abs/2601.20666) · [PDF](https://arxiv.org/pdf/2601.20666.pdf)  
**作者**：Alejandro Luque-Cerpa, Mengyuan Wang, Emil Carlsson, Sanjit A. Seshia, Devdatt Dubhashi, Hazem Torfah  

**一句话要点**：提出基于上下文学习的运行时监控框架，以提升AI控制集成的安全性和性能。

**关键词**：运行时监控, 上下文学习, AI控制集成, 多臂老虎机, 自动驾驶安全

## 3 点简述
- 核心问题：机器学习控制器在陌生环境中性能下降，传统集成方法稀释个体控制器的上下文优势。
- 方法要点：将安全AI控制集成设计重构为上下文监控问题，利用上下文多臂老虎机技术学习监控器。
- 实验或效果：在模拟自动驾驶场景中验证，相比非上下文基线，显著提高安全性和性能。

## 摘要（原文）

> We introduce a novel framework for learning context-aware runtime monitors for AI-based control ensembles. Machine-learning (ML) controllers are increasingly deployed in (autonomous) cyber-physical systems because of their ability to solve complex decision-making tasks. However, their accuracy can degrade sharply in unfamiliar environments, creating significant safety concerns. Traditional ensemble methods aim to improve robustness by averaging or voting across multiple controllers, yet this often dilutes the specialized strengths that individual controllers exhibit in different operating contexts. We argue that, rather than blending controller outputs, a monitoring framework should identify and exploit these contextual strengths. In this paper, we reformulate the design of safe AI-based control ensembles as a contextual monitoring problem. A monitor continuously observes the system's context and selects the controller best suited to the current conditions. To achieve this, we cast monitor learning as a contextual learning task and draw on techniques from contextual multi-armed bandits. Our approach comes with two key benefits: (1) theoretical safety guarantees during controller selection, and (2) improved utilization of controller diversity. We validate our framework in two simulated autonomous driving scenarios, demonstrating significant improvements in both safety and performance compared to non-contextual baselines.

