---
layout: default
title: SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning
---

# SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning
**arXiv**：[2602.19455v1](https://arxiv.org/abs/2602.19455) · [PDF](https://arxiv.org/pdf/2602.19455.pdf)  
**作者**：Zelin He, Boran Han, Xiyuan Zhang, Shuai Zhang, Haotian Lin, Qi Zhu, Haoyang Fang, Danielle C. Maddix, Abdul Fatir Ansari, Akash Chandrayan, Abhinav Pradhan, Bernie Wang, Matthew Reimherr  

**一句话要点**：提出混合知识注入框架以解决时间序列诊断推理中通用与领域模型能力不匹配问题

**关键词**：时间序列推理, 知识注入, 强化学习, 诊断推理, 混合模型

## 3 点简述
- 核心问题：通用推理大模型缺乏时间序列领域知识，而领域模型推理泛化能力不足
- 方法要点：通过强化学习生成知识丰富轨迹，注入通用模型实现高效知识融合
- 实验或效果：在SenTSR-Bench等数据集上超越基线模型，提升7.9%-26.1%

## 摘要（原文）

> Time-series diagnostic reasoning is essential for many applications, yet existing solutions face a persistent gap: general reasoning large language models (GRLMs) possess strong reasoning skills but lack the domain-specific knowledge to understand complex time-series patterns. Conversely, fine-tuned time-series LLMs (TSLMs) understand these patterns but lack the capacity to generalize reasoning for more complicated questions. To bridge this gap, we propose a hybrid knowledge-injection framework that injects TSLM-generated insights directly into GRLM's reasoning trace, thereby achieving strong time-series reasoning with in-domain knowledge. As collecting data for knowledge injection fine-tuning is costly, we further leverage a reinforcement learning-based approach with verifiable rewards (RLVR) to elicit knowledge-rich traces without human supervision, then transfer such an in-domain thinking trace into GRLM for efficient knowledge injection. We further release SenTSR-Bench, a multivariate time-series-based diagnostic reasoning benchmark collected from real-world industrial operations. Across SenTSR-Bench and other public datasets, our method consistently surpasses TSLMs by 9.1%-26.1% and GRLMs by 7.9%-22.4%, delivering robust, context-aware time-series diagnostic insights.

