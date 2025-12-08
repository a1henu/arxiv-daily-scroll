---
layout: default
title: Model Gateway: Model Management Platform for Model-Driven Drug Discovery
---

# Model Gateway: Model Management Platform for Model-Driven Drug Discovery
**arXiv**：[2512.05462v1](https://arxiv.org/abs/2512.05462) · [PDF](https://arxiv.org/pdf/2512.05462.pdf)  
**作者**：Yan-Shiun Wu, Nathan A. Morin  

**一句话要点**：提出Model Gateway平台以管理药物发现中的机器学习与科学计算模型

**关键词**：模型管理平台, 药物发现, MLOps, LLM代理, 生成式AI, 动态共识模型

## 3 点简述
- 核心问题：药物发现中ML和科学计算模型的管理与集成挑战
- 方法要点：支持LLM代理和生成式AI工具，提供动态共识模型、注册管理和异步执行功能
- 实验或效果：测试中实现超过1万并发客户端零失败率，加速药物研发

## 摘要（原文）

> This paper presents the Model Gateway, a management platform for managing machine learning (ML) and scientific computational models in the drug discovery pipeline. The platform supports Large Language Model (LLM) Agents and Generative AI-based tools to perform ML model management tasks in our Machine Learning operations (MLOps) pipelines, such as the dynamic consensus model, a model that aggregates several scientific computational models, registration and management, retrieving model information, asynchronous submission/execution of models, and receiving results once the model complete executions. The platform includes a Model Owner Control Panel, Platform Admin Tools, and Model Gateway API service for interacting with the platform and tracking model execution. The platform achieves a 0% failure rate when testing scaling beyond 10k simultaneous application clients consume models. The Model Gateway is a fundamental part of our model-driven drug discovery pipeline. It has the potential to significantly accelerate the development of new drugs with the maturity of our MLOps infrastructure and the integration of LLM Agents and Generative AI tools.

