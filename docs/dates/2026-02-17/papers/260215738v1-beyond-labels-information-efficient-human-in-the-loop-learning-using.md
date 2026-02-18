---
layout: default
title: Beyond Labels: Information-Efficient Human-in-the-Loop Learning using Ranking and Selection Queries
---

# Beyond Labels: Information-Efficient Human-in-the-Loop Learning using Ranking and Selection Queries
**arXiv**：[2602.15738v1](https://arxiv.org/abs/2602.15738) · [PDF](https://arxiv.org/pdf/2602.15738.pdf)  
**作者**：Belén Martín-Urcelay, Yoonsang Lee, Matthieu R. Bloch, Christopher J. Rozell  

**一句话要点**：提出基于排序与选择查询的人机协同学习框架，以提升信息效率并减少样本复杂度。

**关键词**：人机协同学习, 主动学习, 排序查询, 选择查询, 样本复杂度, 信息效率

## 3 点简述
- 核心问题：传统人机协同学习将专家简化为标注工具，信息交换有限，无法捕捉人类判断的细微差别。
- 方法要点：设计概率人类响应模型，结合排序和选择查询，开发主动学习算法以最大化每次交互的信息增益。
- 实验或效果：在模拟标注者实验中，样本复杂度显著降低，情感分类任务学习时间减少超过57%。

## 摘要（原文）

> Integrating human expertise into machine learning systems often reduces the role of experts to labeling oracles, a paradigm that limits the amount of information exchanged and fails to capture the nuances of human judgment. We address this challenge by developing a human-in-the-loop framework to learn binary classifiers with rich query types, consisting of item ranking and exemplar selection. We first introduce probabilistic human response models for these rich queries motivated by the relationship experimentally observed between the perceived implicit score of an item and its distance to the unknown classifier. Using these models, we then design active learning algorithms that leverage the rich queries to increase the information gained per interaction. We provide theoretical bounds on sample complexity and develop a tractable and computationally efficient variational approximation. Through experiments with simulated annotators derived from crowdsourced word-sentiment and image-aesthetic datasets, we demonstrate significant reductions on sample complexity. We further extend active learning strategies to select queries that maximize information rate, explicitly balancing informational value against annotation cost. This algorithm in the word sentiment classification task reduces learning time by more than 57\% compared to traditional label-only active learning.

