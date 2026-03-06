---
layout: default
title: Uncertainty-aware Blood Glucose Prediction from Continuous Glucose Monitoring Data
---

# Uncertainty-aware Blood Glucose Prediction from Continuous Glucose Monitoring Data
**arXiv**：[2603.04955v1](https://arxiv.org/abs/2603.04955) · [PDF](https://arxiv.org/pdf/2603.04955.pdf)  
**作者**：Hai Siong Tan  

**一句话要点**：提出基于Transformer与证据输出层的血糖预测模型，集成不确定性量化以提升预测准确性与临床风险评估。

**关键词**：血糖预测, 不确定性量化, Transformer模型, 连续血糖监测, 临床风险评估, 证据回归

## 3 点简述
- 研究基于LSTM、GRU和Transformer的序列模型，用于1型糖尿病血糖预测与不良事件识别。
- 采用蒙特卡洛dropout或证据输出层实现不确定性量化，Transformer模型表现最佳，预测误差与不确定性显著相关。
- 使用HUPA-UCM数据集验证，并通过糖尿病技术学会误差网格评估临床风险，证明不确定性量化在实时血糖预测系统中的价值。

## 摘要（原文）

> In this work, we investigate uncertainty-aware neural network models for blood glucose prediction and adverse glycemic event identification in Type 1 diabetes. We consider three families of sequence models based on LSTM, GRU, and Transformer architectures, with uncertainty quantification enabled by either Monte Carlo dropout or through evidential output layers compatible with Deep Evidential Regression. Using the HUPA-UCM diabetes dataset for validation, we find that Transformer-based models equipped with evidential output heads provide the most effective uncertainty-aware framework, achieving consistently higher predictive accuracies and better-calibrated uncertainty estimates whose magnitudes significantly correlate with prediction errors. We further evaluate the clinical risk of each model using the recently proposed Diabetes Technology Society error grid, with risk categories defined by international expert consensus. Our results demonstrate the value of integrating principled uncertainty quantification into real-time machine-learning-based blood glucose prediction systems.

