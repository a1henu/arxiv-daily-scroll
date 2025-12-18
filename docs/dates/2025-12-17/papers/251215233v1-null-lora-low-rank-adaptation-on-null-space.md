---
layout: default
title: Null-LoRA: Low-Rank Adaptation on Null Space
---

# Null-LoRA: Low-Rank Adaptation on Null Space
**arXiv**：[2512.15233v1](https://arxiv.org/abs/2512.15233) · [PDF](https://arxiv.org/pdf/2512.15233.pdf)  
**作者**：Yi Zhang, Yulei Kang, Haoxuan Chen, Jinxuan Li, ian-Fang Hu  

**一句话要点**：提出Null-LoRA以在预训练模型零空间进行低秩适应，提升参数效率

**关键词**：低秩适应, 参数高效微调, 零空间, 图像-文本检索, 视觉问答

## 3 点简述
- 现有方法在全参数空间进行低秩适应，但子空间微调可达到类似效果
- Null-LoRA冻结部分低秩矩阵，减少冗余并约束增量更新于零空间
- 在图像-文本检索和视觉问答任务中，以更少参数超越现有方法

## 摘要（原文）

> Parameter-efficient fine-tuning methods have gained considerable popularity for adapting large-scale models to downstream tasks, particularly LoRA and its variants. Existing methods perform low-rank adaptation over the full parameter space. However, fine-tuning within a subspace can achieve comparable effectiveness. Inspired by the observation that pre-trained models possess non-trivial null spaces, we propose Null-space based Low-Rank Adaptation (Null-LoRA). Null-LoRA effectively reduces redundancy and enhances effective rank by freezing portions of the low-rank matrices. To further improve parameter efficiency, Null-LoRA constrains the entire incremental update within the null space, maximizing the utilization of incremental updates to adapt to new task paradigms. Null-LoRA surpasses the state of the art with fewer parameters in extensive experiments across image-text retrieval and visual question answering tasks.

