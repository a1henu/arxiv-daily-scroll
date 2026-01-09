---
layout: default
title: Evaluative Fingerprints: Stable and Systematic Differences in LLM Evaluator Behavior
---

# Evaluative Fingerprints: Stable and Systematic Differences in LLM Evaluator Behavior
**arXiv**：[2601.05114v1](https://arxiv.org/abs/2601.05114) · [PDF](https://arxiv.org/pdf/2601.05114.pdf)  
**作者**：Wajid Nasser  

**一句话要点**：揭示LLM评估者存在稳定且系统的行为差异，即‘评估指纹’，挑战其作为可互换评估工具的假设。

**关键词**：LLM评估, 评估者一致性, 评估指纹, 可靠性悖论, 评估倾向, 质量理论

## 3 点简述
- 核心问题：LLM评估者间一致性极低，但个体内部行为高度稳定，形成‘可靠性悖论’。
- 方法要点：通过分类器分析评估分数和倾向特征，量化评估者的差异模式，如严苛度和维度侧重。
- 实验或效果：在3240次评估中，分类器仅凭分数识别评估者准确率达77.1%，模型家族内区分度更高。

## 摘要（原文）

> LLM-as-judge systems promise scalable, consistent evaluation. We find the opposite: judges are consistent, but not with each other; they are consistent with themselves. Across 3,240 evaluations (9 judges x 120 unique video x pack items x 3 independent runs), inter-judge agreement is near-zero (Krippendorff's α = 0.042). On two dimensions, judges disagree more than random noise would predict (α < 0). Yet this disagreement isn't chaos; it's structured. A classifier identifies which judge produced an evaluation with 77.1% accuracy from rubric scores alone, rising to 89.9% with disposition features. Within model families, the signal is even stronger: GPT-4.1 and GPT-5.2 are distinguishable with 99.6% accuracy. We call this the reliability paradox: judges cannot agree on what constitutes quality, yet their disagreement patterns are so stable they function as fingerprints. Each judge implements a distinct, stable theory of quality: an "evaluative disposition" that shapes how it interprets any rubric. We characterize these dispositions along multiple axes: harshness/leniency, dimension emphasis, within-judge stability (ICC), and evidence behavior (receipt validity, semantic linkage via NLI, and shotgun index). The implication is stark: LLM judges are not interchangeable instruments measuring a shared construct. They are distinct measurement devices, each encoding its own implicit theory of quality. Averaging their scores produces a synthetic verdict that corresponds to no judge's actual values.

