---
layout: default
title: Glance: Accelerating Diffusion Models with 1 Sample
---

# Glance: Accelerating Diffusion Models with 1 Sample
**arXiv**：[2512.02899v1](https://arxiv.org/abs/2512.02899) · [PDF](https://arxiv.org/pdf/2512.02899.pdf)  
**作者**：Zhuobai Dong, Rui Zhao, Songjie Wu, Junchao Yi, Linjie Li, Zhengyuan Yang, Lijuan Wang, Alex Jinpeng Wang  

**一句话要点**：提出Glance方法，通过阶段感知的LoRA适配器加速扩散模型，仅需1样本训练。

**关键词**：扩散模型加速, LoRA适配器, 阶段感知策略, 轻量训练, 图像生成, 推理优化

## 3 点简述
- 核心问题：扩散模型推理步骤多、计算成本高，现有蒸馏方法训练成本大且泛化性差。
- 方法要点：采用阶段感知策略，用Slow-LoRA和Fast-LoRA适配器分别处理语义和冗余阶段，实现智能加速。
- 实验或效果：在单V100上1小时内用1样本训练，达到5倍加速，保持视觉质量，泛化性强。

## 摘要（原文）

> Diffusion models have achieved remarkable success in image generation, yet their deployment remains constrained by the heavy computational cost and the need for numerous inference steps. Previous efforts on fewer-step distillation attempt to skip redundant steps by training compact student models, yet they often suffer from heavy retraining costs and degraded generalization. In this work, we take a different perspective: we accelerate smartly, not evenly, applying smaller speedups to early semantic stages and larger ones to later redundant phases. We instantiate this phase-aware strategy with two experts that specialize in slow and fast denoising phases. Surprisingly, instead of investing massive effort in retraining student models, we find that simply equipping the base model with lightweight LoRA adapters achieves both efficient acceleration and strong generalization. We refer to these two adapters as Slow-LoRA and Fast-LoRA. Through extensive experiments, our method achieves up to 5 acceleration over the base model while maintaining comparable visual quality across diverse benchmarks. Remarkably, the LoRA experts are trained with only 1 samples on a single V100 within one hour, yet the resulting models generalize strongly on unseen prompts.

