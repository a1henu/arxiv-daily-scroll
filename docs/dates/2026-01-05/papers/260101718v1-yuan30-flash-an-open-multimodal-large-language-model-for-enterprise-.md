---
layout: default
title: Yuan3.0 Flash: An Open Multimodal Large Language Model for Enterprise Applications
---

# Yuan3.0 Flash: An Open Multimodal Large Language Model for Enterprise Applications
**arXiv**：[2601.01718v1](https://arxiv.org/abs/2601.01718) · [PDF](https://arxiv.org/pdf/2601.01718.pdf)  
**作者**：YuanLab. ai, :, Shawn Wu, Sean Wang, Louie Li, Darcy Chen, Allen Wang, Jiangang Luo, Xudong Zhao, Joseph Shen, Gawain Ma, Jasper Jia, Marcus Mao, Claire Wang, Hunter He, Carol Wang, Zera Zhang, Jason Wang, Chonly Shen, Leo Zhang, Logan Chen, Qasim Meng, James Gong, Danied Zhao, Penn Zheng, Owen Zhu, Tong Yu  

**一句话要点**：提出Yuan3.0 Flash开源多模态大语言模型，采用MoE架构和RAPO算法优化企业任务性能。

**关键词**：多模态大语言模型, 混合专家架构, 企业应用优化, 检索增强生成, 自适应策略优化

## 3 点简述
- 针对大型推理模型中的过度思考现象，提出Reflection-aware Adaptive Policy Optimization算法进行调控。
- 模型基于MoE设计，激活参数3.7B，总参数40B，专注于企业任务如检索增强生成和表格理解。
- 在数学和科学等领域展示强推理能力，性能接近前沿模型，但平均token使用量减少约1/4至1/2。

## 摘要（原文）

> We introduce Yuan3.0 Flash, an open-source Mixture-of-Experts (MoE) MultiModal Large Language Model featuring 3.7B activated parameters and 40B total parameters, specifically designed to enhance performance on enterprise-oriented tasks while maintaining competitive capabilities on general-purpose tasks. To address the overthinking phenomenon commonly observed in Large Reasoning Models (LRMs), we propose Reflection-aware Adaptive Policy Optimization (RAPO), a novel RL training algorithm that effectively regulates overthinking behaviors. In enterprise-oriented tasks such as retrieval-augmented generation (RAG), complex table understanding, and summarization, Yuan3.0 Flash consistently achieves superior performance. Moreover, it also demonstrates strong reasoning capabilities in domains such as mathematics, science, etc., attaining accuracy comparable to frontier model while requiring only approximately 1/4 to 1/2 of the average tokens. Yuan3.0 Flash has been fully open-sourced to facilitate further research and real-world deployment: https://github.com/Yuan-lab-LLM/Yuan3.0.

