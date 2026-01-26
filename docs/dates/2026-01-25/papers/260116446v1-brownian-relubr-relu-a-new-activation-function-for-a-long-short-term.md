---
layout: default
title: Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network
---

# Brownian ReLU(Br-ReLU): A New Activation Function for a Long-Short Term Memory (LSTM) Network
**arXiv**：[2601.16446v1](https://arxiv.org/abs/2601.16446) · [PDF](https://arxiv.org/pdf/2601.16446.pdf)  
**作者**：George Awiakye-Marfo, Elijah Agbosu, Victoria Mawuena Barns, Samuel Asante Gyamerah  

**一句话要点**：提出BrownianReLU激活函数以解决LSTM在金融时间序列中的梯度不稳定问题。

**关键词**：激活函数, 长短期记忆网络, 金融时间序列, 梯度传播, 蒙特卡洛模拟, 预测准确性

## 3 点简述
- 核心问题：ReLU等激活函数在噪声、非平稳金融时间序列中易导致梯度不稳定。
- 方法要点：基于布朗运动设计随机激活函数，通过蒙特卡洛模拟平滑负输入响应，缓解死亡ReLU问题。
- 实验或效果：在苹果、GCB、S&P 500和LendingClub数据上评估，显示更低的均方误差和更高的R²值，提升预测准确性和泛化能力。

## 摘要（原文）

> Deep learning models are effective for sequential data modeling, yet commonly used activation functions such as ReLU, LeakyReLU, and PReLU often exhibit gradient instability when applied to noisy, non-stationary financial time series. This study introduces BrownianReLU, a stochastic activation function induced by Brownian motion that enhances gradient propagation and learning stability in Long Short-Term Memory (LSTM) networks. Using Monte Carlo simulation, BrownianReLU provides a smooth, adaptive response for negative inputs, mitigating the dying ReLU problem. The proposed activation is evaluated on financial time series from Apple, GCB, and the S&P 500, as well as LendingClub loan data for classification. Results show consistently lower Mean Squared Error and higher $R^2$ values, indicating improved predictive accuracy and generalization. Although ROC-AUC metric is limited in classification tasks, activation choice significantly affects the trade-off between accuracy and sensitivity, with Brownian ReLU and the selected activation functions yielding practically meaningful performance.

