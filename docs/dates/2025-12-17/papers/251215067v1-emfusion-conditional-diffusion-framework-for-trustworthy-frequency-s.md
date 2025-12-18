---
layout: default
title: EMFusion: Conditional Diffusion Framework for Trustworthy Frequency Selective EMF Forecasting in Wireless Networks
---

# EMFusion: Conditional Diffusion Framework for Trustworthy Frequency Selective EMF Forecasting in Wireless Networks
**arXiv**：[2512.15067v1](https://arxiv.org/abs/2512.15067) · [PDF](https://arxiv.org/pdf/2512.15067.pdf)  
**作者**：Zijiang Yan, Yixiang Huang, Jianhua Pei, Hina Tabassum, Luca Chiaraviglio  

**一句话要点**：提出EMFusion条件扩散框架，用于无线网络中可信的频率选择性电磁场预测。

**关键词**：电磁场预测, 条件扩散模型, 频率选择性, 不确定性量化, 无线网络规划, 多变量预测

## 3 点简述
- 核心问题：现有方法依赖宽带聚合EMF的单变量预测，无法捕捉运营商间和频率间的变化，影响网络规划。
- 方法要点：基于条件扩散模型，集成上下文因素，使用残差U-Net和交叉注意力机制，并采用基于插值的采样策略确保时间一致性。
- 实验或效果：在频率选择性EMF数据集上，EMFusion在CRPS和NRMSE等指标上优于基线模型，提供校准的概率预测区间。

## 摘要（原文）

> The rapid growth in wireless infrastructure has increased the need to accurately estimate and forecast electromagnetic field (EMF) levels to ensure ongoing compliance, assess potential health impacts, and support efficient network planning. While existing studies rely on univariate forecasting of wideband aggregate EMF data, frequency-selective multivariate forecasting is needed to capture the inter-operator and inter-frequency variations essential for proactive network planning. To this end, this paper introduces EMFusion, a conditional multivariate diffusion-based probabilistic forecasting framework that integrates diverse contextual factors (e.g., time of day, season, and holidays) while providing explicit uncertainty estimates. The proposed architecture features a residual U-Net backbone enhanced by a cross-attention mechanism that dynamically integrates external conditions to guide the generation process. Furthermore, EMFusion integrates an imputation-based sampling strategy that treats forecasting as a structural inpainting task, ensuring temporal coherence even with irregular measurements. Unlike standard point forecasters, EMFusion generates calibrated probabilistic prediction intervals directly from the learned conditional distribution, providing explicit uncertainty quantification essential for trustworthy decision-making. Numerical experiments conducted on frequency-selective EMF datasets demonstrate that EMFusion with the contextual information of working hours outperforms the baseline models with or without conditions. The EMFusion outperforms the best baseline by 23.85% in continuous ranked probability score (CRPS), 13.93% in normalized root mean square error, and reduces prediction CRPS error by 22.47%.

