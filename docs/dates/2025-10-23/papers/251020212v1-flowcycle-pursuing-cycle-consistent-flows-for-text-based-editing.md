---
layout: default
title: FlowCycle: Pursuing Cycle-Consistent Flows for Text-based Editing
---

# FlowCycle: Pursuing Cycle-Consistent Flows for Text-based Editing
**arXiv**：[2510.20212v1](https://arxiv.org/abs/2510.20212) · [PDF](https://arxiv.org/pdf/2510.20212.pdf)  
**作者**：Yanghao Wang, Zhen Wang, Long Chen  

**一句话要点**：提出FlowCycle框架，通过目标感知中间状态优化文本图像编辑

**关键词**：文本图像编辑, 循环一致性, 流模型, 目标感知, 无反转框架

## 3 点简述
- 主流方法采用目标无关中间状态，导致编辑不一致或受限
- 引入可学习噪声参数化，通过循环一致性过程优化中间状态
- 实验显示FlowCycle在编辑质量和一致性上优于现有方法

## 摘要（原文）

> Recent advances in pre-trained text-to-image flow models have enabled
> remarkable progress in text-based image editing. Mainstream approaches always
> adopt a corruption-then-restoration paradigm, where the source image is first
> corrupted into an ``intermediate state'' and then restored to the target image
> under the prompt guidance. However, current methods construct this intermediate
> state in a target-agnostic manner, i.e., they primarily focus on realizing
> source image reconstruction while neglecting the semantic gaps towards the
> specific editing target. This design inherently results in limited editability
> or inconsistency when the desired modifications substantially deviate from the
> source. In this paper, we argue that the intermediate state should be
> target-aware, i.e., selectively corrupting editing-relevant contents while
> preserving editing-irrelevant ones. To this end, we propose FlowCycle, a novel
> inversion-free and flow-based editing framework that parameterizes corruption
> with learnable noises and optimizes them through a cycle-consistent process. By
> iteratively editing the source to the target and recovering back to the source
> with dual consistency constraints, FlowCycle learns to produce a target-aware
> intermediate state, enabling faithful modifications while preserving source
> consistency. Extensive ablations have demonstrated that FlowCycle achieves
> superior editing quality and consistency over state-of-the-art methods.

