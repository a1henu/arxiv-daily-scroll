---
layout: default
title: AULLM++: Structural Reasoning with Large Language Models for Micro-Expression Recognition
---

# AULLM++: Structural Reasoning with Large Language Models for Micro-Expression Recognition
**arXiv**：[2603.08387v1](https://arxiv.org/abs/2603.08387) · [PDF](https://arxiv.org/pdf/2603.08387.pdf)  
**作者**：Zhishu Liu, Kaishen Yuan, Bo Zhao, Hui Ma, Zitong Yu  

**一句话要点**：提出AULLM++框架，利用大语言模型进行结构化推理以解决微表情动作单元检测中的关键限制。

**关键词**：微表情识别, 动作单元检测, 大语言模型推理, 图神经网络, 反事实学习, 跨域泛化

## 3 点简述
- 核心问题：现有方法依赖低密度视觉信息、粗粒度特征处理，且忽视动作单元间相关性，导致检测易受噪声干扰和模式解析受限。
- 方法要点：通过多粒度证据增强融合投影器提取内容令牌，结合关系感知动作单元图神经网络编码结构先验，并引入反事实一致性正则化提升泛化能力。
- 实验或效果：在标准基准测试中实现最先进性能，并展现出优越的跨域泛化能力。

## 摘要（原文）

> Micro-expression Action Unit (AU) detection identifies localized AUs from subtle facial muscle activations, providing a foundation for decoding affective cues. Previous methods face three key limitations: (1) heavy reliance on low-density visual information, rendering discriminative evidence vulnerable to background noise; (2) coarse-grained feature processing that misaligns with the demand for fine-grained representations; and (3) neglect of inter-AU correlations, restricting the parsing of complex expression patterns. We propose AULLM++, a reasoning-oriented framework leveraging Large Language Models (LLMs), which injects visual features into textual prompts as actionable semantic premises to guide inference. It formulates AU prediction into three stages: evidence construction, structure modeling, and deduction-based prediction. Specifically, a Multi-Granularity Evidence-Enhanced Fusion Projector (MGE-EFP) fuses mid-level texture cues with high-level semantics, distilling them into a compact Content Token (CT). Furthermore, inspired by micro- and macro-expression AU correspondence, we encode AU relationships as a sparse structural prior and learn interaction strengths via a Relation-Aware AU Graph Neural Network (R-AUGNN), producing an Instruction Token (IT). We then fuse CT and IT into a structured textual prompt and introduce Counterfactual Consistency Regularization (CCR) to construct counterfactual samples, enhancing the model's generalization. Extensive experiments demonstrate AULLM++ achieves state-of-the-art performance on standard benchmarks and exhibits superior cross-domain generalization.

