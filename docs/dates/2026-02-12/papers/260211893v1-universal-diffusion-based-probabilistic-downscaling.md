---
layout: default
title: Universal Diffusion-Based Probabilistic Downscaling
---

# Universal Diffusion-Based Probabilistic Downscaling
**arXiv**：[2602.11893v1](https://arxiv.org/abs/2602.11893) · [PDF](https://arxiv.org/pdf/2602.11893.pdf)  
**作者**：Roberto Molinaro, Niall Siegenheim, Henry Martin, Mark Frey, Niels Poulsen, Philipp Seitz, Marvin Vincent Gabler  

**一句话要点**：提出基于扩散模型的通用降尺度框架，以提升天气预测的空间分辨率和概率表示。

**关键词**：扩散模型, 天气预测降尺度, 概率预测, 零样本学习, 空间分辨率提升

## 3 点简述
- 核心问题：确定性低分辨率天气预报缺乏高分辨率概率预测，需模型无关的降尺度方法。
- 方法要点：训练单一条件扩散模型，利用粗分辨率输入和高分辨率目标，实现零样本应用。
- 实验或效果：在多种天气模型上，降尺度预测的集合平均和概率技能（如CRPS）显著优于原始预测。

## 摘要（原文）

> We introduce a universal diffusion-based downscaling framework that lifts deterministic low-resolution weather forecasts into probabilistic high-resolution predictions without any model-specific fine-tuning. A single conditional diffusion model is trained on paired coarse-resolution inputs (~25 km resolution) and high-resolution regional reanalysis targets (~5 km resolution), and is applied in a fully zero-shot manner to deterministic forecasts from heterogeneous upstream weather models. Focusing on near-surface variables, we evaluate probabilistic forecasts against independent in situ station observations over lead times up to 90 h. Across a diverse set of AI-based and numerical weather prediction (NWP) systems, the ensemble mean of the downscaled forecasts consistently improves upon each model's own raw deterministic forecast, and substantially larger gains are observed in probabilistic skill as measured by CRPS. These results demonstrate that diffusion-based downscaling provides a scalable, model-agnostic probabilistic interface for enhancing spatial resolution and uncertainty representation in operational weather forecasting pipelines.

