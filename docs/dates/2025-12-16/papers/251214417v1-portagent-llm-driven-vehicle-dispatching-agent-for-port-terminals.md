---
layout: default
title: PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
---

# PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals
**arXiv**：[2512.14417v1](https://arxiv.org/abs/2512.14417) · [PDF](https://arxiv.org/pdf/2512.14417.pdf)  
**作者**：Jia Hu, Junqi Li, Weimeng Lin, Peng Jia, Yuxiong Ji, Jintao Lai  

**一句话要点**：提出PortAgent，一种基于大语言模型的车辆调度代理，以解决自动化集装箱码头中车辆调度系统跨码头可移植性低的问题。

**关键词**：车辆调度系统, 大语言模型, 自动化集装箱码头, 虚拟专家团队, 检索增强生成, 少样本学习

## 3 点简述
- 核心问题：车辆调度系统跨码头可移植性低，依赖专家、数据和手动部署。
- 方法要点：利用虚拟专家团队和检索增强生成，通过少样本学习自动化调度系统设计。
- 实验或效果：未知，但声称无需专家、低数据需求和快速部署。

## 摘要（原文）

> Vehicle Dispatching Systems (VDSs) are critical to the operational efficiency of Automated Container Terminals (ACTs). However, their widespread commercialization is hindered due to their low transferability across diverse terminals. This transferability challenge stems from three limitations: high reliance on port operational specialists, a high demand for terminal-specific data, and time-consuming manual deployment processes. Leveraging the emergence of Large Language Models (LLMs), this paper proposes PortAgent, an LLM-driven vehicle dispatching agent that fully automates the VDS transferring workflow. It bears three features: (1) no need for port operations specialists; (2) low need of data; and (3) fast deployment. Specifically, specialist dependency is eliminated by the Virtual Expert Team (VET). The VET collaborates with four virtual experts, including a Knowledge Retriever, Modeler, Coder, and Debugger, to emulate a human expert team for the VDS transferring workflow. These experts specialize in the domain of terminal VDS via a few-shot example learning approach. Through this approach, the experts are able to learn VDS-domain knowledge from a few VDS examples. These examples are retrieved via a Retrieval-Augmented Generation (RAG) mechanism, mitigating the high demand for terminal-specific data. Furthermore, an automatic VDS design workflow is established among these experts to avoid extra manual interventions. In this workflow, a self-correction loop inspired by the LLM Reflexion framework is created

