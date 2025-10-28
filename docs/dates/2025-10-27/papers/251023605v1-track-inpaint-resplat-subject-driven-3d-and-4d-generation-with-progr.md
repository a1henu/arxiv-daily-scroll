---
layout: default
title: Track, Inpaint, Resplat: Subject-driven 3D and 4D Generation with Progressive Texture Infilling
---

# Track, Inpaint, Resplat: Subject-driven 3D and 4D Generation with Progressive Texture Infilling
**arXiv**：[2510.23605v1](https://arxiv.org/abs/2510.23605) · [PDF](https://arxiv.org/pdf/2510.23605.pdf)  
**作者**：Shuhong Zheng, Ashkan Mirzaei, Igor Gilitschenski  

**一句话要点**：提出TIRE方法以解决主题驱动3D/4D生成中的身份保持问题

**关键词**：主题驱动生成, 3D生成, 4D生成, 纹理修复, 视频跟踪, 多视图一致性

## 3 点简述
- 现有3D/4D生成方法难以在不同视角下保持主题的语义身份
- 通过跟踪、修复和重投影，渐进填充纹理以提升身份一致性
- 实验显示在身份保持方面优于现有先进方法

## 摘要（原文）

> Current 3D/4D generation methods are usually optimized for photorealism,
> efficiency, and aesthetics. However, they often fail to preserve the semantic
> identity of the subject across different viewpoints. Adapting generation
> methods with one or few images of a specific subject (also known as
> Personalization or Subject-driven generation) allows generating visual content
> that align with the identity of the subject. However, personalized 3D/4D
> generation is still largely underexplored. In this work, we introduce TIRE
> (Track, Inpaint, REsplat), a novel method for subject-driven 3D/4D generation.
> It takes an initial 3D asset produced by an existing 3D generative model as
> input and uses video tracking to identify the regions that need to be modified.
> Then, we adopt a subject-driven 2D inpainting model for progressively infilling
> the identified regions. Finally, we resplat the modified 2D multi-view
> observations back to 3D while still maintaining consistency. Extensive
> experiments demonstrate that our approach significantly improves identity
> preservation in 3D/4D generation compared to state-of-the-art methods. Our
> project website is available at
> https://zsh2000.github.io/track-inpaint-resplat.github.io/.

