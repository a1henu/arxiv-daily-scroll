---
layout: default
title: SVRG and Beyond via Posterior Correction
---

# SVRG and Beyond via Posterior Correction
**arXiv**：[2512.01930v1](https://arxiv.org/abs/2512.01930) · [PDF](https://arxiv.org/pdf/2512.01930.pdf)  
**作者**：Nico Daheim, Thomas Möllenhoff, Ming Liang Ang, Mohammad Emtiyaz Khan  

**一句话要点**：通过后验校正连接SVRG与贝叶斯方法，提出新变体以提升深度网络训练

**关键词**：随机梯度下降, 贝叶斯方法, 变分训练, 深度网络优化, 后验校正, Transformer模型

## 3 点简述
- 揭示SVRG与后验校正的贝叶斯联系，将其视为各向同性高斯族的特例
- 基于高斯族推导牛顿式和Adam式SVRG变体，引入Hessian校正
- 新变体在Transformer语言模型的预训练和微调中表现提升

## 摘要（原文）

> Stochastic Variance Reduced Gradient (SVRG) and its variants aim to speed-up training by using gradient corrections, but have seen limited success in deep learning. Here, we show surprising new foundational connections of SVRG to a recently proposed Bayesian method called posterior correction. Specifically, we show that SVRG is recovered as a special case of posterior correction over the isotropic-Gaussian family, while novel extensions are automatically obtained by using more flexible exponential families. We derive two new SVRG variants by using Gaussian families: First, a Newton-like variant that employs novel Hessian corrections, and second, an Adam-like extension that improves pretraining and finetuning of Transformer language models. This is the first work to connect SVRG to Bayes and use it to boost variational training for deep networks.

