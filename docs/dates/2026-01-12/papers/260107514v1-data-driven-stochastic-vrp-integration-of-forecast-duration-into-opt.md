---
layout: default
title: Data-Driven Stochastic VRP: Integration of Forecast Duration into Optimization for Utility Workforce Management
---

# Data-Driven Stochastic VRP: Integration of Forecast Duration into Optimization for Utility Workforce Management
**arXiv**：[2601.07514v1](https://arxiv.org/abs/2601.07514) · [PDF](https://arxiv.org/pdf/2601.07514.pdf)  
**作者**：Matteo Garbelli  

**一句话要点**：提出数据驱动的随机车辆路径规划方法，集成机器学习预测以优化公用事业劳动力管理

**关键词**：随机车辆路径规划, 机器学习预测, 多目标优化, 风险缓冲, 公用事业管理, XGBoost

## 3 点简述
- 核心问题：在带时间窗的容量限制车辆路径问题中，处理服务时长不确定性，提升实际应用中的运营效率。
- 方法要点：使用XGBoost预测服务时长和不确定性，结合多目标进化优化和风险缓冲模型进行路径规划。
- 实验或效果：相比默认时长方案，操作员利用率和完成率提高约20-25%，验证了风险模型的有效性。

## 摘要（原文）

> This paper investigates the integration of machine learning forecasts of intervention durations into a stochastic variant of the Capacitated Vehicle Routing Problem with Time Windows (CVRPTW). In particular, we exploit tree-based gradient boosting (XGBoost) trained on eight years of gas meter maintenance data to produce point predictions and uncertainty estimates, which then drive a multi-objective evolutionary optimization routine. The methodology addresses uncertainty through sub-Gaussian concentration bounds for route-level risk buffers and explicitly accounts for competing operational KPIs through a multi-objective formulation. Empirical analysis of prediction residuals validates the sub-Gaussian assumption underlying the risk model. From an empirical point of view, our results report improvements around 20-25\% in operator utilization and completion rates compared with plans computed using default durations. The integration of uncertainty quantification and risk-aware optimization provides a practical framework for handling stochastic service durations in real-world routing applications.

