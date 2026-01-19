---
layout: default
title: ABC-Bench: Benchmarking Agentic Backend Coding in Real-World Development
---

# ABC-Bench: Benchmarking Agentic Backend Coding in Real-World Development
**arXiv**：[2601.11077v1](https://arxiv.org/abs/2601.11077) · [PDF](https://arxiv.org/pdf/2601.11077.pdf)  
**作者**：Jie Yang, Honglin Guo, Li Ji, Jiazheng Zhou, Rui Zheng, Zhikai Lei, Shuo Zhang, Zhiheng Xi, Shichun Liu, Yuxin Wang, Bo Wang, Yining Zheng, Tao Gui, Xipeng Qiu  

**一句话要点**：提出ABC-Bench以评估现实后端开发中的智能体编码能力

**关键词**：智能体编码评估, 后端开发基准, 全流程任务, 容器化服务, API测试, 多语言框架

## 3 点简述
- 当前基准在静态环境中评估代码逻辑，忽略现实后端开发的动态全流程需求
- ABC-Bench通过自动化管道构建224个多语言多框架任务，要求智能体管理从仓库探索到容器化服务部署的完整生命周期
- 评估显示先进模型在这些整体任务上表现不佳，揭示模型能力与实际工程需求间的差距

## 摘要（原文）

> The evolution of Large Language Models (LLMs) into autonomous agents has expanded the scope of AI coding from localized code generation to complex, repository-level, and execution-driven problem solving. However, current benchmarks predominantly evaluate code logic in static contexts, neglecting the dynamic, full-process requirements of real-world engineering, particularly in backend development which demands rigorous environment configuration and service deployment. To address this gap, we introduce ABC-Bench, a benchmark explicitly designed to evaluate agentic backend coding within a realistic, executable workflow. Using a scalable automated pipeline, we curated 224 practical tasks spanning 8 languages and 19 frameworks from open-source repositories. Distinct from previous evaluations, ABC-Bench require the agents to manage the entire development lifecycle from repository exploration to instantiating containerized services and pass the external end-to-end API tests. Our extensive evaluation reveals that even state-of-the-art models struggle to deliver reliable performance on these holistic tasks, highlighting a substantial disparity between current model capabilities and the demands of practical backend engineering. Our code is available at https://github.com/OpenMOSS/ABC-Bench.

