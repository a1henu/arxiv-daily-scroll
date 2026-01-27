---
layout: default
title: Adaptive Domain Shift in Diffusion Models for Cross-Modality Image Translation
---

# Adaptive Domain Shift in Diffusion Models for Cross-Modality Image Translation
**arXiv**：[2601.18623v1](https://arxiv.org/abs/2601.18623) · [PDF](https://arxiv.org/pdf/2601.18623.pdf)  
**作者**：Zihao Wang, Yuzhou Chen, Shaogang Ren  

**一句话要点**：提出自适应域偏移扩散模型，以解决跨模态图像翻译中的语义漂移和效率低下问题。

**关键词**：跨模态图像翻译, 扩散模型, 域偏移, 语义一致性, 自适应采样, 图像生成

## 3 点简述
- 核心问题：标准扩散模型依赖全局线性域转移，导致采样偏离流形，增加校正负担和语义漂移。
- 方法要点：在生成过程中嵌入空间变化的混合场，注入目标一致恢复项，保持更新在流形上，实现局部残差校正。
- 实验或效果：在医学影像、遥感和电致发光语义映射任务中，提升结构保真度和语义一致性，减少去噪步骤。

## 摘要（原文）

> Cross-modal image translation remains brittle and inefficient. Standard diffusion approaches often rely on a single, global linear transfer between domains. We find that this shortcut forces the sampler to traverse off-manifold, high-cost regions, inflating the correction burden and inviting semantic drift. We refer to this shared failure mode as fixed-schedule domain transfer. In this paper, we embed domain-shift dynamics directly into the generative process. Our model predicts a spatially varying mixing field at every reverse step and injects an explicit, target-consistent restoration term into the drift. This in-step guidance keeps large updates on-manifold and shifts the model's role from global alignment to local residual correction. We provide a continuous-time formulation with an exact solution form and derive a practical first-order sampler that preserves marginal consistency. Empirically, across translation tasks in medical imaging, remote sensing, and electroluminescence semantic mapping, our framework improves structural fidelity and semantic consistency while converging in fewer denoising steps.

