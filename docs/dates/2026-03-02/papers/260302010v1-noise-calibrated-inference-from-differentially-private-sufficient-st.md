---
layout: default
title: Noise-Calibrated Inference from Differentially Private Sufficient Statistics in Exponential Families
---

# Noise-Calibrated Inference from Differentially Private Sufficient Statistics in Exponential Families
**arXiv**：[2603.02010v1](https://arxiv.org/abs/2603.02010) · [PDF](https://arxiv.org/pdf/2603.02010.pdf)  
**作者**：Amir Asiaee, Samhita Pal  

**一句话要点**：提出噪声校准推断方法，基于差分隐私充分统计量在指数族中实现不确定性量化

**关键词**：差分隐私, 指数族, 充分统计量, 噪声校准, 不确定性量化, 合成数据生成

## 3 点简述
- 核心问题：差分隐私数据发布常导致推断校准错误或缺乏不确定性量化方法
- 方法要点：发布差分隐私充分统计量，进行噪声校准似然推断和可选合成数据生成
- 实验或效果：理论验证于三个指数族和真实人口普查数据，提供具体设计规则

## 摘要（原文）

> Many differentially private (DP) data release systems either output DP synthetic data and leave analysts to perform inference as usual, which can lead to severe miscalibration, or output a DP point estimate without a principled way to do uncertainty quantification. This paper develops a clean and tractable middle ground for exponential families: release only DP sufficient statistics, then perform noise-calibrated likelihood-based inference and optional parametric synthetic data generation as post-processing. Our contributions are: (1) a general recipe for approximate-DP release of clipped sufficient statistics under the Gaussian mechanism; (2) asymptotic normality, explicit variance inflation, and valid Wald-style confidence intervals for the plug-in DP MLE; (3) a noise-aware likelihood correction that is first-order equivalent to the plug-in but supports bootstrap-based intervals; and (4) a matching minimax lower bound showing the privacy distortion rate is unavoidable. The resulting theory yields concrete design rules and a practical pipeline for releasing DP synthetic data with principled uncertainty quantification, validated on three exponential families and real census data.

