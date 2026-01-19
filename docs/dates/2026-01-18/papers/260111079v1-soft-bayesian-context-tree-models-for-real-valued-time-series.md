---
layout: default
title: Soft Bayesian Context Tree Models for Real-Valued Time Series
---

# Soft Bayesian Context Tree Models for Real-Valued Time Series
**arXiv**：[2601.11079v1](https://arxiv.org/abs/2601.11079) · [PDF](https://arxiv.org/pdf/2601.11079.pdf)  
**作者**：Shota Saito, Yuta Nakahara, Toshiyasu Matsushima  

**一句话要点**：提出软贝叶斯上下文树模型以处理实值时间序列，采用概率分割替代确定性分割。

**关键词**：实值时间序列, 贝叶斯上下文树模型, 软分割, 变分推断, 概率模型

## 3 点简述
- 核心问题：传统贝叶斯上下文树模型对实值时间序列使用硬分割，可能限制模型灵活性。
- 方法要点：引入软分割，通过变分推断设计学习算法，实现概率化的上下文空间划分。
- 实验或效果：在真实数据集上，性能与先前模型相当或更优，验证了方法的有效性。

## 摘要（原文）

> This paper proposes the soft Bayesian context tree model (Soft-BCT), which is a novel BCT model for real-valued time series. The Soft-BCT considers soft (probabilistic) splits of the context space, instead of hard (deterministic) splits of the context space as in the previous BCT for real-valued time series. A learning algorithm of the Soft-BCT is proposed based on the variational inference. For some real-world datasets, the Soft-BCT demonstrates almost the same or superior performance to the previous BCT.

