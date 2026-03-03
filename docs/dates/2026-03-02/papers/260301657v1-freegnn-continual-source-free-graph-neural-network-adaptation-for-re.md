---
layout: default
title: FreeGNN: Continual Source-Free Graph Neural Network Adaptation for Renewable Energy Forecasting
---

# FreeGNN: Continual Source-Free Graph Neural Network Adaptation for Renewable Energy Forecasting
**arXiv**：[2603.01657v1](https://arxiv.org/abs/2603.01657) · [PDF](https://arxiv.org/pdf/2603.01657.pdf)  
**作者**：Abderaouf Bahi, Amel Ourici, Ibtissem Gasmi, Aida Derrablia, Warda Deghmane, Mohamed Amine Ferrag  

**一句话要点**：提出FreeGNN框架，用于无源持续图域适应，以解决可再生能源预测中的隐私与数据限制问题。

**关键词**：图神经网络, 持续学习, 无源域适应, 可再生能源预测, 时空建模, 师生策略

## 3 点简述
- 核心问题：传统监督模型需目标站点标签数据，但常因隐私或成本不可得，影响预测准确性。
- 方法要点：结合时空图神经网络、师生策略、记忆回放、图正则化和漂移感知加权，实现无源持续自适应。
- 实验或效果：在GEFCom、Solar PV和Wind SCADA数据集上验证，MAE和RMSE指标显示准确稳健的预测性能。

## 摘要（原文）

> Accurate forecasting of renewable energy generation is essential for efficient grid management and sustainable power planning. However, traditional supervised models often require access to labeled data from the target site, which may be unavailable due to privacy, cost, or logistical constraints. In this work, we propose FreeGNN, a Continual Source-Free Graph Domain Adaptation framework that enables adaptive forecasting on unseen renewable energy sites without requiring source data or target labels. Our approach integrates a spatio-temporal Graph Neural Network (GNN) backbone with a teacher--student strategy, a memory replay mechanism to mitigate catastrophic forgetting, graph-based regularization to preserve spatial correlations, and a drift-aware weighting scheme to dynamically adjust adaptation strength during streaming updates. This combination allows the model to continuously adapt to non-stationary environmental conditions while maintaining robustness and stability. We conduct extensive experiments on three real-world datasets: GEFCom2012, Solar PV, and Wind SCADA, encompassing multiple sites, temporal resolutions, and meteorological features. The ablation study confirms that each component memory, graph regularization, drift-aware adaptation, and teacher--student strategy contributes significantly to overall performance. The experiments show that FreeGNN achieves an MAE of 5.237 and an RMSE of 7.123 on the GEFCom dataset, an MAE of 1.107 and an RMSE of 1.512 on the Solar PV dataset, and an MAE of 0.382 and an RMSE of 0.523 on the Wind SCADA dataset. These results demonstrate its ability to achieve accurate and robust forecasts in a source-free, continual learning setting, highlighting its potential for real-world deployment in adaptive renewable energy systems. For reproducibility, implementation details are available at: https://github.com/AraoufBh/FreeGNN.

