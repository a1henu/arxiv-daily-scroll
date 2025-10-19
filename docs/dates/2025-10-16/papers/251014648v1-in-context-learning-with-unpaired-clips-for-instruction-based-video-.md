---
layout: default
title: In-Context Learning with Unpaired Clips for Instruction-based Video Editing
---

# In-Context Learning with Unpaired Clips for Instruction-based Video Editing
**arXiv**：[2510.14648v1](https://arxiv.org/abs/2510.14648) · [PDF](https://arxiv.org/pdf/2510.14648.pdf)  
**作者**：Xinyao Liao, Xianfang Zeng, Ziye Song, Zhoujie Fu, Gang Yu, Guosheng Lin  

**一句话要点**：提出基于上下文学习的无配对视频剪辑预训练策略，以解决指令视频编辑的数据稀缺问题。

**关键词**：指令视频编辑, 上下文学习, 无配对数据预训练, 视频生成模型, 编辑指令对齐

## 3 点简述
- 核心问题：指令视频编辑因大规模配对数据成本高而发展受限。
- 方法要点：利用无配对视频剪辑预训练，赋予模型通用编辑能力，再少量精调。
- 实验效果：在指令对齐和视觉保真度上优于现有方法，提升12%指令遵循和15%编辑质量。

## 摘要（原文）

> Despite the rapid progress of instruction-based image editing, its extension
> to video remains underexplored, primarily due to the prohibitive cost and
> complexity of constructing large-scale paired video editing datasets. To
> address this challenge, we introduce a low-cost pretraining strategy for
> instruction-based video editing that leverages in-context learning from
> unpaired video clips. We show that pretraining a foundation video generation
> model with this strategy endows it with general editing capabilities, such as
> adding, replacing, or deleting operations, according to input editing
> instructions. The pretrained model can then be efficiently refined with a small
> amount of high-quality paired editing data. Built upon HunyuanVideoT2V, our
> framework first pretrains on approximately 1M real video clips to learn basic
> editing concepts, and subsequently fine-tunes on fewer than 150k curated
> editing pairs to extend more editing tasks and improve the editing quality.
> Comparative experiments show that our method surpasses existing
> instruction-based video editing approaches in both instruction alignment and
> visual fidelity, achieving a 12\% improvement in editing instruction following
> and a 15\% improvement in editing quality.

