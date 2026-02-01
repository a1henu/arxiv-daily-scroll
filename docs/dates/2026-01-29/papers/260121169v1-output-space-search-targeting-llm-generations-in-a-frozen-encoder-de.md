---
layout: default
title: Output-Space Search: Targeting LLM Generations in a Frozen Encoder-Defined Output Space
---

# Output-Space Search: Targeting LLM Generations in a Frozen Encoder-Defined Output Space
**arXiv**：[2601.21169v1](https://arxiv.org/abs/2601.21169) · [PDF](https://arxiv.org/pdf/2601.21169.pdf)  
**作者**：Tobias Materzok  

**一句话要点**：提出输出空间搜索方法，将LLM生成转化为在冻结编码器定义的输出空间中进行端点搜索。

**关键词**：输出空间搜索, LLM生成优化, 序列级强化学习, 贝叶斯优化, 编码器冻结

## 3 点简述
- 核心问题：传统LLM生成依赖路径依赖的标记或程序搜索，限制了并行性和优化效率。
- 方法要点：通过外层循环在输出空间选择目标点，训练基于检索的策略生成接近该点的输出。
- 实验或效果：在故事生成中提升多样性，在代码生成中通过贝叶斯优化改进目标函数，同时保持有效性。

## 摘要（原文）

> We introduce Output-Space Search (OS-Search), which turns LLM generation into endpoint search. An outer loop selects a target z* in a frozen encoder-defined 3D output space Z, and a retrieval-grounded policy trained with sequence-level RL generates outputs whose coordinates land near z* under standard autoregressive decoding. This enables parallel sweeps and black-box optimization in Z without path-dependent token/program search. On stories, sweeping Z (text) yields 3.1x higher LLM-scored diversity than prompt-chaining. On code, Bayesian optimization over Z (code) improves an objective withheld from the controller under matched inference budgets while preserving validity.

