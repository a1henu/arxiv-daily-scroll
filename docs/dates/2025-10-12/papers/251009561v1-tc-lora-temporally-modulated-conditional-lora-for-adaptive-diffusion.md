---
layout: default
title: TC-LoRA: Temporally Modulated Conditional LoRA for Adaptive Diffusion Control
---

# TC-LoRA: Temporally Modulated Conditional LoRA for Adaptive Diffusion Control
**arXiv**：[2510.09561v1](https://arxiv.org/abs/2510.09561) · [PDF](https://arxiv.org/pdf/2510.09561.pdf)  
**作者**：Minkyoung Cho, Ruben Ohana, Christian Jacobsen, Adityan Jothi, Min-Hung Chen, Z. Morley Mao, Ethem Can  

**一句话要点**：提出TC-LoRA以在扩散模型中实现动态条件控制

**关键词**：可控扩散模型, 动态权重调整, LoRA适配器, 超网络, 生成保真度

## 3 点简述
- 当前可控扩散模型使用静态条件策略，限制生成过程适应性
- TC-LoRA通过超网络动态生成LoRA适配器，基于时间和条件调整权重
- 实验显示该方法提升生成保真度和空间条件遵循能力

## 摘要（原文）

> Current controllable diffusion models typically rely on fixed architectures
> that modify intermediate activations to inject guidance conditioned on a new
> modality. This approach uses a static conditioning strategy for a dynamic,
> multi-stage denoising process, limiting the model's ability to adapt its
> response as the generation evolves from coarse structure to fine detail. We
> introduce TC-LoRA (Temporally Modulated Conditional LoRA), a new paradigm that
> enables dynamic, context-aware control by conditioning the model's weights
> directly. Our framework uses a hypernetwork to generate LoRA adapters
> on-the-fly, tailoring weight modifications for the frozen backbone at each
> diffusion step based on time and the user's condition. This mechanism enables
> the model to learn and execute an explicit, adaptive strategy for applying
> conditional guidance throughout the entire generation process. Through
> experiments on various data domains, we demonstrate that this dynamic,
> parametric control significantly enhances generative fidelity and adherence to
> spatial conditions compared to static, activation-based methods. TC-LoRA
> establishes an alternative approach in which the model's conditioning strategy
> is modified through a deeper functional adaptation of its weights, allowing
> control to align with the dynamic demands of the task and generative stage.

