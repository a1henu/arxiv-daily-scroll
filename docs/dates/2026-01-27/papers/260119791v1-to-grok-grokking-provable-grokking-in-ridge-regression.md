---
layout: default
title: To Grok Grokking: Provable Grokking in Ridge Regression
---

# To Grok Grokking: Provable Grokking in Ridge Regression
**arXiv**：[2601.19791v1](https://arxiv.org/abs/2601.19791) · [PDF](https://arxiv.org/pdf/2601.19791.pdf)  
**作者**：Mingyue Xu, Gal Vardi, Itay Safran  

**一句话要点**：在岭回归中证明梯度下降导致grokking现象，并量化其延迟时间。

**关键词**：grokking现象, 岭回归, 梯度下降, 泛化延迟, 超参数调优, 非线性神经网络

## 3 点简述
- 研究grokking现象，即过拟合后延迟泛化的发生。
- 理论证明岭回归中梯度下降导致过拟合、延迟泛化和最终泛化。
- 实验验证超参数可调控grokking，且结果适用于非线性网络。

## 摘要（原文）

> We study grokking, the onset of generalization long after overfitting, in a classical ridge regression setting. We prove end-to-end grokking results for learning over-parameterized linear regression models using gradient descent with weight decay. Specifically, we prove that the following stages occur: (i) the model overfits the training data early during training; (ii) poor generalization persists long after overfitting has manifested; and (iii) the generalization error eventually becomes arbitrarily small. Moreover, we show, both theoretically and empirically, that grokking can be amplified or eliminated in a principled manner through proper hyperparameter tuning. To the best of our knowledge, these are the first rigorous quantitative bounds on the generalization delay (which we refer to as the "grokking time") in terms of training hyperparameters. Lastly, going beyond the linear setting, we empirically demonstrate that our quantitative bounds also capture the behavior of grokking on non-linear neural networks. Our results suggest that grokking is not an inherent failure mode of deep learning, but rather a consequence of specific training conditions, and thus does not require fundamental changes to the model architecture or learning algorithm to avoid.

