---
layout: default
title: Semantic Anchors in In-Context Learning: Why Small LLMs Cannot Flip Their Labels
---

# Semantic Anchors in In-Context Learning: Why Small LLMs Cannot Flip Their Labels
**arXiv**：[2511.21038v1](https://arxiv.org/abs/2511.21038) · [PDF](https://arxiv.org/pdf/2511.21038.pdf)  
**作者**：Anantha Padmanaban Krishna Kumar  

**一句话要点**：提出语义锚点理论解释小模型无法通过上下文学习翻转标签语义

**关键词**：上下文学习, 语义锚点, 标签语义, 模型对齐, 少样本提示

## 3 点简述
- 核心问题：上下文学习能否覆盖预训练标签语义，或仅优化现有语义骨干。
- 方法要点：对比自然与翻转标签演示，定义语义对齐指标和语义覆盖率。
- 实验效果：在1-12B参数模型中，翻转语义下正确率保持零，支持语义锚点观点。

## 摘要（原文）

> Can in-context learning (ICL) override pre-trained label semantics, or does it merely refine an existing semantic backbone? We address this question by treating LLMs as prompt-induced classifiers and contrasting their behavior under \emph{natural} demonstrations (with correct labels) and \emph{inverted} demonstrations (systematically flipping label meanings). We decompose ICL behavior into three alignment metrics (truth, prior, and prompt alignment) and introduce a semantic override rate, defined as correctness under flipped semantics. Across eight classification tasks and eight open-source LLMs (1--12B parameters), we find consistent evidence for a semantic anchor view. With natural demonstrations, ICL improves accuracy while maintaining strong prior alignment; most correct predictions coincide with zero-shot behavior, even when the prior is weak. With inverted demonstrations, models cannot learn coherent anti-semantic classifiers: prompt alignment increases only by sacrificing accuracy, and semantic override rates remain exactly zero in our few-shot 1--12B setting. Rather than flexibly remapping label meanings, ICL primarily adjusts how inputs project onto stable semantic directions learned during pre-training, clarifying fundamental limits of few-shot prompting and suggesting that overriding label semantics at these scales requires interventions beyond ICL. All code is available at: https://github.com/AnanthaPadmanaban-KrishnaKumar/semantic-anchors-icl.

