---
layout: default
title: Learning to Judge: LLMs Designing and Applying Evaluation Rubrics
---

# Learning to Judge: LLMs Designing and Applying Evaluation Rubrics
**arXiv**：[2602.08672v1](https://arxiv.org/abs/2602.08672) · [PDF](https://arxiv.org/pdf/2602.08672.pdf)  
**作者**：Clemencia Siro, Pourya Aliannejadi, Mohammad Aliannejadi  

**一句话要点**：提出GER-Eval方法，探究大语言模型能否自主设计并应用评估准则以改进自然语言生成评估。

**关键词**：大语言模型评估, 评估准则生成, 自然语言生成, 评分可靠性, 模型对齐

## 3 点简述
- 核心问题：人类定义的评估准则静态且与模型内部语言表示不匹配，影响评估效果。
- 方法要点：引入GER-Eval，让大语言模型生成任务感知的评估维度并应用于输出评分。
- 实验或效果：模型能生成可解释准则并在内部一致应用，但事实性任务中评分可靠性下降，闭源模型表现更优。

## 摘要（原文）

> Large language models (LLMs) are increasingly used as evaluators for natural language generation, applying human-defined rubrics to assess system outputs. However, human rubrics are often static and misaligned with how models internally represent language quality. We introduce GER-Eval (Generating Evaluation Rubrics for Evaluation) to investigate whether LLMs can design and apply their own evaluation rubrics. We evaluate the semantic coherence and scoring reliability of LLM-defined criteria and their alignment with human criteria. LLMs reliably generate interpretable and task-aware evaluation dimensions and apply them consistently within models, but their scoring reliability degrades in factual and knowledge-intensive settings. Closed-source models such as GPT-4o achieve higher agreement and cross-model generalization than open-weight models such as Llama. Our findings position evaluation as a learned linguistic capability of LLMs, consistent within models but fragmented across them, and call for new methods that jointly model human and LLM evaluative language to improve reliability and interpretability.

