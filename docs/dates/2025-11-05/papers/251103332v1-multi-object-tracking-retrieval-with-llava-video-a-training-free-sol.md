---
layout: default
title: Multi-Object Tracking Retrieval with LLaVA-Video: A Training-Free Solution to MOT25-StAG Challenge
---

# Multi-Object Tracking Retrieval with LLaVA-Video: A Training-Free Solution to MOT25-StAG Challenge
**arXiv**：[2511.03332v1](https://arxiv.org/abs/2511.03332) · [PDF](https://arxiv.org/pdf/2511.03332.pdf)  
**作者**：Yi Yang, Yiming Xu, Timo Kaiser, Hao Cheng, Bodo Rosenhahn, Michael Ying Yang  

**一句话要点**：提出基于FastTracker和LLaVA-Video的两阶段零样本方法，解决MOT25-StAG挑战中的多目标跟踪检索问题。

**关键词**：多目标跟踪, 视频检索, 零样本学习, 多模态大模型, 语言查询定位

## 3 点简述
- 核心问题：在复杂真实场景视频中，根据自由形式语言查询准确定位和跟踪多个对象。
- 方法要点：将任务建模为视频检索，结合SOTA跟踪模型和LLaVA-Video多模态大模型。
- 实验或效果：在MOT25-StAG测试集上，m-HIoU和HOTA得分分别为20.68和10.73，获挑战第二名。

## 摘要（原文）

> In this report, we present our solution to the MOT25-Spatiotemporal Action
> Grounding (MOT25-StAG) Challenge. The aim of this challenge is to accurately
> localize and track multiple objects that match specific and free-form language
> queries, using video data of complex real-world scenes as input. We model the
> underlying task as a video retrieval problem and present a two-stage, zero-shot
> approach, combining the advantages of the SOTA tracking model FastTracker and
> Multi-modal Large Language Model LLaVA-Video. On the MOT25-StAG test set, our
> method achieves m-HIoU and HOTA scores of 20.68 and 10.73 respectively, which
> won second place in the challenge.

