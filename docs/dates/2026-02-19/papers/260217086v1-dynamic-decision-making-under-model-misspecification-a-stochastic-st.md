---
layout: default
title: Dynamic Decision-Making under Model Misspecification: A Stochastic Stability Approach
---

# Dynamic Decision-Making under Model Misspecification: A Stochastic Stability Approach
**arXiv**：[2602.17086v1](https://arxiv.org/abs/2602.17086) · [PDF](https://arxiv.org/pdf/2602.17086.pdf)  
**作者**：Xinyu Dai, Daniel Chen, Yian Qian  

**一句话要点**：提出随机稳定性框架，分析模型误设下Thompson Sampling的后验演化与性能

**关键词**：模型误设, Thompson Sampling, 后验演化, 随机稳定性, 贝叶斯强化学习, 老虎机问题

## 3 点简述
- 核心问题：模型误设时Thompson Sampling的行为与性能分析，现有算法依赖正确模型假设
- 方法要点：基于高斯双臂老虎机分类后验演化，扩展至有限模型类，构建马尔可夫过程框架
- 实验或效果：提供后验动态的几何分类，为结构化老虎机中的鲁棒决策奠定基础

## 摘要（原文）

> Dynamic decision-making under model uncertainty is central to many economic environments, yet existing bandit and reinforcement learning algorithms rely on the assumption of correct model specification. This paper studies the behavior and performance of one of the most commonly used Bayesian reinforcement learning algorithms, Thompson Sampling (TS), when the model class is misspecified. We first provide a complete dynamic classification of posterior evolution in a misspecified two-armed Gaussian bandit, identifying distinct regimes: correct model concentration, incorrect model concentration, and persistent belief mixing, characterized by the direction of statistical evidence and the model-action mapping. These regimes yield sharp predictions for limiting beliefs, action frequencies, and asymptotic regret. We then extend the analysis to a general finite model class and develop a unified stochastic stability framework that represents posterior evolution as a Markov process on the belief simplex. This approach characterizes two sufficient conditions to classify the ergodic and transient behaviors and provides inductive dimensional reductions of the posterior dynamics. Our results offer the first qualitative and geometric classification of TS under misspecification, bridging Bayesian learning with evolutionary dynamics, and also build the foundations of robust decision-making in structured bandits.

