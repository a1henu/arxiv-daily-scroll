---
layout: default
title: DRPG (Decompose, Retrieve, Plan, Generate): An Agentic Framework for Academic Rebuttal
---

# DRPG (Decompose, Retrieve, Plan, Generate): An Agentic Framework for Academic Rebuttal
**arXiv**：[2601.18081v1](https://arxiv.org/abs/2601.18081) · [PDF](https://arxiv.org/pdf/2601.18081.pdf)  
**作者**：Peixuan Han, Yingjie Yu, Jingjun Xu, Jiaxuan You  

**一句话要点**：提出DRPG框架以解决学术反驳生成中的长上下文理解和针对性响应问题

**关键词**：学术反驳生成, 代理框架, 长上下文理解, 规划策略, 自动生成, 多轮对话

## 3 点简述
- 核心问题：现有方法在学术反驳生成中难以处理长上下文且缺乏针对性
- 方法要点：通过分解、检索、规划和生成四步框架，提升反驳的准确性和说服力
- 实验或效果：在顶级会议数据上，DRPG超越现有方法，达到超平均人类水平

## 摘要（原文）

> Despite the growing adoption of large language models (LLMs) in scientific research workflows, automated support for academic rebuttal, a crucial step in academic communication and peer review, remains largely underexplored. Existing approaches typically rely on off-the-shelf LLMs or simple pipelines, which struggle with long-context understanding and often fail to produce targeted and persuasive responses. In this paper, we propose DRPG, an agentic framework for automatic academic rebuttal generation that operates through four steps: Decompose reviews into atomic concerns, Retrieve relevant evidence from the paper, Plan rebuttal strategies, and Generate responses accordingly. Notably, the Planner in DRPG reaches over 98% accuracy in identifying the most feasible rebuttal direction. Experiments on data from top-tier conferences demonstrate that DRPG significantly outperforms existing rebuttal pipelines and achieves performance beyond the average human level using only an 8B model. Our analysis further demonstrates the effectiveness of the planner design and its value in providing multi-perspective and explainable suggestions. We also showed that DRPG works well in a more complex multi-round setting. These results highlight the effectiveness of DRPG and its potential to provide high-quality rebuttal content and support the scaling of academic discussions. Codes for this work are available at https://github.com/ulab-uiuc/DRPG-RebuttalAgent.

