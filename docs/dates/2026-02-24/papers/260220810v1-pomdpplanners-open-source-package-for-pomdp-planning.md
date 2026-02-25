---
layout: default
title: POMDPPlanners: Open-Source Package for POMDP Planning
---

# POMDPPlanners: Open-Source Package for POMDP Planning
**arXiv**：[2602.20810v1](https://arxiv.org/abs/2602.20810) · [PDF](https://arxiv.org/pdf/2602.20810.pdf)  
**作者**：Yaacov Pariente, Vadim Indelman  

**一句话要点**：提出POMDPPlanners开源包以支持不确定性决策的实证评估，特别关注风险敏感场景。

**关键词**：POMDP规划, 开源软件包, 不确定性决策, 风险敏感评估, 超参数优化, 并行模拟

## 3 点简述
- 核心问题：部分可观测马尔可夫决策过程（POMDP）规划算法的实证评估缺乏高效、可扩展的工具。
- 方法要点：集成先进规划算法、基准环境、自动化超参数优化和并行模拟，减少大规模仿真开销。
- 实验或效果：通过持久缓存和故障恢复，提升研究的可重复性和效率，适用于安全关键应用。

## 摘要（原文）

> We present POMDPPlanners, an open-source Python package for empirical evaluation of Partially Observable Markov Decision Process (POMDP) planning algorithms. The package integrates state-of-the-art planning algorithms, a suite of benchmark environments with safety-critical variants, automated hyperparameter optimization via Optuna, persistent caching with failure recovery, and configurable parallel simulation -- reducing the overhead of extensive simulation studies. POMDPPlanners is designed to enable scalable, reproducible research on decision-making under uncertainty, with particular emphasis on risk-sensitive settings where standard toolkits fall short.

