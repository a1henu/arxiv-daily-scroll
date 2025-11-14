---
layout: default
title: AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models
---

# AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models
**arXiv**：[2511.10017v1](https://arxiv.org/abs/2511.10017) · [PDF](https://arxiv.org/pdf/2511.10017.pdf)  
**作者**：Xinyi Wang, Xun Yang, Yanlong Xu, Yuchen Wu, Zhen Li, Na Zhao  

**一句话要点**：提出AffordBot框架，通过多模态大语言模型解决3D细粒度具身推理任务。

**关键词**：3D细粒度具身推理, 多模态大语言模型, 链式思维推理, 可供性预测, 3D场景理解, 点云输入

## 3 点简述
- 核心问题：现有方法在物体级别或分离处理细粒度可供性推理，缺乏指令驱动的连贯推理。
- 方法要点：集成MLLMs与链式思维推理，渲染环绕视图并投影3D候选元素以对齐场景几何。
- 实验或效果：在SceneFun3D数据集上实现最优性能，仅用3D点云输入和MLLMs展示强泛化能力。

## 摘要（原文）

> Effective human-agent collaboration in physical environments requires understanding not only what to act upon, but also where the actionable elements are and how to interact with them. Existing approaches often operate at the object level or disjointedly handle fine-grained affordance reasoning, lacking coherent, instruction-driven grounding and reasoning. In this work, we introduce a new task: Fine-grained 3D Embodied Reasoning, which requires an agent to predict, for each referenced affordance element in a 3D scene, a structured triplet comprising its spatial location, motion type, and motion axis, based on a task instruction. To solve this task, we propose AffordBot, a novel framework that integrates Multimodal Large Language Models (MLLMs) with a tailored chain-of-thought (CoT) reasoning paradigm. To bridge the gap between 3D input and 2D-compatible MLLMs, we render surround-view images of the scene and project 3D element candidates into these views, forming a rich visual representation aligned with the scene geometry. Our CoT pipeline begins with an active perception stage, prompting the MLLM to select the most informative viewpoint based on the instruction, before proceeding with step-by-step reasoning to localize affordance elements and infer plausible interaction motions. Evaluated on the SceneFun3D dataset, AffordBot achieves state-of-the-art performance, demonstrating strong generalization and physically grounded reasoning with only 3D point cloud input and MLLMs.

