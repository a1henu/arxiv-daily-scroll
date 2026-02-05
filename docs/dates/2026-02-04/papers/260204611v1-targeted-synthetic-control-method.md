---
layout: default
title: Targeted Synthetic Control Method
---

# Targeted Synthetic Control Method
**arXiv**：[2602.04611v1](https://arxiv.org/abs/2602.04611) · [PDF](https://arxiv.org/pdf/2602.04611.pdf)  
**作者**：Yuxin Wang, Dennis Frauen, Emil Javurek, Konstantin Hess, Yuchen Ma, Stefan Feuerriegel  

**一句话要点**：提出目标合成控制方法以改进面板数据因果效应估计

**关键词**：合成控制方法, 因果推断, 面板数据, 目标估计, 权重校准, 机器学习模型

## 3 点简述
- 核心问题：合成控制方法在单处理单元面板数据中估计因果效应时，存在权重不稳定和反事实估计无界问题。
- 方法要点：采用两阶段估计器，通过权重倾斜子模型进行一维目标更新，校准初始权重以减少偏差，并确保最终估计为凸组合。
- 实验或效果：在合成和真实世界实验中，相比现有方法，TSC一致提高了估计准确性。

## 摘要（原文）

> The synthetic control method (SCM) estimates causal effects in panel data with a single-treated unit by constructing a counterfactual outcome as a weighted combination of untreated control units that matches the pre-treatment trajectory. In this paper, we introduce the targeted synthetic control (TSC) method, a new two-stage estimator that directly estimates the counterfactual outcome. Specifically, our TSC method (1) yields a targeted debiasing estimator, in the sense that the targeted updating refines the initial weights to produce more stable weights; and (2) ensures that the final counterfactual estimation is a convex combination of observed control outcomes to enable direct interpretation of the synthetic control weights. TSC is flexible and can be instantiated with arbitrary machine learning models. Methodologically, TSC starts from an initial set of synthetic-control weights via a one-dimensional targeted update through the weight-tilting submodel, which calibrates the weights to reduce bias of weights estimation arising from pre-treatment fit. Furthermore, TSC avoids key shortcomings of existing methods (e.g., the augmented SCM), which can produce unbounded counterfactual estimates. Across extensive synthetic and real-world experiments, TSC consistently improves estimation accuracy over state-of-the-art SCM baselines.

