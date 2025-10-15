---
layout: default
title: DRL: Discriminative Representation Learning with Parallel Adapters for Class Incremental Learning
---

# DRL: Discriminative Representation Learning with Parallel Adapters for Class Incremental Learning
**arXiv**：[2510.12107v1](https://arxiv.org/abs/2510.12107) · [PDF](https://arxiv.org/pdf/2510.12107.pdf)  
**作者**：Jiawei Zhan, Jun Liu, Jinlong Peng, Xiaochen Chen, Bin-Bin Gao, Yong Liu, Chengjie Wang  

**一句话要点**：提出DRL框架，通过并行适配器和解耦锚监督解决类增量学习中的模型复杂度和表示不一致问题。

**关键词**：类增量学习, 预训练模型, 并行适配器, 解耦锚监督, 表示学习, 轻量级学习

## 3 点简述
- 核心问题：类增量学习中模型复杂度增加、表示偏移不平滑及阶段优化与全局推断不一致。
- 方法要点：使用增量并行适配器网络，轻量级适配器通过传输门继承表示能力，确保平滑表示转移。
- 实验或效果：在六个基准测试中，DRL持续优于现有方法，训练和推断效率高。

## 摘要（原文）

> With the excellent representation capabilities of Pre-Trained Models (PTMs),
> remarkable progress has been made in non-rehearsal Class-Incremental Learning
> (CIL) research. However, it remains an extremely challenging task due to three
> conundrums: increasingly large model complexity, non-smooth representation
> shift during incremental learning and inconsistency between stage-wise
> sub-problem optimization and global inference. In this work, we propose the
> Discriminative Representation Learning (DRL) framework to specifically address
> these challenges. To conduct incremental learning effectively and yet
> efficiently, the DRL's network, called Incremental Parallel Adapter (IPA)
> network, is built upon a PTM and increasingly augments the model by learning a
> lightweight adapter with a small amount of parameter learning overhead in each
> incremental stage. The adapter is responsible for adapting the model to new
> classes, it can inherit and propagate the representation capability from the
> current model through parallel connection between them by a transfer gate. As a
> result, this design guarantees a smooth representation shift between different
> incremental stages. Furthermore, to alleviate inconsistency and enable
> comparable feature representations across incremental stages, we design the
> Decoupled Anchor Supervision (DAS). It decouples constraints of positive and
> negative samples by respectively comparing them with the virtual anchor. This
> decoupling promotes discriminative representation learning and aligns the
> feature spaces learned at different stages, thereby narrowing the gap between
> stage-wise local optimization over a subset of data and global inference across
> all classes. Extensive experiments on six benchmarks reveal that our DRL
> consistently outperforms other state-of-the-art methods throughout the entire
> CIL period while maintaining high efficiency in both training and inference
> phases.

