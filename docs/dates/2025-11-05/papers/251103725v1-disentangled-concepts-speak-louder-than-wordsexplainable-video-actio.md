---
layout: default
title: Disentangled Concepts Speak Louder Than Words:Explainable Video Action Recognition
---

# Disentangled Concepts Speak Louder Than Words:Explainable Video Action Recognition
**arXiv**：[2511.03725v1](https://arxiv.org/abs/2511.03725) · [PDF](https://arxiv.org/pdf/2511.03725.pdf)  
**作者**：Jongseo Lee, Wooil Lee, Gyeong-Moon Park, Seong Tae Kim, Jinwoo Choi  

**一句话要点**：提出DANCE框架以解决视频动作识别中解释性差的问题

**关键词**：视频动作识别, 可解释AI, 概念解耦, 概念瓶颈模型, 运动动态分析

## 3 点简述
- 现有方法产生纠缠解释，无法区分运动与空间上下文对预测的影响
- 使用解耦概念类型：运动动态、对象和场景，基于概念瓶颈设计预测
- 在多个数据集上验证，提高解释清晰度，性能有竞争力，支持模型调试

## 摘要（原文）

> Effective explanations of video action recognition models should disentangle
> how movements unfold over time from the surrounding spatial context. However,
> existing methods based on saliency produce entangled explanations, making it
> unclear whether predictions rely on motion or spatial context. Language-based
> approaches offer structure but often fail to explain motions due to their tacit
> nature -- intuitively understood but difficult to verbalize. To address these
> challenges, we propose Disentangled Action aNd Context concept-based
> Explainable (DANCE) video action recognition, a framework that predicts actions
> through disentangled concept types: motion dynamics, objects, and scenes. We
> define motion dynamics concepts as human pose sequences. We employ a large
> language model to automatically extract object and scene concepts. Built on an
> ante-hoc concept bottleneck design, DANCE enforces prediction through these
> concepts. Experiments on four datasets -- KTH, Penn Action, HAA500, and UCF-101
> -- demonstrate that DANCE significantly improves explanation clarity with
> competitive performance. We validate the superior interpretability of DANCE
> through a user study. Experimental results also show that DANCE is beneficial
> for model debugging, editing, and failure analysis.

