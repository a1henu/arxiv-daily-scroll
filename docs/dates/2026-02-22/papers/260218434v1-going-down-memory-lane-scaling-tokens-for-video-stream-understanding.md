---
layout: default
title: Going Down Memory Lane: Scaling Tokens for Video Stream Understanding with Dynamic KV-Cache Memory
---

# Going Down Memory Lane: Scaling Tokens for Video Stream Understanding with Dynamic KV-Cache Memory
**arXiv**：[2602.18434v1](https://arxiv.org/abs/2602.18434) · [PDF](https://arxiv.org/pdf/2602.18434.pdf)  
**作者**：Vatsal Agarwal, Saksham Suri, Matthew Gwilliam, Pulkit Kumar, Abhinav Shrivastava  

**一句话要点**：提出MemStream方法，通过扩展令牌预算和自适应选择策略，提升流视频理解中的细粒度时空推理能力。

**关键词**：流视频理解, 键值缓存, 自适应令牌选择, 检索专家混合, 视频问答, 时空推理

## 3 点简述
- 核心问题：现有流视频理解方法因每帧令牌数有限，导致细粒度视觉细节丢失，且特征编码使查询-帧相似度随时间增加，偏向检索后期帧。
- 方法要点：引入自适应选择策略减少令牌冗余，并利用训练无关的检索专家混合模型，以外部模型辅助识别相关帧。
- 实验或效果：在CG-Bench、LVBench和VideoMME（Long）数据集上，MemStream相比ReKV方法分别提升8.0%、8.5%和2.4%。

## 摘要（原文）

> Streaming video understanding requires models to robustly encode, store, and retrieve information from a continuous video stream to support accurate video question answering (VQA). Existing state-of-the-art approaches rely on key-value caching to accumulate frame-level information over time, but use a limited number of tokens per frame, leading to the loss of fine-grained visual details. In this work, we propose scaling the token budget to enable more granular spatiotemporal understanding and reasoning. First, we find that current methods are ill-equipped to handle dense streams: their feature encoding causes query-frame similarity scores to increase over time, biasing retrieval toward later frames. To address this, we introduce an adaptive selection strategy that reduces token redundancy while preserving local spatiotemporal information. We further propose a training-free retrieval mixture-of-experts that leverages external models to better identify relevant frames. Our method, MemStream, achieves +8.0% on CG-Bench, +8.5% on LVBench, and +2.4% on VideoMME (Long) over ReKV with Qwen2.5-VL-7B.

