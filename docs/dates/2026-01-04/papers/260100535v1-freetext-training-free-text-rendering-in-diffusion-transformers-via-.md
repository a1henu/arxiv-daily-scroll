---
layout: default
title: FreeText: Training-Free Text Rendering in Diffusion Transformers via Attention Localization and Spectral Glyph Injection
---

# FreeText: Training-Free Text Rendering in Diffusion Transformers via Attention Localization and Spectral Glyph Injection
**arXiv**：[2601.00535v1](https://arxiv.org/abs/2601.00535) · [PDF](https://arxiv.org/pdf/2601.00535.pdf)  
**作者**：Ruiqiang Zhang, Hengyi Wang, Chang Liu, Guanjie Wang, Zehua Ma, Weiming Zhang  

**一句话要点**：提出FreeText框架，通过注意力定位与频谱字形注入，在扩散变换器中实现免训练文本渲染

**关键词**：文本渲染, 扩散变换器, 免训练框架, 注意力定位, 频谱调制, 字形注入

## 3 点简述
- 核心问题：扩散模型在文本渲染上存在困难，如多行布局和中文等长尾脚本，现有方法需重训练或外部约束
- 方法要点：利用扩散变换器内源机制，分解为位置定位（基于注意力锚点）和内容注入（频谱调制字形先验）
- 实验或效果：在多个模型和基准上验证，提升文本可读性，保持语义对齐与美学质量，推理开销小

## 摘要（原文）

> Large-scale text-to-image (T2I) diffusion models excel at open-domain synthesis but still struggle with precise text rendering, especially for multi-line layouts, dense typography, and long-tailed scripts such as Chinese. Prior solutions typically require costly retraining or rigid external layout constraints, which can degrade aesthetics and limit flexibility. We propose \textbf{FreeText}, a training-free, plug-and-play framework that improves text rendering by exploiting intrinsic mechanisms of \emph{Diffusion Transformer (DiT)} models. \textbf{FreeText} decomposes the problem into \emph{where to write} and \emph{what to write}. For \emph{where to write}, we localize writing regions by reading token-wise spatial attribution from endogenous image-to-text attention, using sink-like tokens as stable spatial anchors and topology-aware refinement to produce high-confidence masks. For \emph{what to write}, we introduce Spectral-Modulated Glyph Injection (SGMI), which injects a noise-aligned glyph prior with frequency-domain band-pass modulation to strengthen glyph structure and suppress semantic leakage (rendering the concept instead of the word). Extensive experiments on Qwen-Image, FLUX.1-dev, and SD3 variants across longText-Benchmark, CVTG, and our CLT-Bench show consistent gains in text readability while largely preserving semantic alignment and aesthetic quality, with modest inference overhead.

