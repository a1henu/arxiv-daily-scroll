---
layout: default
title: 3D Space as a Scratchpad for Editable Text-to-Image Generation
---

# 3D Space as a Scratchpad for Editable Text-to-Image Generation
**arXiv**：[2601.14602v1](https://arxiv.org/abs/2601.14602) · [PDF](https://arxiv.org/pdf/2601.14602.pdf)  
**作者**：Oindrila Saha, Vojtech Krs, Radomir Mech, Subhransu Maji, Matheus Gadelha, Kevin Blackburn-Matzen  

**一句话要点**：提出3D空间草稿本方法，通过显式3D推理提升文本到图像生成的空间一致性和可编辑性。

**关键词**：文本到图像生成, 3D推理, 空间一致性, 可编辑图像生成, 视觉语言模型

## 3 点简述
- 问题：视觉语言模型缺乏空间推理机制，难以生成准确反映几何关系和对象身份的图像。
- 方法：将文本提示解析为可编辑3D网格，通过代理场景规划进行布局和视角选择，再渲染回图像域。
- 效果：在GenAI-Bench上文本对齐度提升32%，支持直观3D编辑并可靠传播到最终图像。

## 摘要（原文）

> Recent progress in large language models (LLMs) has shown that reasoning improves when intermediate thoughts are externalized into explicit workspaces, such as chain-of-thought traces or tool-augmented reasoning. Yet, visual language models (VLMs) lack an analogous mechanism for spatial reasoning, limiting their ability to generate images that accurately reflect geometric relations, object identities, and compositional intent. We introduce the concept of a spatial scratchpad -- a 3D reasoning substrate that bridges linguistic intent and image synthesis. Given a text prompt, our framework parses subjects and background elements, instantiates them as editable 3D meshes, and employs agentic scene planning for placement, orientation, and viewpoint selection. The resulting 3D arrangement is rendered back into the image domain with identity-preserving cues, enabling the VLM to generate spatially consistent and visually coherent outputs. Unlike prior 2D layout-based methods, our approach supports intuitive 3D edits that propagate reliably into final images. Empirically, it achieves a 32% improvement in text alignment on GenAI-Bench, demonstrating the benefit of explicit 3D reasoning for precise, controllable image generation. Our results highlight a new paradigm for vision-language models that deliberate not only in language, but also in space. Code and visualizations at https://oindrilasaha.github.io/3DScratchpad/

