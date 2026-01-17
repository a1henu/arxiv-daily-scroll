---
layout: default
title: Contextual StereoSet: Stress-Testing Bias Alignment Robustness in Large Language Models
---

# Contextual StereoSet: Stress-Testing Bias Alignment Robustness in Large Language Models
**arXiv**：[2601.10460v1](https://arxiv.org/abs/2601.10460) · [PDF](https://arxiv.org/pdf/2601.10460.pdf)  
**作者**：Abhinaba Basu, Pavan Chakraborty  

**一句话要点**：提出Contextual StereoSet基准，通过系统变化上下文框架来压力测试大语言模型的偏见对齐鲁棒性。

**关键词**：偏见评估, 上下文敏感性, 大语言模型基准, 鲁棒性测试, 刻板印象分析

## 3 点简述
- 核心问题：实验室基准中避免刻板印象的模型在部署时可能失效，因偏见测量随上下文（如地点、时间、受众）变化而显著偏移。
- 方法要点：引入Contextual StereoSet基准，固定刻板印象内容，系统变化上下文框架，并开发Context Sensitivity Fingerprints（CSF）进行紧凑分析。
- 实验或效果：测试13个模型，发现上下文变化（如锚定1990年、八卦框架）显著影响刻板印象选择，效应在多个场景中可复制。

## 摘要（原文）

> A model that avoids stereotypes in a lab benchmark may not avoid them in deployment. We show that measured bias shifts dramatically when prompts mention different places, times, or audiences -- no adversarial prompting required.
>   We introduce Contextual StereoSet, a benchmark that holds stereotype content fixed while systematically varying contextual framing. Testing 13 models across two protocols, we find striking patterns: anchoring to 1990 (vs. 2030) raises stereotype selection in all models tested on this contrast (p<0.05); gossip framing raises it in 5 of 6 full-grid models; out-group observer framing shifts it by up to 13 percentage points. These effects replicate in hiring, lending, and help-seeking vignettes.
>   We propose Context Sensitivity Fingerprints (CSF): a compact profile of per-dimension dispersion and paired contrasts with bootstrap CIs and FDR correction. Two evaluation tracks support different use cases -- a 360-context diagnostic grid for deep analysis and a budgeted protocol covering 4,229 items for production screening.
>   The implication is methodological: bias scores from fixed-condition tests may not generalize.This is not a claim about ground-truth bias rates; it is a stress test of evaluation robustness. CSF forces evaluators to ask, "Under what conditions does bias appear?" rather than "Is this model biased?" We release our benchmark, code, and results.

