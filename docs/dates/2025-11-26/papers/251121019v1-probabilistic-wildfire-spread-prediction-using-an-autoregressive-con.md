---
layout: default
title: Probabilistic Wildfire Spread Prediction Using an Autoregressive Conditional Generative Adversarial Network
---

# Probabilistic Wildfire Spread Prediction Using an Autoregressive Conditional Generative Adversarial Network
**arXiv**：[2511.21019v1](https://arxiv.org/abs/2511.21019) · [PDF](https://arxiv.org/pdf/2511.21019.pdf)  
**作者**：Taehoon Kang, Taeyong Kim  

**一句话要点**：提出自回归条件生成对抗网络以解决野火传播概率预测问题

**关键词**：野火传播预测, 条件生成对抗网络, 自回归模型, 概率预测, 深度学习

## 3 点简述
- 核心问题：气候变化加剧野火，现有物理模拟器计算量大，深度学习模型预测过于平滑。
- 方法要点：使用自回归条件生成对抗网络学习序列状态转移，确保长期预测稳定性。
- 实验或效果：模型在预测精度和火场边界描绘上优于传统深度学习模型。

## 摘要（原文）

> Climate change has intensified the frequency and severity of wildfires, making rapid and accurate prediction of fire spread essential for effective mitigation and response. Physics-based simulators such as FARSITE offer high-fidelity predictions but are computationally intensive, limiting their applicability in real-time decision-making, while existing deep learning models often yield overly smooth predictions that fail to capture the complex, nonlinear dynamics of wildfire propagation. This study proposes an autoregressive conditional generative adversarial network (CGAN) for probabilistic wildfire spread prediction. By formulating the prediction task as an autoregressive problem, the model learns sequential state transitions, ensuring long-term prediction stability. Experimental results demonstrate that the proposed CGAN-based model outperforms conventional deep learning models in both overall predictive accuracy and boundary delineation of fire perimeters. These results demonstrate that adversarial learning allows the model to capture the strong nonlinearity and uncertainty of wildfire spread, instead of simply fitting the pixel average. Furthermore, the autoregressive framework facilitates systematic temporal forecasting of wildfire evolution. The proposed CGAN-based autoregressive framework enhances both the accuracy and physical interpretability of wildfire spread prediction, offering a promising foundation for time-sensitive response and evacuation planning.

