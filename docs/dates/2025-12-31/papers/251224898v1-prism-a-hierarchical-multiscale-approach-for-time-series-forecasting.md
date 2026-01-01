---
layout: default
title: PRISM: A hierarchical multiscale approach for time series forecasting
---

# PRISM: A hierarchical multiscale approach for time series forecasting
**arXiv**：[2512.24898v1](https://arxiv.org/abs/2512.24898) · [PDF](https://arxiv.org/pdf/2512.24898.pdf)  
**作者**：Zihao Chen, Alexandre Andre, Wenrui Ma, Ian Knight, Sergey Shuvaev, Eva Dyer  

**一句话要点**：提出PRISM方法，通过可学习树状分割解决多尺度时间序列预测问题。

**关键词**：时间序列预测, 多尺度分析, 树状分割, 层次模型, 可学习表示

## 3 点简述
- 核心问题：真实时间序列包含全局趋势与局部多尺度特征，预测准确性挑战大。
- 方法要点：采用可学习树状分割，结合时间-频率基提取尺度特征，层次聚合全局与局部信息。
- 实验或效果：在基准数据集上超越现有方法，提供轻量灵活的多变量时间序列预测框架。

## 摘要（原文）

> Forecasting is critical in areas such as finance, biology, and healthcare. Despite the progress in the field, making accurate forecasts remains challenging because real-world time series contain both global trends, local fine-grained structure, and features on multiple scales in between. Here, we present a new forecasting method, PRISM (Partitioned Representation for Iterative Sequence Modeling), that addresses this challenge through a learnable tree-based partitioning of the signal. At the root of the tree, a global representation captures coarse trends in the signal, while recursive splits reveal increasingly localized views of the signal. At each level of the tree, data are projected onto a time-frequency basis (e.g., wavelets or exponential moving averages) to extract scale-specific features, which are then aggregated across the hierarchy. This design allows the model to jointly capture global structure and local dynamics of the signal, enabling accurate forecasting. Experiments across benchmark datasets show that our method outperforms state-of-the-art methods for forecasting. Overall, these results demonstrate that our hierarchical approach provides a lightweight and flexible framework for forecasting multivariate time series. The code is available at https://github.com/nerdslab/prism.

