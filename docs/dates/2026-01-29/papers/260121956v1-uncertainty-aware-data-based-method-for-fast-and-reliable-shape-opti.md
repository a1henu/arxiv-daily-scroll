---
layout: default
title: Uncertainty-Aware Data-Based Method for Fast and Reliable Shape Optimization
---

# Uncertainty-Aware Data-Based Method for Fast and Reliable Shape Optimization
**arXiv**：[2601.21956v1](https://arxiv.org/abs/2601.21956) · [PDF](https://arxiv.org/pdf/2601.21956.pdf)  
**作者**：Yunjia Yang, Runze Li, Yufei Zhang, Haixin Chen  

**一句话要点**：提出不确定性感知数据优化框架以提升气动外形优化的鲁棒性与效率

**关键词**：数据驱动优化, 不确定性量化, 代理模型, 气动外形优化, 多目标优化

## 3 点简述
- 数据优化依赖训练数据质量，分布外样本易导致预测误差误导优化过程
- 开发概率编码器-解码器代理模型量化不确定性，并集成到目标函数中惩罚高误差样本
- 在翼型多目标优化中验证，相比原方法减少预测误差并加速优化，性能接近全仿真

## 摘要（原文）

> Data-based optimization (DBO) offers a promising approach for efficiently optimizing shape for better aerodynamic performance by leveraging a pretrained surrogate model for offline evaluations during iterations. However, DBO heavily relies on the quality of the training database. Samples outside the training distribution encountered during optimization can lead to significant prediction errors, potentially misleading the optimization process. Therefore, incorporating uncertainty quantification into optimization is critical for detecting outliers and enhancing robustness. This study proposes an uncertainty-aware data-based optimization (UA-DBO) framework to monitor and minimize surrogate model uncertainty during DBO. A probabilistic encoder-decoder surrogate model is developed to predict uncertainties associated with its outputs, and these uncertainties are integrated into a model-confidence-aware objective function to penalize samples with large prediction errors during data-based optimization process. The UA-DBO framework is evaluated on two multipoint optimization problems aimed at improving airfoil drag divergence and buffet performance. Results demonstrate that UA-DBO consistently reduces prediction errors in optimized samples and achieves superior performance gains compared to original DBO. Moreover, compared to multipoint optimization based on full computational simulations, UA-DBO offers comparable optimization effectiveness while significantly accelerating optimization speed.

