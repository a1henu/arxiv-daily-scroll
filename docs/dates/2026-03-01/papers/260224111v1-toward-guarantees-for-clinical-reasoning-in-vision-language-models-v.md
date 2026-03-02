---
layout: default
title: Toward Guarantees for Clinical Reasoning in Vision Language Models via Formal Verification
---

# Toward Guarantees for Clinical Reasoning in Vision Language Models via Formal Verification
**arXiv**：[2602.24111v1](https://arxiv.org/abs/2602.24111) · [PDF](https://arxiv.org/pdf/2602.24111.pdf)  
**作者**：Vikash Singh, Debargha Ganguly, Haotian Yu, Chengwei Zhou, Prerna Singh, Brandon Lee, Vipin Chaudhary, Gourav Datta  

**一句话要点**：提出神经符号验证框架，通过形式化验证确保视觉语言模型在临床推理中的内部一致性。

**关键词**：视觉语言模型, 临床推理, 形式化验证, 神经符号框架, 放射学报告生成, SMT求解器

## 3 点简述
- 核心问题：视觉语言模型在生成放射学报告时存在逻辑不一致，如诊断印象与感知发现不匹配或遗漏逻辑结论。
- 方法要点：利用SMT求解器和临床知识库，将自由文本发现形式化为命题证据，验证诊断声明的数学蕴含性。
- 实验或效果：在五个胸部X光基准上评估七个模型，验证器揭示了传统指标不可见的推理失败模式，并显著提高诊断准确性和精确度。

## 摘要（原文）

> Vision-language models (VLMs) show promise in drafting radiology reports, yet they frequently suffer from logical inconsistencies, generating diagnostic impressions unsupported by their own perceptual findings or missing logically entailed conclusions. Standard lexical metrics heavily penalize clinical paraphrasing and fail to capture these deductive failures in reference-free settings. Toward guarantees for clinical reasoning, we introduce a neurosymbolic verification framework that deterministically audits the internal consistency of VLM-generated reports. Our pipeline autoformalizes free-text radiographic findings into structured propositional evidence, utilizing an SMT solver (Z3) and a clinical knowledge base to verify whether each diagnostic claim is mathematically entailed, hallucinated, or omitted. Evaluating seven VLMs across five chest X-ray benchmarks, our verifier exposes distinct reasoning failure modes, such as conservative observation and stochastic hallucination, that remain invisible to traditional metrics. On labeled datasets, enforcing solver-backed entailment acts as a rigorous post-hoc guarantee, systematically eliminating unsupported hallucinations to significantly increase diagnostic soundness and precision in generative clinical assistants.

