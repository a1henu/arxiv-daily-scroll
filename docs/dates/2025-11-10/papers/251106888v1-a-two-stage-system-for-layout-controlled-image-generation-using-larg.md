---
layout: default
title: A Two-Stage System for Layout-Controlled Image Generation using Large Language Models and Diffusion Models
---

# A Two-Stage System for Layout-Controlled Image Generation using Large Language Models and Diffusion Models
**arXiv**：[2511.06888v1](https://arxiv.org/abs/2511.06888) · [PDF](https://arxiv.org/pdf/2511.06888.pdf)  
**作者**：Jan-Hendrik Koch, Jonas Krumme, Konrad Gadzicki  

**一句话要点**：提出两阶段系统以解决文本到图像生成中对象计数和空间布局控制不足的问题

**关键词**：布局控制图像生成, 大型语言模型, 扩散模型, 两阶段系统, 对象召回率, 条件生成

## 3 点简述
- 核心问题：文本到图像扩散模型缺乏对对象数量和空间排列的精确控制
- 方法要点：使用大型语言模型生成结构化布局，布局条件扩散模型合成图像
- 实验或效果：对象召回率从57.2%提升至99.9%，比较ControlNet和GLIGEN的权衡

## 摘要（原文）

> Text-to-image diffusion models exhibit remarkable generative capabilities,
> but lack precise control over object counts and spatial arrangements. This work
> introduces a two-stage system to address these compositional limitations. The
> first stage employs a Large Language Model (LLM) to generate a structured
> layout from a list of objects. The second stage uses a layout-conditioned
> diffusion model to synthesize a photorealistic image adhering to this layout.
> We find that task decomposition is critical for LLM-based spatial planning; by
> simplifying the initial generation to core objects and completing the layout
> with rule-based insertion, we improve object recall from 57.2% to 99.9% for
> complex scenes. For image synthesis, we compare two leading conditioning
> methods: ControlNet and GLIGEN. After domain-specific finetuning on
> table-setting datasets, we identify a key trade-off: ControlNet preserves
> text-based stylistic control but suffers from object hallucination, while
> GLIGEN provides superior layout fidelity at the cost of reduced prompt-based
> controllability. Our end-to-end system successfully generates images with
> specified object counts and plausible spatial arrangements, demonstrating the
> viability of a decoupled approach for compositionally controlled synthesis.

