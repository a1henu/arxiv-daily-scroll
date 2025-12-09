---
layout: default
title: MMRPT: MultiModal Reinforcement Pre-Training via Masked Vision-Dependent Reasoning
---

# MMRPT: MultiModal Reinforcement Pre-Training via Masked Vision-Dependent Reasoning
**arXiv**：[2512.07203v1](https://arxiv.org/abs/2512.07203) · [PDF](https://arxiv.org/pdf/2512.07203.pdf)  
**作者**：Xuhui Zheng, Kang An, Ziliang Wang, Yuhang Wang, Faqiang Qian, Yichao Wu  

**一句话要点**：提出MMRPT框架，通过掩码多模态强化预训练增强视觉推理，解决多模态预训练中的描述性偏差问题。

**关键词**：多模态预训练, 强化学习, 视觉推理, 掩码学习, 零样本学习, 鲁棒性增强

## 3 点简述
- 核心问题：多模态预训练受图像-文本对描述性偏差限制，模型依赖表面语言线索而非视觉理解。
- 方法要点：首次将强化学习直接融入预训练，通过掩码视觉依赖片段并基于语义-视觉奖励重构，奖励视觉基础而非文本模仿。
- 实验或效果：在零样本基准测试中一致提升，监督微调下显著增强鲁棒性，证明强化驱动的掩码推理提供更可靠预训练目标。

## 摘要（原文）

> Multimodal pre-training remains constrained by the descriptive bias of image-caption pairs, leading models to favor surface linguistic cues over grounded visual understanding. We introduce MMRPT, a masked multimodal reinforcement pre-training framework that strengthens visual reasoning in MLLMs. We are the first to incorporate reinforcement learning directly into the pre-training of large vision-language models, enabling learning signals that reward visual grounding rather than caption imitation. MMRPT constructs masked multimodal data by estimating sentence-level visual dependency via attention over visual tokens and masking highly vision-dependent segments; the model reconstructs these spans through vision-grounded reasoning guided by a semantic-visual reward. Experiments show consistent zero-shot gains across diverse benchmarks and substantially improved robustness under supervised fine-tuning, demonstrating that reinforcement-driven masked reasoning provides a more reliable and generalizable pre-training objective for multimodal models.

