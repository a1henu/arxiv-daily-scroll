---
layout: default
title: BBQ-to-Image: Numeric Bounding Box and Qolor Control in Large-Scale Text-to-Image Models
---

# BBQ-to-Image: Numeric Bounding Box and Qolor Control in Large-Scale Text-to-Image Models
**arXiv**：[2602.20672v1](https://arxiv.org/abs/2602.20672) · [PDF](https://arxiv.org/pdf/2602.20672.pdf)  
**作者**：Eliran Kachlon, Alexander Visheratin, Nimrod Sarid, Tal Hacham, Eyal Gutflaish, Saar Huberman, Hezi Zisman, David Ruppin, Ron Mokady  

**一句话要点**：提出BBQ模型，通过结构化文本框架实现文本到图像生成中的数值边界框和颜色控制。

**关键词**：文本到图像生成, 数值控制, 结构化文本, 边界框对齐, 颜色保真度, 基于流的Transformer

## 3 点简述
- 核心问题：现有文本到图像模型依赖描述性语言，缺乏对物体位置、大小和颜色的精确数值控制。
- 方法要点：在统一结构化文本框架中，直接基于数值边界框和RGB三元组进行条件生成，无需架构修改或推理时优化。
- 实验或效果：在全面评估中，BBQ实现了强边界框对齐，并提升了RGB颜色保真度，优于先进基线。

## 摘要（原文）

> Text-to-image models have rapidly advanced in realism and controllability, with recent approaches leveraging long, detailed captions to support fine-grained generation. However, a fundamental parametric gap remains: existing models rely on descriptive language, whereas professional workflows require precise numeric control over object location, size, and color. In this work, we introduce BBQ, a large-scale text-to-image model that directly conditions on numeric bounding boxes and RGB triplets within a unified structured-text framework. We obtain precise spatial and chromatic control by training on captions enriched with parametric annotations, without architectural modifications or inference-time optimization. This also enables intuitive user interfaces such as object dragging and color pickers, replacing ambiguous iterative prompting with precise, familiar controls. Across comprehensive evaluations, BBQ achieves strong box alignment and improves RGB color fidelity over state-of-the-art baselines. More broadly, our results support a new paradigm in which user intent is translated into an intermediate structured language, consumed by a flow-based transformer acting as a renderer and naturally accommodating numeric parameters.

