---
layout: default
title: DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning
---

# DeepForgeSeal: Latent Space-Driven Semi-Fragile Watermarking for Deepfake Detection Using Multi-Agent Adversarial Reinforcement Learning
**arXiv**：[2511.04949v1](https://arxiv.org/abs/2511.04949) · [PDF](https://arxiv.org/pdf/2511.04949.pdf)  
**作者**：Tharindu Fernando, Clinton Fookes, Sridha Sridharan  

**一句话要点**：提出基于潜在空间和多智能体对抗强化学习的半脆弱水印方法以提升深度伪造检测

**关键词**：深度伪造检测, 半脆弱水印, 潜在空间表示, 多智能体强化学习, 对抗学习

## 3 点简述
- 现有被动检测器依赖特定伪造痕迹，难以泛化到新型深度伪造
- 使用潜在空间嵌入水印，结合MAARL平衡鲁棒性和脆弱性
- 在CelebA和CelebA-HQ基准上性能提升超4.5%和5.3%

## 摘要（原文）

> Rapid advances in generative AI have led to increasingly realistic deepfakes,
> posing growing challenges for law enforcement and public trust. Existing
> passive deepfake detectors struggle to keep pace, largely due to their
> dependence on specific forgery artifacts, which limits their ability to
> generalize to new deepfake types. Proactive deepfake detection using watermarks
> has emerged to address the challenge of identifying high-quality synthetic
> media. However, these methods often struggle to balance robustness against
> benign distortions with sensitivity to malicious tampering. This paper
> introduces a novel deep learning framework that harnesses high-dimensional
> latent space representations and the Multi-Agent Adversarial Reinforcement
> Learning (MAARL) paradigm to develop a robust and adaptive watermarking
> approach. Specifically, we develop a learnable watermark embedder that operates
> in the latent space, capturing high-level image semantics, while offering
> precise control over message encoding and extraction. The MAARL paradigm
> empowers the learnable watermarking agent to pursue an optimal balance between
> robustness and fragility by interacting with a dynamic curriculum of benign and
> malicious image manipulations simulated by an adversarial attacker agent.
> Comprehensive evaluations on the CelebA and CelebA-HQ benchmarks reveal that
> our method consistently outperforms state-of-the-art approaches, achieving
> improvements of over 4.5% on CelebA and more than 5.3% on CelebA-HQ under
> challenging manipulation scenarios.

