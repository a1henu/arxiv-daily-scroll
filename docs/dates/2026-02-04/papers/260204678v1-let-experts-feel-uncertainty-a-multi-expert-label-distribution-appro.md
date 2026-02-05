---
layout: default
title: Let Experts Feel Uncertainty: A Multi-Expert Label Distribution Approach to Probabilistic Time Series Forecasting
---

# Let Experts Feel Uncertainty: A Multi-Expert Label Distribution Approach to Probabilistic Time Series Forecasting
**arXiv**：[2602.04678v1](https://arxiv.org/abs/2602.04678) · [PDF](https://arxiv.org/pdf/2602.04678.pdf)  
**作者**：Zhen Zhou, Zhirui Wang, Qi Hong, Yunyang Shi, Ziyuan Gu, Zhiyuan Liu  

**一句话要点**：提出多专家标签分布框架，以解决时间序列预测中准确性与不确定性量化平衡问题。

**关键词**：时间序列预测, 不确定性量化, 多专家学习, 分布学习, 可解释性分析

## 3 点简述
- 核心问题：传统点预测方法难以量化不确定性，现有概率方法在计算效率与可解释性间存在平衡困难。
- 方法要点：引入多专家学习分布标签框架，包括多专家LDL和模式感知LDL-MoE，通过专家混合架构实现分布学习。
- 实验或效果：在M5数据集上评估，多专家LDL性能最优，模式感知LDL-MoE提供组件级可解释性，平衡预测准确性与可解释性。

## 摘要（原文）

> Time series forecasting in real-world applications requires both high predictive accuracy and interpretable uncertainty quantification. Traditional point prediction methods often fail to capture the inherent uncertainty in time series data, while existing probabilistic approaches struggle to balance computational efficiency with interpretability. We propose a novel Multi-Expert Learning Distributional Labels (LDL) framework that addresses these challenges through mixture-of-experts architectures with distributional learning capabilities. Our approach introduces two complementary methods: (1) Multi-Expert LDL, which employs multiple experts with different learned parameters to capture diverse temporal patterns, and (2) Pattern-Aware LDL-MoE, which explicitly decomposes time series into interpretable components (trend, seasonality, changepoints, volatility) through specialized sub-experts. Both frameworks extend traditional point prediction to distributional learning, enabling rich uncertainty quantification through Maximum Mean Discrepancy (MMD). We evaluate our methods on aggregated sales data derived from the M5 dataset, demonstrating superior performance compared to baseline approaches. The continuous Multi-Expert LDL achieves the best overall performance, while the Pattern-Aware LDL-MoE provides enhanced interpretability through component-wise analysis. Our frameworks successfully balance predictive accuracy with interpretability, making them suitable for real-world forecasting applications where both performance and actionable insights are crucial.

