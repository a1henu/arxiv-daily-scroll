---
layout: default
title: Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA
---

# Semantic Tube Prediction: Beating LLM Data Efficiency with JEPA
**arXiv**：[2602.22617v1](https://arxiv.org/abs/2602.22617) · [PDF](https://arxiv.org/pdf/2602.22617.pdf)  
**作者**：Hai Huang, Yann LeCun, Randall Balestriero  

**一句话要点**：提出语义管预测以提升大语言模型数据效率，基于测地线假设和JEPA正则化。

**关键词**：语义管预测, 大语言模型, 数据效率, JEPA正则化, 测地线假设, 缩放定律

## 3 点简述
- 核心问题：大语言模型的数据效率受限于缩放定律，缺乏优化训练方法。
- 方法要点：引入测地线假设，设计语义管预测任务作为JEPA正则化，约束隐藏状态轨迹。
- 实验或效果：在NL-RX-SYNTH数据集上，用16倍少数据达到基线准确率，违反Chinchilla缩放定律。

## 摘要（原文）

> Large Language Models (LLMs) obey consistent scaling laws -- empirical power-law fits that predict how loss decreases with compute, data, and parameters. While predictive, these laws are descriptive rather than prescriptive: they characterize typical training, not optimal training. Surprisingly few works have successfully challenged the data-efficiency bounds implied by these laws -- which is our primary focus. To that end, we introduce the Geodesic Hypothesis, positing that token sequences trace geodesics on a smooth semantic manifold and are therefore locally linear. Building on this principle, we propose a novel Semantic Tube Prediction (STP) task, a JEPA-style regularizer that confines hidden-state trajectories to a tubular neighborhood of the geodesic. STP generalizes JEPA to language without requiring explicit multi-view augmentations. We show this constraint improves signal-to-noise ratio, and consequently preserves diversity by preventing trajectory collisions during inference. Empirically, STP allows LLMs to match baseline accuracy with 16$\times$ less training data on the NL-RX-SYNTH dataset, directly violating the data term of Chinchilla-style scaling laws and demonstrating that principled geometric priors can surpass brute-force scaling. Code is available at https://github.com/galilai-group/llm-jepa#stp.

