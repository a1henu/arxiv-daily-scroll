---
layout: default
title: Hybrid(Penalized Regression and MLP) Models for Outcome Prediction in HDLSS Health Data
---

# Hybrid(Penalized Regression and MLP) Models for Outcome Prediction in HDLSS Health Data
**arXiv**：[2512.02489v1](https://arxiv.org/abs/2512.02489) · [PDF](https://arxiv.org/pdf/2512.02489.pdf)  
**作者**：Mithra D K  

**一句话要点**：提出混合模型（XGBoost编码器与MLP头）以提升高维低样本健康数据中糖尿病预测性能。

**关键词**：糖尿病预测, 高维低样本数据, 混合模型, XGBoost编码器, 多层感知机, NHANES数据集

## 3 点简述
- 核心问题：基于NHANES健康调查数据预测糖尿病状态，处理高维低样本（HDLSS）挑战。
- 方法要点：结合XGBoost特征编码器与轻量级多层感知机（MLP）头，构建混合模型。
- 实验或效果：在NHANES子集上，混合模型相比基线（逻辑回归、随机森林、XGBoost）获得更高的AUC和平衡准确率。

## 摘要（原文）

> I present an application of established machine learning techniques to NHANES health survey data for predicting diabetes status. I compare baseline models (logistic regression, random forest, XGBoost) with a hybrid approach that uses an XGBoost feature encoder and a lightweight multilayer perceptron (MLP) head. Experiments show the hybrid model attains improved AUC and balanced accuracy compared to baselines on the processed NHANES subset. I release code and reproducible scripts to encourage replication.

