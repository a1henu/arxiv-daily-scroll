---
layout: default
title: Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability
---

# Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability
**arXiv**：[2601.20642v1](https://arxiv.org/abs/2601.20642) · [PDF](https://arxiv.org/pdf/2601.20642.pdf)  
**作者**：Rohan Asthana, Vasileios Belagiannis  

**一句话要点**：提出基于对数概率各向异性的检测与缓解方法以解决扩散模型记忆化问题

**关键词**：扩散模型, 记忆化检测, 对数概率各向异性, 无去噪检测, 图像生成安全, 模型缓解

## 3 点简述
- 核心问题：扩散模型在低噪声下易记忆化，现有基于范数的检测方法在非各向同性场景中效果有限
- 方法要点：结合各向同性范数和各向异性对齐，开发无需去噪步骤的记忆化检测指标
- 实验或效果：在Stable Diffusion上优于现有方法，速度提升约5倍，并展示缓解策略有效性

## 摘要（原文）

> Diffusion-based image generative models produce high-fidelity images through iterative denoising but remain vulnerable to memorization, where they unintentionally reproduce exact copies or parts of training images. Recent memorization detection methods are primarily based on the norm of score difference as indicators of memorization. We prove that such norm-based metrics are mainly effective under the assumption of isotropic log-probability distributions, which generally holds at high or medium noise levels. In contrast, analyzing the anisotropic regime reveals that memorized samples exhibit strong angular alignment between the guidance vector and unconditional scores in the low-noise setting. Through these insights, we develop a memorization detection metric by integrating isotropic norm and anisotropic alignment. Our detection metric can be computed directly on pure noise inputs via two conditional and unconditional forward passes, eliminating the need for costly denoising steps. Detection experiments on Stable Diffusion v1.4 and v2 show that our metric outperforms existing denoising-free detection methods while being at least approximately 5x faster than the previous best approach. Finally, we demonstrate the effectiveness of our approach by utilizing a mitigation strategy that adapts memorized prompts based on our developed metric.

