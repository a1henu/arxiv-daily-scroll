---
layout: default
title: Decomposing and Composing: Towards Efficient Vision-Language Continual Learning via Rank-1 Expert Pool in a Single LoRA
---

# Decomposing and Composing: Towards Efficient Vision-Language Continual Learning via Rank-1 Expert Pool in a Single LoRA
**arXiv**：[2601.22828v1](https://arxiv.org/abs/2601.22828) · [PDF](https://arxiv.org/pdf/2601.22828.pdf)  
**作者**：Zhan Fa, Yue Duan, Jian Zhang, Lei Qi, Wanqi Yang, Yinghuan Shi  

**一句话要点**：提出基于秩-1专家池的单LoRA框架，以解决视觉语言持续学习中的灾难性遗忘问题

**关键词**：视觉语言持续学习, 低秩适应, 秩-1专家池, 正交化损失, 参数高效调优, 灾难性遗忘

## 3 点简述
- 核心问题：视觉语言模型持续学习面临灾难性遗忘和推理负担重的问题
- 方法要点：将单LoRA模块重构为可分解的秩-1专家池，通过稀疏选择和正交化损失实现参数高效更新
- 实验或效果：在多项实验中取得最优结果，参数减少96.7%，无需外部数据或任务ID判别器

## 摘要（原文）

> Continual learning (CL) in vision-language models (VLMs) faces significant challenges in improving task adaptation and avoiding catastrophic forgetting. Existing methods usually have heavy inference burden or rely on external knowledge, while Low-Rank Adaptation (LoRA) has shown potential in reducing these issues by enabling parameter-efficient tuning. However, considering directly using LoRA to alleviate the catastrophic forgetting problem is non-trivial, we introduce a novel framework that restructures a single LoRA module as a decomposable Rank-1 Expert Pool. Our method learns to dynamically compose a sparse, task-specific update by selecting from this expert pool, guided by the semantics of the [CLS] token. In addition, we propose an Activation-Guided Orthogonal (AGO) loss that orthogonalizes critical parts of LoRA weights across tasks. This sparse composition and orthogonalization enable fewer parameter updates, resulting in domain-aware learning while minimizing inter-task interference and maintaining downstream task performance. Extensive experiments across multiple settings demonstrate state-of-the-art results in all metrics, surpassing zero-shot upper bounds in generalization. Notably, it reduces trainable parameters by 96.7% compared to the baseline method, eliminating reliance on external datasets or task-ID discriminators. The merged LoRAs retain less weights and incur no inference latency, making our method computationally lightweight.

