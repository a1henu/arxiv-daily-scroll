---
layout: default
title: Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving
---

# Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving
**arXiv**：[2602.23259v1](https://arxiv.org/abs/2602.23259) · [PDF](https://arxiv.org/pdf/2602.23259.pdf)  
**作者**：Jiangxin Sun, Feng Xue, Teng Long, Chang Liu, Jian-Fang Hu, Wei-Shi Zheng, Nicu Sebe  

**一句话要点**：提出风险感知世界模型预测控制框架，以提升端到端自动驾驶在未见场景下的泛化能力。

**关键词**：端到端自动驾驶, 世界模型预测控制, 风险感知交互, 自评估蒸馏, 泛化能力, 决策可解释性

## 3 点简述
- 核心问题：模仿学习依赖专家演示，在长尾场景中泛化受限，可能导致不安全决策。
- 方法要点：利用世界模型预测候选动作后果，通过风险评估选择低风险动作，并设计风险感知交互策略训练模型。
- 实验或效果：在分布内和分布外场景中优于现有方法，提供更好的决策可解释性。

## 摘要（原文）

> With advances in imitation learning (IL) and large-scale driving datasets, end-to-end autonomous driving (E2E-AD) has made great progress recently. Currently, IL-based methods have become a mainstream paradigm: models rely on standard driving behaviors given by experts, and learn to minimize the discrepancy between their actions and expert actions. However, this objective of "only driving like the expert" suffers from limited generalization: when encountering rare or unseen long-tail scenarios outside the distribution of expert demonstrations, models tend to produce unsafe decisions in the absence of prior experience. This raises a fundamental question: Can an E2E-AD system make reliable decisions without any expert action supervision? Motivated by this, we propose a unified framework named Risk-aware World Model Predictive Control (RaWMPC) to address this generalization dilemma through robust control, without reliance on expert demonstrations. Practically, RaWMPC leverages a world model to predict the consequences of multiple candidate actions and selects low-risk actions through explicit risk evaluation. To endow the world model with the ability to predict the outcomes of risky driving behaviors, we design a risk-aware interaction strategy that systematically exposes the world model to hazardous behaviors, making catastrophic outcomes predictable and thus avoidable. Furthermore, to generate low-risk candidate actions at test time, we introduce a self-evaluation distillation method to distill riskavoidance capabilities from the well-trained world model into a generative action proposal network without any expert demonstration. Extensive experiments show that RaWMPC outperforms state-of-the-art methods in both in-distribution and out-of-distribution scenarios, while providing superior decision interpretability.

