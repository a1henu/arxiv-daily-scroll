---
layout: default
title: Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding
---

# Learning to Refuse: Refusal-Aware Reinforcement Fine-Tuning for Hard-Irrelevant Queries in Video Temporal Grounding
**arXiv**：[2511.23151v1](https://arxiv.org/abs/2511.23151) · [PDF](https://arxiv.org/pdf/2511.23151.pdf)  
**作者**：Jin-Seop Lee, SungJoon Lee, SeongJun Jung, Boyang Li, Jee-Hyong Lee  

**一句话要点**：提出拒绝感知强化微调方法以解决视频时序定位中硬无关查询的拒绝问题

**关键词**：视频时序定位, 强化学习微调, 拒绝感知, 硬无关查询, 语义推理

## 3 点简述
- 现有视频时序定位模型假设查询总是相关，导致对无关查询也预测片段，尤其难以处理语义相似但实际无关的硬无关查询。
- 基于GRPO框架，集成格式、拒绝IoU、解释和查询修正四个奖励目标，提升相关性判别和细粒度语义推理能力。
- 构建硬无关视频时序定位数据集，并在多种相关感知场景中验证方法的有效性，展示其可扩展性。

## 摘要（原文）

> Video Temporal Grounding (VTG) aims to localize a temporal segment in a video corresponding to a natural language query. However, existing VTG models assume that a relevant segment always exists, causing them to always predict a target segment even when the query is irrelevant to the video. While recent approaches attempt to handle irrelevant queries, they can only reject those that are entirely unrelated to the video and still fail to handle hard-irrelevant queries that are semantically similar but not actually relevant. To address this, we propose Refusal-Aware Reinforcement Fine-Tuning (RA-RFT) to effectively refuse hard-irrelevant queries in VTG. Our method is based on the Group Relative Policy Optimization (GRPO) framework and integrates four reward objectives-format, refuse-IoU, explain, and query correction-to improve both relevance discrimination and fine-grained semantic reasoning. In addition, to effectively support RA-RFT, we construct a Hard-Irrelevant VTG (HI-VTG) dataset, which includes hard-irrelevant queries and their refusal answers. We demonstrate the effectiveness of our method across various relevance-aware VTG scenarios, including hard-irrelevant VTG, simply-shuffled RA-VTG, and human-annotated RA-VTG settings. We also show that the proposed method is scalable by applying it to various LVLM-based VTG models. Our code is available at https://github.com/JINSUBY/RA-RFT.

