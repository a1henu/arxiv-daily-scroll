---
layout: default
title: Large-scale Score-based Variational Posterior Inference for Bayesian Deep Neural Networks
---

# Large-scale Score-based Variational Posterior Inference for Bayesian Deep Neural Networks
**arXiv**：[2602.05873v1](https://arxiv.org/abs/2602.05873) · [PDF](https://arxiv.org/pdf/2602.05873.pdf)  
**作者**：Minyoung Kim  

**一句话要点**：提出基于分数匹配的可扩展变分推理方法，用于大规模贝叶斯深度神经网络

**关键词**：贝叶斯神经网络, 变分推理, 分数匹配, 大规模深度学习, 不确定性量化, 视觉识别

## 3 点简述
- 核心问题：现有分数匹配变分推理方法难以扩展至大规模贝叶斯神经网络，受计算和技术限制
- 方法要点：结合分数匹配损失和近端惩罚项，避免重参数化采样，支持随机梯度无偏估计
- 实验或效果：在视觉识别和时间序列预测基准测试中，验证方法对大规模网络如Vision Transformers的有效性

## 摘要（原文）

> Bayesian (deep) neural networks (BNN) are often more attractive than the mainstream point-estimate vanilla deep learning in various aspects including uncertainty quantification, robustness to noise, resistance to overfitting, and more. The variational inference (VI) is one of the most widely adopted approximate inference methods. Whereas the ELBO-based variational free energy method is a dominant choice in the literature, in this paper we introduce a score-based alternative for BNN variational inference. Although there have been quite a few score-based variational inference methods proposed in the community, most are not adequate for large-scale BNNs for various computational and technical reasons. We propose a novel scalable VI method where the learning objective combines the score matching loss and the proximal penalty term in iterations, which helps our method avoid the reparametrized sampling, and allows for noisy unbiased mini-batch scores through stochastic gradients. This in turn makes our method scalable to large-scale neural networks including Vision Transformers, and allows for richer variational density families. On several benchmarks including visual recognition and time-series forecasting with large-scale deep networks, we empirically show the effectiveness of our approach.

