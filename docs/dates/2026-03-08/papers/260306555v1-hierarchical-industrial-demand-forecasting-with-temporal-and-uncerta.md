---
layout: default
title: Hierarchical Industrial Demand Forecasting with Temporal and Uncertainty Explanations
---

# Hierarchical Industrial Demand Forecasting with Temporal and Uncertainty Explanations
**arXiv**：[2603.06555v1](https://arxiv.org/abs/2603.06555) · [PDF](https://arxiv.org/pdf/2603.06555.pdf)  
**作者**：Harshavardhan Kamarthi, Shangqing Xu, Xinjie Tong, Xingyu Zhou, James Peters, Joseph Czyzyk, B. Aditya Prakash  

**一句话要点**：提出分层概率时间序列预测的可解释性方法，以解决工业需求预测中的解释性不足问题。

**关键词**：分层时间序列预测, 可解释性方法, 工业需求预测, 概率预测, 不确定性解释, 供应链分析

## 3 点简述
- 核心问题：分层时间序列预测模型缺乏可解释性，影响实际应用中的信任与决策。
- 方法要点：结合通用可解释技术，针对分层结构和不确定性提供时间点重要性、变量影响和数据集变化解释。
- 实验或效果：基于真实工业数据生成半合成数据集，验证方法在解释准确性和实际案例中的有效性。

## 摘要（原文）

> Hierarchical time-series forecasting is essential for demand prediction across various industries. While machine learning models have obtained significant accuracy and scalability on such forecasting tasks, the interpretability of their predictions, informed by application, is still largely unexplored. To bridge this gap, we introduce a novel interpretability method for large hierarchical probabilistic time-series forecasting, adapting generic interpretability techniques while addressing challenges associated with hierarchical structures and uncertainty. Our approach offers valuable interpretative insights in response to real-world industrial supply chain scenarios, including 1) the significance of various time-series within the hierarchy and external variables at specific time points, 2) the impact of different variables on forecast uncertainty, and 3) explanations for forecast changes in response to modifications in the training dataset. To evaluate the explainability method, we generate semi-synthetic datasets based on real-world scenarios of explaining hierarchical demands for over ten thousand products at a large chemical company. The experiments showed that our explainability method successfully explained state-of-the-art industrial forecasting methods with significantly higher explainability accuracy. Furthermore, we provide multiple real-world case studies that show the efficacy of our approach in identifying important patterns and explanations that help stakeholders better understand the forecasts. Additionally, our method facilitates the identification of key drivers behind forecasted demand, enabling more informed decision-making and strategic planning. Our approach helps build trust and confidence among users, ultimately leading to better adoption and utilization of hierarchical forecasting models in practice.

