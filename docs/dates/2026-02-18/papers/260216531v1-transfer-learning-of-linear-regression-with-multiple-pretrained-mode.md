---
layout: default
title: Transfer Learning of Linear Regression with Multiple Pretrained Models: Benefiting from More Pretrained Models via Overparameterization Debiasing
---

# Transfer Learning of Linear Regression with Multiple Pretrained Models: Benefiting from More Pretrained Models via Overparameterization Debiasing
**arXiv**：[2602.16531v1](https://arxiv.org/abs/2602.16531) · [PDF](https://arxiv.org/pdf/2602.16531.pdf)  
**作者**：Daniel Boharon, Yehuda Dar  

**一句话要点**：提出过参数化去偏方法，利用多个预训练模型提升线性回归迁移学习效果。

**关键词**：迁移学习, 线性回归, 过参数化, 去偏方法, 预训练模型, 最小二乘

## 3 点简述
- 研究多个过参数化最小二乘预训练模型在线性回归任务中的迁移学习。
- 通过惩罚学习模型与预训练模型距离的优化框架，分析测试误差并提出去偏校正因子。
- 实验验证更多预训练模型在过参数化下能改善学习，去偏方法可减少偏差并提升预测性能。

## 摘要（原文）

> We study transfer learning for a linear regression task using several least-squares pretrained models that can be overparameterized.
>   We formulate the target learning task as optimization that minimizes squared errors on the target dataset with penalty on the distance of the learned model from the pretrained models. We analytically formulate the test error of the learned target model and provide the corresponding empirical evaluations.
>   Our results elucidate when using more pretrained models can improve transfer learning. Specifically, if the pretrained models are overparameterized, using sufficiently many of them is important for beneficial transfer learning. However, the learning may be compromised by overparameterization bias of pretrained models, i.e., the minimum $\ell_2$-norm solution's restriction to a small subspace spanned by the training examples in the high-dimensional parameter space. We propose a simple debiasing via multiplicative correction factor that can reduce the overparameterization bias and leverage more pretrained models to learn a target predictor.

