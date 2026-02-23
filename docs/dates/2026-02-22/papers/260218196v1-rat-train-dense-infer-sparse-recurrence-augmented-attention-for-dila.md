---
layout: default
title: RAT+: Train Dense, Infer Sparse -- Recurrence Augmented Attention for Dilated Inference
---

# RAT+: Train Dense, Infer Sparse -- Recurrence Augmented Attention for Dilated Inference
**arXiv**：[2602.18196v1](https://arxiv.org/abs/2602.18196) · [PDF](https://arxiv.org/pdf/2602.18196.pdf)  
**作者**：Xiuying Wei, Caglar Gulcehre  

**一句话要点**：提出RAT+架构，通过密集预训练与循环增强，实现推理时灵活切换稀疏注意力模式。

**关键词**：稀疏注意力, 推理效率, 循环增强, 密集预训练, 长序列处理

## 3 点简述
- 结构化膨胀注意力在推理时效率高，但稀疏化预训练模型会导致精度严重下降。
- RAT+采用密集预训练，通过全序列循环和主动循环学习增强注意力，无需重新训练稀疏模型。
- 在1.5B参数规模下，RAT+在推理时切换至膨胀注意力，精度接近密集模型，优于top-k块注意力。

## 摘要（原文）

> Structured dilated attention has an appealing inference-time efficiency knob: it reduces the FLOPs of the attention and the KV cache size by a factor of the dilation size D, while preserving long-range connectivity. However, we find a persistent failure mode of them -- sparsifying a pretrained attention model to a dilated pattern leads to severe accuracy degradation. We introduce RAT+, a dense-pretraining architecture that augments attention with full-sequence recurrence and active recurrence learning. A single RAT+ model is pretrained densely once, then flexibly switched at inference time to dilated attention (optionally with local windows) or hybrid layer/head compositions, requiring only a short 1B-token resolution adaptation rather than retraining separate sparse models. At 1.5B parameters trained on 100B tokens, RAT+ closely matches dense accuracy at 16 and drops by about 2-3 points at 64 on commonsense reasoning and LongBench tasks, respectively. Moreover, RAT+ outperforms attention when sparsifying to the top-k block attention. We further scale to 2.6B parameters and 200B tokens and observe the same trend.

