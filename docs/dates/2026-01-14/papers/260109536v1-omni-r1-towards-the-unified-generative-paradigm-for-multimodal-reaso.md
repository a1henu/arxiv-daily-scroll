---
layout: default
title: Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning
---

# Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning
**arXiv**：[2601.09536v1](https://arxiv.org/abs/2601.09536) · [PDF](https://arxiv.org/pdf/2601.09536.pdf)  
**作者**：Dongjie Cheng, Yongqi Li, Zhixin Ma, Hongru Cai, Yupeng Hu, Wenjie Wang, Liqiang Nie, Wenjie Li  

**一句话要点**：提出统一生成式多模态推理范式Omni-R1，通过生成中间图像解决多模态任务泛化问题。

**关键词**：多模态推理, 生成式模型, 统一范式, 功能图像生成, 无监督学习

## 3 点简述
- 核心问题：现有多模态大语言模型多采用单一任务特定推理模式，限制跨任务泛化能力。
- 方法要点：采用两阶段SFT+RL框架，引入感知对齐损失和感知奖励，实现功能图像生成以统一推理技能。
- 实验或效果：Omni-R1在广泛多模态任务中实现统一推理，Omni-R1-Zero无需多模态标注，平均性能匹配或超越Omni-R1。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) are making significant progress in multimodal reasoning. Early approaches focus on pure text-based reasoning. More recent studies have incorporated multimodal information into the reasoning steps; however, they often follow a single task-specific reasoning pattern, which limits their generalizability across various multimodal tasks. In fact, there are numerous multimodal tasks requiring diverse reasoning skills, such as zooming in on a specific region or marking an object within an image. To address this, we propose unified generative multimodal reasoning, which unifies diverse multimodal reasoning skills by generating intermediate images during the reasoning process. We instantiate this paradigm with Omni-R1, a two-stage SFT+RL framework featuring perception alignment loss and perception reward, thereby enabling functional image generation. Additionally, we introduce Omni-R1-Zero, which eliminates the need for multimodal annotations by bootstrapping step-wise visualizations from text-only reasoning data. Empirical results show that Omni-R1 achieves unified generative reasoning across a wide range of multimodal tasks, and Omni-R1-Zero can match or even surpass Omni-R1 on average, suggesting a promising direction for generative multimodal reasoning.

