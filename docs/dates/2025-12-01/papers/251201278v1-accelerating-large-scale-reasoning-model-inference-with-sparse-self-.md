---
layout: default
title: Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding
---

# Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding
**arXiv**：[2512.01278v1](https://arxiv.org/abs/2512.01278) · [PDF](https://arxiv.org/pdf/2512.01278.pdf)  
**作者**：Yilong Zhao, Jiaming Tang, Kan Zhu, Zihao Ye, Chi-Chih Chang, Chaofan Lin, Jongseok Park, Guangxuan Xiao, Mohamed S. Abdelfattah, Mingyu Gao, Baris Kasikci, Song Han, Ion Stoica  

**一句话要点**：提出SparseSpec稀疏自推测解码框架，以加速大规模推理模型生成并缓解内存带宽压力

**关键词**：推测解码, 稀疏注意力, KV-Cache优化, 推理加速, 内存带宽

## 3 点简述
- 推理模型长生成导致内存访问瓶颈，从计算密集型转为内存密集型
- SparseSpec采用PillarAttn稀疏注意力作为草稿模型，并协同设计调度、延迟验证和动态KV-Cache管理
- 实验显示在多种模型和数据集上，吞吐量最高提升2.13倍

## 摘要（原文）

> Reasoning language models have demonstrated remarkable capabilities on challenging tasks by generating elaborate chain-of-thought (CoT) solutions. However, such lengthy generation shifts the inference bottleneck from compute-bound to memory-bound. To generate each token, the model applies full attention to all previously generated tokens, requiring memory access to an increasingly large KV-Cache. Consequently, longer generations demand more memory access for every step, leading to substantial pressure on memory bandwidth.
>   To address this, we introduce SparseSpec, a speculative decoding framework that reuses the same model as the draft and target models (i.e., self-speculation). SparseSpec features a novel sparse attention mechanism, PillarAttn, as the draft model, which accurately selects critical tokens via elegantly reusing information from the verification stage. Furthermore, SparseSpec co-designs self-speculation with three system innovations: (1) a unified scheduler to batch token drafting and verification, (2) delayed verification for CPU/GPU overlap, and (3) dynamic KV-Cache management to maximize memory utilization. Across various models and datasets, SparseSpec outperforms state-of-the-art solutions, with an up to 2.13x throughput speedup.

