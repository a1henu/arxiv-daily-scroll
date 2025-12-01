---
layout: default
title: High-Resolution Probabilistic Data-Driven Weather Modeling with a Stretched-Grid
---

# High-Resolution Probabilistic Data-Driven Weather Modeling with a Stretched-Grid
**arXiv**：[2511.23043v1](https://arxiv.org/abs/2511.23043) · [PDF](https://arxiv.org/pdf/2511.23043.pdf)  
**作者**：Even Marius Nordhagen, Håvard Homleid Haugen, Aram Farhad Shafiq Salihi, Magnus Sikora Ingstad, Thomas Nils Nipen, Ivar Ambjørn Seierstad, Inger-Lise Frogner, Mariana Clare, Simon Lang, Matthew Chantry, Peter Dueben, Jørn Kristiansen  

**一句话要点**：提出基于拉伸网格的概率数据驱动天气模型，以生成高分辨率空间一致的气象场。

**关键词**：概率天气建模, 拉伸网格, 随机编码器-解码器, 连续排名概率得分, 空间一致性, 高分辨率气象场

## 3 点简述
- 核心问题：传统天气模型难以高效生成高分辨率、空间一致的概率气象场。
- 方法要点：采用拉伸网格（2.5公里和31公里分辨率）和随机编码器-解码器架构，结合CRPS和谱空间损失训练。
- 实验或效果：与MEPS相比，在观测评估中表现竞争性，且空间一致性优于基于MSE或缺少谱损失组件的模型。

## 摘要（原文）

> We present a probabilistic data-driven weather model capable of providing an ensemble of high spatial resolution realizations of 87 variables at arbitrary forecast length and ensemble size. The model uses a stretched grid, dedicating 2.5 km resolution to a region of interest, and 31 km resolution elsewhere. Based on a stochastic encoder-decoder architecture, the model is trained using a loss function based on the Continuous Ranked Probability Score (CRPS) evaluated point-wise in real and spectral space. The spectral loss components is shown to be necessary to create fields that are spatially coherent. The model is compared to high-resolution operational numerical weather prediction forecasts from the MetCoOp Ensemble Prediction System (MEPS), showing competitive forecasts when evaluated against observations from surface weather stations. The model produced fields that are more spatially coherent than mean squared error based models and CRPS based models without the spectral component in the loss.

