---
layout: default
title: Combating Spurious Correlations in Graph Interpretability via Self-Reflection
---

# Combating Spurious Correlations in Graph Interpretability via Self-Reflection
**arXiv**：[2601.11021v1](https://arxiv.org/abs/2601.11021) · [PDF](https://arxiv.org/pdf/2601.11021.pdf)  
**作者**：Kecheng Cai, Chenyang Xu, Chao Peng  

**一句话要点**：提出自反思框架以提升图可解释性在虚假相关数据集上的性能

**关键词**：图可解释性, 虚假相关, 自反思, 图表示学习, Spurious-Motif基准

## 3 点简述
- 核心问题：图可解释性方法在Spurious-Motif基准上因虚假相关而表现不佳
- 方法要点：集成自反思技术，通过反馈预测进行迭代评估以增强可解释性
- 实验或效果：分析改进原因，提出基于反馈机制的微调训练方法

## 摘要（原文）

> Interpretable graph learning has recently emerged as a popular research topic in machine learning. The goal is to identify the important nodes and edges of an input graph that are crucial for performing a specific graph reasoning task. A number of studies have been conducted in this area, and various benchmark datasets have been proposed to facilitate evaluation. Among them, one of the most challenging is the Spurious-Motif benchmark, introduced at ICLR 2022. The datasets in this synthetic benchmark are deliberately designed to include spurious correlations, making it particularly difficult for models to distinguish truly relevant structures from misleading patterns. As a result, existing methods exhibit significantly worse performance on this benchmark compared to others.
>   In this paper, we focus on improving interpretability on the challenging Spurious-Motif datasets. We demonstrate that the self-reflection technique, commonly used in large language models to tackle complex tasks, can also be effectively adapted to enhance interpretability in datasets with strong spurious correlations. Specifically, we propose a self-reflection framework that can be integrated with existing interpretable graph learning methods. When such a method produces importance scores for each node and edge, our framework feeds these predictions back into the original method to perform a second round of evaluation. This iterative process mirrors how large language models employ self-reflective prompting to reassess their previous outputs. We further analyze the reasons behind this improvement from the perspective of graph representation learning, which motivates us to propose a fine-tuning training method based on this feedback mechanism.

