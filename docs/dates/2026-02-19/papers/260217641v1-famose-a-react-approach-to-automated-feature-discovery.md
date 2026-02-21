---
layout: default
title: FAMOSE: A ReAct Approach to Automated Feature Discovery
---

# FAMOSE: A ReAct Approach to Automated Feature Discovery
**arXiv**：[2602.17641v1](https://arxiv.org/abs/2602.17641) · [PDF](https://arxiv.org/pdf/2602.17641.pdf)  
**作者**：Keith Burghardt, Jienan Liu, Sadman Sakib, Yuning Hao, Bo Li  

**一句话要点**：提出FAMOSE框架，基于ReAct范式自动化特征工程以解决表格数据特征发现难题

**关键词**：特征工程, ReAct范式, 智能体架构, 表格数据, 自动化特征发现

## 3 点简述
- 核心问题：特征工程在机器学习中至关重要，但传统方法依赖领域专家，难以从指数级特征空间中识别最优特征
- 方法要点：FAMOSE利用ReAct范式，通过智能体架构自主探索、生成和优化特征，集成特征选择与评估工具
- 实验或效果：在分类任务中接近或达到SOTA，回归任务中平均降低RMSE 2.0%，对错误更鲁棒

## 摘要（原文）

> Feature engineering remains a critical yet challenging bottleneck in machine learning, particularly for tabular data, as identifying optimal features from an exponentially large feature space traditionally demands substantial domain expertise. To address this challenge, we introduce FAMOSE (Feature AugMentation and Optimal Selection agEnt), a novel framework that leverages the ReAct paradigm to autonomously explore, generate, and refine features while integrating feature selection and evaluation tools within an agent architecture. To our knowledge, FAMOSE represents the first application of an agentic ReAct framework to automated feature engineering, especially for both regression and classification tasks. Extensive experiments demonstrate that FAMOSE is at or near the state-of-the-art on classification tasks (especially tasks with more than 10K instances, where ROC-AUC increases 0.23% on average), and achieves the state-of-the-art for regression tasks by reducing RMSE by 2.0% on average, while remaining more robust to errors than other algorithms. We hypothesize that FAMOSE's strong performance is because ReAct allows the LLM context window to record (via iterative feature discovery and evaluation steps) what features did or did not work. This is similar to a few-shot prompt and guides the LLM to invent better, more innovative features. Our work offers evidence that AI agents are remarkably effective in solving problems that require highly inventive solutions, such as feature engineering.

