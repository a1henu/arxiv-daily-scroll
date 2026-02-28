---
layout: default
title: Causal Motion Diffusion Models for Autoregressive Motion Generation
---

# Causal Motion Diffusion Models for Autoregressive Motion Generation
**arXiv**：[2602.22594v1](https://arxiv.org/abs/2602.22594) · [PDF](https://arxiv.org/pdf/2602.22594.pdf)  
**作者**：Qing Yu, Akihisa Watanabe, Kent Fujiwara  

**一句话要点**：提出因果运动扩散模型以解决自回归运动生成中的因果性和实时性问题

**关键词**：运动生成, 扩散模型, 自回归模型, 因果推理, 文本到运动生成, 实时合成

## 3 点简述
- 现有方法在运动生成中存在因果性限制或累积误差问题
- 基于因果扩散变换器在语义对齐潜空间中进行自回归去噪
- 实验显示在语义保真度和时间平滑度上优于现有模型，并降低推理延迟

## 摘要（原文）

> Recent advances in motion diffusion models have substantially improved the realism of human motion synthesis. However, existing approaches either rely on full-sequence diffusion models with bidirectional generation, which limits temporal causality and real-time applicability, or autoregressive models that suffer from instability and cumulative errors. In this work, we present Causal Motion Diffusion Models (CMDM), a unified framework for autoregressive motion generation based on a causal diffusion transformer that operates in a semantically aligned latent space. CMDM builds upon a Motion-Language-Aligned Causal VAE (MAC-VAE), which encodes motion sequences into temporally causal latent representations. On top of this latent representation, an autoregressive diffusion transformer is trained using causal diffusion forcing to perform temporally ordered denoising across motion frames. To achieve fast inference, we introduce a frame-wise sampling schedule with causal uncertainty, where each subsequent frame is predicted from partially denoised previous frames. The resulting framework supports high-quality text-to-motion generation, streaming synthesis, and long-horizon motion generation at interactive rates. Experiments on HumanML3D and SnapMoGen demonstrate that CMDM outperforms existing diffusion and autoregressive models in both semantic fidelity and temporal smoothness, while substantially reducing inference latency.

