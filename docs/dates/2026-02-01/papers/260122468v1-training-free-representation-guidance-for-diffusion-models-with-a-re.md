---
layout: default
title: Training-Free Representation Guidance for Diffusion Models with a Representation Alignment Projector
---

# Training-Free Representation Guidance for Diffusion Models with a Representation Alignment Projector
**arXiv**：[2601.22468v1](https://arxiv.org/abs/2601.22468) · [PDF](https://arxiv.org/pdf/2601.22468.pdf)  
**作者**：Wenqiang Zu, Shenghao Xie, Bo Lei, Lei Ma  

**一句话要点**：提出表示对齐投影器以解决扩散模型早期去噪阶段的语义漂移问题

**关键词**：扩散模型, 表示对齐, 语义漂移, 无训练指导, 图像合成, 投影器

## 3 点简述
- 核心问题：扩散模型早期去噪阶段存在语义漂移，导致语义对齐不一致
- 方法要点：使用表示对齐投影器在采样步骤中注入预测表示，作为语义锚点
- 实验或效果：在ImageNet合成中显著降低FID分数，如REPA-XL/2从5.9提升至3.3

## 摘要（原文）

> Recent progress in generative modeling has enabled high-quality visual synthesis with diffusion-based frameworks, supporting controllable sampling and large-scale training. Inference-time guidance methods such as classifier-free and representative guidance enhance semantic alignment by modifying sampling dynamics; however, they do not fully exploit unsupervised feature representations. Although such visual representations contain rich semantic structure, their integration during generation is constrained by the absence of ground-truth reference images at inference. This work reveals semantic drift in the early denoising stages of diffusion transformers, where stochasticity results in inconsistent alignment even under identical conditioning. To mitigate this issue, we introduce a guidance scheme using a representation alignment projector that injects representations predicted by a projector into intermediate sampling steps, providing an effective semantic anchor without modifying the model architecture. Experiments on SiTs and REPAs show notable improvements in class-conditional ImageNet synthesis, achieving substantially lower FID scores; for example, REPA-XL/2 improves from 5.9 to 3.3, and the proposed method outperforms representative guidance when applied to SiT models. The approach further yields complementary gains when combined with classifier-free guidance, demonstrating enhanced semantic coherence and visual fidelity. These results establish representation-informed diffusion sampling as a practical strategy for reinforcing semantic preservation and image consistency.

