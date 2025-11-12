---
layout: default
title: Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction
---

# Statistically Assuring Safety of Control Systems using Ensembles of Safety Filters and Conformal Prediction
**arXiv**：[2511.07899v1](https://arxiv.org/abs/2511.07899) · [PDF](https://arxiv.org/pdf/2511.07899.pdf)  
**作者**：Ihab Tabbara, Yuxuan Yang, Hussein Sibai  

**一句话要点**：提出基于保形预测和集成安全过滤器的框架，为学习型控制系统提供概率安全保证

**关键词**：安全保证, 保形预测, Hamilton-Jacobi可达性分析, 强化学习, 控制系统, 集成学习

## 3 点简述
- 核心问题：学习型Hamilton-Jacobi值函数及其安全策略无法保证正确性，存在不确定性。
- 方法要点：利用保形预测校准不安全控制器与学习安全策略的切换，提供概率安全边界。
- 实验或效果：比较集成HJ值函数与单一值函数作为安全过滤器的性能，未知具体结果。

## 摘要（原文）

> Safety assurance is a fundamental requirement for deploying learning-enabled autonomous systems. Hamilton-Jacobi (HJ) reachability analysis is a fundamental method for formally verifying safety and generating safe controllers. However, computing the HJ value function that characterizes the backward reachable set (BRS) of a set of user-defined failure states is computationally expensive, especially for high-dimensional systems, motivating the use of reinforcement learning approaches to approximate the value function. Unfortunately, a learned value function and its corresponding safe policy are not guaranteed to be correct. The learned value function evaluated at a given state may not be equal to the actual safety return achieved by following the learned safe policy. To address this challenge, we introduce a conformal prediction-based (CP) framework that bounds such uncertainty. We leverage CP to provide probabilistic safety guarantees when using learned HJ value functions and policies to prevent control systems from reaching failure states. Specifically, we use CP to calibrate the switching between the unsafe nominal controller and the learned HJ-based safe policy and to derive safety guarantees under this switched policy. We also investigate using an ensemble of independently trained HJ value functions as a safety filter and compare this ensemble approach to using individual value functions alone.

