---
layout: default
title: Human-AI Co-design for Clinical Prediction Models
---

# Human-AI Co-design for Clinical Prediction Models
**arXiv**：[2601.09072v1](https://arxiv.org/abs/2601.09072) · [PDF](https://arxiv.org/pdf/2601.09072.pdf)  
**作者**：Jean Feng, Avni Kothari, Patrick Vossler, Andrew Bishara, Lucas Zier, Newton Addo, Aaron Kornblith, Yan Shuo Tan, Chandan Singh  

**一句话要点**：提出HACHI框架以加速临床预测模型开发，通过人机协同探索临床笔记概念

**关键词**：临床预测模型, 人机协同设计, 非结构化数据, 可解释AI, 迭代框架

## 3 点简述
- 核心问题：传统临床预测模型开发耗时耗力，难以整合非结构化临床笔记中的大量概念。
- 方法要点：HACHI采用迭代人机循环框架，AI代理探索概念，专家提供反馈，使用线性模型实现可解释性。
- 实验或效果：在急性肾损伤和创伤性脑损伤任务中，HACHI优于现有方法，提升模型泛化能力并发现新临床概念。

## 摘要（原文）

> Developing safe, effective, and practically useful clinical prediction models (CPMs) traditionally requires iterative collaboration between clinical experts, data scientists, and informaticists. This process refines the often small but critical details of the model building process, such as which features/patients to include and how clinical categories should be defined. However, this traditional collaboration process is extremely time- and resource-intensive, resulting in only a small fraction of CPMs reaching clinical practice. This challenge intensifies when teams attempt to incorporate unstructured clinical notes, which can contain an enormous number of concepts. To address this challenge, we introduce HACHI, an iterative human-in-the-loop framework that uses AI agents to accelerate the development of fully interpretable CPMs by enabling the exploration of concepts in clinical notes. HACHI alternates between (i) an AI agent rapidly exploring and evaluating candidate concepts in clinical notes and (ii) clinical and domain experts providing feedback to improve the CPM learning process. HACHI defines concepts as simple yes-no questions that are used in linear models, allowing the clinical AI team to transparently review, refine, and validate the CPM learned in each round. In two real-world prediction tasks (acute kidney injury and traumatic brain injury), HACHI outperforms existing approaches, surfaces new clinically relevant concepts not included in commonly-used CPMs, and improves model generalizability across clinical sites and time periods. Furthermore, HACHI reveals the critical role of the clinical AI team, such as directing the AI agent to explore concepts that it had not previously considered, adjusting the granularity of concepts it considers, changing the objective function to better align with the clinical objectives, and identifying issues of data bias and leakage.

