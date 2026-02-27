---
layout: default
title: Evaluating Zero-Shot and One-Shot Adaptation of Small Language Models in Leader-Follower Interaction
---

# Evaluating Zero-Shot and One-Shot Adaptation of Small Language Models in Leader-Follower Interaction
**arXiv**：[2602.23312v1](https://arxiv.org/abs/2602.23312) · [PDF](https://arxiv.org/pdf/2602.23312.pdf)  
**作者**：Rafael R. Baptista, André de Lima Salgado, Ricardo V. Godoy, Marcelo Becker, Thiago Boaventura, Gustavo J. G. Lahr  

**一句话要点**：评估小语言模型在零样本和单样本适应下的人机交互角色分类性能

**关键词**：小语言模型, 人机交互, 角色分类, 零样本适应, 微调, 边缘计算

## 3 点简述
- 核心问题：资源受限移动机器人实时角色分配挑战，大模型部署受限。
- 方法要点：基于新数据集，比较提示工程与微调在零/单样本模式下的效果。
- 实验或效果：Qwen2.5-0.5B零样本微调达86.66%准确率，单样本模式性能下降。

## 摘要（原文）

> Leader-follower interaction is an important paradigm in human-robot interaction (HRI). Yet, assigning roles in real time remains challenging for resource-constrained mobile and assistive robots. While large language models (LLMs) have shown promise for natural communication, their size and latency limit on-device deployment. Small language models (SLMs) offer a potential alternative, but their effectiveness for role classification in HRI has not been systematically evaluated. In this paper, we present a benchmark of SLMs for leader-follower communication, introducing a novel dataset derived from a published database and augmented with synthetic samples to capture interaction-specific dynamics. We investigate two adaptation strategies: prompt engineering and fine-tuning, studied under zero-shot and one-shot interaction modes, compared with an untrained baseline. Experiments with Qwen2.5-0.5B reveal that zero-shot fine-tuning achieves robust classification performance (86.66% accuracy) while maintaining low latency (22.2 ms per sample), significantly outperforming baseline and prompt-engineered approaches. However, results also indicate a performance degradation in one-shot modes, where increased context length challenges the model's architectural capacity. These findings demonstrate that fine-tuned SLMs provide an effective solution for direct role assignment, while highlighting critical trade-offs between dialogue complexity and classification reliability on the edge.

