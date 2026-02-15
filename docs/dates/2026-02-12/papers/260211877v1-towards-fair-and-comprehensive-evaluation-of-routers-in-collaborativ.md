---
layout: default
title: Towards Fair and Comprehensive Evaluation of Routers in Collaborative LLM Systems
---

# Towards Fair and Comprehensive Evaluation of Routers in Collaborative LLM Systems
**arXiv**：[2602.11877v1](https://arxiv.org/abs/2602.11877) · [PDF](https://arxiv.org/pdf/2602.11877.pdf)  
**作者**：Wanxing Wu, He Zhu, Yixia Li, Lei Yang, Jiehui Zhao, Hongru Wang, Jian Yang, Benyou Wang, Bingyi Jing, Guanhua Chen  

**一句话要点**：提出RouterXBench框架和ProbeDirichlet路由器，以系统评估和提升协作LLM系统中的路由性能。

**关键词**：协作LLM系统, 路由器评估, 内部隐藏状态, 狄利克雷分布, 跨域鲁棒性, 轻量级路由器

## 3 点简述
- 现有路由器评估缺乏系统性，忽视场景对齐和跨域鲁棒性。
- 利用内部隐藏状态捕获模型不确定性，提出基于可学习狄利克雷分布的轻量级路由器。
- 在路由器能力和高精度场景中相对最佳基线提升16.68%和18.86%，跨模型和任务表现一致。

## 摘要（原文）

> Large language models (LLMs) have achieved success, but cost and privacy constraints necessitate deploying smaller models locally while offloading complex queries to cloud-based models. Existing router evaluations are unsystematic, overlooking scenario-specific requirements and out-of-distribution robustness. We propose RouterXBench, a principled evaluation framework with three dimensions: router ability, scenario alignment, and cross-domain robustness. Unlike prior work that relies on output probabilities or external embeddings, we utilize internal hidden states that capture model uncertainty before answer generation. We introduce ProbeDirichlet, a lightweight router that aggregates cross-layer hidden states via learnable Dirichlet distributions with probabilistic training. Trained on multi-domain data, it generalizes robustly across in-domain and out-of-distribution scenarios. Our results show ProbeDirichlet achieves 16.68% and 18.86% relative improvements over the best baselines in router ability and high-accuracy scenarios, with consistent performance across model families, model scales, heterogeneous tasks, and agentic workflows.

