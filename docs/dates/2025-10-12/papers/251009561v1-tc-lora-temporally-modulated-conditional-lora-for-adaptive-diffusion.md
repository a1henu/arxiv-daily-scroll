---
layout: default
title: TC-LoRA: Temporally Modulated Conditional LoRA for Adaptive Diffusion Control
---

# TC-LoRA: Temporally Modulated Conditional LoRA for Adaptive Diffusion Control
**arXiv**：[2510.09561v1](https://arxiv.org/abs/2510.09561) · [PDF](https://arxiv.org/pdf/2510.09561.pdf)  
**作者**：Minkyoung Cho, Ruben Ohana, Christian Jacobsen, Adityan Jothi, Min-Hung Chen, Z. Morley Mao, Ethem Can  
**一句话要点**：提出TC-LoRA以动态适应扩散模型的控制需求

**关键词**：扩散模型, 动态控制, LoRA适配器, 超网络, 条件生成

## 3 点简述
- 静态条件策略限制扩散模型在生成过程中动态调整能力
- 使用超网络实时生成LoRA适配器，基于时间和条件动态调整权重
- 实验显示动态控制提升生成保真度和空间条件遵循度

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

