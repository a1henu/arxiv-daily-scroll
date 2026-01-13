---
layout: default
title: Are LLM Decisions Faithful to Verbal Confidence?
---

# Are LLM Decisions Faithful to Verbal Confidence?
**arXiv**：[2601.07767v1](https://arxiv.org/abs/2601.07767) · [PDF](https://arxiv.org/pdf/2601.07767.pdf)  
**作者**：Jiawei Wang, Yanfei Zhou, Siddartha Devic, Deqing Fu  

**一句话要点**：提出RiskEval框架以评估大语言模型在风险敏感决策中的置信度忠实性

**关键词**：大语言模型, 置信度校准, 风险敏感决策, 弃权策略, 模型评估, 人工智能可信性

## 3 点简述
- 核心问题：大语言模型表达的置信度是否与推理、知识或决策过程忠实关联
- 方法要点：引入RiskEval框架，通过调整错误惩罚来测试模型是否优化弃权策略
- 实验或效果：前沿模型在极端惩罚下几乎不弃权，导致效用崩溃，显示置信度与决策脱节

## 摘要（原文）

> Large Language Models (LLMs) can produce surprisingly sophisticated estimates of their own uncertainty. However, it remains unclear to what extent this expressed confidence is tied to the reasoning, knowledge, or decision making of the model. To test this, we introduce $\textbf{RiskEval}$: a framework designed to evaluate whether models adjust their abstention policies in response to varying error penalties. Our evaluation of several frontier models reveals a critical dissociation: models are neither cost-aware when articulating their verbal confidence, nor strategically responsive when deciding whether to engage or abstain under high-penalty conditions. Even when extreme penalties render frequent abstention the mathematically optimal strategy, models almost never abstain, resulting in utility collapse. This indicates that calibrated verbal confidence scores may not be sufficient to create trustworthy and interpretable AI systems, as current models lack the strategic agency to convert uncertainty signals into optimal and risk-sensitive decisions.

