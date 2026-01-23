---
layout: default
title: Grounding Large Language Models in Reaction Knowledge Graphs for Synthesis Retrieval
---

# Grounding Large Language Models in Reaction Knowledge Graphs for Synthesis Retrieval
**arXiv**：[2601.16038v1](https://arxiv.org/abs/2601.16038) · [PDF](https://arxiv.org/pdf/2601.16038.pdf)  
**作者**：Olga Bunkova, Lorenzo Di Fruscia, Sophia Rupprecht, Artur M. Schweidtmann, Marcel J. T. Reinders, Jana M. Weber  

**一句话要点**：提出基于反应知识图谱的Text2Cypher框架以提升LLM在化学合成检索中的准确性和可靠性

**关键词**：化学合成规划, 知识图谱, Text2Cypher, 大语言模型, 反应路径检索, 自校正循环

## 3 点简述
- 核心问题：标准提示方法导致LLM在化学合成规划中产生幻觉或过时建议
- 方法要点：将反应路径检索建模为Text2Cypher生成问题，并引入单步和多步检索任务
- 实验或效果：基于对齐示例的单样本提示表现最佳，自校正循环在零样本设置中主要提升可执行性

## 摘要（原文）

> Large Language Models (LLMs) can aid synthesis planning in chemistry, but standard prompting methods often yield hallucinated or outdated suggestions. We study LLM interactions with a reaction knowledge graph by casting reaction path retrieval as a Text2Cypher (natural language to graph query) generation problem, and define single- and multi-step retrieval tasks. We compare zero-shot prompting to one-shot variants using static, random, and embedding-based exemplar selection, and assess a checklist-driven validator/corrector loop. To evaluate our framework, we consider query validity and retrieval accuracy. We find that one-shot prompting with aligned exemplars consistently performs best. Our checklist-style self-correction loop mainly improves executability in zero-shot settings and offers limited additional retrieval gains once a good exemplar is present. We provide a reproducible Text2Cypher evaluation setup to facilitate further work on KG-grounded LLMs for synthesis planning. Code is available at https://github.com/Intelligent-molecular-systems/KG-LLM-Synthesis-Retrieval.

