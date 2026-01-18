---
layout: default
title: SurgGoal: Rethinking Surgical Planning Evaluation via Goal-Satisfiability
---

# SurgGoal: Rethinking Surgical Planning Evaluation via Goal-Satisfiability
**arXiv**：[2601.10455v1](https://arxiv.org/abs/2601.10455) · [PDF](https://arxiv.org/pdf/2601.10455.pdf)  
**作者**：Ruochen Li, Kun Yuan, Yufei Xia, Yue Zhou, Qingyu Lu, Weihang Li, Youxiang Zhu, Nassir Navab  

**一句话要点**：提出基于阶段目标满足性的手术规划评估方法，以解决现有评估协议在安全关键场景中的不可靠问题。

**关键词**：手术规划评估, 目标满足性, 视觉语言模型, 元评估基准, 规则驱动评估

## 3 点简述
- 核心问题：现有评估协议难以可靠评估视觉语言模型在安全关键手术规划中的性能。
- 方法要点：通过专家定义的手术规则，基于阶段目标满足性定义规划正确性，并引入多中心元评估基准。
- 实验或效果：序列相似性指标系统性地误判规划质量，而基于规则的指标能高精度评估模型，揭示感知错误和推理不足。

## 摘要（原文）

> Surgical planning integrates visual perception, long-horizon reasoning, and procedural knowledge, yet it remains unclear whether current evaluation protocols reliably assess vision-language models (VLMs) in safety-critical settings. Motivated by a goal-oriented view of surgical planning, we define planning correctness via phase-goal satisfiability, where plan validity is determined by expert-defined surgical rules. Based on this definition, we introduce a multicentric meta-evaluation benchmark with valid procedural variations and invalid plans containing order and content errors. Using this benchmark, we show that sequence similarity metrics systematically misjudge planning quality, penalizing valid plans while failing to identify invalid ones. We therefore adopt a rule-based goal-satisfiability metric as a high-precision meta-evaluation reference to assess Video-LLMs under progressively constrained settings, revealing failures due to perception errors and under-constrained reasoning. Structural knowledge consistently improves performance, whereas semantic guidance alone is unreliable and benefits larger models only when combined with structural constraints.

