---
layout: default
title: Compressing image encoders via latent distillation
---

# Compressing image encoders via latent distillation
**arXiv**：[2601.05639v1](https://arxiv.org/abs/2601.05639) · [PDF](https://arxiv.org/pdf/2601.05639.pdf)  
**作者**：Caroline Mazini Rodrigues, Nicolas Keriven, Thomas Maugey  

**一句话要点**：提出基于潜在蒸馏的编码器压缩方法，以在资源受限环境中实现轻量化图像压缩。

**关键词**：图像压缩, 编码器压缩, 知识蒸馏, 潜在空间近似, 轻量化模型

## 3 点简述
- 核心问题：深度学习图像压缩模型编码器复杂、资源消耗大，难以在硬件受限场景部署。
- 方法要点：通过简化知识蒸馏策略，用较少数据和训练时间近似原始模型的潜在空间，生成轻量编码器。
- 实验或效果：在两种架构上评估，相比原始损失训练，本方法能更好保持重建质量和统计保真度。

## 摘要（原文）

> Deep learning models for image compression often face practical limitations in hardware-constrained applications. Although these models achieve high-quality reconstructions, they are typically complex, heavyweight, and require substantial training data and computational resources. We propose a methodology to partially compress these networks by reducing the size of their encoders. Our approach uses a simplified knowledge distillation strategy to approximate the latent space of the original models with less data and shorter training, yielding lightweight encoders from heavyweight ones. We evaluate the resulting lightweight encoders across two different architectures on the image compression task. Experiments show that our method preserves reconstruction quality and statistical fidelity better than training lightweight encoders with the original loss, making it practical for resource-limited environments.

