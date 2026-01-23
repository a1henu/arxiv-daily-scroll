---
layout: default
title: DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning
---

# DextER: Language-driven Dexterous Grasp Generation with Embodied Reasoning
**arXiv**：[2601.16046v1](https://arxiv.org/abs/2601.16046) · [PDF](https://arxiv.org/pdf/2601.16046.pdf)  
**作者**：Junha Lee, Eunha Park, Minsu Cho  

**一句话要点**：提出DextER方法，通过接触式具身推理解决语言驱动的灵巧抓取生成问题。

**关键词**：灵巧抓取生成, 语言驱动, 具身推理, 接触预测, 多指操作, 任务语义理解

## 3 点简述
- 核心问题：现有方法直接映射观测到抓取参数，缺乏对物理交互的中间推理。
- 方法要点：引入接触式具身推理，预测手部链接与物体表面的接触点作为中间表示。
- 实验或效果：在DexGYS上成功率67.14%，超越现有方法3.83个百分点，意图对齐提升96.4%。

## 摘要（原文）

> Language-driven dexterous grasp generation requires the models to understand task semantics, 3D geometry, and complex hand-object interactions. While vision-language models have been applied to this problem, existing approaches directly map observations to grasp parameters without intermediate reasoning about physical interactions. We present DextER, Dexterous Grasp Generation with Embodied Reasoning, which introduces contact-based embodied reasoning for multi-finger manipulation. Our key insight is that predicting which hand links contact where on the object surface provides an embodiment-aware intermediate representation bridging task semantics with physical constraints. DextER autoregressively generates embodied contact tokens specifying which finger links contact where on the object surface, followed by grasp tokens encoding the hand configuration. On DexGYS, DextER achieves 67.14% success rate, outperforming state-of-the-art by 3.83%p with 96.4% improvement in intention alignment. We also demonstrate steerable generation through partial contact specification, providing fine-grained control over grasp synthesis.

