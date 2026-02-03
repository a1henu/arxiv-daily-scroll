---
layout: default
title: Generating Causal Temporal Interaction Graphs for Counterfactual Validation of Temporal Link Prediction
---

# Generating Causal Temporal Interaction Graphs for Counterfactual Validation of Temporal Link Prediction
**arXiv**：[2602.02161v1](https://arxiv.org/abs/2602.02161) · [PDF](https://arxiv.org/pdf/2602.02161.pdf)  
**作者**：Aniq Ur Rahman, Justin P. Coon  

**一句话要点**：提出因果时序交互图框架以验证时序链路预测模型的因果机制

**关键词**：时序链路预测, 因果验证, 结构方程模型, 反事实评估, 交互图生成

## 3 点简述
- 核心问题：现有时序链路预测评估仅关注预测精度，未检验模型是否捕获因果机制。
- 方法要点：构建因果时序交互图，引入支持激励和抑制效应的结构方程模型，并定义跨模型预测误差距离度量。
- 实验或效果：通过因果偏移和时间戳重排实验，验证预测器在因果距离较大时性能下降，支持因果感知基准测试。

## 摘要（原文）

> Temporal link prediction (TLP) models are commonly evaluated based on predictive accuracy, yet such evaluations do not assess whether these models capture the causal mechanisms that govern temporal interactions. In this work, we propose a framework for counterfactual validation of TLP models by generating causal temporal interaction graphs (CTIGs) with known ground-truth causal structure. We first introduce a structural equation model for continuous-time event sequences that supports both excitatory and inhibitory effects, and then extend this mechanism to temporal interaction graphs. To compare causal models, we propose a distance metric based on cross-model predictive error, and empirically validate the hypothesis that predictors trained on one causal model degrade when evaluated on sufficiently distant models. Finally, we instantiate counterfactual evaluation under (i) controlled causal shifts between generating models and (ii) timestamp shuffling as a stochastic distortion with measurable causal distance. Our framework provides a foundation for causality-aware benchmarking.

