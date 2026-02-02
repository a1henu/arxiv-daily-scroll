---
layout: default
title: Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution
---

# Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution
**arXiv**：[2601.22528v1](https://arxiv.org/abs/2601.22528) · [PDF](https://arxiv.org/pdf/2601.22528.pdf)  
**作者**：Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan Li, Yanming Li, Xuelin Zhang, Haotian Luo, Songyang Peng, He Cui, Tengfei Tian, Jun Fang, Hua Chai, Naiqiang Tan  

**一句话要点**：提出达尔文记忆系统以解决GUI代理在长程跨应用任务中的记忆适应性问题

**关键词**：GUI代理, 记忆系统, 自进化架构, 多模态大语言模型, 任务自动化, 自然选择机制

## 3 点简述
- 核心问题：MLLM代理在GUI自动化中因上下文窗口限制和静态记忆积累导致幻觉与粒度不匹配
- 方法要点：设计自进化记忆生态系统，通过效用驱动自然选择分解轨迹并剪枝次优路径
- 实验或效果：在真实多应用基准测试中，无需训练提升成功率18.0%和稳定性33.9%，降低延迟

## 摘要（原文）

> Multimodal Large Language Model (MLLM) agents facilitate Graphical User Interface (GUI) automation but struggle with long-horizon, cross-application tasks due to limited context windows. While memory systems provide a viable solution, existing paradigms struggle to adapt to dynamic GUI environments, suffering from a granularity mismatch between high-level intent and low-level execution, and context pollution where the static accumulation of outdated experiences drives agents into hallucination. To address these bottlenecks, we propose the Darwinian Memory System (DMS), a self-evolving architecture that constructs memory as a dynamic ecosystem governed by the law of survival of the fittest. DMS decomposes complex trajectories into independent, reusable units for compositional flexibility, and implements Utility-driven Natural Selection to track survival value, actively pruning suboptimal paths and inhibiting high-risk plans. This evolutionary pressure compels the agent to derive superior strategies. Extensive experiments on real-world multi-app benchmarks validate that DMS boosts general-purpose MLLMs without training costs or architectural overhead, achieving average gains of 18.0% in success rate and 33.9% in execution stability, while reducing task latency, establishing it as an effective self-evolving memory system for GUI tasks.

