---
layout: default
title: Do LLMs Encode Functional Importance of Reasoning Tokens?
---

# Do LLMs Encode Functional Importance of Reasoning Tokens?
**arXiv**：[2601.03066v1](https://arxiv.org/abs/2601.03066) · [PDF](https://arxiv.org/pdf/2601.03066.pdf)  
**作者**：Janvijay Singh, Dilek Hakkani-Tür  

**一句话要点**：提出贪婪剪枝方法以诊断大语言模型中推理令牌的功能重要性编码

**关键词**：大语言模型, 推理剪枝, 功能重要性, 蒸馏训练, 注意力机制

## 3 点简述
- 核心问题：大语言模型生成长推理链时，是否内部编码令牌级功能重要性以支持答案生成
- 方法要点：通过贪婪剪枝迭代删除对模型似然影响最小的推理令牌，生成长度可控的推理链
- 实验或效果：在蒸馏框架中，基于剪枝链训练的学生模型在匹配长度下优于前沿模型监督的压缩基线

## 摘要（原文）

> Large language models solve complex tasks by generating long reasoning chains, achieving higher accuracy at the cost of increased computational cost and reduced ability to isolate functionally relevant reasoning. Prior work on compact reasoning shortens such chains through probabilistic sampling, heuristics, or supervision from frontier models, but offers limited insight into whether models internally encode token-level functional importance for answer generation. We address this gap diagnostically and propose greedy pruning, a likelihood-preserving deletion procedure that iteratively removes reasoning tokens whose removal minimally degrades model likelihood under a specified objective, yielding length-controlled reasoning chains. We evaluate pruned reasoning in a distillation framework and show that students trained on pruned chains outperform a frontier-model-supervised compression baseline at matched reasoning lengths. Finally, our analysis reveals systematic pruning patterns and shows that attention scores can predict greedy pruning ranks, further suggesting that models encode a nontrivial functional importance structure over reasoning tokens.

