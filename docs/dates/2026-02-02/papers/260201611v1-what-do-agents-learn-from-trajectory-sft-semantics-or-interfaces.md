---
layout: default
title: What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?
---

# What Do Agents Learn from Trajectory-SFT: Semantics or Interfaces?
**arXiv**：[2602.01611v1](https://arxiv.org/abs/2602.01611) · [PDF](https://arxiv.org/pdf/2602.01611.pdf)  
**作者**：Weizheng Gu, Chengze Li, Zhuohao Yu, Mengyuan Sun, Zhibang Yang, Wei Wang, Hongrui Jia, Shikun Zhang, Wei Ye  

**一句话要点**：提出PIPE协议评估方法以诊断大语言模型代理在轨迹监督微调中的界面依赖问题

**关键词**：大语言模型代理, 轨迹监督微调, 界面依赖评估, 语义工具使用, 基准测试混淆, 环境不变能力

## 3 点简述
- 核心问题：标准代理基准混淆语义工具使用与界面模式记忆，无法区分环境不变能力
- 方法要点：通过最小化重写环境界面，保持任务语义，评估代理对训练界面的依赖程度
- 实验或效果：轨迹监督微调显著增强界面捷径，代理在界面改写后性能急剧下降，非轨迹训练模型更稳定

## 摘要（原文）

> Large language models are increasingly evaluated as interactive agents, yet standard agent benchmarks conflate two qualitatively distinct sources of success: semantic tool-use and interface-specific interaction pattern memorization. Because both mechanisms can yield identical task success on the original interface, benchmark scores alone are not identifiable evidence of environment-invariant capability. We propose PIPE, a protocol-level evaluation augmentation for diagnosing interface reliance by minimally rewriting environment interfaces while preserving task semantics and execution behavior. Across 16 environments from AgentBench and AgentGym and a range of open-source and API-based agents, PIPE reveals that trajectory-SFT substantially amplifies interface shortcutting: trained agents degrade sharply under minimal interface rewrites, while non-trajectory-trained models remain largely stable. We further introduce Interface Reliance (IR), a counterbalanced alias-based metric that quantifies preference for training-time interfaces, and show that interface shortcutting exhibits environment-dependent, non-monotonic training dynamics that remain invisible under standard evaluation. Our code is available at https://anonymous.4open.science/r/What-Do-Agents-Learn-from-Trajectory-SFT-Semantics-or-Interfaces--0831/.

