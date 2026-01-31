---
layout: default
title: When Prohibitions Become Permissions: Auditing Negation Sensitivity in Language Models
---

# When Prohibitions Become Permissions: Auditing Negation Sensitivity in Language Models
**arXiv**：[2601.21433v1](https://arxiv.org/abs/2601.21433) · [PDF](https://arxiv.org/pdf/2601.21433.pdf)  
**作者**：Katherine Elkins, Jon Chun  

**一句话要点**：提出否定敏感度指数以评估语言模型在伦理场景下的否定指令处理能力

**关键词**：语言模型审计, 否定敏感度, 伦理对齐, 治理指标, 高风险决策

## 3 点简述
- 核心问题：语言模型常将否定指令误解为肯定，导致在伦理场景中错误支持被禁止行为
- 方法要点：审计16个模型在14个伦理场景下的否定敏感度，提出否定敏感度指数作为治理指标
- 实验或效果：开源模型在简单否定下77%错误支持，复合否定下100%，商业模型波动19-128%

## 摘要（原文）

> When a user tells an AI system that someone "should not" take an action, the system ought to treat this as a prohibition. Yet many large language models do the opposite: they interpret negated instructions as affirmations. We audited 16 models across 14 ethical scenarios and found that open-source models endorse prohibited actions 77% of the time under simple negation and 100% under compound negation -- a 317% increase over affirmative framing. Commercial models fare better but still show swings of 19-128%. Agreement between models drops from 74% on affirmative prompts to 62% on negated ones, and financial scenarios prove twice as fragile as medical ones. These patterns hold under deterministic decoding, ruling out sampling noise. We present case studies showing how these failures play out in practice, propose the Negation Sensitivity Index (NSI) as a governance metric, and outline a tiered certification framework with domain-specific thresholds. The findings point to a gap between what current alignment techniques achieve and what safe deployment requires: models that cannot reliably distinguish "do X" from "do not X" should not be making autonomous decisions in high-stakes contexts.

