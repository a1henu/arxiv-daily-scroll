---
layout: default
title: Thinking Like Van Gogh: Structure-Aware Style Transfer via Flow-Guided 3D Gaussian Splatting
---

# Thinking Like Van Gogh: Structure-Aware Style Transfer via Flow-Guided 3D Gaussian Splatting
**arXiv**：[2601.10075v1](https://arxiv.org/abs/2601.10075) · [PDF](https://arxiv.org/pdf/2601.10075.pdf)  
**作者**：Zhendong Wang, Lebin Zhou, Jingchuan Xiao, Rongduo Han, Nam Ling, Cihan Ruan  

**一句话要点**：提出基于流引导的3D高斯溅射方法，实现无网格结构感知风格迁移以模拟后印象派艺术。

**关键词**：3D风格迁移, 高斯溅射, 流引导, 结构变形, 艺术评估, 后印象派

## 3 点简述
- 核心问题：现有3D风格迁移方法将几何视为刚性基底，无法模拟后印象派强调结构夸张的艺术表达。
- 方法要点：从2D绘画提取流场，引导3D高斯原语对齐形成笔触，实现结构变形与颜色优化解耦。
- 实验或效果：引入VLM评估框架，通过美学判断评估艺术真实性，而非传统像素级指标。

## 摘要（原文）

> In 1888, Vincent van Gogh wrote, "I am seeking exaggeration in the essential." This principle, amplifying structural form while suppressing photographic detail, lies at the core of Post-Impressionist art. However, most existing 3D style transfer methods invert this philosophy, treating geometry as a rigid substrate for surface-level texture projection. To authentically reproduce Post-Impressionist stylization, geometric abstraction must be embraced as the primary vehicle of expression.
>   We propose a flow-guided geometric advection framework for 3D Gaussian Splatting (3DGS) that operationalizes this principle in a mesh-free setting. Our method extracts directional flow fields from 2D paintings and back-propagates them into 3D space, rectifying Gaussian primitives to form flow-aligned brushstrokes that conform to scene topology without relying on explicit mesh priors. This enables expressive structural deformation driven directly by painterly motion rather than photometric constraints.
>   Our contributions are threefold: (1) a projection-based, mesh-free flow guidance mechanism that transfers 2D artistic motion into 3D Gaussian geometry; (2) a luminance-structure decoupling strategy that isolates geometric deformation from color optimization, mitigating artifacts during aggressive structural abstraction; and (3) a VLM-as-a-Judge evaluation framework that assesses artistic authenticity through aesthetic judgment instead of conventional pixel-level metrics, explicitly addressing the subjective nature of artistic stylization.

