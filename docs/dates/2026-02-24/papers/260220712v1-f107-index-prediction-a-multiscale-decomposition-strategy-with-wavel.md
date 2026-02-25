---
layout: default
title: F10.7 Index Prediction: A Multiscale Decomposition Strategy with Wavelet Transform for Performance Optimization
---

# F10.7 Index Prediction: A Multiscale Decomposition Strategy with Wavelet Transform for Performance Optimization
**arXiv**：[2602.20712v1](https://arxiv.org/abs/2602.20712) · [PDF](https://arxiv.org/pdf/2602.20712.pdf)  
**作者**：Xuran Ma, Xuebao Li, Yanfang Zheng, Yongshang Lv, Xiaojia Ji, Jiancheng Xu, Hongwei Ye, Zixian Wu, Shuainan Yan, Liang Dong, Zamri Zainal Abidin, Xusheng Huang, Shunhuang Zhang, Honglei Jin, Tarik Abdul Latef, Noraisyah Mohamed Shah, Mohamadariff Othman, Kamarul Ariffin Noordin  

**一句话要点**：提出基于小波分解的多尺度策略，结合iTransformer模型优化F10.7指数预测性能。

**关键词**：F10.7指数预测, 小波分解, 多尺度策略, iTransformer模型, 太阳活动预测

## 3 点简述
- 核心问题：F10.7指数预测精度不足，需提升模型性能。
- 方法要点：使用小波分解F10.7指数，将近似与细节信号输入iTransformer模型。
- 实验或效果：组合方法显著优于基线及最新方法，在多个指标和太阳活动条件下表现优异。

## 摘要（原文）

> In this study, we construct Dataset A for training, validation, and testing, and Dataset B to evaluate generalization. We propose a novel F10.7 index forecasting method using wavelet decomposition, which feeds F10.7 together with its decomposed approximate and detail signals into the iTransformer model. We also incorporate the International Sunspot Number (ISN) and its wavelet-decomposed signals to assess their influence on prediction performance. Our optimal method is then compared with the latest method from S. Yan et al. (2025) and three operational models (SWPC, BGS, CLS). Additionally, we transfer our method to the PatchTST model used in H. Ye et al. (2024) and compare our method with theirs on Dataset B. Key findings include: (1) The wavelet-based combination methods overall outperform the baseline using only F10.7 index. The prediction performance improves as higher-level approximate and detail signals are incrementally added. The Combination 6 method integrating F10.7 with its first to fifth level approximate and detail signals outperforms methods using only approximate or detail signals. (2) Incorporating ISN and its wavelet-decomposed signals does not enhance prediction performance. (3) The Combination 6 method significantly surpasses S. Yan et al. (2025) and three operational models, with RMSE, MAE, and MAPE reduced by 18.22%, 15.09%, and 8.57%, respectively, against the former method. It also excels across four different conditions of solar activity. (4) Our method demonstrates superior generalization and prediction capability over the method of H. Ye et al. (2024) across all forecast horizons. To our knowledge, this is the first application of wavelet decomposition in F10.7 prediction, substantially improving forecast performance.

