---
layout: default
title: Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models
---

# Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models
**arXiv**：[2602.20501v1](https://arxiv.org/abs/2602.20501) · [PDF](https://arxiv.org/pdf/2602.20501.pdf)  
**作者**：Qing Zhang, Xuesong Li, Jing Zhang  

**一句话要点**：融合几何与交互感知实现视觉基础模型中的零样本可供性推理

**关键词**：可供性推理, 视觉基础模型, 几何感知, 交互感知, 零样本学习, 模型融合

## 3 点简述
- 核心问题：探讨视觉系统理解可供性的本质，强调几何感知与交互感知的互补作用。
- 方法要点：系统探测视觉基础模型，发现DINO编码几何结构，Flux提供交互先验，并训练免费融合两者。
- 实验或效果：通过零样本融合实现可供性估计，性能媲美弱监督方法，验证几何与交互感知为基本构建块。

## 摘要（原文）

> What does it mean for a visual system to truly understand affordance? We argue that this understanding hinges on two complementary capacities: geometric perception, which identifies the structural parts of objects that enable interaction, and interaction perception, which models how an agent's actions engage with those parts. To test this hypothesis, we conduct a systematic probing of Visual Foundation Models (VFMs). We find that models like DINO inherently encode part-level geometric structures, while generative models like Flux contain rich, verb-conditioned spatial attention maps that serve as implicit interaction priors. Crucially, we demonstrate that these two dimensions are not merely correlated but are composable elements of affordance. By simply fusing DINO's geometric prototypes with Flux's interaction maps in a training-free and zero-shot manner, we achieve affordance estimation competitive with weakly-supervised methods. This final fusion experiment confirms that geometric and interaction perception are the fundamental building blocks of affordance understanding in VFMs, providing a mechanistic account of how perception grounds action.

