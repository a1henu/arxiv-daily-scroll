---
layout: default
title: VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing
---

# VLM-DEWM: Dynamic External World Model for Verifiable and Resilient Vision-Language Planning in Manufacturing
**arXiv**：[2602.15549v1](https://arxiv.org/abs/2602.15549) · [PDF](https://arxiv.org/pdf/2602.15549.pdf)  
**作者**：Guoqin Tang, Qingxuan Jia, Gang Chen, Tong Li, Zeyuan Huang, Zihang Lv, Ning Ji  

**一句话要点**：提出VLM-DEWM架构，通过动态外部世界模型解决制造环境中视觉语言规划的状态漂移和诊断困难问题。

**关键词**：视觉语言模型, 动态外部世界模型, 制造环境规划, 状态跟踪, 故障恢复, 结构化记忆

## 3 点简述
- 核心问题：视觉语言模型在动态制造环境中存在状态漂移和推理不透明，导致失败难以诊断。
- 方法要点：引入动态外部世界模型，将推理与状态管理解耦，并通过外部化推理轨迹进行验证。
- 实验或效果：在组装、探索和恢复任务中，状态跟踪准确率从56%提升至93%，恢复成功率从低于5%提高至95%。

## 摘要（原文）

> Vision-language model (VLM) shows promise for high-level planning in smart manufacturing, yet their deployment in dynamic workcells faces two critical challenges: (1) stateless operation, they cannot persistently track out-of-view states, causing world-state drift; and (2) opaque reasoning, failures are difficult to diagnose, leading to costly blind retries. This paper presents VLM-DEWM, a cognitive architecture that decouples VLM reasoning from world-state management through a persistent, queryable Dynamic External World Model (DEWM). Each VLM decision is structured into an Externalizable Reasoning Trace (ERT), comprising action proposal, world belief, and causal assumption, which is validated against DEWM before execution. When failures occur, discrepancy analysis between predicted and observed states enables targeted recovery instead of global replanning. We evaluate VLM-DEWM on multi-station assembly, large-scale facility exploration, and real-robot recovery under induced failures. Compared to baseline memory-augmented VLM systems, VLM DEWM improves state-tracking accuracy from 56% to 93%, increases recovery success rate from below 5% to 95%, and significantly reduces computational overhead through structured memory. These results establish VLM-DEWM as a verifiable and resilient solution for long-horizon robotic operations in dynamic manufacturing environments.

