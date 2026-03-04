---
layout: default
title: CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance
---

# CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance
**arXiv**：[2603.03281v1](https://arxiv.org/abs/2603.03281) · [PDF](https://arxiv.org/pdf/2603.03281.pdf)  
**作者**：Hanyang Wang, Yiyang Liu, Jiawei Chi, Fangfu Liu, Ran Xue, Yueqi Duan  

**一句话要点**：提出SMC-CFG以解决基于线性控制的CFG在扩散模型中不稳定和语义保真度下降的问题

**关键词**：扩散模型, 分类器自由引导, 滑模控制, 文本到图像生成, 稳定性分析

## 3 点简述
- 核心问题：现有CFG方法依赖线性控制，导致大引导尺度下不稳定、过冲和语义保真度降低
- 方法要点：引入滑模控制CFG，定义指数滑模面并使用切换控制项建立非线性反馈校正
- 实验或效果：在Stable Diffusion 3.5等模型上验证，SMC-CFG在语义对齐和鲁棒性上优于标准CFG

## 摘要（原文）

> Classifier-Free Guidance (CFG) has emerged as a central approach for enhancing semantic alignment in flow-based diffusion models. In this paper, we explore a unified framework called CFG-Ctrl, which reinterprets CFG as a control applied to the first-order continuous-time generative flow, using the conditional-unconditional discrepancy as an error signal to adjust the velocity field. From this perspective, we summarize vanilla CFG as a proportional controller (P-control) with fixed gain, and typical follow-up variants develop extended control-law designs derived from it. However, existing methods mainly rely on linear control, inherently leading to instability, overshooting, and degraded semantic fidelity especially on large guidance scales. To address this, we introduce Sliding Mode Control CFG (SMC-CFG), which enforces the generative flow toward a rapidly convergent sliding manifold. Specifically, we define an exponential sliding mode surface over the semantic prediction error and introduce a switching control term to establish nonlinear feedback-guided correction. Moreover, we provide a Lyapunov stability analysis to theoretically support finite-time convergence. Experiments across text-to-image generation models including Stable Diffusion 3.5, Flux, and Qwen-Image demonstrate that SMC-CFG outperforms standard CFG in semantic alignment and enhances robustness across a wide range of guidance scales. Project Page: https://hanyang-21.github.io/CFG-Ctrl

