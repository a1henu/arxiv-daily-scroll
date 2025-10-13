---
layout: default
title: Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation
---

# Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation
**arXiv**：[2510.08994v1](https://arxiv.org/abs/2510.08994) · [PDF](https://arxiv.org/pdf/2510.08994.pdf)  
**作者**：Yao Teng, Fuyun Wang, Xian Liu, Zhekai Chen, Han Shi, Yu Wang, Zhenguo Li, Weiyang Liu, Difan Zou, Xihui Liu  
**一句话要点**：提出推测性雅可比去噪解码以加速自回归文本到图像生成
**关键词**：自回归模型, 文本到图像生成, 推理加速, 雅可比迭代, 去噪解码

## 3 点简述
- 自回归文本到图像模型因逐令牌解码导致推理缓慢，需数千次前向传播
- 引入去噪过程到雅可比迭代，通过预测下一干净令牌实现并行生成
- 实验显示方法减少前向传播次数，同时保持生成图像视觉质量

## 摘要（原文）

> As a new paradigm of visual content generation, autoregressive text-to-image
> models suffer from slow inference due to their sequential token-by-token
> decoding process, often requiring thousands of model forward passes to generate
> a single image. To address this inefficiency, we propose Speculative
> Jacobi-Denoising Decoding (SJD2), a framework that incorporates the denoising
> process into Jacobi iterations to enable parallel token generation in
> autoregressive models. Our method introduces a next-clean-token prediction
> paradigm that enables the pre-trained autoregressive models to accept
> noise-perturbed token embeddings and predict the next clean tokens through
> low-cost fine-tuning. This denoising paradigm guides the model towards more
> stable Jacobi trajectories. During inference, our method initializes token
> sequences with Gaussian noise and performs iterative
> next-clean-token-prediction in the embedding space. We employ a probabilistic
> criterion to verify and accept multiple tokens in parallel, and refine the
> unaccepted tokens for the next iteration with the denoising trajectory.
> Experiments show that our method can accelerate generation by reducing model
> forward passes while maintaining the visual quality of generated images.

