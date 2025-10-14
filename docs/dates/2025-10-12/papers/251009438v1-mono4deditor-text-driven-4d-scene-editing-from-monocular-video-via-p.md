---
layout: default
title: Mono4DEditor: Text-Driven 4D Scene Editing from Monocular Video via Point-Level Localization of Language-Embedded Gaussians
---

# Mono4DEditor: Text-Driven 4D Scene Editing from Monocular Video via Point-Level Localization of Language-Embedded Gaussians
**arXiv**：[2510.09438v1](https://arxiv.org/abs/2510.09438) · [PDF](https://arxiv.org/pdf/2510.09438.pdf)  
**作者**：Jin-Chuan Shi, Chengye Su, Jiajun Wang, Ariel Shamir, Miao Wang  

**一句话要点**：提出Mono4DEditor框架，通过语言嵌入高斯实现单目视频4D场景的文本驱动编辑

**关键词**：4D场景编辑, 文本驱动编辑, 3D高斯表示, CLIP特征嵌入, 扩散模型编辑, 时空一致性

## 3 点简述
- 核心问题：单目视频4D场景编辑中，实现语义精确的局部编辑并保持未编辑内容完整性。
- 方法要点：使用量化CLIP特征增强3D高斯，结合点级定位策略和扩散模型进行编辑。
- 实验或效果：在多样场景中实现高质量编辑，超越现有方法，保持时空一致性。

## 摘要（原文）

> Editing 4D scenes reconstructed from monocular videos based on text prompts
> is a valuable yet challenging task with broad applications in content creation
> and virtual environments. The key difficulty lies in achieving semantically
> precise edits in localized regions of complex, dynamic scenes, while preserving
> the integrity of unedited content. To address this, we introduce Mono4DEditor,
> a novel framework for flexible and accurate text-driven 4D scene editing. Our
> method augments 3D Gaussians with quantized CLIP features to form a
> language-embedded dynamic representation, enabling efficient semantic querying
> of arbitrary spatial regions. We further propose a two-stage point-level
> localization strategy that first selects candidate Gaussians via CLIP
> similarity and then refines their spatial extent to improve accuracy. Finally,
> targeted edits are performed on localized regions using a diffusion-based video
> editing model, with flow and scribble guidance ensuring spatial fidelity and
> temporal coherence. Extensive experiments demonstrate that Mono4DEditor enables
> high-quality, text-driven edits across diverse scenes and object types, while
> preserving the appearance and geometry of unedited areas and surpassing prior
> approaches in both flexibility and visual fidelity.

