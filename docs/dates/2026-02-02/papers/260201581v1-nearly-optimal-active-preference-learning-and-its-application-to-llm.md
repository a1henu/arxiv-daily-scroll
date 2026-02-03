---
layout: default
title: Nearly Optimal Active Preference Learning and Its Application to LLM Alignment
---

# Nearly Optimal Active Preference Learning and Its Application to LLM Alignment
**arXiv**：[2602.01581v1](https://arxiv.org/abs/2602.01581) · [PDF](https://arxiv.org/pdf/2602.01581.pdf)  
**作者**：Yao Zhao, Kwang-Sung Jun  

**一句话要点**：提出两种主动学习算法以提升大语言模型对齐中的偏好学习样本效率

**关键词**：主动学习, 偏好学习, 大语言模型对齐, 样本效率, 实验设计

## 3 点简述
- 核心问题：现有主动学习方法未针对偏好学习结构优化，样本效率低
- 方法要点：基于偏好学习特定直觉，设计理论保证算法和实用贪婪方法
- 实验或效果：在真实偏好数据集上验证，相比现有方法样本效率提升

## 摘要（原文）

> Aligning large language models (LLMs) depends on high-quality datasets of human preference labels, which are costly to collect. Although active learning has been studied to improve sample efficiency relative to passive collection, many existing approaches adopt classical experimental design criteria such as G- or D-optimality. These objectives are not tailored to the structure of preference learning, leaving open the design of problem-specific algorithms. In this work, we identify a simple intuition specific to preference learning that calls into question the suitability of these existing design objectives. Motivated by this insight, we propose two active learning algorithms. The first provides the first instance-dependent label complexity guarantee for this setting, and the second is a simple, practical greedy method. We evaluate our algorithm on real-world preference datasets and observe improved sample efficiency compared to existing methods.

