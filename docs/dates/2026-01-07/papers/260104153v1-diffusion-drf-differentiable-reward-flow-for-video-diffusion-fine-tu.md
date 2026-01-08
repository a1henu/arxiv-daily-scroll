---
layout: default
title: Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning
---

# Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning
**arXiv**：[2601.04153v1](https://arxiv.org/abs/2601.04153) · [PDF](https://arxiv.org/pdf/2601.04153.pdf)  
**作者**：Yifan Wang, Yanyu Li, Sergey Tulyakov, Yun Fu, Anil Kag  

**一句话要点**：提出Diffusion-DRF，通过可微分奖励流优化视频扩散模型，无需额外奖励模型或偏好数据。

**关键词**：视频扩散模型, 可微分优化, 视觉语言模型, 奖励流, 微调, 文本到视频生成

## 3 点简述
- 核心问题：现有方法依赖不可微分偏好信号，导致训练不稳定、易受奖励攻击。
- 方法要点：使用冻结视觉语言模型作为训练免费评论家，通过扩散去噪链反向传播反馈。
- 实验或效果：提升视频质量和语义对齐，缓解奖励攻击和崩溃，模型无关且可泛化。

## 摘要（原文）

> Direct Preference Optimization (DPO) has recently improved Text-to-Video (T2V) generation by enhancing visual fidelity and text alignment. However, current methods rely on non-differentiable preference signals from human annotations or learned reward models. This reliance makes training label-intensive, bias-prone, and easy-to-game, which often triggers reward hacking and unstable training. We propose Diffusion-DRF, a differentiable reward flow for fine-tuning video diffusion models using a frozen, off-the-shelf Vision-Language Model (VLM) as a training-free critic. Diffusion-DRF directly backpropagates VLM feedback through the diffusion denoising chain, converting logit-level responses into token-aware gradients for optimization. We propose an automated, aspect-structured prompting pipeline to obtain reliable multi-dimensional VLM feedback, while gradient checkpointing enables efficient updates through the final denoising steps. Diffusion-DRF improves video quality and semantic alignment while mitigating reward hacking and collapse -- without additional reward models or preference datasets. It is model-agnostic and readily generalizes to other diffusion-based generative tasks.

