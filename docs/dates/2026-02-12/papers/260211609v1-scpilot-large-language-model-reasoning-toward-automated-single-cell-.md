---
layout: default
title: scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery
---

# scPilot: Large Language Model Reasoning Toward Automated Single-Cell Analysis and Discovery
**arXiv**：[2602.11609v1](https://arxiv.org/abs/2602.11609) · [PDF](https://arxiv.org/pdf/2602.11609.pdf)  
**作者**：Yiming Gao, Zhen Wang, Jefferson Chen, Mark Antkowiak, Mengzhou Hu, JungHo Kong, Dexter Pratt, Jieyuan Liu, Enze Ma, Zhiting Hu, Eric P. Xing  

**一句话要点**：提出scPilot框架，通过大语言模型在单细胞RNA-seq数据上的原生推理实现自动化分析

**关键词**：单细胞RNA测序分析, 大语言模型推理, 生物信息学自动化, 可解释人工智能, 细胞类型注释, 发育轨迹重建

## 3 点简述
- 核心问题：单细胞分析依赖专家经验，缺乏自动化、可解释的推理流程
- 方法要点：将单细胞分析任务转化为LLM可逐步推理、验证和修正的步骤化问题
- 实验效果：在scBench基准上，迭代推理比单次提示提升细胞类型注释准确率11%，轨迹重建图编辑距离减少30%

## 摘要（原文）

> We present scPilot, the first systematic framework to practice omics-native reasoning: a large language model (LLM) converses in natural language while directly inspecting single-cell RNA-seq data and on-demand bioinformatics tools. scPilot converts core single-cell analyses, i.e., cell-type annotation, developmental-trajectory reconstruction, and transcription-factor targeting, into step-by-step reasoning problems that the model must solve, justify, and, when needed, revise with new evidence.
>   To measure progress, we release scBench, a suite of 9 expertly curated datasets and graders that faithfully evaluate the omics-native reasoning capability of scPilot w.r.t various LLMs. Experiments with o1 show that iterative omics-native reasoning lifts average accuracy by 11% for cell-type annotation and Gemini-2.5-Pro cuts trajectory graph-edit distance by 30% versus one-shot prompting, while generating transparent reasoning traces explain marker gene ambiguity and regulatory logic. By grounding LLMs in raw omics data, scPilot enables auditable, interpretable, and diagnostically informative single-cell analyses.
>   Code, data, and package are available at https://github.com/maitrix-org/scPilot

