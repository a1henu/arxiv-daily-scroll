---
layout: default
title: On Electric Vehicle Energy Demand Forecasting and the Effect of Federated Learning
---

# On Electric Vehicle Energy Demand Forecasting and the Effect of Federated Learning
**arXiv**：[2602.20782v1](https://arxiv.org/abs/2602.20782) · [PDF](https://arxiv.org/pdf/2602.20782.pdf)  
**作者**：Andreas Tritsarolis, Gil Sampaio, Nikos Pelekis, Yannis Theodoridis  

**一句话要点**：比较多种时间序列预测方法，评估联邦学习在电动汽车充电桩能源需求预测中的性能与权衡。

**关键词**：能源需求预测, 电动汽车充电桩, 时间序列预测, 联邦学习, XGBoost, 隐私保护

## 3 点简述
- 核心问题：电动汽车充电桩能源需求预测受用户行为、天气等外部因素影响，且数据分散，需兼顾隐私与可持续性。
- 方法要点：对比统计方法（ARIMA）、传统机器学习（XGBoost）和深度神经网络（GRU/LSTM），在集中式和联邦学习范式下评估。
- 实验或效果：XGBoost在预测精度和能效上优于其他模型；联邦学习模型在预测保真度、隐私保护和能耗间取得平衡。

## 摘要（原文）

> The wide spread of new energy resources, smart devices, and demand side management strategies has motivated several analytics operations, from infrastructure load modeling to user behavior profiling. Energy Demand Forecasting (EDF) of Electric Vehicle Supply Equipments (EVSEs) is one of the most critical operations for ensuring efficient energy management and sustainability, since it enables utility providers to anticipate energy/power demand, optimize resource allocation, and implement proactive measures to improve grid reliability. However, accurate EDF is a challenging problem due to external factors, such as the varying user routines, weather conditions, driving behaviors, unknown state of charge, etc. Furthermore, as concerns and restrictions about privacy and sustainability have grown, training data has become increasingly fragmented, resulting in distributed datasets scattered across different data silos and/or edge devices, calling for federated learning solutions. In this paper, we investigate different well-established time series forecasting methodologies to address the EDF problem, from statistical methods (the ARIMA family) to traditional machine learning models (such as XGBoost) and deep neural networks (GRU and LSTM). We provide an overview of these methods through a performance comparison over four real-world EVSE datasets, evaluated under both centralized and federated learning paradigms, focusing on the trade-offs between forecasting fidelity, privacy preservation, and energy overheads. Our experimental results demonstrate, on the one hand, the superiority of gradient boosted trees (XGBoost) over statistical and NN-based models in both prediction accuracy and energy efficiency and, on the other hand, an insight that Federated Learning-enabled models balance these factors, offering a promising direction for decentralized energy demand forecasting.

