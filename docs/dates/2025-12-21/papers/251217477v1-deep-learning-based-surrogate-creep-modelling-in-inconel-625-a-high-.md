---
layout: default
title: Deep Learning-Based Surrogate Creep Modelling in Inconel 625: A High-Temperature Alloy Study
---

# Deep Learning-Based Surrogate Creep Modelling in Inconel 625: A High-Temperature Alloy Study
**arXiv**：[2512.17477v1](https://arxiv.org/abs/2512.17477) · [PDF](https://arxiv.org/pdf/2512.17477.pdf)  
**作者**：Shubham Das, Kaushal Singhania, Amit Sadhu, Suprabhat Das, Arghya Nandi  

**一句话要点**：提出基于深度学习的代理模型以加速Inconel 625高温合金蠕变模拟

**关键词**：深度学习代理模型, 高温合金蠕变模拟, BiLSTM-VAE, BiLSTM-Transformer, 计算加速

## 3 点简述
- 核心问题：Inconel 625高温合金的蠕变模拟在ANSYS中计算成本高，单次运行需数十分钟。
- 方法要点：使用BiLSTM-VAE和BiLSTM-Transformer架构，基于ANSYS生成的蠕变应变数据训练代理模型。
- 实验或效果：代理模型预测在秒级完成，相比ANSYS模拟加速显著，BiLSTM-VAE提供概率输出，BiLSTM-Transformer实现高确定性精度。

## 摘要（原文）

> Time-dependent deformation, particularly creep, in high-temperature alloys such as Inconel 625 is a key factor in the long-term reliability of components used in aerospace and energy systems. Although Inconel 625 shows excellent creep resistance, finite-element creep simulations in tools such as ANSYS remain computationally expensive, often requiring tens of minutes for a single 10,000-hour run. This work proposes deep learning based surrogate models to provide fast and accurate replacements for such simulations. Creep strain data was generated in ANSYS using the Norton law under uniaxial stresses of 50 to 150 MPa and temperatures of 700 to 1000 $^\circ$C, and this temporal dataset was used to train two architectures: a BiLSTM Variational Autoencoder for uncertainty-aware and generative predictions, and a BiLSTM Transformer hybrid that employs self-attention to capture long-range temporal behavior. Both models act as surrogate predictors, with the BiLSTM-VAE offering probabilistic output and the BiLSTM-Transformer delivering high deterministic accuracy. Performance is evaluated using RMSE, MAE, and $R^2$. Results show that the BiLSTM-VAE provides stable and reliable creep strain forecasts, while the BiLSTM-Transformer achieves strong accuracy across the full time range. Latency tests indicate substantial speedup: while each ANSYS simulation requires 30 to 40 minutes for a given stress-temperature condition, the surrogate models produce predictions within seconds. The proposed framework enables rapid creep assessment for design optimization and structural health monitoring, and provides a scalable solution for high-temperature alloy applications.

