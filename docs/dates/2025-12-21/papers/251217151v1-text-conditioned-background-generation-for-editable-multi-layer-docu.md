---
layout: default
title: Text-Conditioned Background Generation for Editable Multi-Layer Documents
---

# Text-Conditioned Background Generation for Editable Multi-Layer Documents
**arXiv**：[2512.17151v1](https://arxiv.org/abs/2512.17151) · [PDF](https://arxiv.org/pdf/2512.17151.pdf)  
**作者**：Taewon Kang, Joseph K J, Chris Tensmeyer, Jihyung Kil, Wanrong Zhu, Ming C. Lin, Vlad I. Morariu  

**一句话要点**：提出基于扩散模型和潜在掩码的框架，用于生成可编辑多页文档的背景，确保文本可读性和主题连续性。

**关键词**：文档背景生成, 扩散模型, 潜在掩码, 自动可读性优化, 多页一致性, 分层编辑

## 3 点简述
- 核心问题：文档背景生成需保持文本可读性、多页主题一致性和分层编辑能力。
- 方法要点：使用潜在掩码衰减扩散更新，引入自动可读性优化放置半透明形状，通过摘要递归保持多页一致性。
- 实验或效果：训练免费框架生成视觉连贯、文本保留且主题对齐的文档，支持用户提示风格调整。

## 摘要（原文）

> We present a framework for document-centric background generation with multi-page editing and thematic continuity. To ensure text regions remain readable, we employ a \emph{latent masking} formulation that softly attenuates updates in the diffusion space, inspired by smooth barrier functions in physics and numerical optimization. In addition, we introduce \emph{Automated Readability Optimization (ARO)}, which automatically places semi-transparent, rounded backing shapes behind text regions. ARO determines the minimal opacity needed to satisfy perceptual contrast standards (WCAG 2.2) relative to the underlying background, ensuring readability while maintaining aesthetic harmony without human intervention. Multi-page consistency is maintained through a summarization-and-instruction process, where each page is distilled into a compact representation that recursively guides subsequent generations. This design reflects how humans build continuity by retaining prior context, ensuring that visual motifs evolve coherently across an entire document. Our method further treats a document as a structured composition in which text, figures, and backgrounds are preserved or regenerated as separate layers, allowing targeted background editing without compromising readability. Finally, user-provided prompts allow stylistic adjustments in color and texture, balancing automated consistency with flexible customization. Our training-free framework produces visually coherent, text-preserving, and thematically aligned documents, bridging generative modeling with natural design workflows.

