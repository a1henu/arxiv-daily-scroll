---
layout: default
title: Right for the Wrong Reasons: Epistemic Regret Minimization for Causal Rung Collapse in LLMs
---

# Right for the Wrong Reasons: Epistemic Regret Minimization for Causal Rung Collapse in LLMs
**arXiv**：[2602.11675v1](https://arxiv.org/abs/2602.11675) · [PDF](https://arxiv.org/pdf/2602.11675.pdf)  
**作者**：Edward Y. Chang  

**一句话要点**：提出认知遗憾最小化以解决大语言模型中的因果层级塌缩问题

**关键词**：因果推理, 大语言模型, 认知遗憾最小化, 信念修正, 分布偏移, 干预学习

## 3 点简述
- 核心问题：自回归训练导致模型混淆关联与干预，形成因果层级塌缩和错误推理固化。
- 方法要点：引入认知遗憾最小化作为因果信念修正算子，结合三层架构和物理接地定理。
- 实验或效果：在1360个因果陷阱场景中，该方法能恢复53-59%的固化错误，而结果级反馈失败。

## 摘要（原文）

> Machine learning systems that are "right for the wrong reasons" achieve high performance through shortcuts that collapse under distributional shift. We show this pathology has a precise causal origin: autoregressive training provides no gradient signal to distinguish association P(Y\|X) from intervention P(Y\|do(X)), a failure we formalize as Rung Collapse. When outcome-based learning reinforces correct answers obtained through incorrect causal models, the agent becomes entrenched in flawed reasoning, a phenomenon we term Aleatoric Entrenchment. We propose Epistemic Regret Minimization (ERM), a belief revision objective that penalizes errors in causal reasoning independently of task success, and embed it within a three-layer architecture with three contributions grounded in knowledge representation: (1) a Physical Grounding Theorem proving that actions satisfying actuator independence implement valid do-operations, bridging action languages and do-calculus; (2) ERM as a causal belief revision operator satisfying AGM postulates, preventing entrenchment even when the agent succeeds for the wrong reasons; and (3) a failure mode taxonomy that classifies recurring reasoning errors and injects domain-independent guards, enabling cross-domain transfer. We prove asymptotic recovery of the true interventional distribution with finite-sample bounds. Experiments on 1,360 causal trap scenarios across six frontier LLMs reveal that Rung Collapse persists even in reasoning-enhanced models (3.7% for GPT-5.2), that steerability exhibits inverse scaling where advanced models resist generic correction, and that targeted ERM feedback recovers 53-59% of entrenched errors where outcome-level feedback fails.

