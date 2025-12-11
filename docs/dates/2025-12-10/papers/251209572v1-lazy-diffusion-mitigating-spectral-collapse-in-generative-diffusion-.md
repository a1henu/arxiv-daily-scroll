---
layout: default
title: Lazy Diffusion: Mitigating spectral collapse in generative diffusion-based stable autoregressive emulation of turbulent flows
---

# Lazy Diffusion: Mitigating spectral collapse in generative diffusion-based stable autoregressive emulation of turbulent flows
**arXiv**：[2512.09572v1](https://arxiv.org/abs/2512.09572) · [PDF](https://arxiv.org/pdf/2512.09572.pdf)  
**作者**：Anish Sambamurthy, Ashesh Chattopadhyay  

**一句话要点**：提出Lazy Diffusion与幂律噪声调度以解决生成扩散模型中湍流模拟的频谱崩溃问题

**关键词**：生成扩散模型, 湍流模拟, 频谱崩溃, 噪声调度, 蒸馏方法, 多尺度系统

## 3 点简述
- 标准DDPM在湍流模拟中导致频谱崩溃，高波数模式被噪声淹没
- 引入幂律噪声调度和Lazy Diffusion蒸馏方法，保留精细结构并提升效率
- 在2D湍流和海洋再分析数据中验证，恢复物理惯性范围尺度

## 摘要（原文）

> Turbulent flows posses broadband, power-law spectra in which multiscale interactions couple high-wavenumber fluctuations to large-scale dynamics. Although diffusion-based generative models offer a principled probabilistic forecasting framework, we show that standard DDPMs induce a fundamental \emph{spectral collapse}: a Fourier-space analysis of the forward SDE reveals a closed-form, mode-wise signal-to-noise ratio (SNR) that decays monotonically in wavenumber, $\|k\|$ for spectra $S(k)\!\propto\!\|k\|^{-λ}$, rendering high-wavenumber modes indistinguishable from noise and producing an intrinsic spectral bias. We reinterpret the noise schedule as a spectral regularizer and introduce power-law schedules $β(τ)\!\propto\!τ^γ$ that preserve fine-scale structure deeper into diffusion time, along with \emph{Lazy Diffusion}, a one-step distillation method that leverages the learned score geometry to bypass long reverse-time trajectories and prevent high-$k$ degradation. Applied to high-Reynolds-number 2D Kolmogorov turbulence and $1/12^\circ$ Gulf of Mexico ocean reanalysis, these methods resolve spectral collapse, stabilize long-horizon autoregression, and restore physically realistic inertial-range scaling. Together, they show that naïve Gaussian scheduling is structurally incompatible with power-law physics and that physics-aware diffusion processes can yield accurate, efficient, and fully probabilistic surrogates for multiscale dynamical systems.

