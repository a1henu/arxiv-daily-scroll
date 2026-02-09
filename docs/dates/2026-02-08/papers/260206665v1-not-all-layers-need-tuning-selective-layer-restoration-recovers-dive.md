---
layout: default
title: Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity
---

# Not All Layers Need Tuning: Selective Layer Restoration Recovers Diversity
**arXiv**：[2602.06665v1](https://arxiv.org/abs/2602.06665) · [PDF](https://arxiv.org/pdf/2602.06665.pdf)  
**作者**：Bowen Zhang, Meiyi Wang, Harold Soh  

**一句话要点**：提出选择性层恢复方法以解决后训练导致大语言模型生成多样性下降的问题

**关键词**：大语言模型, 后训练优化, 生成多样性, 层恢复, 模式崩溃, 训练免费方法

## 3 点简述
- 核心问题：后训练提升指令遵循和帮助性，但常导致生成多样性下降，引发模式崩溃
- 方法要点：基于层功能差异假设，通过约束随机字符任务选择层范围，恢复预训练权重以恢复多样性
- 实验或效果：在创意写作、开放问答和多步推理任务中，SLR能显著提升多样性并保持高质量输出

## 摘要（原文）

> Post-training improves instruction-following and helpfulness of large language models (LLMs) but often reduces generation diversity, which leads to repetitive outputs in open-ended settings, a phenomenon known as mode collapse. Motivated by evidence that LLM layers play distinct functional roles, we hypothesize that mode collapse can be localized to specific layers and that restoring a carefully chosen range of layers to their pre-trained weights can recover diversity while maintaining high output quality. To validate this hypothesis and decide which layers to restore, we design a proxy task -- Constrained Random Character(CRC) -- with an explicit validity set and a natural diversity objective. Results on CRC reveal a clear diversity-validity trade-off across restoration ranges and identify configurations that increase diversity with minimal quality loss. Based on these findings, we propose Selective Layer Restoration (SLR), a training-free method that restores selected layers in a post-trained model to their pre-trained weights, yielding a hybrid model with the same architecture and parameter count, incurring no additional inference cost. Across three different tasks (creative writing, open-ended question answering, and multi-step reasoning) and three different model families (Llama, Qwen, and Gemma), we find SLR can consistently and substantially improve output diversity while maintaining high output quality.

