---
layout: default
title: Evaluating Feature Dependent Noise in Preference-based Reinforcement Learning
---

# Evaluating Feature Dependent Noise in Preference-based Reinforcement Learning
**arXiv**：[2601.01904v1](https://arxiv.org/abs/2601.01904) · [PDF](https://arxiv.org/pdf/2601.01904.pdf)  
**作者**：Yuxuan Li, Harshith Reddy Kethireddy, Srijita Das  

**一句话要点**：提出特征依赖噪声概念以评估偏好强化学习中的噪声影响

**关键词**：偏好强化学习, 特征依赖噪声, 噪声鲁棒性, 连续控制任务, 语言模型噪声

## 3 点简述
- 核心问题：偏好强化学习中噪声常与观测特征相关，现有方法未充分处理此类噪声。
- 方法要点：形式化特征依赖噪声，提出轨迹特征噪声、轨迹相似性噪声等变体。
- 实验或效果：在DMControl和Meta-world任务中，特征依赖噪声显著降低现有噪声鲁棒方法性能。

## 摘要（原文）

> Learning from Preferences in Reinforcement Learning (PbRL) has gained attention recently, as it serves as a natural fit for complicated tasks where the reward function is not easily available. However, preferences often come with uncertainty and noise if they are not from perfect teachers. Much prior literature aimed to detect noise, but with limited types of noise and most being uniformly distributed with no connection to observations. In this work, we formalize the notion of targeted feature-dependent noise and propose several variants like trajectory feature noise, trajectory similarity noise, uncertainty-aware noise, and Language Model noise.
>   We evaluate feature-dependent noise, where noise is correlated with certain features in complex continuous control tasks from DMControl and Meta-world. Our experiments show that in some feature-dependent noise settings, the state-of-the-art noise-robust PbRL method's learning performance is significantly deteriorated, while PbRL method with no explicit denoising can surprisingly outperform noise-robust PbRL in majority settings.
>   We also find language model's noise exhibits similar characteristics to feature-dependent noise, thereby simulating realistic humans and call for further study in learning with feature-dependent noise robustly.

