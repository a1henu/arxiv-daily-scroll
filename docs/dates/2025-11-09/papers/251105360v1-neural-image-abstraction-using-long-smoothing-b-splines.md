---
layout: default
title: Neural Image Abstraction Using Long Smoothing B-Splines
---

# Neural Image Abstraction Using Long Smoothing B-Splines
**arXiv**：[2511.05360v1](https://arxiv.org/abs/2511.05360) · [PDF](https://arxiv.org/pdf/2511.05360.pdf)  
**作者**：Daniel Berio, Michael Stroh, Sylvain Calinon, Frederic Fol Leymarie, Oliver Deussen, Ariel Shamir  

**一句话要点**：提出长平滑B样条集成方法以生成风格化矢量图形

**关键词**：可微矢量图形, 平滑B样条, 图像抽象, 风格化生成, 路径生成

## 3 点简述
- 核心问题：如何在深度学习中生成平滑且长路径的矢量图形。
- 方法要点：通过线性映射将平滑B样条集成到可微矢量图形管道中。
- 实验效果：应用于风格化路径生成、图像抽象和文本生成，展示多功能性。

## 摘要（原文）

> We integrate smoothing B-splines into a standard differentiable vector
> graphics (DiffVG) pipeline through linear mapping, and show how this can be
> used to generate smooth and arbitrarily long paths within image-based deep
> learning systems. We take advantage of derivative-based smoothing costs for
> parametric control of fidelity vs. simplicity tradeoffs, while also enabling
> stylization control in geometric and image spaces. The proposed pipeline is
> compatible with recent vector graphics generation and vectorization methods. We
> demonstrate the versatility of our approach with four applications aimed at the
> generation of stylized vector graphics: stylized space-filling path generation,
> stroke-based image abstraction, closed-area image abstraction, and stylized
> text generation.

