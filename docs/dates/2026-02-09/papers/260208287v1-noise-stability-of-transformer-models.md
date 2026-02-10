---
layout: default
title: Noise Stability of Transformer Models
---

# Noise Stability of Transformer Models
**arXiv**：[2602.08287v1](https://arxiv.org/abs/2602.08287) · [PDF](https://arxiv.org/pdf/2602.08287.pdf)  
**作者**：Themistoklis Haris, Zihan Zhang, Yuichi Yoshida  

**一句话要点**：提出噪声稳定性作为Transformer模型的简洁性度量，以解决平均敏感度的局限性并加速训练。

**关键词**：噪声稳定性, Transformer模型, 简洁性度量, 正则化方法, 训练加速, 信号传播

## 3 点简述
- 核心问题：平均敏感度在实值域泛化不足，无法解释现代LLM中的'类junta'输入依赖性。
- 方法要点：引入噪声稳定性度量，理论分析单层注意力与ReLU MLP，采用协方差区间传播处理多层问题。
- 实验或效果：在算法和下一个词预测任务中，噪声稳定性正则化催化grokking，训练加速约35%和75%。

## 摘要（原文）

> Understanding simplicity biases in deep learning offers a promising path toward developing reliable AI. A common metric for this, inspired by Boolean function analysis, is average sensitivity, which captures a model's robustness to single-token perturbations. We argue that average sensitivity has two key limitations: it lacks a natural generalization to real-valued domains and fails to explain the "junta-like" input dependence we empirically observe in modern LLMs. To address these limitations, we propose noise stability as a more comprehensive simplicity metric. Noise stability expresses a model's robustness to correlated noise applied to all input coordinates simultaneously. We provide a theoretical analysis of noise stability for single-layer attention and ReLU MLP layers and tackle the multi-layer propagation problem with a covariance interval propagation approach. Building on this theory, we develop a practical noise stability regularization method. Experiments on algorithmic and next-token-prediction tasks show that our regularizer consistently catalyzes grokking and accelerates training by approximately $35\%$ and $75\%$ respectively. Our results sculpt a new connection between signal propagation in neural networks and interpretability, with noise stability emerging as a powerful tool for understanding and improving modern Transformers.

