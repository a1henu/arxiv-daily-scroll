---
layout: default
title: PlanT 2.0: Exposing Biases and Structural Flaws in Closed-Loop Driving
---

# PlanT 2.0: Exposing Biases and Structural Flaws in Closed-Loop Driving
**arXiv**：[2511.07292v1](https://arxiv.org/abs/2511.07292) · [PDF](https://arxiv.org/pdf/2511.07292.pdf)  
**作者**：Simon Gerstenecker, Andreas Geiger, Katrin Renz  

**一句话要点**：提出PlanT 2.0以分析自动驾驶模型偏见与结构缺陷

**关键词**：自动驾驶规划, 模型偏见分析, 对象级表示, CARLA基准, 数据驱动开发

## 3 点简述
- 核心问题：自动驾驶模型缺乏失败原因分析，存在偏见和捷径学习
- 方法要点：使用对象级表示和输入扰动进行可控分析
- 实验或效果：在CARLA基准上实现先进性能，暴露模型失败模式

## 摘要（原文）

> Most recent work in autonomous driving has prioritized benchmark performance
> and methodological innovation over in-depth analysis of model failures, biases,
> and shortcut learning. This has led to incremental improvements without a deep
> understanding of the current failures. While it is straightforward to look at
> situations where the model fails, it is hard to understand the underlying
> reason. This motivates us to conduct a systematic study, where inputs to the
> model are perturbed and the predictions observed. We introduce PlanT 2.0, a
> lightweight, object-centric planning transformer designed for autonomous
> driving research in CARLA. The object-level representation enables controlled
> analysis, as the input can be easily perturbed (e.g., by changing the location
> or adding or removing certain objects), in contrast to sensor-based models. To
> tackle the scenarios newly introduced by the challenging CARLA Leaderboard 2.0,
> we introduce multiple upgrades to PlanT, achieving state-of-the-art performance
> on Longest6 v2, Bench2Drive, and the CARLA validation routes. Our analysis
> exposes insightful failures, such as a lack of scene understanding caused by
> low obstacle diversity, rigid expert behaviors leading to exploitable
> shortcuts, and overfitting to a fixed set of expert trajectories. Based on
> these findings, we argue for a shift toward data-centric development, with a
> focus on richer, more robust, and less biased datasets. We open-source our code
> and model at https://github.com/autonomousvision/plant2.

