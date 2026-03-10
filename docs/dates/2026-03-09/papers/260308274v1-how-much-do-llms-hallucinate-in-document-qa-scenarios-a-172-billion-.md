---
layout: default
title: How Much Do LLMs Hallucinate in Document Q&A Scenarios? A 172-Billion-Token Study Across Temperatures, Context Lengths, and Hardware Platforms
---

# How Much Do LLMs Hallucinate in Document Q&A Scenarios? A 172-Billion-Token Study Across Temperatures, Context Lengths, and Hardware Platforms
**arXiv**：[2603.08274v1](https://arxiv.org/abs/2603.08274) · [PDF](https://arxiv.org/pdf/2603.08274.pdf)  
**作者**：JV Roig  

**一句话要点**：提出RIKER评估方法，在1720亿token规模下量化LLM在文档问答中的幻觉率

**关键词**：文档问答幻觉, RIKER评估方法, 上下文长度影响, 模型选择, 硬件平台一致性, 温度设置效应

## 3 点简述
- 核心问题：量化LLM在文档问答中的幻觉程度，现有方法受限于数据污染、偏见或规模不足
- 方法要点：采用RIKER方法，基于真实优先原则实现无需人工标注的确定性评分
- 实验或效果：评估35个模型，发现幻觉率随上下文长度显著上升，模型选择是关键因素，硬件平台影响一致

## 摘要（原文）

> How much do large language models actually hallucinate when answering questions grounded in provided documents? Despite the critical importance of this question for enterprise AI deployments, reliable measurement has been hampered by benchmarks that rely on static datasets vulnerable to contamination, LLM-based judges with documented biases, or evaluation scales too small for statistical confidence. We address this gap using RIKER, a ground-truth-first evaluation methodology that enables deterministic scoring without human annotation. Across 35 open-weight models, three context lengths (32K, 128K, and 200K tokens), four temperature settings, and three hardware platforms (NVIDIA H200, AMD MI300X, and Intel Gaudi 3), we conducted over 172 billion tokens of evaluation - an order of magnitude beyond prior work. Our findings reveal that: (1) even the best-performing models fabricate answers at a non-trivial rate - 1.19% at best at 32K, with top-tier models at 5 - 7% - and fabrication rises steeply with context length, nearly tripling at 128K and exceeding 10% for all models at 200K; (2) model selection dominates all other factors, with overall accuracy spanning a 72-percentage-point range and model family predicting fabrication resistance better than model size; (3) temperature effects are nuanced - T=0.0 yields the best overall accuracy in roughly 60% of cases, but higher temperatures reduce fabrication for the majority of models and dramatically reduce coherence loss (infinite generation loops), which can reach 48x higher rates at T=0.0 versus T=1.0; (4) grounding ability and fabrication resistance are distinct capabilities - models that excel at finding facts may still fabricate facts that do not exist; and (5) results are consistent across hardware platforms, confirming that deployment decisions need not be hardware-dependent.

