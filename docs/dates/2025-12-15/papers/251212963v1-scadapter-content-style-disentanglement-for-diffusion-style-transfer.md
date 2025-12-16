---
layout: default
title: SCAdapter: Content-Style Disentanglement for Diffusion Style Transfer
---

# SCAdapter: Content-Style Disentanglement for Diffusion Style Transfer
**arXiv**：[2512.12963v1](https://arxiv.org/abs/2512.12963) · [PDF](https://arxiv.org/pdf/2512.12963.pdf)  
**作者**：Luan Thanh Trinh, Kenji Doi, Atsuki Osanai  

**一句话要点**：提出SCAdapter以解决扩散模型风格迁移中内容-风格纠缠和细节缺失问题

**关键词**：扩散模型, 风格迁移, 内容-风格解耦, CLIP特征, 快速推理, 图像生成

## 3 点简述
- 核心问题：扩散模型在风格迁移中易产生绘画化结果或丢失细节，现有方法未能有效分离内容风格和风格参考内容特征
- 方法要点：利用CLIP图像空间分离内容与风格特征，结合CSAdaIN、KVS注入和一致性目标实现精确迁移
- 实验或效果：在传统和扩散基线中显著优于现有方法，无需DDIM反转和推理优化，推理速度至少快2倍

## 摘要（原文）

> Diffusion models have emerged as the leading approach for style transfer, yet they struggle with photo-realistic transfers, often producing painting-like results or missing detailed stylistic elements. Current methods inadequately address unwanted influence from original content styles and style reference content features. We introduce SCAdapter, a novel technique leveraging CLIP image space to effectively separate and integrate content and style features. Our key innovation systematically extracts pure content from content images and style elements from style references, ensuring authentic transfers. This approach is enhanced through three components: Controllable Style Adaptive Instance Normalization (CSAdaIN) for precise multi-style blending, KVS Injection for targeted style integration, and a style transfer consistency objective maintaining process coherence. Comprehensive experiments demonstrate SCAdapter significantly outperforms state-of-the-art methods in both conventional and diffusion-based baselines. By eliminating DDIM inversion and inference-stage optimization, our method achieves at least $2\times$ faster inference than other diffusion-based approaches, making it both more effective and efficient for practical applications.

