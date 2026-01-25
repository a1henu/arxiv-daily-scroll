---
layout: default
title: Structured Hints for Sample-Efficient Lean Theorem Proving
---

# Structured Hints for Sample-Efficient Lean Theorem Proving
**arXiv**：[2601.16172v1](https://arxiv.org/abs/2601.16172) · [PDF](https://arxiv.org/pdf/2601.16172.pdf)  
**作者**：Zachary Burton  

**一句话要点**：提出结构化提示策略以提升神经定理证明器的样本效率

**关键词**：神经定理证明, 推理时指导, 样本效率, 结构化提示, 战术语言, 轻量干预

## 3 点简述
- 研究问题：训练充分的神经定理证明器在推理时是否仍受益于简单结构指导
- 方法要点：在推理时应用固定提示计划，覆盖15种常见战术骨架
- 实验效果：在miniF2F基准上，pass@16从15.2%提升至21.7%，相对提升43%

## 摘要（原文）

> State-of-the-art neural theorem provers like DeepSeek-Prover-V1.5 combine large language models with reinforcement learning, achieving impressive results through sophisticated training. We ask: do these highly-trained models still benefit from simple structural guidance at inference time? We evaluate a lightweight intervention -- a fixed prompt schedule over 15 common tactic skeletons -- on the miniF2F benchmark. This simple approach yields 21.7% pass@16 compared to 15.2% for standard sampling from the same model, a 43% relative improvement using the same number of samples (k=16) and same maximum generation length (1024 tokens). Our results suggest that even capable RL-trained provers underutilize structural priors available in the tactic language, and that simple inference-time guidance remains a cheap, complementary boost.

