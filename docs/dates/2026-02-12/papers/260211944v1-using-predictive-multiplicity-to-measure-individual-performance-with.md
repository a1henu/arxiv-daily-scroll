---
layout: default
title: Using predictive multiplicity to measure individual performance within the AI Act
---

# Using predictive multiplicity to measure individual performance within the AI Act
**arXiv**：[2602.11944v1](https://arxiv.org/abs/2602.11944) · [PDF](https://arxiv.org/pdf/2602.11944.pdf)  
**作者**：Karolin Frohnapfel, Mara Seyfert, Sebastian Bordt, Ulrike von Luxburg, Kristof Meding  

**一句话要点**：提出预测多样性评估方法以支持欧盟AI法案下高风险AI系统的个体性能报告

**关键词**：预测多样性, 欧盟AI法案, 个体性能评估, 模型分歧, 高风险AI系统, 准确性报告

## 3 点简述
- 核心问题：预测多样性导致AI模型对个体案例的预测不一致，可能违反欧盟AI法案的准确性要求。
- 方法要点：建议使用个体冲突比和δ-模糊度量化模型间个体预测分歧，帮助检测受冲突预测影响的个体。
- 实验或效果：基于计算分析，推导易于实施的规则，指导模型提供商在实践中评估预测多样性。

## 摘要（原文）

> When building AI systems for decision support, one often encounters the phenomenon of predictive multiplicity: a single best model does not exist; instead, one can construct many models with similar overall accuracy that differ in their predictions for individual cases. Especially when decisions have a direct impact on humans, this can be highly unsatisfactory. For a person subject to high disagreement between models, one could as well have chosen a different model of similar overall accuracy that would have decided the person's case differently. We argue that this arbitrariness conflicts with the EU AI Act, which requires providers of high-risk AI systems to report performance not only at the dataset level but also for specific persons. The goal of this paper is to put predictive multiplicity in context with the EU AI Act's provisions on accuracy and to subsequently derive concrete suggestions on how to evaluate and report predictive multiplicity in practice. Specifically: (1) We argue that incorporating information about predictive multiplicity can serve compliance with the EU AI Act's accuracy provisions for providers. (2) Based on this legal analysis, we suggest individual conflict ratios and $δ$-ambiguity as tools to quantify the disagreement between models on individual cases and to help detect individuals subject to conflicting predictions. (3) Based on computational insights, we derive easy-to-implement rules on how model providers could evaluate predictive multiplicity in practice. (4) Ultimately, we suggest that information about predictive multiplicity should be made available to deployers under the AI Act, enabling them to judge whether system outputs for specific individuals are reliable enough for their use case.

