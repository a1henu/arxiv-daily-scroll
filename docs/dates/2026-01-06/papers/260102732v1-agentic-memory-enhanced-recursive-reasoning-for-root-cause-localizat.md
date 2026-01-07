---
layout: default
title: Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices
---

# Agentic Memory Enhanced Recursive Reasoning for Root Cause Localization in Microservices
**arXiv**：[2601.02732v1](https://arxiv.org/abs/2601.02732) · [PDF](https://arxiv.org/pdf/2601.02732.pdf)  
**作者**：Lingzhe Zhang, Tong Jia, Yunpeng Zhai, Leyi Pan, Chiming Duan, Minghua He, Mengxi Jia, Ying Li  

**一句话要点**：提出AMER-RCL框架，通过代理记忆增强递归推理以提升微服务根因定位的准确性和效率

**关键词**：微服务根因定位, 递归推理, 代理记忆, 多代理框架, LLM应用

## 3 点简述
- 核心问题：现有LLM方法在微服务根因定位中存在推理浅层和跨告警冗余问题，导致准确性低和延迟高
- 方法要点：基于专家分析特征，设计递归推理引擎和多代理框架，结合代理记忆实现推理的累积与重用
- 实验或效果：实验表明AMER-RCL在定位准确性和推理效率上优于现有先进方法

## 摘要（原文）

> As contemporary microservice systems become increasingly popular and complex-often comprising hundreds or even thousands of fine-grained, interdependent subsystems-they are experiencing more frequent failures. Ensuring system reliability thus demands accurate root cause localization. While many traditional graph-based and deep learning approaches have been explored for this task, they often rely heavily on pre-defined schemas that struggle to adapt to evolving operational contexts. Consequently, a number of LLM-based methods have recently been proposed. However, these methods still face two major limitations: shallow, symptom-centric reasoning that undermines accuracy, and a lack of cross-alert reuse that leads to redundant reasoning and high latency. In this paper, we conduct a comprehensive study of how Site Reliability Engineers (SREs) localize the root causes of failures, drawing insights from professionals across multiple organizations. Our investigation reveals that expert root cause analysis exhibits three key characteristics: recursiveness, multi-dimensional expansion, and cross-modal reasoning. Motivated by these findings, we introduce AMER-RCL, an agentic memory enhanced recursive reasoning framework for root cause localization in microservices. AMER-RCL employs the Recursive Reasoning RCL engine, a multi-agent framework that performs recursive reasoning on each alert to progressively refine candidate causes, while Agentic Memory incrementally accumulates and reuses reasoning from prior alerts within a time window to reduce redundant exploration and lower inference latency. Experimental results demonstrate that AMER-RCL consistently outperforms state-of-the-art methods in both localization accuracy and inference efficiency.

