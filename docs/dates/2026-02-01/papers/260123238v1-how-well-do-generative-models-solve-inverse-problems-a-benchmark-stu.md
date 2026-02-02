---
layout: default
title: How well do generative models solve inverse problems? A benchmark study
---

# How well do generative models solve inverse problems? A benchmark study
**arXiv**：[2601.23238v1](https://arxiv.org/abs/2601.23238) · [PDF](https://arxiv.org/pdf/2601.23238.pdf)  
**作者**：Patrick Krüger, Patrick Materne, Werner Krebs, Hanno Gottschalk  

**一句话要点**：比较生成模型在燃气轮机燃烧室设计逆问题中的性能，条件流匹配表现最佳

**关键词**：生成模型, 逆问题求解, 条件流匹配, 贝叶斯方法, 燃气轮机设计, 基准测试

## 3 点简述
- 核心问题：评估生成模型在解决贝叶斯逆问题中的有效性，应用于燃气轮机燃烧室设计
- 方法要点：比较传统贝叶斯方法与三种生成模型，提出评估指标衡量准确性和多样性
- 实验或效果：条件流匹配在基准测试中一致优于其他方法，性能随训练数据集大小变化

## 摘要（原文）

> Generative learning generates high dimensional data based on low dimensional conditions, also called prompts. Therefore, generative learning algorithms are eligible for solving (Bayesian) inverse problems. In this article we compare a traditional Bayesian inverse approach based on a forward regression model and a prior sampled with the Markov Chain Monte Carlo method with three state of the art generative learning models, namely conditional Generative Adversarial Networks, Invertible Neural Networks and Conditional Flow Matching. We apply them to a problem of gas turbine combustor design where we map six independent design parameters to three performance labels. We propose several metrics for the evaluation of this inverse design approaches and measure the accuracy of the labels of the generated designs along with the diversity. We also study the performance as a function of the training dataset size. Our benchmark has a clear winner, as Conditional Flow Matching consistently outperforms all competing approaches.

