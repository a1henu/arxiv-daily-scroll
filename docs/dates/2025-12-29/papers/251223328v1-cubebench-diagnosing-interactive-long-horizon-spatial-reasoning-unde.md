---
layout: default
title: CubeBench: Diagnosing Interactive, Long-Horizon Spatial Reasoning Under Partial Observations
---

# CubeBench: Diagnosing Interactive, Long-Horizon Spatial Reasoning Under Partial Observations
**arXiv**：[2512.23328v1](https://arxiv.org/abs/2512.23328) · [PDF](https://arxiv.org/pdf/2512.23328.pdf)  
**作者**：Huan-ang Gao, Zikang Zhang, Tianwei Luo, Kaisen Yang, Xinzhe Juan, Jiahao Qiu, Tianxing Chen, Bingxiang He, Hao Zhao, Hao Zhou, Shilong Liu, Mengdi Wang  

**一句话要点**：提出CubeBench基准以诊断LLM在部分观测下的交互式长程空间推理能力

**关键词**：空间推理, 长程状态跟踪, 部分观测, 基准测试, 认知诊断, LLM代理

## 3 点简述
- 核心问题：LLM在物理世界部署中面临空间推理、长程状态跟踪和部分观测下主动探索的认知挑战
- 方法要点：引入基于魔方的CubeBench基准，采用三层诊断框架从全符号信息到部分视觉数据渐进评估
- 实验或效果：实验显示领先LLM在长程任务中通过率为0.00%，暴露长期规划的根本失败

## 摘要（原文）

> Large Language Model (LLM) agents, while proficient in the digital realm, face a significant gap in physical-world deployment due to the challenge of forming and maintaining a robust spatial mental model. We identify three core cognitive challenges hindering this transition: spatial reasoning, long-horizon state tracking via mental simulation, and active exploration under partial observation. To isolate and evaluate these faculties, we introduce CubeBench, a novel generative benchmark centered on the Rubik's Cube. CubeBench uses a three-tiered diagnostic framework that progressively assesses agent capabilities, from foundational state tracking with full symbolic information to active exploration with only partial visual data. Our experiments on leading LLMs reveal critical limitations, including a uniform 0.00% pass rate on all long-horizon tasks, exposing a fundamental failure in long-term planning. We also propose a diagnostic framework to isolate these cognitive bottlenecks by providing external solver tools. By analyzing the failure modes, we provide key insights to guide the development of more physically-grounded intelligent agents.

