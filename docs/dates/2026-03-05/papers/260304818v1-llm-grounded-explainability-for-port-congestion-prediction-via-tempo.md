---
layout: default
title: LLM-Grounded Explainability for Port Congestion Prediction via Temporal Graph Attention Networks
---

# LLM-Grounded Explainability for Port Congestion Prediction via Temporal Graph Attention Networks
**arXiv**：[2603.04818v1](https://arxiv.org/abs/2603.04818) · [PDF](https://arxiv.org/pdf/2603.04818.pdf)  
**作者**：Zhiming Xue, Yujue Wang  

**一句话要点**：提出AIS-TGNN框架，结合TGAT与LLM，实现港口拥堵预测与可解释性分析。

**关键词**：港口拥堵预测, 时空图注意力网络, 大语言模型解释, 可解释人工智能, 供应链风险管理

## 3 点简述
- 核心问题：港口拥堵预测系统缺乏可操作解释，影响供应链风险管理。
- 方法要点：基于AIS数据构建时空图，TGAT预测拥堵，LLM生成证据约束的自然语言解释。
- 实验或效果：在洛杉矶和长滩港数据上，AUC达0.761，解释方向一致性99.6%，性能优于基线。

## 摘要（原文）

> Port congestion at major maritime hubs disrupts global supply chains, yet existing prediction systems typically prioritize forecasting accuracy without providing operationally interpretable explanations. This paper proposes AIS-TGNN, an evidence-grounded framework that jointly performs congestion-escalation prediction and faithful natural-language explanation by coupling a Temporal Graph Attention Network (TGAT) with a structured large language model (LLM) reasoning module. Daily spatial graphs are constructed from Automatic Identification System (AIS) broadcasts, where each grid cell represents localized vessel activity and inter-cell interactions are modeled through attention-based message passing. The TGAT predictor captures spatiotemporal congestion dynamics, while model-internal evidence, including feature z-scores and attention-derived neighbor influence, is transformed into structured prompts that constrain LLM reasoning to verifiable model outputs. To evaluate explanatory reliability, we introduce a directional-consistency validation protocol that quantitatively measures agreement between generated narratives and underlying statistical evidence. Experiments on six months of AIS data from the Port of Los Angeles and Long Beach demonstrate that the proposed framework outperforms both LR and GCN baselines, achieving a test AUC of 0.761, AP of 0.344, and recall of 0.504 under a strict chronological split while producing explanations with 99.6% directional consistency. Results show that grounding LLM generation in graph-model evidence enables interpretable and auditable risk reporting without sacrificing predictive performance. The framework provides a practical pathway toward operationally deployable explainable AI for maritime congestion monitoring and supply-chain risk management.

