---
layout: default
title: PRISM: Festina Lente Proactivity -- Risk-Sensitive, Uncertainty-Aware Deliberation for Proactive Agents
---

# PRISM: Festina Lente Proactivity -- Risk-Sensitive, Uncertainty-Aware Deliberation for Proactive Agents
**arXiv**：[2602.01532v1](https://arxiv.org/abs/2602.01532) · [PDF](https://arxiv.org/pdf/2602.01532.pdf)  
**作者**：Yuxuan Fu, Xiaoyu Tan, Teqi Hao, Chen Zhan, Xihe Qiu  

**一句话要点**：提出PRISM框架，通过决策理论门控和双过程推理解决主动代理的干预时机问题。

**关键词**：主动代理, 决策理论门控, 双过程推理, 成本敏感干预, 蒸馏训练, 不确定性感知

## 3 点简述
- 核心问题：主动代理需权衡干预的收益与负担，现有方法依赖启发式或冗长推理，缺乏可控性。
- 方法要点：结合决策理论门控和双过程推理，仅在用户接受概率超过成本阈值时干预，并选择性调用慢速推理模式。
- 实验或效果：在ProactiveBench上，PRISM减少22.78%误报，提升20.14% F1分数，实现精确、高效和可控的主动代理。

## 摘要（原文）

> Proactive agents must decide not only what to say but also whether and when to intervene. Many current systems rely on brittle heuristics or indiscriminate long reasoning, which offers little control over the benefit-burden tradeoff. We formulate the problem as cost-sensitive selective intervention and present PRISM, a novel framework that couples a decision-theoretic gate with a dual-process reasoning architecture. At inference time, the agent intervenes only when a calibrated probability of user acceptance exceeds a threshold derived from asymmetric costs of missed help and false alarms. Inspired by festina lente (Latin: "make haste slowly"), we gate by an acceptance-calibrated, cost-derived threshold and invoke a resource-intensive Slow mode with counterfactual checks only near the decision boundary, concentrating computation on ambiguous and high-stakes cases. Training uses gate-aligned, schema-locked distillation: a teacher running the full PRISM pipeline provides dense, executable supervision on unlabeled interaction traces, while the student learns a response policy that is explicitly decoupled from the intervention gate to enable tunable and auditable control. On ProactiveBench, PRISM reduces false alarms by 22.78% and improves F1 by 20.14% over strong baselines. These results show that principled decision-theoretic gating, paired with selective slow reasoning and aligned distillation, yields proactive agents that are precise, computationally efficient, and controllable. To facilitate reproducibility, we release our code, models, and resources at https://prism-festinalente.github.io/; all experiments use the open-source ProactiveBench benchmark.

