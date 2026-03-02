---
layout: default
title: FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation
---

# FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation
**arXiv**：[2602.23636v1](https://arxiv.org/abs/2602.23636) · [PDF](https://arxiv.org/pdf/2602.23636.pdf)  
**作者**：Zhihao Ding, Jinming Li, Ze Lu, Jieming Shi  

**一句话要点**：提出FlexGuard以解决LLM内容审核中严格度变化导致的模型脆弱性问题

**关键词**：LLM内容审核, 严格度自适应, 连续风险评分, 阈值选择, 风险对齐优化

## 3 点简述
- 现有LLM内容审核模型基于固定二元分类，难以适应不同平台和时间的严格度变化
- FlexGuard输出校准的连续风险分数，通过阈值调整支持严格度自适应决策
- 在FlexBench和公开基准测试中，FlexGuard提高了审核准确性和严格度变化下的鲁棒性

## 摘要（原文）

> Ensuring the safety of LLM-generated content is essential for real-world deployment. Most existing guardrail models formulate moderation as a fixed binary classification task, implicitly assuming a fixed definition of harmfulness. In practice, enforcement strictness - how conservatively harmfulness is defined and enforced - varies across platforms and evolves over time, making binary moderators brittle under shifting requirements. We first introduce FlexBench, a strictness-adaptive LLM moderation benchmark that enables controlled evaluation under multiple strictness regimes. Experiments on FlexBench reveal substantial cross-strictness inconsistency in existing moderators: models that perform well under one regime can degrade substantially under others, limiting their practical usability. To address this, we propose FlexGuard, an LLM-based moderator that outputs a calibrated continuous risk score reflecting risk severity and supports strictness-specific decisions via thresholding. We train FlexGuard via risk-alignment optimization to improve score-severity consistency and provide practical threshold selection strategies to adapt to target strictness at deployment. Experiments on FlexBench and public benchmarks demonstrate that FlexGuard achieves higher moderation accuracy and substantially improved robustness under varying strictness. We release the source code and data to support reproducibility.

