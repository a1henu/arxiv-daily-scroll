---
layout: default
title: How to Build AI Agents by Augmenting LLMs with Codified Human Expert Domain Knowledge? A Software Engineering Framework
---

# How to Build AI Agents by Augmenting LLMs with Codified Human Expert Domain Knowledge? A Software Engineering Framework
**arXiv**：[2601.15153v1](https://arxiv.org/abs/2601.15153) · [PDF](https://arxiv.org/pdf/2601.15153.pdf)  
**作者**：Choro Ulan uulu, Mikhail Kulyabin, Iris Fuhrmann, Jan Joosten, Nuno Miguel Martins Pacheco, Filippos Petridis, Rebecca Johnson, Jan Bosch, Helena Holmström Olsson  

**一句话要点**：提出软件工程框架以构建AI代理，通过增强LLM将专家领域知识编码化，解决仿真数据可视化中的非专家瓶颈问题。

**关键词**：AI代理构建, 专家知识编码化, LLM增强, 仿真数据可视化, 软件工程框架, RAG系统

## 3 点简述
- 核心问题：关键领域知识集中于少数专家，导致组织可扩展性和决策瓶颈，非专家难以生成有效可视化。
- 方法要点：设计框架，结合请求分类器、RAG系统、编码化专家规则和可视化设计原则，构建具备自主、反应、主动和社交行为的AI代理。
- 实验或效果：在五个工程场景中评估，输出质量提升206%，代理在所有案例中达到专家级评分，代码质量高且方差低。

## 摘要（原文）

> Critical domain knowledge typically resides with few experts, creating organizational bottlenecks in scalability and decision-making. Non-experts struggle to create effective visualizations, leading to suboptimal insights and diverting expert time. This paper investigates how to capture and embed human domain knowledge into AI agent systems through an industrial case study. We propose a software engineering framework to capture human domain knowledge for engineering AI agents in simulation data visualization by augmenting a Large Language Model (LLM) with a request classifier, Retrieval-Augmented Generation (RAG) system for code generation, codified expert rules, and visualization design principles unified in an agent demonstrating autonomous, reactive, proactive, and social behavior. Evaluation across five scenarios spanning multiple engineering domains with 12 evaluators demonstrates 206% improvement in output quality, with our agent achieving expert-level ratings in all cases versus baseline's poor performance, while maintaining superior code quality with lower variance. Our contributions are: an automated agent-based system for visualization generation and a validated framework for systematically capturing human domain knowledge and codifying tacit expert knowledge into AI agents, demonstrating that non-experts can achieve expert-level outcomes in specialized domains.

