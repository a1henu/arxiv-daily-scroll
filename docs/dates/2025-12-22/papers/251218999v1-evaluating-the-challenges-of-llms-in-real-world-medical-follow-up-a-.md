---
layout: default
title: Evaluating the Challenges of LLMs in Real-world Medical Follow-up: A Comparative Study and An Optimized Framework
---

# Evaluating the Challenges of LLMs in Real-world Medical Follow-up: A Comparative Study and An Optimized Framework
**arXiv**：[2512.18999v1](https://arxiv.org/abs/2512.18999) · [PDF](https://arxiv.org/pdf/2512.18999.pdf)  
**作者**：Jinyan Liu, Zikang Chen, Qinchuan Wang, Tan Xie, Heming Zheng, Xudong Lv  

**一句话要点**：提出模块化流程控制框架以解决LLM在医疗随访中的对话不稳定和信息提取不准确问题

**关键词**：医疗随访, 大型语言模型, 模块化管道, 任务分解, 语义聚类, 流程控制

## 3 点简述
- 核心问题：LLM端到端应用于医疗随访时，因随访表单复杂导致对话流失控和信息提取不准确
- 方法要点：设计模块化管道，基于任务分解、语义聚类和流程控制来优化系统
- 实验或效果：模块化方法显著提升对话稳定性和提取精度，减少对话轮次46.73%，降低token消耗80%-87.5%

## 摘要（原文）

> When applied directly in an end-to-end manner to medical follow-up tasks, Large Language Models (LLMs) often suffer from uncontrolled dialog flow and inaccurate information extraction due to the complexity of follow-up forms. To address this limitation, we designed and compared two follow-up chatbot systems: an end-to-end LLM-based system (control group) and a modular pipeline with structured process control (experimental group). Experimental results show that while the end-to-end approach frequently fails on lengthy and complex forms, our modular method-built on task decomposition, semantic clustering, and flow management-substantially improves dialog stability and extraction accuracy. Moreover, it reduces the number of dialogue turns by 46.73% and lowers token consumption by 80% to 87.5%. These findings highlight the necessity of integrating external control mechanisms when deploying LLMs in high-stakes medical follow-up scenarios.

