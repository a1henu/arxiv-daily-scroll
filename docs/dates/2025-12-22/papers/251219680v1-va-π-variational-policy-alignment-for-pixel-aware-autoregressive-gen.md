---
layout: default
title: VA-$π$: Variational Policy Alignment for Pixel-Aware Autoregressive Generation
---

# VA-$π$: Variational Policy Alignment for Pixel-Aware Autoregressive Generation
**arXiv**：[2512.19680v1](https://arxiv.org/abs/2512.19680) · [PDF](https://arxiv.org/pdf/2512.19680.pdf)  
**作者**：Xinyao Liao, Qiyuan He, Kai Xu, Xiaoye Qu, Yicong Li, Wei Wei, Angela Yao  

**一句话要点**：提出VA-π框架以解决自回归视觉生成中tokenizer与生成器不对齐导致图像质量下降的问题

**关键词**：自回归视觉生成, 变分优化, 像素对齐, 强化学习对齐, 图像质量提升, 轻量级微调

## 3 点简述
- 核心问题：自回归视觉生成中tokenizer训练目标与生成器优化目标不一致，导致生成token序列解码为低质量图像
- 方法要点：通过变分优化将生成器-tokenizer对齐，引入基于强化学习的对齐策略，以像素重建质量作为内在奖励
- 实验或效果：在ImageNet-1K上仅用1%数据和25分钟微调，显著降低FID并提高IS，在文本到图像任务中也获得提升

## 摘要（原文）

> Autoregressive (AR) visual generation relies on tokenizers to map images to and from discrete sequences. However, tokenizers are trained to reconstruct clean images from ground-truth tokens, while AR generators are optimized only for token likelihood. This misalignment leads to generated token sequences that may decode into low-quality images, without direct supervision from the pixel space. We propose VA-$π$, a lightweight post-training framework that directly optimizes AR models with a principled pixel-space objective. VA-$π$ formulates the generator-tokenizer alignment as a variational optimization, deriving an evidence lower bound (ELBO) that unifies pixel reconstruction and autoregressive modeling. To optimize under the discrete token space, VA-$π$ introduces a reinforcement-based alignment strategy that treats the AR generator as a policy, uses pixel-space reconstruction quality as its intrinsic reward. The reward is measured by how well the predicted token sequences can reconstruct the original image under teacher forcing, giving the model direct pixel-level guidance without expensive free-running sampling. The regularization term of the ELBO serves as a natural regularizer, maintaining distributional consistency of tokens. VA-$π$ enables rapid adaptation of existing AR generators, without neither tokenizer retraining nor external reward models. With only 1% ImageNet-1K data and 25 minutes of tuning, it reduces FID from 14.36 to 7.65 and improves IS from 86.55 to 116.70 on LlamaGen-XXL, while also yielding notable gains in the text-to-image task on GenEval for both visual generation model (LlamaGen: from 0.306 to 0.339) and unified multi-modal model (Janus-Pro: from 0.725 to 0.744). Code is available at https://github.com/Lil-Shake/VA-Pi.

