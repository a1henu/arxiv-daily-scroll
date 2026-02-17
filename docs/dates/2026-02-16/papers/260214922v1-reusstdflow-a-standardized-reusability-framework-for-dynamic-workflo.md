---
layout: default
title: ReusStdFlow: A Standardized Reusability Framework for Dynamic Workflow Construction in Agentic AI
---

# ReusStdFlow: A Standardized Reusability Framework for Dynamic Workflow Construction in Agentic AI
**arXiv**：[2602.14922v1](https://arxiv.org/abs/2602.14922) · [PDF](https://arxiv.org/pdf/2602.14922.pdf)  
**作者**：Gaoyang Zhang, Shanghong Zou, Yafang Wang, He Zhang, Ruohua Xu, Feng Zhao  

**一句话要点**：提出ReusStdFlow框架以解决企业Agentic AI中的可重用性困境和结构幻觉问题

**关键词**：工作流构建, 可重用性框架, 检索增强生成, 图数据库, 向量数据库, 企业Agentic AI

## 3 点简述
- 核心问题：企业Agentic AI存在可重用性困境和结构幻觉，阻碍异构DSL工作流的标准化与复用
- 方法要点：基于提取-存储-构建范式，将DSL解构为模块化工作流段，结合图与向量数据库实现协同检索
- 实验或效果：在200个真实n8n工作流上测试，提取和构建准确率均超过90%，支持企业数字资产自动化重组

## 摘要（原文）

> To address the ``reusability dilemma'' and structural hallucinations in enterprise Agentic AI,this paper proposes ReusStdFlow, a framework centered on a novel ``Extraction-Storage-Construction'' paradigm. The framework deconstructs heterogeneous, platform-specific Domain Specific Languages (DSLs) into standardized, modular workflow segments. It employs a dual knowledge architecture-integrating graph and vector databases-to facilitate synergistic retrieval of both topological structures and functional semantics. Finally, workflows are intelligently assembled using a retrieval-augmented generation (RAG) strategy. Tested on 200 real-world n8n workflows, the system achieves over 90% accuracy in both extraction and construction. This framework provides a standardized solution for the automated reorganization and efficient reuse of enterprise digital assets.

