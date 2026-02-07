---
layout: default
title: Beyond Length: Context-Aware Expansion and Independence as Developmentally Sensitive Evaluation in Child Utterances
---

# Beyond Length: Context-Aware Expansion and Independence as Developmentally Sensitive Evaluation in Child Utterances
**arXiv**：[2602.05392v1](https://arxiv.org/abs/2602.05392) · [PDF](https://arxiv.org/pdf/2602.05392.pdf)  
**作者**：Jiyun Chun, Eric Fosler-Lussier, Michael White, Andrew Perrault  

**一句话要点**：提出基于LLM的儿童话语评估框架，通过扩展性和独立性维度解决上下文敏感度量不足问题。

**关键词**：儿童话语评估, 上下文敏感度量, LLM作为评判者, 扩展性评分, 独立性评分, 语言发展研究

## 3 点简述
- 核心问题：现有儿童话语评估指标如MLU和词汇多样性忽略上下文，无法捕捉推理深度和话题维持。
- 方法要点：引入LLM作为评判者，先分类成人话语类型，再沿扩展性和独立性两个轴评分。
- 实验或效果：验证了与年龄相关的模式，提升年龄估计准确性，并与人类判断一致。

## 摘要（原文）

> Evaluating the quality of children's utterances in adult-child dialogue remains challenging due to insufficient context-sensitive metrics. Common proxies such as Mean Length of Utterance (MLU), lexical diversity (vocd-D), and readability indices (Flesch-Kincaid Grade Level, Gunning Fog Index) are dominated by length and ignore conversational context, missing aspects of response quality such as reasoning depth, topic maintenance, and discourse planning. We introduce an LLM-as-a-judge framework that first classifies the Previous Adult Utterance Type and then scores the child's response along two axes: Expansion (contextual elaboration and inferential depth) and Independence (the child's contribution to advancing the discourse). These axes reflect fundamental dimensions in child language development, where Expansion captures elaboration, clause combining, and causal and contrastive connectives. Independence captures initiative, topic control, decreasing reliance on adult scaffolding through growing self-regulation, and audience design. We establish developmental validity by showing age-related patterns and demonstrate predictive value by improving age estimation over common baselines. We further confirm semantic sensitivity by detecting differences tied to discourse relations. Our metrics align with human judgments, enabling large-scale evaluation. This shifts child utterance assessment from simply measuring length to evaluating how meaningfully the child's speech contributes to and advances the conversation within its context.

