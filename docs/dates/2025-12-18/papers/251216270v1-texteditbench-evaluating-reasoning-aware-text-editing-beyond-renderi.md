---
layout: default
title: TextEditBench: Evaluating Reasoning-aware Text Editing Beyond Rendering
---

# TextEditBench: Evaluating Reasoning-aware Text Editing Beyond Rendering
**arXiv**：[2512.16270v1](https://arxiv.org/abs/2512.16270) · [PDF](https://arxiv.org/pdf/2512.16270.pdf)  
**作者**：Rui Gui, Yang Wan, Haochen Han, Dongxing Mao, Fangming Liu, Min Li, Alex Jinpeng Wang  

**一句话要点**：提出TextEditBench评估基准，专注于图像中文本区域的推理感知编辑能力。

**关键词**：文本编辑评估, 多模态推理, 语义一致性, 图像生成, 基准测试

## 3 点简述
- 核心问题：图像文本编辑需保持语义、几何和上下文一致性，现有方法对此探索不足。
- 方法要点：引入语义期望维度，评估模型在编辑中的语义一致性和跨模态对齐能力。
- 实验或效果：实验显示当前模型在上下文依赖推理和物理一致性方面仍面临挑战。

## 摘要（原文）

> Text rendering has recently emerged as one of the most challenging frontiers in visual generation, drawing significant attention from large-scale diffusion and multimodal models. However, text editing within images remains largely unexplored, as it requires generating legible characters while preserving semantic, geometric, and contextual coherence. To fill this gap, we introduce TextEditBench, a comprehensive evaluation benchmark that explicitly focuses on text-centric regions in images. Beyond basic pixel manipulations, our benchmark emphasizes reasoning-intensive editing scenarios that require models to understand physical plausibility, linguistic meaning, and cross-modal dependencies. We further propose a novel evaluation dimension, Semantic Expectation (SE), which measures reasoning ability of model to maintain semantic consistency, contextual coherence, and cross-modal alignment during text editing. Extensive experiments on state-of-the-art editing systems reveal that while current models can follow simple textual instructions, they still struggle with context-dependent reasoning, physical consistency, and layout-aware integration. By focusing evaluation on this long-overlooked yet fundamental capability, TextEditBench establishes a new testing ground for advancing text-guided image editing and reasoning in multimodal generation.

