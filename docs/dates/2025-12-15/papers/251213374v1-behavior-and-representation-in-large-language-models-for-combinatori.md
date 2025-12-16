---
layout: default
title: Behavior and Representation in Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection
---

# Behavior and Representation in Large Language Models for Combinatorial Optimization: From Feature Extraction to Algorithm Selection
**arXiv**：[2512.13374v1](https://arxiv.org/abs/2512.13374) · [PDF](https://arxiv.org/pdf/2512.13374.pdf)  
**作者**：Francesca Da Ros, Luca Di Gaspero, Kevin Roitero  

**一句话要点**：探究大语言模型在组合优化中的内部表示与算法选择能力

**关键词**：大语言模型, 组合优化, 特征提取, 算法选择, 隐藏层表示, 探测分析

## 3 点简述
- 核心问题：大语言模型如何内部表示组合优化问题结构及其对算法性能的预测能力
- 方法要点：结合直接查询与探测分析，评估特征提取和隐藏层表示
- 实验或效果：在四个基准问题上，LLM表示与传统特征提取预测能力相当

## 摘要（原文）

> Recent advances in Large Language Models (LLMs) have opened new perspectives for automation in optimization. While several studies have explored how LLMs can generate or solve optimization models, far less is understood about what these models actually learn regarding problem structure or algorithmic behavior. This study investigates how LLMs internally represent combinatorial optimization problems and whether such representations can support downstream decision tasks. We adopt a twofold methodology combining direct querying, which assesses LLM capacity to explicitly extract instance features, with probing analyses that examine whether such information is implicitly encoded within their hidden layers. The probing framework is further extended to a per-instance algorithm selection task, evaluating whether LLM-derived representations can predict the best-performing solver. Experiments span four benchmark problems and three instance representations. Results show that LLMs exhibit moderate ability to recover feature information from problem instances, either through direct querying or probing. Notably, the predictive power of LLM hidden-layer representations proves comparable to that achieved through traditional feature extraction, suggesting that LLMs capture meaningful structural information relevant to optimization performance.

