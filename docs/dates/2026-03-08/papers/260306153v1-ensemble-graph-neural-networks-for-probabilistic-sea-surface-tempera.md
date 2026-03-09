---
layout: default
title: Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations
---

# Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations
**arXiv**：[2603.06153v1](https://arxiv.org/abs/2603.06153) · [PDF](https://arxiv.org/pdf/2603.06153.pdf)  
**作者**：Alejandro J. González-Santana, Giovanny A. Cuervo-Londoño, Javier Sánchez  

**一句话要点**：提出基于输入扰动的集成图神经网络，用于海面温度概率预测，提升不确定性表征。

**关键词**：海面温度预测, 图神经网络, 集成学习, 输入扰动, 不确定性表征, 概率预测

## 3 点简述
- 核心问题：区域海洋预测需高效模型和不确定性表征，传统方法计算成本高。
- 方法要点：采用同质集成策略，通过扰动初始海洋状态引入多样性，无需重训练多个模型。
- 实验或效果：评估多种噪声策略，空间相干扰动（如低分辨率Perlin噪声）在长期预测中校准更好、CRPS更低。

## 摘要（原文）

> Accurate regional ocean forecasting requires models that are both computationally efficient and capable of representing predictive uncertainty. This work investigates ensemble learning strategies for sea surface temperature (SST) forecasting using Graph Neural Networks (GNNs), with a focus on how input perturbation design affects forecast skill and uncertainty representation. We adapt a GNN architecture to the Canary Islands region in the North Atlantic and implement a homogeneous ensemble approach inspired by bagging, where diversity is introduced during inference by perturbing initial ocean states rather than retraining multiple models. Several noise-based ensemble generation strategies are evaluated, including Gaussian noise, Perlin noise, and fractal Perlin noise, with systematic variation of noise intensity and spatial structure. Ensemble forecasts are assessed over a 15-day horizon using deterministic metrics (RMSE and bias) and probabilistic metrics, including the Continuous Ranked Probability Score (CRPS) and the Spread-skill ratio. Results show that, while deterministic skill remains comparable to the single-model forecast, the type and structure of input perturbations strongly influence uncertainty representation, particularly at longer lead times. Ensembles generated with spatially coherent perturbations, such as low-resolution Perlin noise, achieve better calibration and lower CRPS than purely random Gaussian perturbations. These findings highlight the critical role of noise structure and scale in ensemble GNN design and demonstrate that carefully constructed input perturbations can yield well-calibrated probabilistic forecasts without additional training cost, supporting the feasibility of ensemble GNNs for operational regional ocean prediction.

