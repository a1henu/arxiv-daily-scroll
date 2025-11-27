---
layout: default
title: CaFlow: Enhancing Long-Term Action Quality Assessment with Causal Counterfactual Flow
---

# CaFlow: Enhancing Long-Term Action Quality Assessment with Causal Counterfactual Flow
**arXiv**：[2511.21653v1](https://arxiv.org/abs/2511.21653) · [PDF](https://arxiv.org/pdf/2511.21653.pdf)  
**作者**：Ruisheng Han, Kanglei Zhou, Shuang Chen, Amir Atapour-Abarghouei, Hubert P. H. Shum  

**一句话要点**：提出CaFlow框架以解决长时动作质量评估中的因果混淆和时序建模问题

**关键词**：动作质量评估, 因果推理, 反事实学习, 时序建模, 长视频分析, 自监督学习

## 3 点简述
- 核心问题：长时动作质量评估易受上下文混淆影响，现有方法依赖高成本标注或单向时序建模
- 方法要点：结合因果反事实正则化自监督解耦特征，双向时间条件流建模前后向动态
- 实验或效果：在多个长时AQA基准上实现最先进性能，代码已开源

## 摘要（原文）

> Action Quality Assessment (AQA) predicts fine-grained execution scores from action videos and is widely applied in sports, rehabilitation, and skill evaluation. Long-term AQA, as in figure skating or rhythmic gymnastics, is especially challenging since it requires modeling extended temporal dynamics while remaining robust to contextual confounders. Existing approaches either depend on costly annotations or rely on unidirectional temporal modeling, making them vulnerable to spurious correlations and unstable long-term representations. To this end, we propose CaFlow, a unified framework that integrates counterfactual de-confounding with bidirectional time-conditioned flow. The Causal Counterfactual Regularization (CCR) module disentangles causal and confounding features in a self-supervised manner and enforces causal robustness through counterfactual interventions, while the BiT-Flow module models forward and backward dynamics with a cycle-consistency constraint to produce smoother and more coherent representations. Extensive experiments on multiple long-term AQA benchmarks demonstrate that CaFlow achieves state-of-the-art performance. Code is available at https://github.com/Harrison21/CaFlow

