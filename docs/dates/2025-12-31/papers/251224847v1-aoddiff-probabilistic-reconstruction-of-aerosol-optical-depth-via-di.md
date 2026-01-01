---
layout: default
title: AODDiff: Probabilistic Reconstruction of Aerosol Optical Depth via Diffusion-based Bayesian Inference
---

# AODDiff: Probabilistic Reconstruction of Aerosol Optical Depth via Diffusion-based Bayesian Inference
**arXiv**：[2512.24847v1](https://arxiv.org/abs/2512.24847) · [PDF](https://arxiv.org/pdf/2512.24847.pdf)  
**作者**：Linhao Fan, Hongqiang Fang, Jingyang Dai, Yong Jiang, Qixing Zhang  

**一句话要点**：提出AODDiff框架，基于扩散贝叶斯推断概率性重建气溶胶光学厚度，解决数据稀缺和不确定性量化问题。

**关键词**：气溶胶光学厚度重建, 扩散模型, 贝叶斯推断, 不确定性量化, 时空概率分布, 生成先验

## 3 点简述
- 核心问题：气溶胶光学厚度重建受限于训练数据不完整和缺乏不确定性量化。
- 方法要点：利用学习到的时空概率分布作为生成先验，无需任务特定重训练，支持异构观测约束。
- 实验或效果：在降尺度和修复任务中验证，保持高空间谱保真度，通过多次采样实现不确定性量化。

## 摘要（原文）

> High-quality reconstruction of Aerosol Optical Depth (AOD) fields is critical for Atmosphere monitoring, yet current models remain constrained by the scarcity of complete training data and a lack of uncertainty quantification.To address these limitations, we propose AODDiff, a probabilistic reconstruction framework based on diffusion-based Bayesian inference. By leveraging the learned spatiotemporal probability distribution of the AOD field as a generative prior, this framework can be flexibly adapted to various reconstruction tasks without requiring task-specific retraining. We first introduce a corruption-aware training strategy to learns a spatiotemporal AOD prior solely from naturally incomplete data. Subsequently, we employ a decoupled annealing posterior sampling strategy that enables the more effective and integration of heterogeneous observations as constraints to guide the generation process. We validate the proposed framework through extensive experiments on Reanalysis data. Results across downscaling and inpainting tasks confirm the efficacy and robustness of AODDiff, specifically demonstrating its advantage in maintaining high spatial spectral fidelity. Furthermore, as a generative model, AODDiff inherently enables uncertainty quantification via multiple sampling, offering critical confidence metrics for downstream applications.

