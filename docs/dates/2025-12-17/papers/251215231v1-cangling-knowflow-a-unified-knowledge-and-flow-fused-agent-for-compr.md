---
layout: default
title: CangLing-KnowFlow: A Unified Knowledge-and-Flow-fused Agent for Comprehensive Remote Sensing Applications
---

# CangLing-KnowFlow: A Unified Knowledge-and-Flow-fused Agent for Comprehensive Remote Sensing Applications
**arXiv**：[2512.15231v1](https://arxiv.org/abs/2512.15231) · [PDF](https://arxiv.org/pdf/2512.15231.pdf)  
**作者**：Zhengchao Chen, Haoran Wang, Jing Yao, Pedram Ghamisi, Jun Zhou, Peter M. Atkinson, Bing Zhang  

**一句话要点**：提出CangLing-KnowFlow统一智能体框架，以解决遥感应用端到端工作流自动化问题。

**关键词**：遥感智能体, 过程知识库, 动态工作流调整, 进化记忆模块, 端到端自动化, 大语言模型评估

## 3 点简述
- 核心问题：现有遥感自动化系统任务特定，缺乏统一框架管理从预处理到高级解释的多样化工作流。
- 方法要点：集成过程知识库、动态工作流调整和进化记忆模块，利用专家知识指导规划并自适应学习。
- 实验或效果：在KnowFlow-Bench基准测试中，任务成功率比Reflexion基线至少提升4%，验证了其鲁棒性和可扩展性。

## 摘要（原文）

> The automated and intelligent processing of massive remote sensing (RS) datasets is critical in Earth observation (EO). Existing automated systems are normally task-specific, lacking a unified framework to manage diverse, end-to-end workflows--from data preprocessing to advanced interpretation--across diverse RS applications. To address this gap, this paper introduces CangLing-KnowFlow, a unified intelligent agent framework that integrates a Procedural Knowledge Base (PKB), Dynamic Workflow Adjustment, and an Evolutionary Memory Module. The PKB, comprising 1,008 expert-validated workflow cases across 162 practical RS tasks, guides planning and substantially reduces hallucinations common in general-purpose agents. During runtime failures, the Dynamic Workflow Adjustment autonomously diagnoses and replans recovery strategies, while the Evolutionary Memory Module continuously learns from these events, iteratively enhancing the agent's knowledge and performance. This synergy enables CangLing-KnowFlow to adapt, learn, and operate reliably across diverse, complex tasks. We evaluated CangLing-KnowFlow on the KnowFlow-Bench, a novel benchmark of 324 workflows inspired by real-world applications, testing its performance across 13 top Large Language Model (LLM) backbones, from open-source to commercial. Across all complex tasks, CangLing-KnowFlow surpassed the Reflexion baseline by at least 4% in Task Success Rate. As the first most comprehensive validation along this emerging field, this research demonstrates the great potential of CangLing-KnowFlow as a robust, efficient, and scalable automated solution for complex EO challenges by leveraging expert knowledge (Knowledge) into adaptive and verifiable procedures (Flow).

