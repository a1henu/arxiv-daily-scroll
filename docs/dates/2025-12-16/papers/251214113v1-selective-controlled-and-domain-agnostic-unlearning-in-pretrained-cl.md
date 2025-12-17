---
layout: default
title: Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach
---

# Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach
**arXiv**：[2512.14113v1](https://arxiv.org/abs/2512.14113) · [PDF](https://arxiv.org/pdf/2512.14113.pdf)  
**作者**：Ashish Mishra, Gyanaranjan Nayak, Tarun Kumar, Arpit Shah, Suparna Bhattacharya, Martin Foltin  

**一句话要点**：提出训练与数据无关的遗忘框架，实现CLIP模型中对特定类别的选择性、可控和领域无关的遗忘。

**关键词**：模型遗忘, CLIP模型, 多模态学习, 零样本分类, 训练无关方法

## 3 点简述
- 核心问题：预训练模型如CLIP需移除特定对象类别，无需额外数据或重训练，且不影响无关任务性能。
- 方法要点：利用多模态零空间，通过文本提示和合成视觉原型协同集成，高效移除不需要的类别信息。
- 实验或效果：支持三种遗忘范式，包括全局遗忘、领域特定知识移除和选择性领域完全遗忘，提供灵活高效解决方案。

## 摘要（原文）

> Pretrained models like CLIP have demonstrated impressive zero-shot classification capabilities across diverse visual domains, spanning natural images, artistic renderings, and abstract representations. However, real-world applications often demand the removal (or "unlearning") of specific object classes without requiring additional data or retraining, or affecting the model's performance on unrelated tasks. In this paper, we propose a novel training- and data-free unlearning framework that enables three distinct forgetting paradigms: (1) global unlearning of selected objects across all domains, (2) domain-specific knowledge removal (e.g., eliminating sketch representations while preserving photo recognition), and (3) complete unlearning in selective domains. By leveraging a multimodal nullspace through synergistic integration of text prompts and synthesized visual prototypes derived from CLIP's joint embedding space, our method efficiently removes undesired class information while preserving the remaining knowledge. This approach overcomes the limitations of existing retraining-based methods and offers a flexible and computationally efficient solution for controlled model forgetting.

