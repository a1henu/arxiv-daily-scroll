---
layout: default
title: ReasonEdit: Editing Vision-Language Models using Human Reasoning
---

# ReasonEdit: Editing Vision-Language Models using Human Reasoning
**arXiv**：[2602.02408v1](https://arxiv.org/abs/2602.02408) · [PDF](https://arxiv.org/pdf/2602.02408.pdf)  
**作者**：Jiaxing Qiu, Kaihua Hou, Roxana Daneshjou, Ahmed Alaa, Thomas Hartvigsen  

**一句话要点**：提出ReasonEdit以解决视觉语言模型在推理密集型任务中的编辑问题，通过引入人类推理解释

**关键词**：视觉语言模型编辑, 推理密集型任务, 人类推理解释, 多模态嵌入, 代码本检索, 视觉问答

## 3 点简述
- 核心问题：现有视觉语言模型编辑器未处理需要人类和模型共同推理的复杂任务
- 方法要点：利用代码本存储人类推理，通过拓扑平衡多模态嵌入检索相关事实
- 实验或效果：在多个视觉问答数据集上实现最先进的编辑性能，提升编辑泛化能力

## 摘要（原文）

> Model editing aims to correct errors in large, pretrained models without altering unrelated behaviors. While some recent works have edited vision-language models (VLMs), no existing editors tackle reasoning-heavy tasks, which typically require humans and models to reason about images.We therefore propose ReasonEdit, the first VLM editor to let users explain their reasoning during editing, introducing a new, practical model editing setup. ReasonEdit continuously stores human reasoning in a codebook, and retrieves only relevant facts during inference using a novel topology-balanced multimodal embedding method inspired by network science. Across four VLMs on multiple rationale-based visual question answering datasets, ReasonEdit achieves state-of-the-art editing performance, ultimately showing that using human reasoning during editing greatly improves edit generalization.

