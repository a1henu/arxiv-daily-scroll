---
layout: default
title: Collaborative Low-Rank Adaptation for Pre-Trained Vision Transformers
---

# Collaborative Low-Rank Adaptation for Pre-Trained Vision Transformers
**arXiv**：[2512.24603v1](https://arxiv.org/abs/2512.24603) · [PDF](https://arxiv.org/pdf/2512.24603.pdf)  
**作者**：Zheng Liu, Jinchao Zhu, Gao Huang  

**一句话要点**：提出协作低秩适应方法以平衡预训练视觉Transformer微调中的性能与参数效率

**关键词**：低秩适应, 视觉Transformer微调, 参数效率, 协作学习, 点云分析

## 3 点简述
- 现有低秩适应方法在微调预训练视觉Transformer时，难以平衡学习性能与参数效率。
- CLoRA通过基础空间共享和样本无关多样性增强组件，协作构建低秩模块以提升学习能力。
- 实验表明，CLoRA在图像和点云数据集上优于现有方法，实现更好平衡且计算开销低。

## 摘要（原文）

> Low-rank adaptation (LoRA) has achieved remarkable success in fine-tuning pre-trained vision transformers for various downstream tasks. Existing studies mainly focus on exploring more parameter-efficient strategies or more effective representation learning schemes. However, these methods either sacrifice fine-tuning performance or introduce excessive trainable parameters, failing to strike a balance between learning performance and parameter efficiency. To address this problem, we propose a novel tuning method named collaborative low-rank adaptation (CLoRA) in this paper. CLoRA consists of base-space sharing and sample-agnostic diversity enhancement (SADE) components. To maintain parameter efficiency while expanding the learning capacity of low-rank modules (LRMs), base-space sharing allows all LRMs to share a set of down/up-projection spaces. In CLoRA, the low-rank matrices obtained from the shared spaces collaboratively construct each LRM. Since the representations extracted by these matrices may contain redundant information, SADE is employed to regularize the similarities among them to encourage diverse representations in the training process. We conduct extensive experiments on widely used image and point cloud datasets to evaluate the performance of CLoRA. Experimental results demonstrate that CLoRA strikes a better balance between learning performance and parameter efficiency, while requiring the fewest GFLOPs for point cloud analysis, compared with the state-of-the-art methods.

