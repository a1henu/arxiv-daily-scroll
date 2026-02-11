---
layout: default
title: SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
---

# SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
**arXiv**：[2602.10116v1](https://arxiv.org/abs/2602.10116) · [PDF](https://arxiv.org/pdf/2602.10116.pdf)  
**作者**：Hongchi Xia, Xuan Li, Zhaoshuo Li, Qianli Ma, Jiashu Xu, Ming-Yu Liu, Yin Cui, Tsung-Yi Lin, Wei-Chiu Ma, Shenlong Wang, Shuran Song, Fangyin Wei  

**一句话要点**：提出SAGE框架，通过智能体迭代生成仿真就绪的3D场景以支持具身AI任务。

**关键词**：具身AI, 3D场景生成, 智能体框架, 仿真就绪环境, 物理稳定性评估

## 3 点简述
- 核心问题：现有场景生成系统依赖规则或任务特定流程，导致伪影和物理无效场景。
- 方法要点：结合布局与对象生成器及评估器，通过迭代推理和自适应工具选择自优化场景。
- 实验或效果：生成环境真实多样，支持策略训练，在未见对象和布局上展现泛化能力。

## 摘要（原文）

> Real-world data collection for embodied agents remains costly and unsafe, calling for scalable, realistic, and simulator-ready 3D environments. However, existing scene-generation systems often rely on rule-based or task-specific pipelines, yielding artifacts and physically invalid scenes. We present SAGE, an agentic framework that, given a user-specified embodied task (e.g., "pick up a bowl and place it on the table"), understands the intent and automatically generates simulation-ready environments at scale. The agent couples multiple generators for layout and object composition with critics that evaluate semantic plausibility, visual realism, and physical stability. Through iterative reasoning and adaptive tool selection, it self-refines the scenes until meeting user intent and physical validity. The resulting environments are realistic, diverse, and directly deployable in modern simulators for policy training. Policies trained purely on this data exhibit clear scaling trends and generalize to unseen objects and layouts, demonstrating the promise of simulation-driven scaling for embodied AI. Code, demos, and the SAGE-10k dataset can be found on the project page here: https://nvlabs.github.io/sage.

