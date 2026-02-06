---
layout: default
title: VisRefiner: Learning from Visual Differences for Screenshot-to-Code Generation
---

# VisRefiner: Learning from Visual Differences for Screenshot-to-Code Generation
**arXiv**：[2602.05998v1](https://arxiv.org/abs/2602.05998) · [PDF](https://arxiv.org/pdf/2602.05998.pdf)  
**作者**：Jie Deng, Kaichun Yao, Libo Zhang  

**一句话要点**：提出VisRefiner框架，通过视觉差异学习提升截图到代码生成的准确性和自优化能力。

**关键词**：截图到代码生成, 视觉差异学习, 强化学习, 自优化, 布局保真度, 多模态大语言模型

## 3 点简述
- 现有模型直接从截图生成代码，但未观察生成代码的视觉结果，导致布局和样式保真度不足。
- VisRefiner引入差异对齐监督，关联视觉差异与代码编辑，并采用强化学习阶段进行自优化。
- 实验表明，VisRefiner显著提升单步生成质量和布局保真度，并赋予模型强大的自优化能力。

## 摘要（原文）

> Screenshot-to-code generation aims to translate user interface screenshots into executable frontend code that faithfully reproduces the target layout and style. Existing multimodal large language models perform this mapping directly from screenshots but are trained without observing the visual outcomes of their generated code. In contrast, human developers iteratively render their implementation, compare it with the design, and learn how visual differences relate to code changes. Inspired by this process, we propose VisRefiner, a training framework that enables models to learn from visual differences between rendered predictions and reference designs. We construct difference-aligned supervision that associates visual discrepancies with corresponding code edits, allowing the model to understand how appearance variations arise from implementation changes. Building on this, we introduce a reinforcement learning stage for self-refinement, where the model improves its generated code by observing both the rendered output and the target design, identifying their visual differences, and updating the code accordingly. Experiments show that VisRefiner substantially improves single-step generation quality and layout fidelity, while also endowing models with strong self-refinement ability. These results demonstrate the effectiveness of learning from visual differences for advancing screenshot-to-code generation.

