---
layout: default
title: Parallel Vision Token Scheduling for Fast and Accurate Multimodal LMMs Inference
---

# Parallel Vision Token Scheduling for Fast and Accurate Multimodal LMMs Inference
**arXiv**：[2511.18875v1](https://arxiv.org/abs/2511.18875) · [PDF](https://arxiv.org/pdf/2511.18875.pdf)  
**作者**：Wengyi Zhan, Mingbao Lin, Zhihang Lin, Rongrong Ji  

**一句话要点**：提出并行视觉令牌调度以加速多模态大语言模型推理

**关键词**：多模态大语言模型, 视觉令牌调度, 推理加速, 计算复杂度降低, 训练无关方法

## 3 点简述
- 多模态大语言模型推理延迟高，因自注意力随序列长度平方增长和视觉令牌过多
- 将视觉令牌分为主体和非主体组并行处理，转移语义后丢弃非主体路径以减少计算
- 实验显示可剪枝88.9%视觉令牌，性能损失小，实现1.77倍加速和70%FLOPs减少

## 摘要（原文）

> Multimodal large language models (MLLMs) deliver impressive vision-language reasoning but suffer steep inference latency because self-attention scales quadratically with sequence length and thousands of visual tokens contributed by high-resolution images. Naively pruning less-informative visual tokens reduces this burden, yet indiscriminate removal can strip away contextual cues essential for background or fine-grained questions, undermining accuracy. In this paper, we present ParVTS (Parallel Vision Token Scheduling), a training-free scheduling framework that partitions visual tokens into subject and non-subject groups, processes them in parallel to transfer their semantics into question tokens, and discards the non-subject path mid-inference to reduce computation. This scheduling reduces computational complexity, requires no heuristics or additional modules, and is compatible with diverse existing MLLM architectures. Experiments across multiple MLLM backbones show that ParVTS prunes up to 88.9% of visual tokens with minimal performance drop, achieving 1.77x speedup and 70% FLOPs reduction.

