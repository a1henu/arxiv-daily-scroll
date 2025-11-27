---
layout: default
title: I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation
---

# I-GLIDE: Input Groups for Latent Health Indicators in Degradation Estimation
**arXiv**：[2511.21208v1](https://arxiv.org/abs/2511.21208) · [PDF](https://arxiv.org/pdf/2511.21208.pdf)  
**作者**：Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet  

**一句话要点**：提出I-GLIDE框架，通过指标组和不确定性量化改进复杂系统剩余寿命预测

**关键词**：剩余寿命预测, 健康指标构建, 不确定性量化, 退化建模, 多传感器系统, 可解释诊断

## 3 点简述
- 现有健康指标方法难以解耦多传感器系统中的复杂退化机制和量化不确定性
- 首次将RaPP用作健康指标，并集成不确定性量化与指标组以提升鲁棒性和可解释性
- 在航空航天和制造数据上验证，准确性和泛化性优于现有方法

## 摘要（原文）

> Accurate remaining useful life (RUL) prediction hinges on the quality of health indicators (HIs), yet existing methods often fail to disentangle complex degradation mechanisms in multi-sensor systems or quantify uncertainty in HI reliability. This paper introduces a novel framework for HI construction, advancing three key contributions. First, we adapt Reconstruction along Projected Pathways (RaPP) as a health indicator (HI) for RUL prediction for the first time, showing that it outperforms traditional reconstruction error metrics. Second, we show that augmenting RaPP-derived HIs with aleatoric and epistemic uncertainty quantification (UQ) via Monte Carlo dropout and probabilistic latent spaces- significantly improves RUL-prediction robustness. Third, and most critically, we propose indicator groups, a paradigm that isolates sensor subsets to model system-specific degradations, giving rise to our novel method, I-GLIDE which enables interpretable, mechanism-specific diagnostics. Evaluated on data sourced from aerospace and manufacturing systems, our approach achieves marked improvements in accuracy and generalizability compared to state-of-the-art HI methods while providing actionable insights into system failure pathways. This work bridges the gap between anomaly detection and prognostics, offering a principled framework for uncertainty-aware degradation modeling in complex systems.

