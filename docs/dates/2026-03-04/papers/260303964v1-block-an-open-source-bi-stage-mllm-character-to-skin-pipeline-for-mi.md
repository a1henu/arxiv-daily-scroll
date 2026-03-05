---
layout: default
title: BLOCK: An Open-Source Bi-Stage MLLM Character-to-Skin Pipeline for Minecraft
---

# BLOCK: An Open-Source Bi-Stage MLLM Character-to-Skin Pipeline for Minecraft
**arXiv**：[2603.03964v1](https://arxiv.org/abs/2603.03964) · [PDF](https://arxiv.org/pdf/2603.03964.pdf)  
**作者**：Hengquan Guo  

**一句话要点**：提出BLOCK开源双阶段流程，通过MLLM和FLUX.2模型从任意角色概念生成像素级Minecraft皮肤。

**关键词**：多模态大模型, 图像生成, 渐进式微调, 开源工具, Minecraft皮肤

## 3 点简述
- 核心问题：从任意角色概念生成像素级Minecraft皮肤，涉及概念到预览和预览到皮肤的转换。
- 方法要点：采用双阶段流程，包括MLLM驱动的3D预览合成和FLUX.2模型的皮肤解码，并引入EvolveLoRA渐进式训练。
- 实验或效果：发布开源代码、提示模板和微调权重，支持可复现的角色到皮肤生成，具体效果未知。

## 摘要（原文）

> We present \textbf{BLOCK}, an open-source bi-stage character-to-skin pipeline that generates pixel-perfect Minecraft skins from arbitrary character concepts. BLOCK decomposes the problem into (i) a \textbf{3D preview synthesis stage} driven by a large multimodal model (MLLM) with a carefully designed prompt-and-reference template, producing a consistent dual-panel (front/back) oblique-view Minecraft-style preview; and (ii) a \textbf{skin decoding stage} based on a fine-tuned FLUX.2 model that translates the preview into a skin atlas image. We further propose \textbf{EvolveLoRA}, a progressive LoRA curriculum (text-to-image $\rightarrow$ image-to-image $\rightarrow$ preview-to-skin) that initializes each phase from the previous adapter to improve stability and efficiency. BLOCK is released with all prompt templates and fine-tuned weights to support reproducible character-to-skin generation.

