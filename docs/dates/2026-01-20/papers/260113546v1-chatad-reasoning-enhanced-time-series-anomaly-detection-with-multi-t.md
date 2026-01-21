---
layout: default
title: ChatAD: Reasoning-Enhanced Time-Series Anomaly Detection with Multi-Turn Instruction Evolution
---

# ChatAD: Reasoning-Enhanced Time-Series Anomaly Detection with Multi-Turn Instruction Evolution
**arXiv**：[2601.13546v1](https://arxiv.org/abs/2601.13546) · [PDF](https://arxiv.org/pdf/2601.13546.pdf)  
**作者**：Hui Sun, Chang Xu, Haonan Xie, Hao Li, Yuhao Huang, Chuheng Zhang, Ming Jin, Xiaoguang Liu, Gang Wang, Jiang Bian  

**一句话要点**：提出ChatAD框架，通过多轮指令演进增强时间序列异常检测的推理与泛化能力

**关键词**：时间序列异常检测, 大语言模型推理, 多轮指令演进, 跨任务泛化, 多代理算法, 基准评估

## 3 点简述
- 针对现有LLM驱动异常检测方法推理能力不足、多轮对话能力欠缺和泛化性窄的问题
- 提出TSEvol算法、TSEData-20K数据集、TKTO优化方法和LLADBench基准，构建ChatAD模型家族
- 实验显示ChatAD模型在准确率、F1分数和误报率上显著提升，并通过TKTO优化实现跨任务泛化

## 摘要（原文）

> LLM-driven Anomaly Detection (AD) helps enhance the understanding and explanatory abilities of anomalous behaviors in Time Series (TS). Existing methods face challenges of inadequate reasoning ability, deficient multi-turn dialogue capability, and narrow generalization. To this end, we 1) propose a multi-agent-based TS Evolution algorithm named TSEvol. On top of it, we 2) introduce the AD reasoning and multi-turn dialogue Dataset TSEData-20K and contribute the Chatbot family for AD, including ChatAD-Llama3-8B, Qwen2.5-7B, and Mistral-7B. Furthermore, 3) we propose the TS Kahneman-Tversky Optimization (TKTO) to enhance ChatAD's cross-task generalization capability. Lastly, 4) we propose a LLM-driven Learning-based AD Benchmark LLADBench to evaluate the performance of ChatAD and nine baselines across seven datasets and tasks. Our three ChatAD models achieve substantial gains, up to 34.50% in accuracy, 34.71% in F1, and a 37.42% reduction in false positives. Besides, via KTKO, our optimized ChatAD achieves competitive performance in reasoning and cross-task generalization on classification, forecasting, and imputation.

