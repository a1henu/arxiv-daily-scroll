---
layout: default
title: Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents
---

# Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents
**arXiv**：[2601.03515v1](https://arxiv.org/abs/2601.03515) · [PDF](https://arxiv.org/pdf/2601.03515.pdf)  
**作者**：Yuanchen Bei, Tianxin Wei, Xuying Ning, Yanjun Zhao, Zhining Liu, Xiao Lin, Yada Zhu, Hendrik Hamann, Jingrui He, Hanghang Tong  

**一句话要点**：提出Mem-Gallery基准以评估多模态大语言模型代理在长期对话中的记忆能力

**关键词**：多模态长时记忆, 对话记忆基准, 记忆评估框架, 多模态大语言模型, 记忆推理, 知识管理

## 3 点简述
- 现有基准无法评估多模态记忆在长期对话中的保留、组织和演化
- Mem-Gallery包含高质量多会话对话，基于视觉和文本信息，具有长交互范围和丰富多模态依赖
- 评估框架从记忆提取与测试时适应、记忆推理和记忆知识管理三个维度评估关键记忆能力

## 摘要（原文）

> Long-term memory is a critical capability for multimodal large language model (MLLM) agents, particularly in conversational settings where information accumulates and evolves over time. However, existing benchmarks either evaluate multi-session memory in text-only conversations or assess multimodal understanding within localized contexts, failing to evaluate how multimodal memory is preserved, organized, and evolved across long-term conversational trajectories. Thus, we introduce Mem-Gallery, a new benchmark for evaluating multimodal long-term conversational memory in MLLM agents. Mem-Gallery features high-quality multi-session conversations grounded in both visual and textual information, with long interaction horizons and rich multimodal dependencies. Building on this dataset, we propose a systematic evaluation framework that assesses key memory capabilities along three functional dimensions: memory extraction and test-time adaptation, memory reasoning, and memory knowledge management. Extensive benchmarking across thirteen memory systems reveals several key findings, highlighting the necessity of explicit multimodal information retention and memory organization, the persistent limitations in memory reasoning and knowledge management, as well as the efficiency bottleneck of current models.

