---
layout: default
title: Causality is Key for Interpretability Claims to Generalise
---

# Causality is Key for Interpretability Claims to Generalise
**arXiv**：[2602.16698v1](https://arxiv.org/abs/2602.16698) · [PDF](https://arxiv.org/pdf/2602.16698.pdf)  
**作者**：Shruti Joshi, Aaron Mueller, David Klindt, Wieland Brendel, Patrik Reizinger, Dhanya Sridhar  

**一句话要点**：提出因果推理框架以提升大语言模型可解释性研究的泛化能力

**关键词**：大语言模型可解释性, 因果推理, 因果表示学习, 干预实验, 泛化性评估, 模型诊断

## 3 点简述
- 指出当前可解释性研究存在泛化性不足和因果推断过度的问题
- 引入Pearl因果层次理论阐明不同干预方法对应的可验证性边界
- 提出基于因果表示学习的诊断框架以匹配证据与结论

## 摘要（原文）

> Interpretability research on large language models (LLMs) has yielded important insights into model behaviour, yet recurring pitfalls persist: findings that do not generalise, and causal interpretations that outrun the evidence. Our position is that causal inference specifies what constitutes a valid mapping from model activations to invariant high-level structures, the data or assumptions needed to achieve it, and the inferences it can support. Specifically, Pearl's causal hierarchy clarifies what an interpretability study can justify. Observations establish associations between model behaviour and internal components. Interventions (e.g., ablations or activation patching) support claims how these edits affect a behavioural metric (\eg, average change in token probabilities) over a set of prompts. However, counterfactual claims -- i.e., asking what the model output would have been for the same prompt under an unobserved intervention -- remain largely unverifiable without controlled supervision. We show how causal representation learning (CRL) operationalises this hierarchy, specifying which variables are recoverable from activations and under what assumptions. Together, these motivate a diagnostic framework that helps practitioners select methods and evaluations matching claims to evidence such that findings generalise.

