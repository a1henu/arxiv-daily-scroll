---
layout: default
title: CAPTAIN: Semantic Feature Injection for Memorization Mitigation in Text-to-Image Diffusion Models
---

# CAPTAIN: Semantic Feature Injection for Memorization Mitigation in Text-to-Image Diffusion Models
**arXiv**：[2512.10655v1](https://arxiv.org/abs/2512.10655) · [PDF](https://arxiv.org/pdf/2512.10655.pdf)  
**作者**：Tong Zhang, Carlos Hinojosa, Bernard Ghanem  

**一句话要点**：提出CAPTAIN框架，通过语义特征注入缓解文本到图像扩散模型的记忆化问题

**关键词**：文本到图像生成, 扩散模型, 记忆化缓解, 语义特征注入, 隐私保护

## 3 点简述
- 扩散模型可能无意中复制训练数据，引发隐私和版权担忧
- CAPTAIN在去噪过程中修改潜在特征，结合频率噪声初始化和语义特征注入
- 实验显示CAPTAIN显著减少记忆化，同时保持提示对齐和视觉质量

## 摘要（原文）

> Diffusion models can unintentionally reproduce training examples, raising privacy and copyright concerns as these systems are increasingly deployed at scale. Existing inference-time mitigation methods typically manipulate classifier-free guidance (CFG) or perturb prompt embeddings; however, they often struggle to reduce memorization without compromising alignment with the conditioning prompt. We introduce CAPTAIN, a training-free framework that mitigates memorization by directly modifying latent features during denoising. CAPTAIN first applies frequency-based noise initialization to reduce the tendency to replicate memorized patterns early in the denoising process. It then identifies the optimal denoising timesteps for feature injection and localizes memorized regions. Finally, CAPTAIN injects semantically aligned features from non-memorized reference images into localized latent regions, suppressing memorization while preserving prompt fidelity and visual quality. Our experiments show that CAPTAIN achieves substantial reductions in memorization compared to CFG-based baselines while maintaining strong alignment with the intended prompt.

