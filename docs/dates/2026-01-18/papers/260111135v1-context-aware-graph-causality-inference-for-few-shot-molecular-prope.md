---
layout: default
title: Context-aware Graph Causality Inference for Few-Shot Molecular Property Prediction
---

# Context-aware Graph Causality Inference for Few-Shot Molecular Property Prediction
**arXiv**：[2601.11135v1](https://arxiv.org/abs/2601.11135) · [PDF](https://arxiv.org/pdf/2601.11135.pdf)  
**作者**：Van Thuy Hoang, O-Joun Lee  

**一句话要点**：提出CaMol框架，通过因果推断解决少样本分子性质预测中的功能组利用和关键子结构识别问题。

**关键词**：分子性质预测, 少样本学习, 因果推断, 图神经网络, 可解释性, 化学知识图谱

## 3 点简述
- 核心问题：少样本分子性质预测中，现有方法难以利用功能组先验知识和识别与性质直接相关的关键子结构。
- 方法要点：构建上下文图编码化学知识，采用可学习原子掩码策略解耦因果子结构，引入分布干预器进行后门调整。
- 实验或效果：在多个分子数据集上，CaMol在少样本任务中实现更高准确性和样本效率，且发现的因果子结构与化学知识一致。

## 摘要（原文）

> Molecular property prediction is becoming one of the major applications of graph learning in Web-based services, e.g., online protein structure prediction and drug discovery. A key challenge arises in few-shot scenarios, where only a few labeled molecules are available for predicting unseen properties. Recently, several studies have used in-context learning to capture relationships among molecules and properties, but they face two limitations in: (1) exploiting prior knowledge of functional groups that are causally linked to properties and (2) identifying key substructures directly correlated with properties. We propose CaMol, a context-aware graph causality inference framework, to address these challenges by using a causal inference perspective, assuming that each molecule consists of a latent causal structure that determines a specific property. First, we introduce a context graph that encodes chemical knowledge by linking functional groups, molecules, and properties to guide the discovery of causal substructures. Second, we propose a learnable atom masking strategy to disentangle causal substructures from confounding ones. Third, we introduce a distribution intervener that applies backdoor adjustment by combining causal substructures with chemically grounded confounders, disentangling causal effects from real-world chemical variations. Experiments on diverse molecular datasets showed that CaMol achieved superior accuracy and sample efficiency in few-shot tasks, showing its generalizability to unseen properties. Also, the discovered causal substructures were strongly aligned with chemical knowledge about functional groups, supporting the model interpretability.

