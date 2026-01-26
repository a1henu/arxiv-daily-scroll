---
layout: default
title: Fast, faithful and photorealistic diffusion-based image super-resolution with enhanced Flow Map models
---

# Fast, faithful and photorealistic diffusion-based image super-resolution with enhanced Flow Map models
**arXiv**：[2601.16660v1](https://arxiv.org/abs/2601.16660) · [PDF](https://arxiv.org/pdf/2601.16660.pdf)  
**作者**：Maxence Noble, Gonzalo Iñaki Quintana, Benjamin Aubin, Clément Chadebec  

**一句话要点**：提出FlowMapSR框架，基于增强Flow Map模型实现快速、忠实且逼真的扩散图像超分辨率。

**关键词**：图像超分辨率, 扩散模型, Flow Map模型, 知识蒸馏, LoRA微调, 推理效率

## 3 点简述
- 核心问题：扩散图像超分辨率在忠实重建与逼真感之间存在权衡，且现有蒸馏方法可能损失感知线索。
- 方法要点：结合Flow Map模型、正负提示引导和LoRA对抗微调，提升推理效率与图像质量。
- 实验或效果：在x4和x8上采样中优于现有方法，平衡忠实度与逼真感，推理时间具竞争力。

## 摘要（原文）

> Diffusion-based image super-resolution (SR) has recently attracted significant attention by leveraging the expressive power of large pre-trained text-to-image diffusion models (DMs). A central practical challenge is resolving the trade-off between reconstruction faithfulness and photorealism. To address inference efficiency, many recent works have explored knowledge distillation strategies specifically tailored to SR, enabling one-step diffusion-based approaches. However, these teacher-student formulations are inherently constrained by information compression, which can degrade perceptual cues such as lifelike textures and depth of field, even with high overall perceptual quality. In parallel, self-distillation DMs, known as Flow Map models, have emerged as a promising alternative for image generation tasks, enabling fast inference while preserving the expressivity and training stability of standard DMs. Building on these developments, we propose FlowMapSR, a novel diffusion-based framework for image super-resolution explicitly designed for efficient inference. Beyond adapting Flow Map models to SR, we introduce two complementary enhancements: (i) positive-negative prompting guidance, based on a generalization of classifier free-guidance paradigm to Flow Map models, and (ii) adversarial fine-tuning using Low-Rank Adaptation (LoRA). Among the considered Flow Map formulations (Eulerian, Lagrangian, and Shortcut), we find that the Shortcut variant consistently achieves the best performance when combined with these enhancements. Extensive experiments show that FlowMapSR achieves a better balance between reconstruction faithfulness and photorealism than recent state-of-the-art methods for both x4 and x8 upscaling, while maintaining competitive inference time. Notably, a single model is used for both upscaling factors, without any scale-specific conditioning or degradation-guided mechanisms.

