---
layout: default
title: A Decomposition-based State Space Model for Multivariate Time-Series Forecasting
---

# A Decomposition-based State Space Model for Multivariate Time-Series Forecasting
**arXiv**：[2602.05389v1](https://arxiv.org/abs/2602.05389) · [PDF](https://arxiv.org/pdf/2602.05389.pdf)  
**作者**：Shunya Nagashima, Shuntaro Suzuki, Shuitsu Koyama, Shinnosuke Hirano  

**一句话要点**：提出DecompSSM，一种基于分解的状态空间模型，用于解决多变量时间序列预测中趋势、季节性和残差交织的挑战。

**关键词**：多变量时间序列预测, 状态空间模型, 序列分解, 深度学习, 跨变量上下文, 自适应时间尺度

## 3 点简述
- 核心问题：多变量时间序列预测中，真实序列交织慢趋势、多速率季节性和不规则残差，现有方法依赖刚性分解或通用架构，导致组件纠缠和跨变量结构利用不足。
- 方法要点：采用三个并行深度状态空间模型分支，分别捕获趋势、季节性和残差组件，结合输入依赖预测器、跨变量上下文精炼模块和重建正交性辅助损失。
- 实验或效果：在ECL、Weather、ETTm2和PEMS04基准测试中，DecompSSM优于强基线，验证了组件深度状态空间模型与全局上下文精炼结合的有效性。

## 摘要（原文）

> Multivariate time series (MTS) forecasting is crucial for decision-making in domains such as weather, energy, and finance. It remains challenging because real-world sequences intertwine slow trends, multi-rate seasonalities, and irregular residuals. Existing methods often rely on rigid, hand-crafted decompositions or generic end-to-end architectures that entangle components and underuse structure shared across variables. To address these limitations, we propose DecompSSM, an end-to-end decomposition framework using three parallel deep state space model branches to capture trend, seasonal, and residual components. The model features adaptive temporal scales via an input-dependent predictor, a refinement module for shared cross-variable context, and an auxiliary loss that enforces reconstruction and orthogonality. Across standard benchmarks (ECL, Weather, ETTm2, and PEMS04), DecompSSM outperformed strong baselines, indicating the effectiveness of combining component-wise deep state space models and global context refinement.

