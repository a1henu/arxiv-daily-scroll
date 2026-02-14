---
layout: default
title: Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation
---

# Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation
**arXiv**：[2602.11790v1](https://arxiv.org/abs/2602.11790) · [PDF](https://arxiv.org/pdf/2602.11790.pdf)  
**作者**：Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  

**一句话要点**：提出LAVES多智能体系统，基于LLM生成高质量教育视频以解决逻辑严谨性不足问题。

**关键词**：教育视频生成, 多智能体系统, 大语言模型, 逻辑推理, 自动化生产, 成本优化

## 3 点简述
- 核心问题：现有端到端视频生成模型在需要严格逻辑和知识表示的教育场景中表现有限。
- 方法要点：采用分层多智能体系统，分解生成流程为专门代理，通过质量门和迭代批判机制确保正确性。
- 实验或效果：在大型部署中，日产量超百万视频，成本降低超95%，保持高接受率。

## 摘要（原文）

> Although recent end-to-end video generation models demonstrate impressive performance in visually oriented content creation, they remain limited in scenarios that require strict logical rigor and precise knowledge representation, such as instructional and educational media. To address this problem, we propose LAVES, a hierarchical LLM-based multi-agent system for generating high-quality instructional videos from educational problems. The LAVES formulates educational video generation as a multi-objective task that simultaneously demands correct step-by-step reasoning, pedagogically coherent narration, semantically faithful visual demonstrations, and precise audio--visual alignment. To address the limitations of prior approaches--including low procedural fidelity, high production cost, and limited controllability--LAVES decomposes the generation workflow into specialized agents coordinated by a central Orchestrating Agent with explicit quality gates and iterative critique mechanisms. Specifically, the Orchestrating Agent supervises a Solution Agent for rigorous problem solving, an Illustration Agent that produces executable visualization codes, and a Narration Agent for learner-oriented instructional scripts. In addition, all outputs from the working agents are subject to semantic critique, rule-based constraints, and tool-based compilation checks. Rather than directly synthesizing pixels, the system constructs a structured executable video script that is deterministically compiled into synchronized visuals and narration using template-driven assembly rules, enabling fully automated end-to-end production without manual editing. In large-scale deployments, LAVES achieves a throughput exceeding one million videos per day, delivering over a 95% reduction in cost compared to current industry-standard approaches while maintaining a high acceptance rate.

