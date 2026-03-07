---
layout: default
title: Uncertainty-aware Blood Glucose Prediction from Continuous Glucose Monitoring Data
---

# Uncertainty-aware Blood Glucose Prediction from Continuous Glucose Monitoring Data
**arXiv**：[2603.04955v1](https://arxiv.org/abs/2603.04955) · [PDF](https://arxiv.org/pdf/2603.04955.pdf)  
**作者**：Hai Siong Tan  

**一句话要点**：提出不确定性感知神经网络模型，用于1型糖尿病血糖预测与不良事件识别。

**关键词**：血糖预测, 不确定性量化, 序列模型, 1型糖尿病, 深度证据回归

## 3 点简述
- 核心问题：研究不确定性感知模型在1型糖尿病血糖预测和不良事件识别中的应用。
- 方法要点：基于LSTM、GRU和Transformer序列模型，采用蒙特卡洛dropout或深度证据回归输出层进行不确定性量化。
- 实验或效果：在HUPA-UCM数据集上验证，Transformer模型结合证据输出头提供最有效框架，预测精度高且不确定性估计校准良好。

## 摘要（原文）

> In this work, we investigate uncertainty-aware neural network models for blood glucose prediction and adverse glycemic event identification in Type 1 diabetes. We consider three families of sequence models based on LSTM, GRU, and Transformer architectures, with uncertainty quantification enabled by either Monte Carlo dropout or through evidential output layers compatible with Deep Evidential Regression. Using the HUPA-UCM diabetes dataset for validation, we find that Transformer-based models equipped with evidential output heads provide the most effective uncertainty-aware framework, achieving consistently higher predictive accuracies and better-calibrated uncertainty estimates whose magnitudes significantly correlate with prediction errors. We further evaluate the clinical risk of each model using the recently proposed Diabetes Technology Society error grid, with risk categories defined by international expert consensus. Our results demonstrate the value of integrating principled uncertainty quantification into real-time machine-learning-based blood glucose prediction systems.

