---
layout: default
title: Routing with Generated Data: Annotation-Free LLM Skill Estimation and Expert Selection
---

# Routing with Generated Data: Annotation-Free LLM Skill Estimation and Expert Selection
**arXiv**：[2601.09692v1](https://arxiv.org/abs/2601.09692) · [PDF](https://arxiv.org/pdf/2601.09692.pdf)  
**作者**：Tianyi Niu, Justin Chih-Yao Chen, Genta Indra Winata, Shi-Xiong Zhang, Supriyo Chakraborty, Sambit Sahu, Yue Zhang, Elias Stengel-Eskin, Mohit Bansal  

**一句话要点**：提出RGD框架和CASCAL路由器，以生成数据解决无标注LLM路由问题

**关键词**：LLM路由, 生成数据训练, 无标注学习, 模型选择, 共识投票, 分层聚类

## 3 点简述
- 核心问题：LLM路由缺乏真实标注数据，尤其在用户请求分布未知时
- 方法要点：RGD框架用生成器LLM从任务描述生成查询和答案训练路由器
- 实验或效果：CASCAL路由器在弱生成器数据上优于最佳查询-答案路由器4.6%准确率

## 摘要（原文）

> Large Language Model (LLM) routers dynamically select optimal models for given inputs. Existing approaches typically assume access to ground-truth labeled data, which is often unavailable in practice, especially when user request distributions are heterogeneous and unknown. We introduce Routing with Generated Data (RGD), a challenging setting in which routers are trained exclusively on generated queries and answers produced from high-level task descriptions by generator LLMs. We evaluate query-answer routers (using both queries and labels) and query-only routers across four diverse benchmarks and 12 models, finding that query-answer routers degrade faster than query-only routers as generator quality decreases. Our analysis reveals two crucial characteristics of effective generators: they must accurately respond to their own questions, and their questions must produce sufficient performance differentiation among the model pool. We then show how filtering for these characteristics can improve the quality of generated data. We further propose CASCAL, a novel query-only router that estimates model correctness through consensus voting and identifies model-specific skill niches via hierarchical clustering. CASCAL is substantially more robust to generator quality, outperforming the best query-answer router by 4.6% absolute accuracy when trained on weak generator data.

