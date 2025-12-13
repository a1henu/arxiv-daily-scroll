---
layout: default
title: Disentangled and Distilled Encoder for Out-of-Distribution Reasoning with Rademacher Guarantees
---

# Disentangled and Distilled Encoder for Out-of-Distribution Reasoning with Rademacher Guarantees
**arXiv**：[2512.10522v1](https://arxiv.org/abs/2512.10522) · [PDF](https://arxiv.org/pdf/2512.10522.pdf)  
**作者**：Zahra Rahiminasab, Michael Yuhas, Arvind Easwaran  

**一句话要点**：提出解耦蒸馏编码器框架，以压缩模型用于资源受限设备上的分布外推理

**关键词**：解耦潜在空间, 模型压缩, 分布外推理, 师生蒸馏, Rademacher复杂度, 资源受限设备

## 3 点简述
- 核心问题：变分自编码器的解耦潜在空间用于多标签分布外推理，但模型大小不适合资源受限设备部署。
- 方法要点：通过师生蒸馏将模型压缩形式化为约束优化问题，并基于Rademacher复杂度提供解耦的理论保证。
- 实验或效果：在NVIDIA设备上部署压缩模型进行实证评估，未知具体性能指标。

## 摘要（原文）

> Recently, the disentangled latent space of a variational autoencoder (VAE) has been used to reason about multi-label out-of-distribution (OOD) test samples that are derived from different distributions than training samples. Disentangled latent space means having one-to-many maps between latent dimensions and generative factors or important characteristics of an image. This paper proposes a disentangled distilled encoder (DDE) framework to decrease the OOD reasoner size for deployment on resource-constrained devices while preserving disentanglement. DDE formalizes student-teacher distillation for model compression as a constrained optimization problem while preserving disentanglement with disentanglement constraints. Theoretical guarantees for disentanglement during distillation based on Rademacher complexity are established. The approach is evaluated empirically by deploying the compressed model on an NVIDIA

