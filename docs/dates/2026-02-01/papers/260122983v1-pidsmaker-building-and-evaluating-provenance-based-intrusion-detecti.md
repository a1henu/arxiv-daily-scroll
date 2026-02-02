---
layout: default
title: PIDSMaker: Building and Evaluating Provenance-based Intrusion Detection Systems
---

# PIDSMaker: Building and Evaluating Provenance-based Intrusion Detection Systems
**arXiv**：[2601.22983v1](https://arxiv.org/abs/2601.22983) · [PDF](https://arxiv.org/pdf/2601.22983.pdf)  
**作者**：Tristan Bilot, Baoxiang Jiang, Thomas Pasquier  

**一句话要点**：提出PIDSMaker框架以解决基于溯源图的入侵检测系统评估不一致问题

**关键词**：入侵检测系统, 溯源图分析, 机器学习评估, 可复现性框架, 开源工具

## 3 点简述
- 核心问题：现有PIDS评估存在预处理、数据集划分和指标不一致，阻碍公平比较和可复现性。
- 方法要点：整合八个先进系统为模块化架构，提供标准化预处理和标签，支持YAML配置快速原型开发。
- 实验或效果：包含消融研究、超参数调优等工具，发布预处理数据集以支持社区共享评估。

## 摘要（原文）

> Recent provenance-based intrusion detection systems (PIDSs) have demonstrated strong potential for detecting advanced persistent threats (APTs) by applying machine learning to system provenance graphs. However, evaluating and comparing PIDSs remains difficult: prior work uses inconsistent preprocessing pipelines, non-standard dataset splits, and incompatible ground-truth labeling and metrics. These discrepancies undermine reproducibility, impede fair comparison, and impose substantial re-implementation overhead on researchers. We present PIDSMaker, an open-source framework for developing and evaluating PIDSs under consistent protocols. PIDSMaker consolidates eight state-of-the-art systems into a modular, extensible architecture with standardized preprocessing and ground-truth labels, enabling consistent experiments and apples-to-apples comparisons. A YAML-based configuration interface supports rapid prototyping by composing components across systems without code changes. PIDSMaker also includes utilities for ablation studies, hyperparameter tuning, multi-run instability measurement, and visualization, addressing methodological gaps identified in prior work. We demonstrate PIDSMaker through concrete use cases and release it with preprocessed datasets and labels to support shared evaluation for the PIDS community.

