---
layout: default
title: SceneAlign: Aligning Multimodal Reasoning to Scene Graphs in Complex Visual Scenes
---

# SceneAlign: Aligning Multimodal Reasoning to Scene Graphs in Complex Visual Scenes
**arXiv**：[2601.05600v1](https://arxiv.org/abs/2601.05600) · [PDF](https://arxiv.org/pdf/2601.05600.pdf)  
**作者**：Chuhan Wang, Xintong Li, Jennifer Yuntong Zhang, Junda Wu, Chengkai Huang, Lina Yao, Julian McAuley, Jingbo Shang  

**一句话要点**：提出SceneAlign框架，利用场景图进行可控结构干预以提升复杂视觉场景中的多模态推理忠实性。

**关键词**：多模态推理, 场景图, 直接偏好优化, 视觉接地, 结构干预, 推理忠实性

## 3 点简述
- 核心问题：多模态大语言模型在复杂视觉场景中推理不忠实，常出现幻觉实体、错误接地、跳过步骤和过度指定推理。
- 方法要点：基于场景图识别关键节点，通过四种针对性扰动策略构建硬负例理性，用于直接偏好优化以引导模型进行细粒度结构忠实推理。
- 实验或效果：在七个视觉推理基准测试中，SceneAlign持续提升答案准确性和推理忠实性，验证了接地感知对齐的有效性。

## 摘要（原文）

> Multimodal large language models often struggle with faithful reasoning in complex visual scenes, where intricate entities and relations require precise visual grounding at each step. This reasoning unfaithfulness frequently manifests as hallucinated entities, mis-grounded relations, skipped steps, and over-specified reasoning. Existing preference-based approaches, typically relying on textual perturbations or answer-conditioned rationales, fail to address this challenge as they allow models to exploit language priors to bypass visual grounding. To address this, we propose SceneAlign, a framework that leverages scene graphs as structured visual information to perform controllable structural interventions. By identifying reasoning-critical nodes and perturbing them through four targeted strategies that mimic typical grounding failures, SceneAlign constructs hard negative rationales that remain linguistically plausible but are grounded in inaccurate visual facts. These contrastive pairs are used in Direct Preference Optimization to steer models toward fine-grained, structure-faithful reasoning. Across seven visual reasoning benchmarks, SceneAlign consistently improves answer accuracy and reasoning faithfulness, highlighting the effectiveness of grounding-aware alignment for multimodal reasoning.

