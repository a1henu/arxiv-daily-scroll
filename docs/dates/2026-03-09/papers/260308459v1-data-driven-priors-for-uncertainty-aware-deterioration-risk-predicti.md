---
layout: default
title: Data-Driven Priors for Uncertainty-Aware Deterioration Risk Prediction with Multimodal Data
---

# Data-Driven Priors for Uncertainty-Aware Deterioration Risk Prediction with Multimodal Data
**arXiv**：[2603.08459v1](https://arxiv.org/abs/2603.08459) · [PDF](https://arxiv.org/pdf/2603.08459.pdf)  
**作者**：L. Julián Lechuga López, Tim G. J. Rudner, Farah E. Shamout  

**一句话要点**：提出MedCertAIn框架，利用多模态临床数据提升院内风险预测的性能与不确定性量化

**关键词**：不确定性量化, 多模态融合, 临床风险预测, 数据驱动先验, 院内预测

## 3 点简述
- 核心问题：当前机器学习模型在多模态临床预测中缺乏可靠的不确定性估计，阻碍实际部署。
- 方法要点：设计数据驱动的先验，结合跨模态相似性和模态特定数据损坏，以改进不确定性量化。
- 实验或效果：在MIMIC-IV和MIMIC-CXR数据集上验证，相比基线方法显著提升预测性能和不确定性估计。

## 摘要（原文）

> Safe predictions are a crucial requirement for integrating predictive models into clinical decision support systems. One approach for ensuring trustworthiness is to enable models' ability to express their uncertainty about individual predictions. However, current machine learning models frequently lack reliable uncertainty estimation, hindering real-world deployment. This is further observed in multimodal settings, where the goal is to enable effective information fusion. In this work, we propose $\texttt{MedCertAIn}$, a predictive uncertainty framework that leverages multimodal clinical data for in-hospital risk prediction to improve model performance and reliability. We design data-driven priors over neural network parameters using a hybrid strategy that considers cross-modal similarity in self-supervised latent representations and modality-specific data corruptions. We train and evaluate the models with such priors using clinical time-series and chest X-ray images from the publicly-available datasets MIMIC-IV and MIMIC-CXR. Our results show that $\texttt{MedCertAIn}$ significantly improves predictive performance and uncertainty quantification compared to state-of-the-art deterministic baselines and alternative Bayesian methods. These findings highlight the promise of data-driven priors in advancing robust, uncertainty-aware AI tools for high-stakes clinical applications.

