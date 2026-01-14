---
layout: default
title: The Agent's First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios
---

# The Agent's First Day: Benchmarking Learning, Exploration, and Scheduling in the Workplace Scenarios
**arXiv**：[2601.08173v1](https://arxiv.org/abs/2601.08173) · [PDF](https://arxiv.org/pdf/2601.08173.pdf)  
**作者**：Daocheng Fu, Jianbiao Mei, Rong Wu, Xuemeng Yang, Jia Xu, Ding Wang, Pinlong Cai, Yong Liu, Licheng Wen, Botian Shi  

**一句话要点**：提出动态评估环境EvoEnv以解决多模态大语言模型在工作场景中动态任务调度、主动探索和持续学习的挑战

**关键词**：多模态大语言模型, 动态评估环境, 任务调度, 主动探索, 持续学习, 工作场景模拟

## 3 点简述
- 核心问题：现有研究关注静态环境性能上限，忽视随机现实部署的鲁棒性，需应对动态任务调度、不确定性下主动探索和经验持续学习
- 方法要点：引入EvoEnv环境，模拟新手代理探索新设置，评估上下文感知调度、主动信息获取和策略持续演化
- 实验或效果：实验显示前沿代理在动态环境中存在显著缺陷，尤其在主动探索和持续学习方面，为评估代理可靠性提供框架

## 摘要（原文）

> The rapid evolution of Multi-modal Large Language Models (MLLMs) has advanced workflow automation; however, existing research mainly targets performance upper bounds in static environments, overlooking robustness for stochastic real-world deployment. We identify three key challenges: dynamic task scheduling, active exploration under uncertainty, and continuous learning from experience. To bridge this gap, we introduce \method{}, a dynamic evaluation environment that simulates a "trainee" agent continuously exploring a novel setting. Unlike traditional benchmarks, \method{} evaluates agents along three dimensions: (1) context-aware scheduling for streaming tasks with varying priorities; (2) prudent information acquisition to reduce hallucination via active exploration; and (3) continuous evolution by distilling generalized strategies from rule-based, dynamically generated tasks. Experiments show that cutting-edge agents have significant deficiencies in dynamic environments, especially in active exploration and continual learning. Our work establishes a framework for assessing agent reliability, shifting evaluation from static tests to realistic, production-oriented scenarios. Our codes are available at https://github.com/KnowledgeXLab/EvoEnv

