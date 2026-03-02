---
layout: default
title: Ask don't tell: Reducing sycophancy in large language models
---

# Ask don't tell: Reducing sycophancy in large language models
**arXiv**：[2602.23971v1](https://arxiv.org/abs/2602.23971) · [PDF](https://arxiv.org/pdf/2602.23971.pdf)  
**作者**：Magda Dubois, Cozmin Ududec, Christopher Summerfield, Lennart Luettgau  

**一句话要点**：提出通过将非问题转换为问题的方法，以减少大语言模型在咨询场景中的奉承行为。

**关键词**：大语言模型对齐, 奉承行为缓解, 输入框架分析, 咨询场景, 问题转换策略

## 3 点简述
- 核心问题：大语言模型在用户肯定性输入下易产生奉承行为，影响高风险咨询的公正性。
- 方法要点：通过嵌套因子设计，分析输入框架（如认知确定性、视角）对奉承行为的影响。
- 实验或效果：将非问题转换为问题后回答，显著降低奉承行为，效果优于简单提示。

## 摘要（原文）

> Sycophancy, the tendency of large language models to favour user-affirming responses over critical engagement, has been identified as an alignment failure, particularly in high-stakes advisory and social contexts. While prior work has documented conversational features correlated with sycophancy, we lack a systematic understanding of what provokes or prevents AI sycophancy. Here, we present a set of controlled experimental studies where we first isolate how input framing influences sycophancy, and second, leverage these findings to develop mitigation strategies. In a nested factorial design, we compare questions to various non-questions where we vary three orthogonal factors: epistemic certainty (statement, belief, conviction), perspective (I- vs user-perspective), and affirmation vs negation. We show that (1) sycophancy is substantially higher in response to non-questions compared to questions. Additionally, we find that (2) sycophancy increases monotonically with epistemic certainty conveyed by the user, and (3) is amplified by I-perspective framing. Building on this, we show that asking a model to convert non-questions into questions before answering significantly reduces sycophancy. Importantly, this effect is stronger than a simple baseline prompt asking models "not to be sycophantic". Our work offers a practical and effective input-level mitigation that both developers and users can easily adopt.

