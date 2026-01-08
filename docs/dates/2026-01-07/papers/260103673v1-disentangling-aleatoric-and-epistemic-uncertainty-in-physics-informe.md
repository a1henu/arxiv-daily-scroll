---
layout: default
title: Disentangling Aleatoric and Epistemic Uncertainty in Physics-Informed Neural Networks. Application to Insulation Material Degradation Prognostics
---

# Disentangling Aleatoric and Epistemic Uncertainty in Physics-Informed Neural Networks. Application to Insulation Material Degradation Prognostics
**arXiv**：[2601.03673v1](https://arxiv.org/abs/2601.03673) · [PDF](https://arxiv.org/pdf/2601.03673.pdf)  
**作者**：Ibai Ramirez, Jokin Alcibar, Joel Pino, Mikel Sanz, Jose I. Aizpurua  

**一句话要点**：提出异方差贝叶斯物理信息神经网络框架，联合建模认知与偶然不确定性，应用于变压器绝缘材料老化预测。

**关键词**：贝叶斯物理信息神经网络, 不确定性量化, 绝缘材料老化预测, 健康管理, 概率推理, 变压器资产管理

## 3 点简述
- 核心问题：物理信息神经网络在健康管理中不确定性量化不足，仅处理认知不确定性，限制风险决策。
- 方法要点：结合贝叶斯神经网络与物理残差约束，通过先验分布实现概率推理，支持全预测后验。
- 实验或效果：在变压器绝缘老化应用中验证，相比确定性PINN等方法，提升预测精度和不确定性校准。

## 摘要（原文）

> Physics-Informed Neural Networks (PINNs) provide a framework for integrating physical laws with data. However, their application to Prognostics and Health Management (PHM) remains constrained by the limited uncertainty quantification (UQ) capabilities. Most existing PINN-based prognostics approaches are deterministic or account only for epistemic uncertainty, limiting their suitability for risk-aware decision-making. This work introduces a heteroscedastic Bayesian Physics-Informed Neural Network (B-PINN) framework that jointly models epistemic and aleatoric uncertainty, yielding full predictive posteriors for spatiotemporal insulation material ageing estimation. The approach integrates Bayesian Neural Networks (BNNs) with physics-based residual enforcement and prior distributions, enabling probabilistic inference within a physics-informed learning architecture. The framework is evaluated on transformer insulation ageing application, validated with a finite-element thermal model and field measurements from a solar power plant, and benchmarked against deterministic PINNs, dropout-based PINNs (d-PINNs), and alternative B-PINN variants. Results show that the proposed B-PINN provides improved predictive accuracy and better-calibrated uncertainty estimates than competing approaches. A systematic sensitivity study further analyzes the impact of boundary-condition, initial-condition, and residual sampling strategies on accuracy, calibration, and generalization. Overall, the findings highlight the potential of Bayesian physics-informed learning to support uncertainty-aware prognostics and informed decision-making in transformer asset management.

