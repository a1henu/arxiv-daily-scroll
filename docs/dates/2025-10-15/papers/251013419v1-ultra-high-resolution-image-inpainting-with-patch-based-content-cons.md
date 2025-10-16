---
layout: default
title: Ultra High-Resolution Image Inpainting with Patch-Based Content Consistency Adapter
---

# Ultra High-Resolution Image Inpainting with Patch-Based Content Consistency Adapter
**arXiv**：[2510.13419v1](https://arxiv.org/abs/2510.13419) · [PDF](https://arxiv.org/pdf/2510.13419.pdf)  
**作者**：Jianhui Zhang, Sheng Cheng, Qirui Sun, Jia Liu, Wang Luyang, Chaoyu Feng, Chen Fang, Lei Lei, Jue Wang, Shuaicheng Liu  

**一句话要点**：提出Patch-Adapter框架以解决超高分辨率图像修复中的内容一致性和提示对齐问题

**关键词**：图像修复, 超高分辨率, 扩散模型, 内容一致性, 文本引导, 补丁级注意力

## 3 点简述
- 核心问题：高分辨率图像修复中内容一致性和提示对齐随分辨率与纹理复杂度增加而恶化
- 方法要点：采用双阶段适配器架构，包括全局结构一致性和局部细节保真机制
- 实验或效果：在OpenImages等数据集上实现SOTA，提升感知质量和文本提示对齐

## 摘要（原文）

> In this work, we present Patch-Adapter, an effective framework for
> high-resolution text-guided image inpainting. Unlike existing methods limited
> to lower resolutions, our approach achieves 4K+ resolution while maintaining
> precise content consistency and prompt alignment, two critical challenges in
> image inpainting that intensify with increasing resolution and texture
> complexity. Patch-Adapter leverages a two-stage adapter architecture to scale
> the diffusion model's resolution from 1K to 4K+ without requiring structural
> overhauls: (1) Dual Context Adapter learns coherence between masked and
> unmasked regions at reduced resolutions to establish global structural
> consistency; and (2) Reference Patch Adapter implements a patch-level attention
> mechanism for full-resolution inpainting, preserving local detail fidelity
> through adaptive feature fusion. This dual-stage architecture uniquely
> addresses the scalability gap in high-resolution inpainting by decoupling
> global semantics from localized refinement. Experiments demonstrate that
> Patch-Adapter not only resolves artifacts common in large-scale inpainting but
> also achieves state-of-the-art performance on the OpenImages and
> Photo-Concept-Bucket datasets, outperforming existing methods in both
> perceptual quality and text-prompt adherence.

