---
layout: default
title: Probabilistic Transformers for Joint Modeling of Global Weather Dynamics and Decision-Centric Variables
---

# Probabilistic Transformers for Joint Modeling of Global Weather Dynamics and Decision-Centric Variables
**arXiv**：[2601.03753v1](https://arxiv.org/abs/2601.03753) · [PDF](https://arxiv.org/pdf/2601.03753.pdf)  
**作者**：Paulius Rauba, Viktor Cikojevic, Fran Bartolic, Sam Levang, Ty Dickinson, Chase Dwelle  

**一句话要点**：提出GEM-2概率变换器，联合建模全球天气动态与决策变量以优化下游应用。

**关键词**：概率变换器, 天气预测, 决策变量建模, CRPS训练, 全球大气动态, 经济价值评估

## 3 点简述
- 核心问题：传统天气预测模型未直接学习决策相关变量分布，导致后处理偏差。
- 方法要点：GEM-2通过CRPS目标训练，轻量高效，直接输出用户行动变量。
- 实验或效果：在决策理论评估中表现优异，超越操作NWP模型，收敛稳定。

## 摘要（原文）

> Weather forecasts sit upstream of high-stakes decisions in domains such as grid operations, aviation, agriculture, and emergency response. Yet forecast users often face a difficult trade-off. Many decision-relevant targets are functionals of the atmospheric state variables, such as extrema, accumulations, and threshold exceedances, rather than state variables themselves. As a result, users must estimate these targets via post-processing, which can be suboptimal and can introduce structural bias. The core issue is that decisions depend on distributions over these functionals that the model is not trained to learn directly.
>   In this work, we introduce GEM-2, a probabilistic transformer that jointly learns global atmospheric dynamics alongside a suite of variables that users directly act upon. Using this training recipe, we show that a lightweight (~275M params) and computationally efficient (~20-100x training speedup relative to state-of-the-art) transformer trained on the CRPS objective can directly outperform operational numerical weather prediction (NWP) models and be competitive with ML models that rely on expensive multi-step diffusion processes or require bespoke multi-stage fine-tuning strategies. We further demonstrate state-of-the-art economic value metrics under decision-theoretic evaluation, stable convergence to climatology at S2S and seasonal timescales, and a surprising insensitivity to many commonly assumed architectural and training design choices.

