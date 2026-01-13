---
layout: default
title: Variational Autoencoder with Normalizing flow for X-ray spectral fitting
---

# Variational Autoencoder with Normalizing flow for X-ray spectral fitting
**arXiv**：[2601.07440v1](https://arxiv.org/abs/2601.07440) · [PDF](https://arxiv.org/pdf/2601.07440.pdf)  
**作者**：Fiona Redmen, Ethan Tregidga, James F. Steiner, Cecilia Garraffo  

**一句话要点**：提出变分自编码器结合归一化流，用于黑洞X射线双星光谱拟合，以加速物理参数预测。

**关键词**：黑洞X射线双星, 光谱拟合, 变分自编码器, 归一化流, 概率模型, 计算加速

## 3 点简述
- 核心问题：传统MCMC方法在黑洞X射线双星光谱拟合中计算耗时，限制物理约束获取。
- 方法要点：使用变分自编码器与归一化流构建概率模型，训练物理潜在空间以预测参数及其分布。
- 实验或效果：相比先前确定性模型，光谱重建显著改进，计算速度比传统方法快三个数量级。

## 摘要（原文）

> Black hole X-ray binaries (BHBs) can be studied with spectral fitting to provide physical constraints on accretion in extreme gravitational environments. Traditional methods of spectral fitting such as Markov Chain Monte Carlo (MCMC) face limitations due to computational times. We introduce a probabilistic model, utilizing a variational autoencoder with a normalizing flow, trained to adopt a physical latent space. This neural network produces predictions for spectral-model parameters as well as their full probability distributions. Our implementations result in a significant improvement in spectral reconstructions over a previous deterministic model while performing three orders of magnitude faster than traditional methods.

