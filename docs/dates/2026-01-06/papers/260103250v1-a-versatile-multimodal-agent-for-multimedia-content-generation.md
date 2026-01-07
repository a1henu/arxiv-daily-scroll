---
layout: default
title: A Versatile Multimodal Agent for Multimedia Content Generation
---

# A Versatile Multimodal Agent for Multimedia Content Generation
**arXiv**：[2601.03250v1](https://arxiv.org/abs/2601.03250) · [PDF](https://arxiv.org/pdf/2601.03250.pdf)  
**作者**：Daoan Zhang, Wenlin Yao, Xiaoyang Wang, Yebowen Hu, Jiebo Luo, Dong Yu  

**一句话要点**：提出MultiMedia-Agent以自动化复杂多媒体内容生成，整合多模态工具与偏好对齐评估。

**关键词**：多模态代理, 内容生成自动化, 技能习得理论, 计划优化, 偏好对齐评估, 多媒体整合

## 3 点简述
- 核心问题：现有AIGC模型多为单模态组件，难以端到端处理真实世界多模态内容生成任务。
- 方法要点：基于技能习得理论设计数据生成管道与工具库，采用两阶段关联策略优化计划，并通过三阶段训练提升代理性能。
- 实验或效果：对比实验显示MultiMedia-Agent能生成更优多媒体内容，验证了方法的有效性。

## 摘要（原文）

> With the advancement of AIGC (AI-generated content) technologies, an increasing number of generative models are revolutionizing fields such as video editing, music generation, and even film production. However, due to the limitations of current AIGC models, most models can only serve as individual components within specific application scenarios and are not capable of completing tasks end-to-end in real-world applications. In real-world applications, editing experts often work with a wide variety of images and video inputs, producing multimodal outputs -- a video typically includes audio, text, and other elements. This level of integration across multiple modalities is something current models are unable to achieve effectively. However, the rise of agent-based systems has made it possible to use AI tools to tackle complex content generation tasks. To deal with the complex scenarios, in this paper, we propose a MultiMedia-Agent designed to automate complex content creation. Our agent system includes a data generation pipeline, a tool library for content creation, and a set of metrics for evaluating preference alignment. Notably, we introduce the skill acquisition theory to model the training data curation and agent training. We designed a two-stage correlation strategy for plan optimization, including self-correlation and model preference correlation. Additionally, we utilized the generated plans to train the MultiMedia-Agent via a three stage approach including base/success plan finetune and preference optimization. The comparison results demonstrate that the our approaches are effective and the MultiMedia-Agent can generate better multimedia content compared to novel models.

