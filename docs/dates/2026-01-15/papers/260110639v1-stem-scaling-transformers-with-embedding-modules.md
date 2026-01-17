---
layout: default
title: STEM: Scaling Transformers with Embedding Modules
---

# STEM: Scaling Transformers with Embedding Modules
**arXiv**：[2601.10639v1](https://arxiv.org/abs/2601.10639) · [PDF](https://arxiv.org/pdf/2601.10639.pdf)  
**作者**：Ranajoy Sadhukhan, Sheng Cao, Harry Dong, Changsheng Zhao, Attiano Purpura-Pontoniere, Yuandong Tian, Zechun Liu, Beidi Chen  

**一句话要点**：提出STEM以静态嵌入模块扩展Transformer参数容量，提升效率与可解释性。

**关键词**：Transformer扩展, 稀疏计算, 参数效率, 知识编辑, 长上下文性能, 训练稳定性

## 3 点简述
- 核心问题：细粒度稀疏性导致训练不稳定、负载不均和通信开销。
- 方法要点：用静态令牌索引嵌入查找替换FFN上投影，保持门和下投影密集。
- 实验效果：在350M和1B模型上提升下游性能，减少计算和参数访问，增强可解释性。

## 摘要（原文）

> Fine-grained sparsity promises higher parametric capacity without proportional per-token compute, but often suffers from training instability, load balancing, and communication overhead. We introduce STEM (Scaling Transformers with Embedding Modules), a static, token-indexed approach that replaces the FFN up-projection with a layer-local embedding lookup while keeping the gate and down-projection dense. This removes runtime routing, enables CPU offload with asynchronous prefetch, and decouples capacity from both per-token FLOPs and cross-device communication. Empirically, STEM trains stably despite extreme sparsity. It improves downstream performance over dense baselines while reducing per-token FLOPs and parameter accesses (eliminating roughly one-third of FFN parameters). STEM learns embedding spaces with large angular spread which enhances its knowledge storage capacity. More interestingly, this enhanced knowledge capacity comes with better interpretability. The token-indexed nature of STEM embeddings allows simple ways to perform knowledge editing and knowledge injection in an interpretable manner without any intervention in the input text or additional computation. In addition, STEM strengthens long-context performance: as sequence length grows, more distinct parameters are activated, yielding practical test-time capacity scaling. Across 350M and 1B model scales, STEM delivers up to ~3--4% accuracy improvements overall, with notable gains on knowledge and reasoning-heavy benchmarks (ARC-Challenge, OpenBookQA, GSM8K, MMLU). Overall, STEM is an effective way of scaling parametric memory while providing better interpretability, better training stability and improved efficiency.

