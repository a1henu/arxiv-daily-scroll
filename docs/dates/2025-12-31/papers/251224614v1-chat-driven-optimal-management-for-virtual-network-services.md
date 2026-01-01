---
layout: default
title: Chat-Driven Optimal Management for Virtual Network Services
---

# Chat-Driven Optimal Management for Virtual Network Services
**arXiv**：[2512.24614v1](https://arxiv.org/abs/2512.24614) · [PDF](https://arxiv.org/pdf/2512.24614.pdf)  
**作者**：Yuya Miyaoka, Masaki Inoue, Kengo Urata, Shigeaki Harada  

**一句话要点**：提出聊天驱动的虚拟网络服务管理框架，结合自然语言处理与优化分配以实现可靠重配置。

**关键词**：虚拟网络管理, 自然语言处理, 意图提取, 整数线性规划, 优化分配, 聊天驱动框架

## 3 点简述
- 核心问题：传统意图网络依赖统计语言模型，无法保证配置可行性。
- 方法要点：两阶段框架包括NLP意图提取器和整数线性规划优化器，支持迭代更新。
- 实验或效果：LLM提取器精度高，Sentence-BERT+SVM延迟低，框架在单/多用户设置中保持可行性。

## 摘要（原文）

> This paper proposes a chat-driven network management framework that integrates natural language processing (NLP) with optimization-based virtual network allocation, enabling intuitive and reliable reconfiguration of virtual network services. Conventional intent-based networking (IBN) methods depend on statistical language models to interpret user intent but cannot guarantee the feasibility of generated configurations. To overcome this, we develop a two-stage framework consisting of an Interpreter, which extracts intent from natural language prompts using NLP, and an Optimizer, which computes feasible virtual machine (VM) placement and routing via an integer linear programming. In particular, the Interpreter translates user chats into update directions, i.e., whether to increase, decrease, or maintain parameters such as CPU demand and latency bounds, thereby enabling iterative refinement of the network configuration. In this paper, two intent extractors, which are a Sentence-BERT model with support vector machine (SVM) classifiers and a large language model (LLM), are introduced. Experiments in single-user and multi-user settings show that the framework dynamically updates VM placement and routing while preserving feasibility. The LLM-based extractor achieves higher accuracy with fewer labeled samples, whereas the Sentence-BERT with SVM classifiers provides significantly lower latency suitable for real-time operation. These results underscore the effectiveness of combining NLP-driven intent extraction with optimization-based allocation for safe, interpretable, and user-friendly virtual network management.

