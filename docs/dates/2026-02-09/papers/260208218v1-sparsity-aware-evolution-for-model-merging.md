---
layout: default
title: Sparsity-Aware Evolution for Model Merging
---

# Sparsity-Aware Evolution for Model Merging
**arXiv**：[2602.08218v1](https://arxiv.org/abs/2602.08218) · [PDF](https://arxiv.org/pdf/2602.08218.pdf)  
**作者**：Huan Zhang, Yanjian Zhang, Guillaume Wisniewski, Nadi Tomeh, Bang Liu  

**一句话要点**：提出稀疏感知进化框架以提升大语言模型合并的可靠性

**关键词**：模型合并, 稀疏感知进化, 大语言模型, 剪枝-合并循环, 进化算法

## 3 点简述
- 核心问题：模型合并中如何平衡性能与稀疏性以提高可靠性
- 方法要点：通过迭代剪枝-合并循环作为变异算子，在评分函数中融入稀疏约束
- 实验或效果：在多个大规模LLM基准测试中验证了方法能提升合并可靠性

## 摘要（原文）

> We propose a sparsity-aware evolutionary (SAE) framework for model merging that involves iterative pruning-merging cycles to act as a novel mutation operator. We incorporate the sparsity constraints into the score function, which steers the evolutionary process to favor more sparse models, in addition to other conventional performance scores. Interestingly, the by-product of \textit{competition} for sparsity introduces an extra local \textit{attraction} and interplay into the evolutionary process: if one competitor has more zero elements, the other competitor's non-zero elements will occupy those positions, even though the less sparse competitor loses to the more sparse competitor in other positions. The proposed pipeline is evaluated on a variety of large-scale LLM benchmarks. Experiments demonstrate that our approach can improve model merging reliability across multiple benchmarks, and is easy to incorporate due to its simplicity and being orthogonal to most existing approaches.

