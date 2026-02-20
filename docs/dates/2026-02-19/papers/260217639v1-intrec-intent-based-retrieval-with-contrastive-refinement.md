---
layout: default
title: IntRec: Intent-based Retrieval with Contrastive Refinement
---

# IntRec: Intent-based Retrieval with Contrastive Refinement
**arXiv**：[2602.17639v1](https://arxiv.org/abs/2602.17639) · [PDF](https://arxiv.org/pdf/2602.17639.pdf)  
**作者**：Pourya Shamsolmoali, Masoumeh Zareapoor, Eric Granger, Yue Lu  

**一句话要点**：提出IntRec交互式对象检索框架，通过用户反馈精炼预测以解决复杂场景中模糊查询的挑战。

**关键词**：交互式对象检索, 意图状态, 对比对齐, 开放词汇检测, 用户反馈精炼, 细粒度消歧

## 3 点简述
- 核心问题：现有开放词汇检测器缺乏基于用户反馈的预测精炼能力，难以处理模糊或多相似对象查询。
- 方法要点：引入意图状态维护正负记忆集，通过对比对齐函数排序候选对象，实现细粒度消歧。
- 实验或效果：在LVIS上AP达35.4，优于基线方法；在LVIS-Ambiguous基准上单次反馈提升+7.9 AP，交互延迟低于30毫秒。

## 摘要（原文）

> Retrieving user-specified objects from complex scenes remains a challenging task, especially when queries are ambiguous or involve multiple similar objects. Existing open-vocabulary detectors operate in a one-shot manner, lacking the ability to refine predictions based on user feedback. To address this, we propose IntRec, an interactive object retrieval framework that refines predictions based on user feedback. At its core is an Intent State (IS) that maintains dual memory sets for positive anchors (confirmed cues) and negative constraints (rejected hypotheses). A contrastive alignment function ranks candidate objects by maximizing similarity to positive cues while penalizing rejected ones, enabling fine-grained disambiguation in cluttered scenes. Our interactive framework provides substantial improvements in retrieval accuracy without additional supervision. On LVIS, IntRec achieves 35.4 AP, outperforming OVMR, CoDet, and CAKE by +2.3, +3.7, and +0.5, respectively. On the challenging LVIS-Ambiguous benchmark, it improves performance by +7.9 AP over its one-shot baseline after a single corrective feedback, with less than 30 ms of added latency per interaction.

