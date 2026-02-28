---
layout: default
title: Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction
---

# Plug-and-Play Diffusion Meets ADMM: Dual-Variable Coupling for Robust Medical Image Reconstruction
**arXiv**：[2602.23214v1](https://arxiv.org/abs/2602.23214) · [PDF](https://arxiv.org/pdf/2602.23214.pdf)  
**作者**：Chenhe Du, Xuanyu Tian, Qing Wu, Muyu Liu, Jingyi Yu, Hongjiang Wei, Yuyao Zhang  

**一句话要点**：提出双耦合PnP扩散与谱同质化方法，解决医学图像重建中的偏差-幻觉权衡问题。

**关键词**：医学图像重建, 扩散模型, PnP框架, 双变量耦合, 谱同质化, 优化算法

## 3 点简述
- 核心问题：现有PnP扩散求解器因无记忆更新导致稳态偏差，且双变量耦合引入结构化伪影。
- 方法要点：引入双变量耦合确保渐近收敛，并设计谱同质化机制将结构化残差调制为伪AWGN输入。
- 实验或效果：在CT和MRI重建中实现高保真度与加速收敛，达到先进性能。

## 摘要（原文）

> Plug-and-Play diffusion prior (PnPDP) frameworks have emerged as a powerful paradigm for solving imaging inverse problems by treating pretrained generative models as modular priors. However, we identify a critical flaw in prevailing PnP solvers (e.g., based on HQS or Proximal Gradient): they function as memoryless operators, updating estimates solely based on instantaneous gradients. This lack of historical tracking inevitably leads to non-vanishing steady-state bias, where the reconstruction fails to strictly satisfy physical measurements under heavy corruption. To resolve this, we propose Dual-Coupled PnP Diffusion, which restores the classical dual variable to provide integral feedback, theoretically guaranteeing asymptotic convergence to the exact data manifold. However, this rigorous geometric coupling introduces a secondary challenge: the accumulated dual residuals exhibit spectrally colored, structured artifacts that violate the Additive White Gaussian Noise (AWGN) assumption of diffusion priors, causing severe hallucinations. To bridge this gap, we introduce Spectral Homogenization (SH), a frequency-domain adaptation mechanism that modulates these structured residuals into statistically compliant pseudo-AWGN inputs. This effectively aligns the solver's rigorous optimization trajectory with the denoiser's valid statistical manifold. Extensive experiments on CT and MRI reconstruction demonstrate that our approach resolves the bias-hallucination trade-off, achieving state-of-the-art fidelity with significantly accelerated convergence.

