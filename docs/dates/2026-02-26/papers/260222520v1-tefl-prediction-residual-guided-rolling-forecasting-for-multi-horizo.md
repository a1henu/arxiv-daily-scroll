---
layout: default
title: TEFL: Prediction-Residual-Guided Rolling Forecasting for Multi-Horizon Time Series
---

# TEFL: Prediction-Residual-Guided Rolling Forecasting for Multi-Horizon Time Series
**arXiv**：[2602.22520v1](https://arxiv.org/abs/2602.22520) · [PDF](https://arxiv.org/pdf/2602.22520.pdf)  
**作者**：Xiannan Huang, Shen Fang, Shuhan Qiu, Chengcheng Yu, Jiayuan Du, Chao Yang  

**一句话要点**：提出TEFL框架，通过历史预测残差反馈提升多步时间序列预测精度与鲁棒性。

**关键词**：时间序列预测, 预测残差, 滚动预测, 低秩适配器, 鲁棒性增强

## 3 点简述
- 核心问题：现有深度预测模型忽略滚动预测中的历史残差信息，导致偏差和未建模模式。
- 方法要点：设计轻量级低秩适配器整合可观测多步残差，采用两阶段训练联合优化基础预测器和误差模块。
- 实验或效果：在10个真实数据集上平均降低MAE 5-10%，在分布偏移下误差减少最高达19.5%。

## 摘要（原文）

> Time series forecasting plays a critical role in domains such as transportation, energy, and meteorology. Despite their success, modern deep forecasting models are typically trained to minimize point-wise prediction loss without leveraging the rich information contained in past prediction residuals from rolling forecasts - residuals that reflect persistent biases, unmodeled patterns, or evolving dynamics. We propose TEFL (Temporal Error Feedback Learning), a unified learning framework that explicitly incorporates these historical residuals into the forecasting pipeline during both training and evaluation. To make this practical in deep multi-step settings, we address three key challenges: (1) selecting observable multi-step residuals under the partial observability of rolling forecasts, (2) integrating them through a lightweight low-rank adapter to preserve efficiency and prevent overfitting, and (3) designing a two-stage training procedure that jointly optimizes the base forecaster and error module. Extensive experiments across 10 real-world datasets and 5 backbone architectures show that TEFL consistently improves accuracy, reducing MAE by 5-10% on average. Moreover, it demonstrates strong robustness under abrupt changes and distribution shifts, with error reductions exceeding 10% (up to 19.5%) in challenging scenarios. By embedding residual-based feedback directly into the learning process, TEFL offers a simple, general, and effective enhancement to modern deep forecasting systems.

