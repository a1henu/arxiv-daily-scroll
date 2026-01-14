---
layout: default
title: Project Synapse: A Hierarchical Multi-Agent Framework with Hybrid Memory for Autonomous Resolution of Last-Mile Delivery Disruptions
---

# Project Synapse: A Hierarchical Multi-Agent Framework with Hybrid Memory for Autonomous Resolution of Last-Mile Delivery Disruptions
**arXiv**：[2601.08156v1](https://arxiv.org/abs/2601.08156) · [PDF](https://arxiv.org/pdf/2601.08156.pdf)  
**作者**：Arin Gopalan Yadav, Varad Dherange, Kumar Shivam  

**一句话要点**：提出Synapse分层多智能体框架，用于自主解决最后一公里配送中断问题。

**关键词**：多智能体系统, 配送中断解决, 分层架构, LangGraph, LLM评估, 混合内存

## 3 点简述
- 核心问题：最后一公里配送中断的自主解决，缺乏高效框架。
- 方法要点：采用分层多智能体架构，结合混合内存和LangGraph编排工作流。
- 实验或效果：基于真实用户评论构建基准数据集，使用LLM-as-a-Judge协议评估性能。

## 摘要（原文）

> This paper introduces Project Synapse, a novel agentic framework designed for the autonomous resolution of last-mile delivery disruptions. Synapse employs a hierarchical multi-agent architecture in which a central Resolution Supervisor agent performs strategic task decomposition and delegates subtasks to specialized worker agents responsible for tactical execution. The system is orchestrated using LangGraph to manage complex and cyclical workflows. To validate the framework, a benchmark dataset of 30 complex disruption scenarios was curated from a qualitative analysis of over 6,000 real-world user reviews. System performance is evaluated using an LLM-as-a-Judge protocol with explicit bias mitigation.

