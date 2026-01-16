---
layout: default
title: EvoMorph: Counterfactual Explanations for Continuous Time-Series Extrinsic Regression Applied to Photoplethysmography
---

# EvoMorph: Counterfactual Explanations for Continuous Time-Series Extrinsic Regression Applied to Photoplethysmography
**arXiv**：[2601.10356v1](https://arxiv.org/abs/2601.10356) · [PDF](https://arxiv.org/pdf/2601.10356.pdf)  
**作者**：Mesut Ceylan, Alexis Tabin, Patrick Langer, Elgar Fleisch, Filipe Barata  

**一句话要点**：提出EvoMorph框架，为连续生物医学时间序列回归生成生理合理的反事实解释。

**关键词**：反事实解释, 时间序列回归, 光电容积描记术, 进化算法, 不确定性量化, 生物医学信号处理

## 3 点简述
- 核心问题：现有反事实解释方法多用于分类，忽略波形形态，难以生成生理合理的连续时间序列解释。
- 方法要点：采用多目标进化框架，优化基于可解释信号描述符的形态感知目标，保持波形结构。
- 实验或效果：在三个PPG数据集上评估，优于基线，并用于不确定性量化案例研究。

## 摘要（原文）

> Wearable devices enable continuous, population-scale monitoring of physiological signals, such as photoplethysmography (PPG), creating new opportunities for data-driven clinical assessment. Time-series extrinsic regression (TSER) models increasingly leverage PPG signals to estimate clinically relevant outcomes, including heart rate, respiratory rate, and oxygen saturation. For clinical reasoning and trust, however, single point estimates alone are insufficient: clinicians must also understand whether predictions are stable under physiologically plausible variations and to what extent realistic, attainable changes in physiological signals would meaningfully alter a model's prediction. Counterfactual explanations (CFE) address these "what-if" questions, yet existing time series CFE generation methods are largely restricted to classification, overlook waveform morphology, and often produce physiologically implausible signals, limiting their applicability to continuous biomedical time series. To address these limitations, we introduce EvoMorph, a multi-objective evolutionary framework for generating physiologically plausible and diverse CFE for TSER applications. EvoMorph optimizes morphology-aware objectives defined on interpretable signal descriptors and applies transformations to preserve the waveform structure. We evaluated EvoMorph on three PPG datasets (heart rate, respiratory rate, and oxygen saturation) against a nearest-unlike-neighbor baseline. In addition, in a case study, we evaluated EvoMorph as a tool for uncertainty quantification by relating counterfactual sensitivity to bootstrap-ensemble uncertainty and data-density measures. Overall, EvoMorph enables the generation of physiologically-aware counterfactuals for continuous biomedical signals and supports uncertainty-aware interpretability, advancing trustworthy model analysis for clinical time-series applications.

