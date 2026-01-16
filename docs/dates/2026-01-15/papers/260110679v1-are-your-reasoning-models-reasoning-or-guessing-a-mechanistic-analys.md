---
layout: default
title: Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models
---

# Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models
**arXiv**：[2601.10679v1](https://arxiv.org/abs/2601.10679) · [PDF](https://arxiv.org/pdf/2601.10679.pdf)  
**作者**：Zirui Ren, Ziming Liu  

**一句话要点**：提出增强策略以提升分层推理模型的猜测质量与数量，解决其推理失败问题

**关键词**：分层推理模型, 机制分析, 固定点性质, 数据增强, 模型自举, 推理失败

## 3 点简述
- 核心问题：分层推理模型在简单谜题中因违反固定点假设而失败，表现为猜测而非推理
- 方法要点：通过数据增强、输入扰动和模型自举策略，扩展模型的猜测能力
- 实验或效果：结合所有方法开发增强HRM，在Sudoku-Extreme任务上准确率从54.5%提升至96.9%

## 摘要（原文）

> Hierarchical reasoning model (HRM) achieves extraordinary performance on various reasoning tasks, significantly outperforming large language model-based reasoners. To understand the strengths and potential failure modes of HRM, we conduct a mechanistic study on its reasoning patterns and find three surprising facts: (a) Failure of extremely simple puzzles, e.g., HRM can fail on a puzzle with only one unknown cell. We attribute this failure to the violation of the fixed point property, a fundamental assumption of HRM. (b) "Grokking" dynamics in reasoning steps, i.e., the answer is not improved uniformly, but instead there is a critical reasoning step that suddenly makes the answer correct; (c) Existence of multiple fixed points. HRM "guesses" the first fixed point, which could be incorrect, and gets trapped there for a while or forever. All facts imply that HRM appears to be "guessing" instead of "reasoning". Leveraging this "guessing" picture, we propose three strategies to scale HRM's guesses: data augmentation (scaling the quality of guesses), input perturbation (scaling the number of guesses by leveraging inference randomness), and model bootstrapping (scaling the number of guesses by leveraging training randomness). On the practical side, by combining all methods, we develop Augmented HRM, boosting accuracy on Sudoku-Extreme from 54.5% to 96.9%. On the scientific side, our analysis provides new insights into how reasoning models "reason".

