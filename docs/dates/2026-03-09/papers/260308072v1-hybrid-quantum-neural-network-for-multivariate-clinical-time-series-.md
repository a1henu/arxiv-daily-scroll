---
layout: default
title: Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting
---

# Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting
**arXiv**：[2603.08072v1](https://arxiv.org/abs/2603.08072) · [PDF](https://arxiv.org/pdf/2603.08072.pdf)  
**作者**：Irene Iele, Floriano Caprio, Paolo Soda, Matteo Tortora  

**一句话要点**：提出混合量子神经网络，用于临床多变量时间序列预测，提升鲁棒性。

**关键词**：量子机器学习, 时间序列预测, 临床生理信号, 混合神经网络, 变分量子电路

## 3 点简述
- 核心问题：预测生理信号以支持临床干预，需处理多变量多时间步预测。
- 方法要点：结合GRU编码器和变分量子电路，量子层作为非线性特征混合器建模变量交互。
- 实验或效果：在BIDMC数据集上验证，相比经典方法具有竞争性精度和更强鲁棒性。

## 摘要（原文）

> Forecasting physiological signals can support proactive monitoring and timely clinical intervention by anticipating critical changes in patient status. In this work, we address multivariate multi-horizon forecasting of physiological time series by jointly predicting heart rate, oxygen saturation, pulse rate, and respiratory rate at forecasting horizons of 15, 30, and 60 seconds. We propose a hybrid quantum-classical architecture that integrates a Variational Quantum Circuit (VQC) within a recurrent neural backbone. A GRU encoder summarizes the historical observation window into a latent representation, which is then projected into quantum angles used to parameterize the VQC. The quantum layer acts as a learnable non-linear feature mixer, modeling cross-variable interactions before the final prediction stage. We evaluate the proposed approach on the BIDMC PPG and Respiration dataset under a Leave-One-Patient-Out protocol. The results show competitive accuracy compared with classical and deep learning baselines, together with greater robustness to noise and missing inputs. These findings suggest that hybrid quantum layers can provide useful inductive biases for physiological time series forecasting in small-cohort clinical settings.

