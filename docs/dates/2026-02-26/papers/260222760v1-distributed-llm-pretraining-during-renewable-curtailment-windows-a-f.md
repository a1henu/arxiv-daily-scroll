---
layout: default
title: Distributed LLM Pretraining During Renewable Curtailment Windows: A Feasibility Study
---

# Distributed LLM Pretraining During Renewable Curtailment Windows: A Feasibility Study
**arXiv**：[2602.22760v1](https://arxiv.org/abs/2602.22760) · [PDF](https://arxiv.org/pdf/2602.22760.pdf)  
**作者**：Philipp Wiesner, Soeren Becker, Brett Cornick, Dominik Scheinert, Alexander Acker, Odej Kao  

**一句话要点**：提出分布式LLM预训练系统，利用可再生能源弃电窗口降低碳排放

**关键词**：分布式训练, 联邦学习, 可再生能源, 碳排放优化, LLM预训练

## 3 点简述
- 核心问题：LLM训练能耗高，可再生能源弃电造成浪费
- 方法要点：基于Flower框架，在弃电窗口弹性切换单点与联邦训练
- 实验或效果：原型系统训练561M参数模型，碳排放降至基线5-12%

## 摘要（原文）

> Training large language models (LLMs) requires substantial compute and energy. At the same time, renewable energy sources regularly produce more electricity than the grid can absorb, leading to curtailment, the deliberate reduction of clean generation that would otherwise go to waste. These periods represent an opportunity: if training is aligned with curtailment windows, LLMs can be pretrained using electricity that is both clean and cheap. This technical report presents a system that performs full-parameter LLM training across geo-distributed GPU clusters during regional curtailment windows, elastically switching between local single-site training and federated multi-site synchronization as sites become available or unavailable. Our prototype trains a 561M-parameter transformer model across three clusters using the Flower federated learning framework, with curtailment periods derived from real-world marginal carbon intensity traces. Preliminary results show that curtailment-aware scheduling preserves training quality while reducing operational emissions to 5-12% of single-site baselines.

