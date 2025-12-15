---
layout: default
title: CIP: A Plug-and-Play Causal Prompting Framework for Mitigating Hallucinations under Long-Context Noise
---

# CIP: A Plug-and-Play Causal Prompting Framework for Mitigating Hallucinations under Long-Context Noise
**arXiv**：[2512.11282v1](https://arxiv.org/abs/2512.11282) · [PDF](https://arxiv.org/pdf/2512.11282.pdf)  
**作者**：Qingsen Ma, Dianyun Wang, Ran Jing, Yujun Sun, Zhenbo Xu  

**一句话要点**：提出CIP因果提示框架以缓解长上下文噪声下的幻觉问题

**关键词**：因果推理, 幻觉缓解, 长上下文处理, 提示工程, 大语言模型

## 3 点简述
- 核心问题：大语言模型在长噪声检索上下文中因依赖伪相关而产生幻觉
- 方法要点：构建实体-动作-事件因果序列并注入提示，引导因果推理
- 实验或效果：在七种主流模型中提升归因率和因果一致性，降低响应延迟

## 摘要（原文）

> Large language models often hallucinate when processing long and noisy retrieval contexts because they rely on spurious correlations rather than genuine causal relationships. We propose CIP, a lightweight and plug-and-play causal prompting framework that mitigates hallucinations at the input stage. CIP constructs a causal relation sequence among entities, actions, and events and injects it into the prompt to guide reasoning toward causally relevant evidence. Through causal intervention and counterfactual reasoning, CIP suppresses non causal reasoning paths, improving factual grounding and interpretability. Experiments across seven mainstream language models, including GPT-4o, Gemini 2.0 Flash, and Llama 3.1, show that CIP consistently enhances reasoning quality and reliability, achieving 2.6 points improvement in Attributable Rate, 0.38 improvement in Causal Consistency Score, and a fourfold increase in effective information density. API level profiling further shows that CIP accelerates contextual understanding and reduces end to end response latency by up to 55.1 percent. These results suggest that causal reasoning may serve as a promising paradigm for improving the explainability, stability, and efficiency of large language models.

