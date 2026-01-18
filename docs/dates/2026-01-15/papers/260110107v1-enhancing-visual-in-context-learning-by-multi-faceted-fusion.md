---
layout: default
title: Enhancing Visual In-Context Learning by Multi-Faceted Fusion
---

# Enhancing Visual In-Context Learning by Multi-Faceted Fusion
**arXiv**：[2601.10107v1](https://arxiv.org/abs/2601.10107) · [PDF](https://arxiv.org/pdf/2601.10107.pdf)  
**作者**：Wenwen Liao, Jianbo Yu, Yuansong Wang, Qingchao Jiang, Xiaofeng Yang  

**一句话要点**：提出多组合协同融合框架以增强视觉上下文学习，超越单提示融合限制。

**关键词**：视觉上下文学习, 多提示融合, 协同表示, 跨任务泛化, MULTI-VQGAN

## 3 点简述
- 核心问题：现有视觉上下文学习方法依赖单提示或简单融合，丢弃多候选的丰富上下文信息。
- 方法要点：生成三个上下文表示分支，通过不同高质量提示组合集成信息，并设计MULTI-VQGAN架构协同利用多源信息。
- 实验或效果：在分割、检测和着色等任务上验证了强跨任务泛化、有效上下文融合及更鲁棒准确的预测能力。

## 摘要（原文）

> Visual In-Context Learning (VICL) has emerged as a powerful paradigm, enabling models to perform novel visual tasks by learning from in-context examples. The dominant "retrieve-then-prompt" approach typically relies on selecting the single best visual prompt, a practice that often discards valuable contextual information from other suitable candidates. While recent work has explored fusing the top-K prompts into a single, enhanced representation, this still simply collapses multiple rich signals into one, limiting the model's reasoning capability. We argue that a more multi-faceted, collaborative fusion is required to unlock the full potential of these diverse contexts. To address this limitation, we introduce a novel framework that moves beyond single-prompt fusion towards an multi-combination collaborative fusion. Instead of collapsing multiple prompts into one, our method generates three contextual representation branches, each formed by integrating information from different combinations of top-quality prompts. These complementary guidance signals are then fed into proposed MULTI-VQGAN architecture, which is designed to jointly interpret and utilize collaborative information from multiple sources. Extensive experiments on diverse tasks, including foreground segmentation, single-object detection, and image colorization, highlight its strong cross-task generalization, effective contextual fusion, and ability to produce more robust and accurate predictions than existing methods.

