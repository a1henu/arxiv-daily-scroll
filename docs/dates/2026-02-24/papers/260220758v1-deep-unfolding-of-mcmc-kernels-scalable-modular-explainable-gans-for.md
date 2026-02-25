---
layout: default
title: Deep unfolding of MCMC kernels: scalable, modular & explainable GANs for high-dimensional posterior sampling
---

# Deep unfolding of MCMC kernels: scalable, modular & explainable GANs for high-dimensional posterior sampling
**arXiv**：[2602.20758v1](https://arxiv.org/abs/2602.20758) · [PDF](https://arxiv.org/pdf/2602.20758.pdf)  
**作者**：Jonathan Spence, Tobías I. Liaudat, Konstantinos Zygalakis, Marcelo Pereyra  

**一句话要点**：提出基于深度展开MCMC核的GAN架构，用于高维后验采样，提升计算效率与可解释性。

**关键词**：深度展开, MCMC采样, 生成对抗网络, 后验采样, 贝叶斯计算, 可解释AI

## 3 点简述
- 核心问题：传统MCMC方法在高维后验采样中计算成本高，而推前生成模型缺乏模块化，泛化能力差。
- 方法要点：通过深度展开Langevin MCMC算法，构建模块化神经网络架构，支持推理时指定关键参数。
- 实验或效果：在贝叶斯成像实验中，实现高采样精度、计算效率，并保持物理一致性和可解释性。

## 摘要（原文）

> Markov chain Monte Carlo (MCMC) methods are fundamental to Bayesian computation, but can be computationally intensive, especially in high-dimensional settings. Push-forward generative models, such as generative adversarial networks (GANs), variational auto-encoders and normalising flows offer a computationally efficient alternative for posterior sampling. However, push-forward models are opaque as they lack the modularity of Bayes Theorem, leading to poor generalisation with respect to changes in the likelihood function. In this work, we introduce a novel approach to GAN architecture design by applying deep unfolding to Langevin MCMC algorithms. This paradigm maps fixed-step iterative algorithms onto modular neural networks, yielding architectures that are both flexible and amenable to interpretation. Crucially, our design allows key model parameters to be specified at inference time, offering robustness to changes in the likelihood parameters. We train these unfolded samplers end-to-end using a supervised regularized Wasserstein GAN framework for posterior sampling. Through extensive Bayesian imaging experiments, we demonstrate that our proposed approach achieves high sampling accuracy and excellent computational efficiency, while retaining the physics consistency, adaptability and interpretability of classical MCMC strategies.

