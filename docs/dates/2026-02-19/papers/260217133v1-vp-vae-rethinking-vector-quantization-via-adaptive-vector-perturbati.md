---
layout: default
title: VP-VAE: Rethinking Vector Quantization via Adaptive Vector Perturbation
---

# VP-VAE: Rethinking Vector Quantization via Adaptive Vector Perturbation
**arXiv**：[2602.17133v1](https://arxiv.org/abs/2602.17133) · [PDF](https://arxiv.org/pdf/2602.17133.pdf)  
**作者**：Linwei Zhai, Han Ding, Mingzhi Lin, Cui Zhao, Fei Wang, Ge Wang, Wang Zhi, Wei Xi  

**一句话要点**：提出VP-VAE，通过自适应向量扰动解耦表示学习与离散化，以解决VQ-VAE训练不稳定和码本崩溃问题。

**关键词**：向量量化, 变分自编码器, 自适应扰动, 码本解耦, 生成建模, 训练稳定性

## 3 点简述
- 核心问题：VQ-VAE因表示学习与离散码本优化耦合，导致训练不稳定和码本崩溃。
- 方法要点：用Metropolis-Hastings采样生成分布一致、尺度自适应的潜在扰动，替代不可微量化器，无需显式码本。
- 实验或效果：在图像和音频基准上，VP-VAE和FSP提升重建保真度，实现更平衡的令牌使用，避免耦合训练不稳定性。

## 摘要（原文）

> Vector Quantized Variational Autoencoders (VQ-VAEs) are fundamental to modern generative modeling, yet they often suffer from training instability and "codebook collapse" due to the inherent coupling of representation learning and discrete codebook optimization. In this paper, we propose VP-VAE (Vector Perturbation VAE), a novel paradigm that decouples representation learning from discretization by eliminating the need for an explicit codebook during training. Our key insight is that, from the neural network's viewpoint, performing quantization primarily manifests as injecting a structured perturbation in latent space. Accordingly, VP-VAE replaces the non-differentiable quantizer with distribution-consistent and scale-adaptive latent perturbations generated via Metropolis--Hastings sampling. This design enables stable training without a codebook while making the model robust to inference-time quantization error. Moreover, under the assumption of approximately uniform latent variables, we derive FSP (Finite Scalar Perturbation), a lightweight variant of VP-VAE that provides a unified theoretical explanation and a practical improvement for FSQ-style fixed quantizers. Extensive experiments on image and audio benchmarks demonstrate that VP-VAE and FSP improve reconstruction fidelity and achieve substantially more balanced token usage, while avoiding the instability inherent to coupled codebook training.

