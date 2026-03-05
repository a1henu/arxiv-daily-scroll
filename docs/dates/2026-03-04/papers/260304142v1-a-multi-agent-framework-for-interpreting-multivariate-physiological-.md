---
layout: default
title: A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series
---

# A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series
**arXiv**：[2603.04142v1](https://arxiv.org/abs/2603.04142) · [PDF](https://arxiv.org/pdf/2603.04142.pdf)  
**作者**：Davide Gabrielli, Paola Velardi, Stefano Faralli, Bardh Prenkaj  

**一句话要点**：提出Vivaldi多智能体框架以解释多元生理时间序列，评估其在急诊医疗中的性能与设计权衡。

**关键词**：多智能体系统, 生理时间序列解释, 急诊医疗AI, 可解释人工智能, 临床评估, 智能体推理

## 3 点简述
- 核心问题：在急诊医疗中，如何评估多智能体系统相对于零样本推理在解释生理信号时的性能与临床效用。
- 方法要点：开发Vivaldi角色结构化多智能体系统，通过专家评估在受控临床试点中测试其解释能力。
- 实验或效果：智能体管道提升非思考模型性能，但对思考模型可能降低解释质量，同时工具计算对客观指标关键，主观指标变化有限。

## 摘要（原文）

> Continuous physiological monitoring is central to emergency care, yet deploying trustworthy AI is challenging. While LLMs can translate complex physiological signals into clinical narratives, it is unclear how agentic systems perform relative to zero-shot inference. To address these questions, we present Vivaldi, a role-structured multi-agent system that explains multivariate physiological time series. Due to regulatory constraints that preclude live deployment, we instantiate Vivaldi in a controlled, clinical pilot to a small, highly qualified cohort of emergency medicine experts, whose evaluations reveal a context-dependent picture that contrasts with prevailing assumptions that agentic reasoning uniformly improves performance. Our experiments show that agentic pipelines substantially benefit non-thinking and medically fine-tuned models, improving expert-rated explanation justification and relevance by +6.9 and +9.7 points, respectively. Contrarily, for thinking models, agentic orchestration often degrades explanation quality, including a 14-point drop in relevance, while improving diagnostic precision (ESI F1 +3.6). We also find that explicit tool-based computation is decisive for codifiable clinical metrics, whereas subjective targets, such as pain scores and length of stay, show limited or inconsistent changes. Expert evaluation further indicates that gains in clinical utility depend on visualization conventions, with medically specialized models achieving the most favorable trade-offs between utility and clarity. Together, these findings show that the value of agentic AI lies in the selective externalization of computation and structure rather than in maximal reasoning complexity, and highlight concrete design trade-offs and learned lessons, broadly applicable to explainable AI in safety-critical healthcare settings.

