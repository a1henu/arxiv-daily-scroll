---
layout: default
title: Robust Online Learning
---

# Robust Online Learning
**arXiv**：[2602.06775v1](https://arxiv.org/abs/2602.06775) · [PDF](https://arxiv.org/pdf/2602.06775.pdf)  
**作者**：Sajad Ashkezari  

**一句话要点**：提出新维度以分析在线学习中的鲁棒分类问题，涵盖可实现和不可知设置。

**关键词**：鲁棒在线学习, 对抗性扰动, 维度分析, 可实现学习, 不可知学习, 多类分类

## 3 点简述
- 研究鲁棒分类问题，其中输入被扰动且数据和标签由对手选择。
- 定义新维度控制可实现设置中的错误界和不可知设置中的遗憾界。
- 将维度推广到多类假设类，并研究未知扰动集的情况。

## 摘要（原文）

> We study the problem of learning robust classifiers where the classifier will receive a perturbed input. Unlike robust PAC learning studied in prior work, here the clean data and its label are also adversarially chosen. We formulate this setting as an online learning problem and consider both the realizable and agnostic learnability of hypothesis classes. We define a new dimension of classes and show it controls the mistake bounds in the realizable setting and the regret bounds in the agnostic setting. In contrast to the dimension that characterizes learnability in the PAC setting, our dimension is rather simple and resembles the Littlestone dimension. We generalize our dimension to multiclass hypothesis classes and prove similar results in the realizable case. Finally, we study the case where the learner does not know the set of allowed perturbations for each point and only has some prior on them.

