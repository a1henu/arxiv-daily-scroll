---
layout: default
title: Vector Cost Behavioral Planning for Autonomous Robotic Systems with Contemporary Validation Strategies
---

# Vector Cost Behavioral Planning for Autonomous Robotic Systems with Contemporary Validation Strategies
**arXiv**：[2511.17375v1](https://arxiv.org/abs/2511.17375) · [PDF](https://arxiv.org/pdf/2511.17375.pdf)  
**作者**：Benjamin R. Toaz, Quentin Goss, John Thompson, Seta Boğosyan, Shaunak D. Bopardikar, Mustafa İlhan Akbaş, Metin Gökaşan  

**一句话要点**：提出向量成本双矩阵游戏方法，用于自主机器人多目标行为规划，优于标量化方法。

**关键词**：多目标决策, 向量成本游戏, 机器人行为规划, 可解释AI, 参数空间探索

## 3 点简述
- 核心问题：自主机器人需同时优化多目标并避免最坏情况，现有标量加权和方法不足。
- 方法要点：扩展向量成本双矩阵游戏至任意目标数，结合XAI和SEMBAS进行高维数据分析。
- 实验或效果：仿真显示向量成本方法性能显著优于标量化，提供可解释通用框架。

## 摘要（原文）

> The vector cost bimatrix game is a method for multi-objective decision making that enables autonomous robotic systems to optimize for multiple goals at once while avoiding worst-case scenarios in neglected objectives. We expand this approach to arbitrary numbers of objectives and compare its performance to scalar weighted sum methods during competitive motion planning. Explainable Artificial Intelligence (XAI) software is used to aid in the analysis of high dimensional decision-making data. State-space Exploration of Multidimensional Boundaries using Adherence Strategies (SEMBAS) is applied to explore performance modes in the parameter space as a sensitivity study for the baseline and proposed frameworks. While some works have explored aspects of game theoretic planning and intelligent systems validation separately, we combine each of these into a novel and comprehensive simulation pipeline. This integration demonstrates a dramatic improvement of the vector cost method over scalarization and offers an interpretable and generalizable framework for robotic behavioral planning. Code available at https://github.com/toazbenj/race_simulation. The video companion to this work is available at https://tinyurl.com/vectorcostvideo.

