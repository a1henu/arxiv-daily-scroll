---
layout: default
title: Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks
---

# Toward Expert Investment Teams:A Multi-Agent LLM System with Fine-Grained Trading Tasks
**arXiv**：[2602.23330v1](https://arxiv.org/abs/2602.23330) · [PDF](https://arxiv.org/pdf/2602.23330.pdf)  
**作者**：Kunihiro Miyazaki, Takanobu Kawahara, Stephen Roberts, Stefan Zohren  

**一句话要点**：提出细粒度任务分解的多智能体LLM交易框架以提升投资系统性能

**关键词**：多智能体系统, 细粒度任务分解, 金融交易, 大语言模型, 投资分析, 风险调整收益

## 3 点简述
- 主流多智能体系统依赖抽象指令，忽视实际工作流细节，导致推理性能下降和决策不透明
- 框架将投资分析分解为细粒度任务，而非粗粒度指令，在泄漏控制回测中使用日本股票数据评估
- 实验显示细粒度分解显著改善风险调整后收益，分析输出与决策偏好对齐是性能关键驱动因素

## 摘要（原文）

> The advancement of large language models (LLMs) has accelerated the development of autonomous financial trading systems. While mainstream approaches deploy multi-agent systems mimicking analyst and manager roles, they often rely on abstract instructions that overlook the intricacies of real-world workflows, which can lead to degraded inference performance and less transparent decision-making. Therefore, we propose a multi-agent LLM trading framework that explicitly decomposes investment analysis into fine-grained tasks, rather than providing coarse-grained instructions. We evaluate the proposed framework using Japanese stock data, including prices, financial statements, news, and macro information, under a leakage-controlled backtesting setting. Experimental results show that fine-grained task decomposition significantly improves risk-adjusted returns compared to conventional coarse-grained designs. Crucially, further analysis of intermediate agent outputs suggests that alignment between analytical outputs and downstream decision preferences is a critical driver of system performance. Moreover, we conduct standard portfolio optimization, exploiting low correlation with the stock index and the variance of each system's output. This approach achieves superior performance. These findings contribute to the design of agent structure and task configuration when applying LLM agents to trading systems in practical settings.

