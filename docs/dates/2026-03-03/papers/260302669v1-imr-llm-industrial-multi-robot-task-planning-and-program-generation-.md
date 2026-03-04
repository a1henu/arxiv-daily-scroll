---
layout: default
title: IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models
---

# IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models
**arXiv**：[2603.02669v1](https://arxiv.org/abs/2603.02669) · [PDF](https://arxiv.org/pdf/2603.02669.pdf)  
**作者**：Xiangyu Su, Juzhan Xu, Oliver van Kaick, Kai Xu, Ruizhen Hu  

**一句话要点**：提出IMR-LLM框架，利用大语言模型解决工业多机器人任务规划与程序生成问题。

**关键词**：工业多机器人, 任务规划, 程序生成, 大语言模型, 析取图, 过程树

## 3 点简述
- 工业多机器人任务存在严格顺序约束和复杂依赖，对大语言模型提出新挑战。
- 结合大语言模型构建析取图，通过确定性求解和过程树指导生成高低层程序。
- 创建IMR-Bench基准，实验显示方法在多项指标上显著优于现有方法。

## 摘要（原文）

> In modern industrial production, multiple robots often collaborate to complete complex manufacturing tasks. Large language models (LLMs), with their strong reasoning capabilities, have shown potential in coordinating robots for simple household and manipulation tasks. However, in industrial scenarios, stricter sequential constraints and more complex dependencies within tasks present new challenges for LLMs. To address this, we propose IMR-LLM, a novel LLM-driven Industrial Multi-Robot task planning and program generation framework. Specifically, we utilize LLMs to assist in constructing disjunctive graphs and employ deterministic solving methods to obtain a feasible and efficient high-level task plan. Based on this, we use a process tree to guide LLMs to generate executable low-level programs. Additionally, we create IMR-Bench, a challenging benchmark that encompasses multi-robot industrial tasks across three levels of complexity. Experimental results indicate that our method significantly surpasses existing methods across all evaluation metrics.

