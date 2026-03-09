---
layout: default
title: Latent Transfer Attack: Adversarial Examples via Generative Latent Spaces
---

# Latent Transfer Attack: Adversarial Examples via Generative Latent Spaces
**arXiv**：[2603.06311v1](https://arxiv.org/abs/2603.06311) · [PDF](https://arxiv.org/pdf/2603.06311.pdf)  
**作者**：Eitan Shaar, Ariel Shaulov, Yalcin Tur, Gal Chechik, Ravid Shwartz-Ziv  

**一句话要点**：提出LTA攻击，在生成式潜在空间中优化对抗扰动以提升跨模型迁移性

**关键词**：对抗攻击, 潜在空间优化, 迁移攻击, 生成模型, 鲁棒性评估, Stable Diffusion

## 3 点简述
- 核心问题：像素空间对抗攻击易受预处理影响且跨架构迁移性差
- 方法要点：在预训练Stable Diffusion VAE潜在空间中优化扰动，结合EOT和潜在平滑
- 实验或效果：在CNN和视觉Transformer目标上实现强迁移攻击，产生空间相干低频扰动

## 摘要（原文）

> Adversarial attacks are a central tool for probing the robustness of modern vision models, yet most methods optimize perturbations directly in pixel space under $\ell_\infty$ or $\ell_2$ constraints. While effective in white-box settings, pixel-space optimization often produces high-frequency, texture-like noise that is brittle to common preprocessing (e.g., resizing and cropping) and transfers poorly across architectures. We propose $\textbf{LTA}$ ($\textbf{L}$atent $\textbf{T}$ransfer $\textbf{A}$ttack), a transfer-based attack that instead optimizes perturbations in the latent space of a pretrained Stable Diffusion VAE. Given a clean image, we encode it into a latent code and optimize the latent representation to maximize a surrogate classifier loss, while softly enforcing a pixel-space $\ell_\infty$ budget after decoding. To improve robustness to resolution mismatch and standard input pipelines, we incorporate Expectation Over Transformations (EOT) via randomized resizing, interpolation, and cropping, and apply periodic latent Gaussian smoothing to suppress emerging artifacts and stabilize optimization. Across a suite of CNN and vision-transformer targets, LTA achieves strong transfer attack success while producing spatially coherent, predominantly low-frequency perturbations that differ qualitatively from pixel-space baselines and occupy a distinct point in the transfer-quality trade-off. Our results highlight pretrained generative latent spaces as an effective and structured domain for adversarial optimization, bridging robustness evaluation with modern generative priors.

