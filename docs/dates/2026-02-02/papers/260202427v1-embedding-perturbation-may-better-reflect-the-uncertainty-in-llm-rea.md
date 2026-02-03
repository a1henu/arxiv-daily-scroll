---
layout: default
title: Embedding Perturbation may Better Reflect the Uncertainty in LLM Reasoning
---

# Embedding Perturbation may Better Reflect the Uncertainty in LLM Reasoning
**arXiv**：[2602.02427v1](https://arxiv.org/abs/2602.02427) · [PDF](https://arxiv.org/pdf/2602.02427.pdf)  
**作者**：Qihao Wen, Jiahao Wang, Yang Nan, Pengfei He, Ravi Tandon, Han Xu  

**一句话要点**：提出基于嵌入扰动的指标以量化大语言模型推理中的中间不确定性

**关键词**：不确定性量化, 大语言模型推理, 嵌入扰动, 中间步骤分析, 敏感度分数

## 3 点简述
- 核心问题：大语言模型推理任务中，需量化中间步骤的不确定性以支持精细干预
- 方法要点：通过扰动前序词嵌入，计算敏感度分数识别错误推理步骤
- 实验或效果：该指标在不确定性量化性能上优于基线方法，且更简单高效

## 摘要（原文）

> Large language Models (LLMs) have achieved significant breakthroughs across diverse domains; however, they can still produce unreliable or misleading outputs. For responsible LLM application, Uncertainty Quantification (UQ) techniques are used to estimate a model's uncertainty about its outputs, indicating the likelihood that those outputs may be problematic. For LLM reasoning tasks, it is essential to estimate the uncertainty not only for the final answer, but also for the intermediate steps of the reasoning, as this can enable more fine-grained and targeted interventions. In this study, we explore what UQ metrics better reflect the LLM's ``intermediate uncertainty''during reasoning. Our study reveals that an LLMs' incorrect reasoning steps tend to contain tokens which are highly sensitive to the perturbations on the preceding token embeddings. In this way, incorrect (uncertain) intermediate steps can be readily identified using this sensitivity score as guidance in practice. In our experiments, we show such perturbation-based metric achieves stronger uncertainty quantification performance compared with baseline methods such as token (generation) probability and token entropy. Besides, different from approaches that rely on multiple sampling, the perturbation-based metrics offer better simplicity and efficiency.

