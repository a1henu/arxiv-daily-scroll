---
layout: default
title: NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion
---

# NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion
**arXiv**：[2603.06533v1](https://arxiv.org/abs/2603.06533) · [PDF](https://arxiv.org/pdf/2603.06533.pdf)  
**作者**：Taewon Kang, Ming C. Lin  

**一句话要点**：提出NEGATE方法，通过约束语义引导在扩散模型中统一处理语言否定问题

**关键词**：文本到视频生成, 扩散模型, 语言否定, 语义引导, 约束优化, 训练免费方法

## 3 点简述
- 核心问题：扩散生成系统对语言否定建模不足，缺乏统一框架
- 方法要点：将否定建模为扩散动态中的可行性约束，通过投影更新实现训练免费处理
- 实验或效果：在图像和视频生成中实现稳健否定合规，保持视觉保真度和结构连贯性

## 摘要（原文）

> Negation is a fundamental linguistic operator, yet it remains inadequately modeled in diffusion-based generative systems. In this work, we present a formal treatment of linguistic negation in diffusion-based generative models by modeling it as a structured feasibility constraint on semantic guidance within diffusion dynamics. Rather than introducing heuristics or retraining model parameters, we reinterpret classifier-free guidance as defining a semantic update direction and enforce negation by projecting the update onto a convex constraint set derived from linguistic structure. This novel formulation provides a unified framework for handling diverse negation phenomena, including object absence, graded non-inversion semantics, multi-negation composition, and scope-sensitive disambiguation. Our approach is training-free, compatible with pretrained diffusion backbones, and naturally extends from image generation to temporally evolving video trajectories. In addition, we introduce a structured negation-centric benchmark suite that isolates distinct linguistic failure modes in generative systems, to further research in this area. Experiments demonstrate that our method achieves robust negation compliance while preserving visual fidelity and structural coherence, establishing the first unified formulation of linguistic negation in diffusion-based generative models beyond representation-level evaluation.

