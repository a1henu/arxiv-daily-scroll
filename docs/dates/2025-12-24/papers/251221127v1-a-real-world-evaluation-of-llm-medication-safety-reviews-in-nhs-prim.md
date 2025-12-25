---
layout: default
title: A Real-World Evaluation of LLM Medication Safety Reviews in NHS Primary Care
---

# A Real-World Evaluation of LLM Medication Safety Reviews in NHS Primary Care
**arXiv**：[2512.21127v1](https://arxiv.org/abs/2512.21127) · [PDF](https://arxiv.org/pdf/2512.21127.pdf)  
**作者**：Oliver Normand, Esther Borsi, Mitch Fruin, Lauren E Walker, Jamie Heagerty, Chris C. Holmes, Anthony J Avery, Iain E Buchan, Harry Coppock  

**一句话要点**：评估LLM在NHS初级保健中药物安全审查的真实世界表现，揭示主要失败模式为情境推理不足。

**关键词**：药物安全审查, 大型语言模型评估, 真实世界数据, 临床情境推理, 失败模式分析, 初级保健

## 3 点简述
- 核心问题：LLM在医学基准测试中表现优异，但缺乏真实临床数据评估，特别是失败行为的详细分析。
- 方法要点：基于NHS Cheshire和Merseyside的212万成人电子健康记录，战略抽样277名患者，由专家临床医生评估LLM系统识别的药物安全问题和干预措施。
- 实验或效果：LLM系统在识别临床问题存在时灵敏度高（100%），但仅46.9%的患者中正确识别所有问题和干预，失败主要源于情境推理错误，如过度自信和指南应用不当。

## 摘要（原文）

> Large language models (LLMs) often match or exceed clinician-level performance on medical benchmarks, yet very few are evaluated on real clinical data or examined beyond headline metrics. We present, to our knowledge, the first evaluation of an LLM-based medication safety review system on real NHS primary care data, with detailed characterisation of key failure behaviours across varying levels of clinical complexity. In a retrospective study using a population-scale EHR spanning 2,125,549 adults in NHS Cheshire and Merseyside, we strategically sampled patients to capture a broad range of clinical complexity and medication safety risk, yielding 277 patients after data-quality exclusions. An expert clinician reviewed these patients and graded system-identified issues and proposed interventions. Our primary LLM system showed strong performance in recognising when a clinical issue is present (sensitivity 100\% [95\% CI 98.2--100], specificity 83.1\% [95\% CI 72.7--90.1]), yet correctly identified all issues and interventions in only 46.9\% [95\% CI 41.1--52.8] of patients. Failure analysis reveals that, in this setting, the dominant failure mechanism is contextual reasoning rather than missing medication knowledge, with five primary patterns: overconfidence in uncertainty, applying standard guidelines without adjusting for patient context, misunderstanding how healthcare is delivered in practice, factual errors, and process blindness. These patterns persisted across patient complexity and demographic strata, and across a range of state-of-the-art models and configurations. We provide 45 detailed vignettes that comprehensively cover all identified failure cases. This work highlights shortcomings that must be addressed before LLM-based clinical AI can be safely deployed. It also begs larger-scale, prospective evaluations and deeper study of LLM behaviours in clinical contexts.

