---
layout: default
title: Amortising Inference and Meta-Learning Priors in Neural Networks
---

# Amortising Inference and Meta-Learning Priors in Neural Networks
**arXiv**：[2602.08782v1](https://arxiv.org/abs/2602.08782) · [PDF](https://arxiv.org/pdf/2602.08782.pdf)  
**作者**：Tommy Rochussen, Vincent Fortuin  

**一句话要点**：提出基于神经过程的权重先验学习方法，以解决贝叶斯深度学习中的先验缺失问题。

**关键词**：贝叶斯深度学习, 神经过程, 摊销变分推断, 权重先验学习, 元学习

## 3 点简述
- 核心问题：贝叶斯深度学习中缺乏先验信念，难以表示任务信念。
- 方法要点：通过数据集集合学习权重先验，实现每数据集摊销变分推断。
- 实验或效果：支持在指定先验下研究贝叶斯神经网络行为，并作为生成模型使用。

## 摘要（原文）

> One of the core facets of Bayesianism is in the updating of prior beliefs in light of new evidence$\text{ -- }$so how can we maintain a Bayesian approach if we have no prior beliefs in the first place? This is one of the central challenges in the field of Bayesian deep learning, where it is not clear how to represent beliefs about a prediction task by prior distributions over model parameters. Bridging the fields of Bayesian deep learning and probabilistic meta-learning, we introduce a way to $\textit{learn}$ a weights prior from a collection of datasets by introducing a way to perform per-dataset amortised variational inference. The model we develop can be viewed as a neural process whose latent variable is the set of weights of a BNN and whose decoder is the neural network parameterised by a sample of the latent variable itself. This unique model allows us to study the behaviour of Bayesian neural networks under well-specified priors, use Bayesian neural networks as flexible generative models, and perform desirable but previously elusive feats in neural processes such as within-task minibatching or meta-learning under extreme data-starvation.

