---
layout: default
title: Memo-SQL: Structured Decomposition and Experience-Driven Self-Correction for Training-Free NL2SQL
---

# Memo-SQL: Structured Decomposition and Experience-Driven Self-Correction for Training-Free NL2SQL
**arXiv**：[2601.10011v1](https://arxiv.org/abs/2601.10011) · [PDF](https://arxiv.org/pdf/2601.10011.pdf)  
**作者**：Zerui Yang, Weichuan Wang, Yanwei Xu, Linqi Song, Yudai Matsuda, Wei Han, Bo Bai  

**一句话要点**：提出Memo-SQL框架，通过结构化分解和经验驱动自校正解决NL2SQL训练中的效率与鲁棒性问题。

**关键词**：NL2SQL, 结构化分解, 经验驱动自校正, 训练免费框架, 检索增强提示, 执行准确率

## 3 点简述
- 现有NL2SQL系统依赖正确示例的上下文学习，忽略错误修复对的历史信号，导致自校正能力不足。
- Memo-SQL采用实体、层次和原子序列三种策略进行结构化分解，以促进推理多样性，避免候选SQL重复。
- 在BIRD数据集上，Memo-SQL达到68.5%执行准确率，资源消耗比先前方法减少10倍以上，无需微调或外部API。

## 摘要（原文）

> Existing NL2SQL systems face two critical limitations: (1) they rely on in-context learning with only correct examples, overlooking the rich signal in historical error-fix pairs that could guide more robust self-correction; and (2) test-time scaling approaches often decompose questions arbitrarily, producing near-identical SQL candidates across runs and diminishing ensemble gains. Moreover, these methods suffer from a stark accuracy-efficiency trade-off: high performance demands excessive computation, while fast variants compromise quality. We present Memo-SQL, a training-free framework that addresses these issues through two simple ideas: structured decomposition and experience-aware self-correction. Instead of leaving decomposition to chance, we apply three clear strategies, entity-wise, hierarchical, and atomic sequential, to encourage diverse reasoning. For correction, we build a dynamic memory of both successful queries and historical error-fix pairs, and use retrieval-augmented prompting to bring relevant examples into context at inference time, no fine-tuning or external APIs required. On BIRD, Memo-SQL achieves 68.5% execution accuracy, setting a new state of the art among open, zero-fine-tuning methods, while using over 10 times fewer resources than prior TTS approaches.

