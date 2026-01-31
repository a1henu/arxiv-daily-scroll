---
layout: default
title: XFACTORS: Disentangled Information Bottleneck via Contrastive Supervision
---

# XFACTORS: Disentangled Information Bottleneck via Contrastive Supervision
**arXiv**：[2601.21688v1](https://arxiv.org/abs/2601.21688) · [PDF](https://arxiv.org/pdf/2601.21688.pdf)  
**作者**：Alexandre Myara, Nicolas Bourriez, Thomas Boyer, Thomas Lemercier, Ihab Bendidi, Auguste Genovesio  

**一句话要点**：提出XFACTORS框架，通过对比监督实现弱监督解耦表示学习，以控制选定因素。

**关键词**：解耦表示学习, 弱监督学习, 信息瓶颈, 对比学习, 变分自编码器, 潜在空间控制

## 3 点简述
- 核心问题：无监督方法在真实数据上难以解耦语义因素，监督方法不稳定且难以扩展。
- 方法要点：基于解耦信息瓶颈，将表示分解为残差和因子特定子空间，使用InfoNCE损失进行对比监督。
- 实验或效果：在多个数据集上达到最优解耦分数，在CelebA上验证可扩展性，支持潜在替换控制因素。

## 摘要（原文）

> Disentangled representation learning aims to map independent factors of variation to independent representation components. On one hand, purely unsupervised approaches have proven successful on fully disentangled synthetic data, but fail to recover semantic factors from real data without strong inductive biases. On the other hand, supervised approaches are unstable and hard to scale to large attribute sets because they rely on adversarial objectives or auxiliary classifiers.
>   We introduce \textsc{XFactors}, a weakly-supervised VAE framework that disentangles and provides explicit control over a chosen set of factors. Building on the Disentangled Information Bottleneck perspective, we decompose the representation into a residual subspace $\mathcal{S}$ and factor-specific subspaces $\mathcal{T}_1,\ldots,\mathcal{T}_K$ and a residual subspace $\mathcal{S}$. Each target factor is encoded in its assigned $\mathcal{T}_i$ through contrastive supervision: an InfoNCE loss pulls together latents sharing the same factor value and pushes apart mismatched pairs. In parallel, KL regularization imposes a Gaussian structure on both $\mathcal{S}$ and the aggregated factor subspaces, organizing the geometry without additional supervision for non-targeted factors and avoiding adversarial training and classifiers.
>   Across multiple datasets, with constant hyperparameters, \textsc{XFactors} achieves state-of-the-art disentanglement scores and yields consistent qualitative factor alignment in the corresponding subspaces, enabling controlled factor swapping via latent replacement. We further demonstrate that our method scales correctly with increasing latent capacity and evaluate it on the real-world dataset CelebA. Our code is available at \href{https://github.com/ICML26-anon/XFactors}{github.com/ICML26-anon/XFactors}.

