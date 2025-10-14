---
layout: default
title: COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision Language Models
---

# COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision Language Models
**arXiv**：[2510.11012v1](https://arxiv.org/abs/2510.11012) · [PDF](https://arxiv.org/pdf/2510.11012.pdf)  
**作者**：Sanchit Sinha, Guangzhi Xiong, Aidong Zhang  

**一句话要点**：提出COCO-Tree概念树方法以增强视觉语言模型的组合推理能力

**关键词**：视觉语言模型, 组合推理, 概念树, 神经符号方法, 基准测试, 解释性推理

## 3 点简述
- 核心问题：视觉语言模型在组合推理中表现不佳，难以理解多对象、属性和关系的交互。
- 方法要点：使用神经符号概念树从大型语言模型学习，提升推理过程并提供解释性。
- 实验或效果：在多个基准测试中，组合泛化性能提升5-10%，优于基线方法。

## 摘要（原文）

> Compositional reasoning remains a persistent weakness of modern vision
> language models (VLMs): they often falter when a task hinges on understanding
> how multiple objects, attributes, and relations interact within an image.
> Multiple research works have attempted to improve compositionality performance
> by creative tricks such as improving prompt structure, chain of thought
> reasoning, etc. A more recent line of work attempts to impart additional
> reasoning in VLMs using well-trained Large Language Models (LLMs), which are
> far superior in linguistic understanding than VLMs to compensate for the
> limited linguistic prowess of VLMs. However, these approaches are either
> resource-intensive or do not provide an interpretable reasoning process. In
> this paper, we present 'COCO-Tree' - a novel approach that augments VLM outputs
> with carefully designed neurosymbolic concept trees learned from LLMs to
> improve VLM's linguistic reasoning. COCO-Tree's beam search-inspired reasoning
> process boosts compositionality performance and provides a rationale behind VLM
> predictions. Empirical results on four compositionality benchmarks, Winoground,
> EqBench, ColorSwap, and SugarCrepe, in seven different open-source VLMs with
> varying sizes, demonstrate that COCO-Tree significantly improves compositional
> generalization by 5-10% over baselines.

