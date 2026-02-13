---
layout: default
title: Calibration and Evaluation of Car-Following Models for Autonomous Shuttles Using a Novel Multi-Criteria Framework
---

# Calibration and Evaluation of Car-Following Models for Autonomous Shuttles Using a Novel Multi-Criteria Framework
**arXiv**：[2602.11517v1](https://arxiv.org/abs/2602.11517) · [PDF](https://arxiv.org/pdf/2602.11517.pdf)  
**作者**：Renan Favero, Lily Elefteriadou  

**一句话要点**：提出多准则框架校准与评估自动驾驶班车跟驰模型，提升模型性能与可比性。

**关键词**：自动驾驶班车, 跟驰模型, 机器学习校准, 多准则评估, 轨迹分析

## 3 点简述
- 核心问题：自动驾驶班车跟驰模型缺乏专用校准与统一评估框架，限制其交通影响分析。
- 方法要点：校准八种机器学习算法和两种物理模型，引入多准则评估框架整合预测精度、轨迹稳定性和统计相似性。
- 实验或效果：校准XGBoost模型表现最佳，序列模型捕获长期稳定性但短期响应不足，传统模型准确性较低。

## 摘要（原文）

> Autonomous shuttles (AS) are fully autonomous transit vehicles with operating characteristics distinct from conventional autonomous vehicles (AV). Developing dedicated car-following models for AS is critical to understanding their traffic impacts; however, few studies have calibrated such models with field data. More advanced machine learning (ML) techniques have not yet been applied to AS trajectories, leaving the potential of ML for capturing AS dynamics unexplored and constraining the development of dedicated AS models. Furthermore, there is a lack of a unified framework for systematically evaluating and comparing the performance of car-following models to replicate real trajectories. Existing car-following studies often rely on disparate metrics, which limit reproducibility and performance comparability.
>   This study addresses these gaps through two main contributions: (1) the calibration of a diverse set of car-following models using real-world AS trajectory data, including eight machine learning algorithms and two physics-based models; and (2) the introduction of a multi-criteria evaluation framework that integrates measures of prediction accuracy, trajectory stability, and statistical similarity, which provides a generalizable methodology for a systematic assessment of car-following models.
>   Results indicated that the proposed calibrated XGBoost model achieved the best overall performance. Sequential model type, such as LSTM and CNN, captured long-term positional stability but were less responsive to short-term dynamics. LSTM and CNN captured long-term positional stability but were less responsive to short-term dynamics. Traditional models (IDM, ACC) and kernel methods showed lower accuracy and stability than most ML models tested.

