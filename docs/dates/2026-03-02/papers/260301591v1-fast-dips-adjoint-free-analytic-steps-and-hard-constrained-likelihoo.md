---
layout: default
title: FAST-DIPS: Adjoint-Free Analytic Steps and Hard-Constrained Likelihood Correction for Diffusion-Prior Inverse Problems
---

# FAST-DIPS: Adjoint-Free Analytic Steps and Hard-Constrained Likelihood Correction for Diffusion-Prior Inverse Problems
**arXiv**：[2603.01591v1](https://arxiv.org/abs/2603.01591) · [PDF](https://arxiv.org/pdf/2603.01591.pdf)  
**作者**：Minwoo Kim, Seunghyeok Shin, Hongki Lim  

**一句话要点**：提出FAST-DIPS以解决无训练扩散先验逆问题中数据一致性的计算效率问题

**关键词**：扩散先验, 逆问题求解, 无训练方法, 计算效率优化, 硬约束投影, 解析步长

## 3 点简述
- 核心问题：非线性前向算子下，数据一致性依赖重复导数或内循环，导致计算开销大
- 方法要点：采用硬约束投影和解析最优步长，结合ADMM风格分裂与回溯，避免伴随计算
- 实验或效果：在PSNR/SSIM/LPIPS指标上竞争，实现高达19.5倍加速，无需手动伴随或内MCMC

## 摘要（原文）

> Training-free diffusion priors enable inverse-problem solvers without retraining, but for nonlinear forward operators data consistency often relies on repeated derivatives or inner optimization/MCMC loops with conservative step sizes, incurring many iterations and denoiser/score evaluations. We propose a training-free solver that replaces these inner loops with a hard measurement-space feasibility constraint (closed-form projection) and an analytic, model-optimal step size, enabling a small, fixed compute budget per noise level. Anchored at the denoiser prediction, the correction is approximated via an adjoint-free, ADMM-style splitting with projection and a few steepest-descent updates, using one VJP and either one JVP or a forward-difference probe, followed by backtracking and decoupled re-annealing. We prove local model optimality and descent under backtracking for the step-size rule, and derive an explicit KL bound for mode-substitution re-annealing under a local Gaussian conditional surrogate. We also develop a latent variant and a one-parameter pixel$\rightarrow$latent hybrid schedule. Experiments achieve competitive PSNR/SSIM/LPIPS with up to 19.5$\times$ speedup, without hand-coded adjoints or inner MCMC.

