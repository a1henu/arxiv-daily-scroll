---
layout: default
title: Decomposing Reasoning Efficiency in Large Language Models
---

# Decomposing Reasoning Efficiency in Large Language Models
**arXiv**：[2602.09805v1](https://arxiv.org/abs/2602.09805) · [PDF](https://arxiv.org/pdf/2602.09805.pdf)  
**作者**：Daniel Kaiser, Arnoldo Frigessi, Ali Ramezani-Kebrya, Benjamin Ricaud  

**一句话要点**：提出可追踪框架以分解大语言模型推理效率，揭示令牌使用瓶颈。

**关键词**：大语言模型, 推理效率, 令牌分解, 可追踪框架, CogniLoad基准

## 3 点简述
- 核心问题：现有评估仅关注最终准确率，忽略推理过程中令牌效率的分解。
- 方法要点：引入可追踪框架，将令牌效率分解为完成度、条件正确性和冗余度等可解释因素。
- 实验或效果：在CogniLoad基准上评估25个模型，发现效率排名与准确率排名差异显著，效率差距主要由条件正确性驱动。

## 摘要（原文）

> Large language models trained for reasoning trade off inference tokens against accuracy, yet standard evaluations report only final accuracy, obscuring where tokens are spent or wasted. We introduce a trace-optional framework that decomposes token efficiency into interpretable factors: completion under a fixed token budget (avoiding truncation), conditional correctness given completion, and verbosity (token usage). When benchmark metadata provides per-instance workload proxies, we further factor verbosity into two components: mean verbalization overhead (tokens per work unit) and a coupling coefficient capturing how overhead scales with task workload. When reasoning traces are available, we add deterministic trace-quality measures (grounding, repetition, prompt copying) to separate degenerate looping from verbose-but-engaged reasoning, avoiding human labeling and LLM judges. Evaluating 25 models on CogniLoad, we find that accuracy and token-efficiency rankings diverge (Spearman $ρ=0.63$), efficiency gaps are often driven by conditional correctness, and verbalization overhead varies by about 9 times (only weakly related to model scale). Our decomposition reveals distinct bottleneck profiles that suggest different efficiency interventions.

