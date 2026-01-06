---
layout: default
title: Thinking with Blueprints: Assisting Vision-Language Models in Spatial Reasoning via Structured Object Representation
---

# Thinking with Blueprints: Assisting Vision-Language Models in Spatial Reasoning via Structured Object Representation
**arXiv**：[2601.01984v1](https://arxiv.org/abs/2601.01984) · [PDF](https://arxiv.org/pdf/2601.01984.pdf)  
**作者**：Weijian Ma, Shizhao Sun, Tianyu Yu, Ruiyu Wang, Tat-Seng Chua, Jiang Bian  

**一句话要点**：提出基于对象中心蓝图的视觉语言模型增强方法以解决空间推理问题

**关键词**：空间推理, 视觉语言模型, 对象中心蓝图, 结构化表示, 强化学习奖励, 抗捷径数据增强

## 3 点简述
- 核心问题：现有方法在空间推理中局部感知与全局组织难以兼顾，影响视觉语言模型的空间语义理解。
- 方法要点：引入对象中心蓝图作为结构化表示，结合监督微调、强化学习奖励和抗捷径数据增强技术。
- 实验或效果：实验表明该方法在空间推理任务上优于现有视觉语言模型和专用模型，提升推理性能。

## 摘要（原文）

> Spatial reasoning -- the ability to perceive and reason about relationships in space -- advances vision-language models (VLMs) from visual perception toward spatial semantic understanding. Existing approaches either revisit local image patches, improving fine-grained perception but weakening global spatial awareness, or mark isolated coordinates, which capture object locations but overlook their overall organization. In this work, we integrate the cognitive concept of an object-centric blueprint into VLMs to enhance spatial reasoning. Given an image and a question, the model first constructs a JSON-style blueprint that records the positions, sizes, and attributes of relevant objects, and then reasons over this structured representation to produce the final answer. To achieve this, we introduce three key techniques: (1) blueprint-embedded reasoning traces for supervised fine-tuning to elicit basic reasoning skills; (2) blueprint-aware rewards in reinforcement learning to encourage the blueprint to include an appropriate number of objects and to align final answers with this causal reasoning; and (3) anti-shortcut data augmentation that applies targeted perturbations to images and questions, discouraging reliance on superficial visual or linguistic cues. Experiments show that our method consistently outperforms existing VLMs and specialized spatial reasoning models.

