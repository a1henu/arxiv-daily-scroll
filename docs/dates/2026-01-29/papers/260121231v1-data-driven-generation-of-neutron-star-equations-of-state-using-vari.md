---
layout: default
title: Data-Driven Generation of Neutron Star Equations of State Using Variational Autoencoders
---

# Data-Driven Generation of Neutron Star Equations of State Using Variational Autoencoders
**arXiv**：[2601.21231v1](https://arxiv.org/abs/2601.21231) · [PDF](https://arxiv.org/pdf/2601.21231.pdf)  
**作者**：Alex Ross, Tianqi Zhao, Sanjay Reddy  

**一句话要点**：提出基于变分自编码器的数据驱动方法，生成满足天文约束的中子星状态方程。

**关键词**：变分自编码器, 中子星状态方程, 数据驱动生成, 隐空间建模, 天文约束, 贝叶斯推断

## 3 点简述
- 核心问题：如何从高维数据中重建和生成满足物理约束的中子星状态方程。
- 方法要点：使用结构化变分自编码器，编码器降维至包含监督观测值和潜在变量的隐空间。
- 实验或效果：在Skyrme数据集上训练，隐空间含两个监督观测值和一个潜在变量，重建误差约0.15%。

## 摘要（原文）

> We develop a machine learning model based on a structured variational autoencoder (VAE) framework to reconstruct and generate neutron star (NS) equations of state (EOS). The VAE consists of an encoder network that maps high-dimensional EOS data into a lower-dimensional latent space and a decoder network that reconstructs the full EOS from the latent representation. The latent space includes supervised NS observables derived from the training EOS data, as well as latent random variables corresponding to additional unspecified EOS features learned automatically. Sampling the latent space enables the generation of new, causal, and stable EOS models that satisfy astronomical constraints on the supervised NS observables, while allowing Bayesian inference of the EOS incorporating additional multimessenger data, including gravitational waves from LIGO/Virgo and mass and radius measurements of pulsars. Based on a VAE trained on a Skyrme EOS dataset, we find that a latent space with two supervised NS observables, the maximum mass $(M_{\max})$ and the canonical radius $(R_{1.4})$, together with one latent random variable controlling the EOS near the crust--core transition, can already reconstruct Skyrme EOSs with high fidelity, achieving mean absolute percentage errors of approximately $(0.15\%)$ for $(M_{\max})$ and $(R_{1.4})$ derived from the decoder-reconstructed EOS.

