---
layout: default
title: Lethe:Adapter-Augmented Dual-Stream Update for Persistent Knowledge Erasure in Federated Unlearning
---

# Lethe:Adapter-Augmented Dual-Stream Update for Persistent Knowledge Erasure in Federated Unlearning
**arXiv**：[2601.22601v1](https://arxiv.org/abs/2601.22601) · [PDF](https://arxiv.org/pdf/2601.22601.pdf)  
**作者**：Hanwei Tan, Wentai Hu, Ligang He, Yijun Quan  

**一句话要点**：提出Lethe方法以解决联邦学习中持续训练导致遗忘知识重现的问题

**关键词**：联邦学习, 知识遗忘, 持续训练, 适配器, 双流更新, 持久性

## 3 点简述
- 核心问题：持续训练可能重新激活已遗忘知识，导致知识重现
- 方法要点：采用适配器增强双流更新，通过重塑-纠正-恢复流程实现持久遗忘
- 实验或效果：支持多级遗忘，在多数情况下知识重现率低于1%

## 摘要（原文）

> Federated unlearning (FU) aims to erase designated client-level, class-level, or sample-level knowledge from a global model. Existing studies commonly assume that the collaboration ends up with the unlearning operation, overlooking the follow-up situation where the federated training continues over the remaining data.We identify a critical failure mode, termed Knowledge resurfacing, by revealing that continued training can re-activate unlearned knowledge and cause the removed influence to resurface in the global model. To address this, we propose Lethe, a novel federated unlearning method that de-correlates knowledge to be unlearned from knowledge to be retained, ensuring persistent erasure during continued training.Lethe follows a Reshape--Rectify--Restore pipeline: a temporary adapter is first trained with gradient ascent on the unlearning data to obtain magnified updates, which is then used as corrective signals to diverge layer-wise rectification on the remaining updates in two streams. Finally, the adapter is removed and a short recovery stage is performed on the retained data. Our experiments show that Lethe supports unlearning in the federated system at all levels in a unified manner and maintains superior persistence (Resurfacing Rate <1% in most cases) even after numerous rounds of follow-up training.

