---
layout: default
title: Reasoning with Autoregressive-Diffusion Collaborative Thoughts
---

# Reasoning with Autoregressive-Diffusion Collaborative Thoughts
**arXiv**：[2602.01608v1](https://arxiv.org/abs/2602.01608) · [PDF](https://arxiv.org/pdf/2602.01608.pdf)  
**作者**：Mu Yuan, Liekang Zeng, Guoliang Xing, Lan Zhang, Yunhao Liu  

**一句话要点**：提出Collaborative Thoughts框架，通过自回归与扩散模型协作解决空间推理与生成可控性问题

**关键词**：自回归模型, 扩散模型, 协作推理, 空间推理, 生成可控性, 多模态交互

## 3 点简述
- 核心问题：自回归模型缺乏空间基础，扩散模型缺乏逻辑控制，导致多模态任务中错误传播
- 方法要点：构建闭环协作框架，自回归模型规划约束，扩散模型生成视觉中间结果，视觉批评模块评估反馈
- 实验或效果：通过代表性示例展示，提升空间推理可靠性和生成可控性，统一处理问答与视觉生成任务

## 摘要（原文）

> Autoregressive and diffusion models represent two complementary generative paradigms. Autoregressive models excel at sequential planning and constraint composition, yet struggle with tasks that require explicit spatial or physical grounding. Diffusion models, in contrast, capture rich spatial structure through high-dimensional generation, but lack the stepwise logical control needed to satisfy complex, multi-stage constraints or to reliably identify and correct errors. We introduce Collaborative Thoughts, a unified collaborative framework that enables autoregressive and diffusion models to reason and generate jointly through a closed-loop interaction. In Collaborative Thoughts, autoregressive models perform structured planning and constraint management, diffusion models instantiate these constraints as intermediate visual thoughts, and a vision-based critic module evaluates whether the visual thoughts satisfy the intended structural and physical requirements. This feedback is then used to iteratively refine subsequent planning and generation steps, mitigating error propagation across modalities. Importantly, Collaborative Thoughts uses the same collaborative loop regardless of whether the task is autoregressive question answering or diffusion-based visual generation. Through representative examples, we illustrate how Collaborative Thoughts can improve the reliability of spatial reasoning and the controllability of generation.

