---
layout: default
title: Many Experiments, Few Repetitions, Unpaired Data, and Sparse Effects: Is Causal Inference Possible?
---

# Many Experiments, Few Repetitions, Unpaired Data, and Sparse Effects: Is Causal Inference Possible?
**arXiv**：[2601.15254v1](https://arxiv.org/abs/2601.15254) · [PDF](https://arxiv.org/pdf/2601.15254.pdf)  
**作者**：Felix Schur, Niklas Pfister, Peng Ding, Sach Mukherjee, Jonas Peters  

**一句话要点**：提出基于交叉折叠样本分割的GMM型估计器，以解决未配对数据下隐藏混淆的因果效应估计问题。

**关键词**：因果推断, 工具变量回归, 未配对数据, 隐藏混淆, GMM估计, 稀疏效应

## 3 点简述
- 研究未配对数据下隐藏混淆的因果效应估计问题，环境作为高维工具变量。
- 提出GMM型估计器，通过工具变量-协变量样本的交叉折叠分割实现一致性估计。
- 扩展方法至稀疏因果效应，采用ℓ1正则化估计和后选择重拟合。

## 摘要（原文）

> We study the problem of estimating causal effects under hidden confounding in the following unpaired data setting: we observe some covariates $X$ and an outcome $Y$ under different experimental conditions (environments) but do not observe them jointly; we either observe $X$ or $Y$. Under appropriate regularity conditions, the problem can be cast as an instrumental variable (IV) regression with the environment acting as a (possibly high-dimensional) instrument. When there are many environments but only a few observations per environment, standard two-sample IV estimators fail to be consistent. We propose a GMM-type estimator based on cross-fold sample splitting of the instrument-covariate sample and prove that it is consistent as the number of environments grows but the sample size per environment remains constant. We further extend the method to sparse causal effects via $\ell_1$-regularized estimation and post-selection refitting.

