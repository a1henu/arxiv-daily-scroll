---
layout: default
title: Efficient Real-Time Adaptation of ROMs for Unsteady Flows Using Data Assimilation
---

# Efficient Real-Time Adaptation of ROMs for Unsteady Flows Using Data Assimilation
**arXiv**：[2602.23188v1](https://arxiv.org/abs/2602.23188) · [PDF](https://arxiv.org/pdf/2602.23188.pdf)  
**作者**：Ismaël Zighed, Andrea Nóvoa, Luca Magri, Taraneh Sayadi  

**一句话要点**：提出高效重训练策略，利用稀疏观测实现非定常流参数化降阶模型的实时适应。

**关键词**：降阶模型, 数据同化, 变分自编码器, Transformer网络, 实时适应, 不确定性量化

## 3 点简述
- 核心问题：参数化降阶模型在样本外参数区域预测时，需高效适应以保持准确性。
- 方法要点：采用VAE-Transformer架构，通过集成卡尔曼滤波同化稀疏数据，仅重训练自编码器。
- 实验或效果：在纳维-斯托克斯设置中，计算时间大幅减少，提供预测均值和不确定性量化。

## 摘要（原文）

> We propose an efficient retraining strategy for a parameterized Reduced Order Model (ROM) that attains accuracy comparable to full retraining while requiring only a fraction of the computational time and relying solely on sparse observations of the full system. The architecture employs an encode-process-decode structure: a Variational Autoencoder (VAE) to perform dimensionality reduction, and a transformer network to evolve the latent states and model the dynamics. The ROM is parameterized by an external control variable, the Reynolds number in the Navier-Stokes setting, with the transformer exploiting attention mechanisms to capture both temporal dependencies and parameter effects. The probabilistic VAE enables stochastic sampling of trajectory ensembles, providing predictive means and uncertainty quantification through the first two moments. After initial training on a limited set of dynamical regimes, the model is adapted to out-of-sample parameter regions using only sparse data. Its probabilistic formulation naturally supports ensemble generation, which we employ within an ensemble Kalman filtering framework to assimilate data and reconstruct full-state trajectories from minimal observations. We further show that, for the dynamical system considered, the dominant source of error in out-of-sample forecasts stems from distortions of the latent manifold rather than changes in the latent dynamics. Consequently, retraining can be limited to the autoencoder, allowing for a lightweight, computationally efficient, real-time adaptation procedure with very sparse fine-tuning data.

