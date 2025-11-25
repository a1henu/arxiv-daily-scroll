---
layout: default
title: DiP: Taming Diffusion Models in Pixel Space
---

# DiP: Taming Diffusion Models in Pixel Space
**arXiv**：[2511.18822v1](https://arxiv.org/abs/2511.18822) · [PDF](https://arxiv.org/pdf/2511.18822.pdf)  
**作者**：Zhennan Chen, Junwei Zhu, Xu Chen, Jiangning Zhang, Xiaobin Hu, Hanzhen Zhao, Chengjie Wang, Jian Yang, Ying Tai  

**一句话要点**：提出DiP框架以解决扩散模型在像素空间的计算效率与质量权衡问题

**关键词**：扩散模型, 像素空间生成, 计算效率优化, 全局局部解耦, 轻量细节恢复

## 3 点简述
- 扩散模型面临生成质量与计算效率的根本权衡，潜在扩散模型效率高但信息损失
- DiP将生成解耦为全局和局部阶段，使用DiT构建结构，轻量头恢复细节
- 实验显示DiP推理速度提升10倍，FID达1.90，参数仅增0.3%

## 摘要（原文）

> Diffusion models face a fundamental trade-off between generation quality and computational efficiency. Latent Diffusion Models (LDMs) offer an efficient solution but suffer from potential information loss and non-end-to-end training. In contrast, existing pixel space models bypass VAEs but are computationally prohibitive for high-resolution synthesis. To resolve this dilemma, we propose DiP, an efficient pixel space diffusion framework. DiP decouples generation into a global and a local stage: a Diffusion Transformer (DiT) backbone operates on large patches for efficient global structure construction, while a co-trained lightweight Patch Detailer Head leverages contextual features to restore fine-grained local details. This synergistic design achieves computational efficiency comparable to LDMs without relying on a VAE. DiP is accomplished with up to 10$\times$ faster inference speeds than previous method while increasing the total number of parameters by only 0.3%, and achieves an 1.90 FID score on ImageNet 256$\times$256.

