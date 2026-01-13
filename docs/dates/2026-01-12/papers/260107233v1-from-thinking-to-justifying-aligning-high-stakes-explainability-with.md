---
layout: default
title: From "Thinking" to "Justifying": Aligning High-Stakes Explainability with Professional Communication Standards
---

# From "Thinking" to "Justifying": Aligning High-Stakes Explainability with Professional Communication Standards
**arXiv**：[2601.07233v1](https://arxiv.org/abs/2601.07233) · [PDF](https://arxiv.org/pdf/2601.07233.pdf)  
**作者**：Chen Qian, Yimeng Wang, Yu Chen, Lingfei Wu, Andreas Stathopoulos  

**一句话要点**：提出SEF框架以在高风险领域通过结构化论证提升可解释AI的可靠性和可验证性

**关键词**：可解释人工智能, 高风险领域, 结构化论证, 思维链方法, 专业通信标准, 可验证性

## 3 点简述
- 核心问题：高风险领域可解释AI中，思维链方法存在逻辑漏洞或幻觉，导致结论与理由不一致。
- 方法要点：提出'结果->论证'方法，强制输出先结论后结构化论证，并引入SEF框架基于专业标准定义六个评估指标。
- 实验或效果：在三个领域的四个任务中验证，SEF准确率达83.9%，比思维链方法提升5.3%，所有指标与正确性显著相关。

## 摘要（原文）

> Explainable AI (XAI) in high-stakes domains should help stakeholders trust and verify system outputs. Yet Chain-of-Thought methods reason before concluding, and logical gaps or hallucinations can yield conclusions that do not reliably align with their rationale. Thus, we propose "Result -> Justify", which constrains the output communication to present a conclusion before its structured justification. We introduce SEF (Structured Explainability Framework), operationalizing professional conventions (e.g., CREAC, BLUF) via six metrics for structure and grounding. Experiments across four tasks in three domains validate this approach: all six metrics correlate with correctness (r=0.20-0.42; p<0.001), and SEF achieves 83.9% accuracy (+5.3 over CoT). These results suggest structured justification can improve verifiability and may also improve reliability.

