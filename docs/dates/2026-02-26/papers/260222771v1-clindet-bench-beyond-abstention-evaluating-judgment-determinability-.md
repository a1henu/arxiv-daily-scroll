---
layout: default
title: ClinDet-Bench: Beyond Abstention, Evaluating Judgment Determinability of LLMs in Clinical Decision-Making
---

# ClinDet-Bench: Beyond Abstention, Evaluating Judgment Determinability of LLMs in Clinical Decision-Making
**arXiv**：[2602.22771v1](https://arxiv.org/abs/2602.22771) · [PDF](https://arxiv.org/pdf/2602.22771.pdf)  
**作者**：Yusuke Watanabe, Yohei Kobashi, Takeshi Kojima, Yusuke Iwasawa, Yasushi Okuno, Yutaka Matsuo  

**一句话要点**：提出ClinDet-Bench基准，评估大语言模型在临床决策中判断确定性的能力

**关键词**：临床决策评估, 大语言模型基准, 判断确定性, 信息不完整场景, 安全评估框架

## 3 点简述
- 核心问题：临床决策常面临信息不完整，需评估大语言模型是否能识别信息是否足以做出判断。
- 方法要点：基于临床评分系统，将不完整信息场景分解为可确定和不可确定条件，要求模型考虑所有缺失信息假设。
- 实验或效果：发现近期大语言模型在信息不完整时无法识别确定性，导致过早判断或过度弃权，尽管在完整信息下表现良好。

## 摘要（原文）

> Clinical decisions are often required under incomplete information. Clinical experts must identify whether available information is sufficient for judgment, as both premature conclusion and unnecessary abstention can compromise patient safety. To evaluate this capability of large language models (LLMs), we developed ClinDet-Bench, a benchmark based on clinical scoring systems that decomposes incomplete-information scenarios into determinable and undeterminable conditions. Identifying determinability requires considering all hypotheses about missing information, including unlikely ones, and verifying whether the conclusion holds across them. We find that recent LLMs fail to identify determinability under incomplete information, producing both premature judgments and excessive abstention, despite correctly explaining the underlying scoring knowledge and performing well under complete information. These findings suggest that existing benchmarks are insufficient to evaluate the safety of LLMs in clinical settings. ClinDet-Bench provides a framework for evaluating determinability recognition, leading to appropriate abstention, with potential applicability to medicine and other high-stakes domains, and is publicly available.

