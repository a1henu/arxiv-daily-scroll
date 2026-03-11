---
layout: default
title: Evolving Prompt Adaptation for Vision-Language Models
---

# Evolving Prompt Adaptation for Vision-Language Models
**arXiv**：[2603.09493v1](https://arxiv.org/abs/2603.09493) · [PDF](https://arxiv.org/pdf/2603.09493.pdf)  
**作者**：Enming Zhang, Jiayang Li, Yanru Wu, Zhenyu Liu, Yang Li  

**一句话要点**：提出EvoPrompt框架，通过进化提示适应解决视觉语言模型在少样本学习中的灾难性遗忘问题。

**关键词**：视觉语言模型, 提示学习, 少样本学习, 灾难性遗忘, 进化训练, 特征正则化

## 3 点简述
- 核心问题：视觉语言模型在少样本下游任务适应时易发生灾难性遗忘，丢失预训练知识。
- 方法要点：采用进化训练策略，解耦低秩更新为方向和幅度分量，结合模态共享提示投影器和特征几何正则化稳定提示演化。
- 实验或效果：在少样本学习中达到先进性能，同时保持预训练模型的零样本能力。

## 摘要（原文）

> The adaptation of large-scale vision-language models (VLMs) to downstream tasks with limited labeled data remains a significant challenge. While parameter-efficient prompt learning methods offer a promising path, they often suffer from catastrophic forgetting of pre-trained knowledge. Toward addressing this limitation, our work is grounded in the insight that governing the evolutionary path of prompts is essential for forgetting-free adaptation. To this end, we propose EvoPrompt, a novel framework designed to explicitly steer the prompt trajectory for stable, knowledge-preserving fine-tuning. Specifically, our approach employs a Modality-Shared Prompt Projector (MPP) to generate hierarchical prompts from a unified embedding space. Critically, an evolutionary training strategy decouples low-rank updates into directional and magnitude components, preserving early-learned semantic directions while only adapting their magnitude, thus enabling prompts to evolve without discarding foundational knowledge. This process is further stabilized by Feature Geometric Regularization (FGR), which enforces feature decorrelation to prevent representation collapse. Extensive experiments demonstrate that EvoPrompt achieves state-of-the-art performance in few-shot learning while robustly preserving the original zero-shot capabilities of pre-trained VLMs.

