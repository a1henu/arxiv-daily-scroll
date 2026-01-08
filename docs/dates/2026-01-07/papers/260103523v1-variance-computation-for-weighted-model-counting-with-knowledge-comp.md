---
layout: default
title: Variance Computation for Weighted Model Counting with Knowledge Compilation Approach
---

# Variance Computation for Weighted Model Counting with Knowledge Compilation Approach
**arXiv**：[2601.03523v1](https://arxiv.org/abs/2601.03523) · [PDF](https://arxiv.org/pdf/2601.03523.pdf)  
**作者**：Kengo Nakamura, Masaaki Nishino, Norihito Yasuda  

**一句话要点**：提出基于知识编译的加权模型计数方差计算算法，用于评估贝叶斯网络推理的不确定性。

**关键词**：加权模型计数, 知识编译, 方差计算, 贝叶斯网络, 不确定性评估, 结构化d-DNNF

## 3 点简述
- 核心问题：加权模型计数（WMC）的方差计算在参数不确定性下的可处理性未知。
- 方法要点：针对结构化d-DNNF输入，设计多项式时间算法计算WMC方差。
- 实验或效果：在真实贝叶斯网络上评估边际概率方差，分析参数方差影响。

## 摘要（原文）

> One of the most important queries in knowledge compilation is weighted model counting (WMC), which has been applied to probabilistic inference on various models, such as Bayesian networks. In practical situations on inference tasks, the model's parameters have uncertainty because they are often learned from data, and thus we want to compute the degree of uncertainty in the inference outcome. One possible approach is to regard the inference outcome as a random variable by introducing distributions for the parameters and evaluate the variance of the outcome. Unfortunately, the tractability of computing such a variance is hardly known. Motivated by this, we consider the problem of computing the variance of WMC and investigate this problem's tractability. First, we derive a polynomial time algorithm to evaluate the WMC variance when the input is given as a structured d-DNNF. Second, we prove the hardness of this problem for structured DNNFs, d-DNNFs, and FBDDs, which is intriguing because the latter two allow polynomial time WMC algorithms. Finally, we show an application that measures the uncertainty in the inference of Bayesian networks. We empirically show that our algorithm can evaluate the variance of the marginal probability on real-world Bayesian networks and analyze the impact of the variances of parameters on the variance of the marginal.

