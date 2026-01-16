---
layout: default
title: Contextual StereoSet: Stress-Testing Bias Alignment Robustness in Large Language Models
---

# Contextual StereoSet: Stress-Testing Bias Alignment Robustness in Large Language Models
**arXiv**：[2601.10460v1](https://arxiv.org/abs/2601.10460) · [PDF](https://arxiv.org/pdf/2601.10460.pdf)  
**作者**：Abhinaba Basu, Pavan Chakraborty  

**一句话要点**：提出Contextual StereoSet基准以测试大语言模型在不同上下文中的偏见稳健性

**关键词**：偏见评估, 大语言模型, 上下文敏感性, 基准测试, 稳健性分析

## 3 点简述
- 核心问题：固定条件偏见测试可能无法泛化，模型偏见随上下文变化而显著波动
- 方法要点：引入Contextual StereoSet基准，固定刻板印象内容，系统变化上下文框架
- 实验或效果：测试13个模型，发现时间、受众等上下文因素显著影响偏见选择，提出Context Sensitivity Fingerprints进行量化分析

## 摘要（原文）

> A model that avoids stereotypes in a lab benchmark may not avoid them in deployment. We show that measured bias shifts dramatically when prompts mention different places, times, or audiences -- no adversarial prompting required.
>   We introduce Contextual StereoSet, a benchmark that holds stereotype content fixed while systematically varying contextual framing. Testing 13 models across two protocols, we find striking patterns: anchoring to 1990 (vs. 2030) raises stereotype selection in all models tested on this contrast (p<0.05); gossip framing raises it in 5 of 6 full-grid models; out-group observer framing shifts it by up to 13 percentage points. These effects replicate in hiring, lending, and help-seeking vignettes.
>   We propose Context Sensitivity Fingerprints (CSF): a compact profile of per-dimension dispersion and paired contrasts with bootstrap CIs and FDR correction. Two evaluation tracks support different use cases -- a 360-context diagnostic grid for deep analysis and a budgeted protocol covering 4,229 items for production screening.
>   The implication is methodological: bias scores from fixed-condition tests may not generalize.This is not a claim about ground-truth bias rates; it is a stress test of evaluation robustness. CSF forces evaluators to ask, "Under what conditions does bias appear?" rather than "Is this model biased?" We release our benchmark, code, and results.

