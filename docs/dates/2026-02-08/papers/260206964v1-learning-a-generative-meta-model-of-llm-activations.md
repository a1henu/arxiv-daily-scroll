---
layout: default
title: Learning a Generative Meta-Model of LLM Activations
---

# Learning a Generative Meta-Model of LLM Activations
**arXiv**：[2602.06964v1](https://arxiv.org/abs/2602.06964) · [PDF](https://arxiv.org/pdf/2602.06964.pdf)  
**作者**：Grace Luo, Jiahai Feng, Trevor Darrell, Alec Radford, Jacob Steinhardt  

**一句话要点**：提出基于扩散模型的生成元模型，以学习LLM激活分布并提升可解释性

**关键词**：生成模型, 扩散模型, 神经网络激活分析, 可解释性, 元模型, 先验学习

## 3 点简述
- 现有神经网络激活分析方法依赖强结构假设，如PCA和稀疏自编码器
- 训练扩散模型于十亿残差流激活，学习内部状态分布作为先验改善干预保真度
- 扩散损失随计算平滑下降，预测下游效用，提升流畅性并稀疏化概念单元

## 摘要（原文）

> Existing approaches for analyzing neural network activations, such as PCA and sparse autoencoders, rely on strong structural assumptions. Generative models offer an alternative: they can uncover structure without such assumptions and act as priors that improve intervention fidelity. We explore this direction by training diffusion models on one billion residual stream activations, creating "meta-models" that learn the distribution of a network's internal states. We find that diffusion loss decreases smoothly with compute and reliably predicts downstream utility. In particular, applying the meta-model's learned prior to steering interventions improves fluency, with larger gains as loss decreases. Moreover, the meta-model's neurons increasingly isolate concepts into individual units, with sparse probing scores that scale as loss decreases. These results suggest generative meta-models offer a scalable path toward interpretability without restrictive structural assumptions. Project page: https://generative-latent-prior.github.io.

