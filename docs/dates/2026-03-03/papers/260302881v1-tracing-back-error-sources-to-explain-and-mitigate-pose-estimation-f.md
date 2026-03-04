---
layout: default
title: Tracing Back Error Sources to Explain and Mitigate Pose Estimation Failures
---

# Tracing Back Error Sources to Explain and Mitigate Pose Estimation Failures
**arXiv**：[2603.02881v1](https://arxiv.org/abs/2603.02881) · [PDF](https://arxiv.org/pdf/2603.02881.pdf)  
**作者**：Loris Schneider, Yitian Shi, Rosa Wolf, Carolin Brenner, Rudolph Triebel, Rania Rayyes  

**一句话要点**：提出模块化不确定性感知框架以提升机器人抓取中姿态估计的鲁棒性

**关键词**：姿态估计, 机器人抓取, 不确定性感知, 模块化框架, 错误归因, ICP算法

## 3 点简述
- 核心问题：基础姿态估计模型因环境不确定性导致鲁棒性差、计算开销大
- 方法要点：通过故障检测、错误归因和针对性恢复模块化处理姿态估计误差
- 实验或效果：在真实机器人抓取任务中显著提升ICP鲁棒性，性能媲美复杂模型

## 摘要（原文）

> Robust estimation of object poses in robotic manipulation is often addressed using foundational general estimators, that aim to handle diverse error sources naively within a single model. Still, they struggle due to environmental uncertainties, while requiring long inference times and heavy computation. In contrast, we propose a modular, uncertainty-aware framework that attributes pose estimation errors to specific error sources and applies targeted mitigation strategies only when necessary. Instantiated with Iterative Closest Point (ICP) as a simple and lightweight pose estimator, we leverage our framework for real-world robotic grasping tasks. By decomposing pose estimation into failure detection, error attribution, and targeted recovery, we significantly improve the robustness of ICP and achieve competitive performance compared to foundation models, while relying on a substantially simpler and faster pose estimator.

