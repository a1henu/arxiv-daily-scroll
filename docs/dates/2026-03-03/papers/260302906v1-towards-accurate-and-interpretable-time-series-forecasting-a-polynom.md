---
layout: default
title: Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach
---

# Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach
**arXiv**：[2603.02906v1](https://arxiv.org/abs/2603.02906) · [PDF](https://arxiv.org/pdf/2603.02906.pdf)  
**作者**：Bo Liu, Shao-Bo Lin, Changmiao Wang, Xiaotong Liu  

**一句话要点**：提出可解释多项式学习方法，以解决时间序列预测中准确性与可解释性难以兼顾的问题。

**关键词**：时间序列预测, 可解释性, 多项式学习, 特征交互, 预警机制

## 3 点简述
- 核心问题：现有方法在时间依赖性建模不足、缺乏特征级可解释性，且难以平衡准确性与可解释性。
- 方法要点：通过多项式表示显式建模原始特征及其任意阶交互，将可解释性融入模型结构，调整多项式阶数以灵活权衡。
- 实验或效果：在模拟、比特币价格和天线数据上验证，IPL实现高预测精度和优越可解释性，提供更简单高效的预警机制。

## 摘要（原文）

> Time series forecasting enables early warning and has driven asset performance management from traditional planned maintenance to predictive maintenance. However, the lack of interpretability in forecasting methods undermines users' trust and complicates debugging for developers. Consequently, interpretable time-series forecasting has attracted increasing research attention. Nevertheless, existing methods suffer from several limitations, including insufficient modeling of temporal dependencies, lack of feature-level interpretability to support early warning, and difficulty in simultaneously achieving the accuracy and interpretability. This paper proposes the interpretable polynomial learning (IPL) method, which integrates interpretability into the model structure by explicitly modeling original features and their interactions of arbitrary order through polynomial representations. This design preserves temporal dependencies, provides feature-level interpretability, and offers a flexible trade-off between prediction accuracy and interpretability by adjusting the polynomial degree. We evaluate IPL on simulated and Bitcoin price data, showing that it achieves high prediction accuracy with superior interpretability compared with widely used explainability methods. Experiments on field-collected antenna data further demonstrate that IPL yields simpler and more efficient early warning mechanisms.

