---
layout: default
title: SafeMo: Linguistically Grounded Unlearning for Trustworthy Text-to-Motion Generation
---

# SafeMo: Linguistically Grounded Unlearning for Trustworthy Text-to-Motion Generation
**arXiv**：[2601.00590v1](https://arxiv.org/abs/2601.00590) · [PDF](https://arxiv.org/pdf/2601.00590.pdf)  
**作者**：Yiling Wang, Zeyu Zhang, Yiran Wang, Hao Tang  

**一句话要点**：提出SafeMo框架，通过最小化运动遗忘策略解决文本到运动生成中的安全问题。

**关键词**：文本到运动生成, 机器遗忘, 安全生成, 连续运动空间, 运动数据集

## 3 点简述
- 现有基于离散码本替换的方法导致良性任务性能下降和运动伪影。
- SafeMo采用两阶段机器遗忘策略，在连续空间生成安全运动，避免量化损失。
- 实验显示SafeMo在遗忘不安全提示上表现优异，同时保持或提升安全提示的性能。

## 摘要（原文）

> Text-to-motion (T2M) generation with diffusion backbones achieves strong realism and alignment. Safety concerns in T2M methods have been raised in recent years; existing methods replace discrete VQ-VAE codebook entries to steer the model away from unsafe behaviors. However, discrete codebook replacement-based methods have two critical flaws: firstly, replacing codebook entries which are reused by benign prompts leads to drifts on everyday tasks, degrading the model's benign performance; secondly, discrete token-based methods introduce quantization and smoothness loss, resulting in artifacts and jerky transitions. Moreover, existing text-to-motion datasets naturally contain unsafe intents and corresponding motions, making them unsuitable for safety-driven machine learning. To address these challenges, we propose SafeMo, a trustworthy motion generative framework integrating Minimal Motion Unlearning (MMU), a two-stage machine unlearning strategy, enabling safe human motion generation in continuous space, preserving continuous kinematics without codebook loss and delivering strong safety-utility trade-offs compared to current baselines. Additionally, we present the first safe text-to-motion dataset SafeMoVAE-29K integrating rewritten safe text prompts and continuous refined motion for trustworthy human motion unlearning. Built upon DiP, SafeMo efficiently generates safe human motions with natural transitions. Experiments demonstrate effective unlearning performance of SafeMo by showing strengthened forgetting on unsafe prompts, reaching 2.5x and 14.4x higher forget-set FID on HumanML3D and Motion-X respectively, compared to the previous SOTA human motion unlearning method LCR, with benign performance on safe prompts being better or comparable. Code: https://github.com/AIGeeksGroup/SafeMo. Website: https://aigeeksgroup.github.io/SafeMo.

