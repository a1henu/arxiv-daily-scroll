---
layout: default
title: JudgeRLVR: Judge First, Generate Second for Efficient Reasoning
---

# JudgeRLVR: Judge First, Generate Second for Efficient Reasoning
**arXiv**：[2601.08468v1](https://arxiv.org/abs/2601.08468) · [PDF](https://arxiv.org/pdf/2601.08468.pdf)  
**作者**：Jiangshan Duo, Hanyu Li, Hailin Zhang, Yudong Wang, Sujian Li, Liang Zhao  

**一句话要点**：提出JudgeRLVR两阶段范式，通过先判别后生成提升大语言模型推理效率

**关键词**：强化学习可验证奖励, 判别式训练, 两阶段推理, 搜索空间剪枝, 大语言模型效率优化

## 3 点简述
- 核心问题：传统RLVR仅优化最终答案正确性，导致模型陷入冗长无目标的试错探索
- 方法要点：先训练模型判别有效解，再基于判别能力初始化进行生成式微调
- 实验效果：在数学领域实现准确率提升3.7分同时生成长度减少42%，泛化能力增强

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has become a standard paradigm for reasoning in Large Language Models. However, optimizing solely for final-answer correctness often drives models into aimless, verbose exploration, where they rely on exhaustive trial-and-error tactics rather than structured planning to reach solutions. While heuristic constraints like length penalties can reduce verbosity, they often truncate essential reasoning steps, creating a difficult trade-off between efficiency and verification. In this paper, we argue that discriminative capability is a prerequisite for efficient generation: by learning to distinguish valid solutions, a model can internalize a guidance signal that prunes the search space. We propose JudgeRLVR, a two-stage judge-then-generate paradigm. In the first stage, we train the model to judge solution responses with verifiable answers. In the second stage, we fine-tune the same model with vanilla generating RLVR initialized from the judge. Compared to Vanilla RLVR using the same math-domain training data, JudgeRLVR achieves a better quality--efficiency trade-off for Qwen3-30B-A3B: on in-domain math, it delivers about +3.7 points average accuracy gain with -42\% average generation length; on out-of-domain benchmarks, it delivers about +4.5 points average accuracy improvement, demonstrating enhanced generalization.

