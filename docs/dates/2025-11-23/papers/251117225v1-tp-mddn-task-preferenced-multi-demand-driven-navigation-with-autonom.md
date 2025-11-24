---
layout: default
title: TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making
---

# TP-MDDN: Task-Preferenced Multi-Demand-Driven Navigation with Autonomous Decision-Making
**arXiv**：[2511.17225v1](https://arxiv.org/abs/2511.17225) · [PDF](https://arxiv.org/pdf/2511.17225.pdf)  
**作者**：Shanshan Li, Da Huang, Yu He, Yanwei Fu, Yu-Gang Jiang, Xiangyang Xue  

**一句话要点**：提出TP-MDDN基准和AWMSystem以解决多需求导航中的自主决策问题

**关键词**：多需求导航, 自主决策系统, 空间记忆映射, 长视野任务, 强化学习控制, 语义理解

## 3 点简述
- 核心问题：传统需求驱动导航无法处理多需求和任务偏好，限制了真实世界应用。
- 方法要点：AWMSystem集成BreakLLM、LocateLLM和StatusMLLM模块，结合MASMap空间记忆和双节奏动作生成。
- 实验或效果：在感知精度和导航鲁棒性上优于现有基线方法。

## 摘要（原文）

> In daily life, people often move through spaces to find objects that meet their needs, posing a key challenge in embodied AI. Traditional Demand-Driven Navigation (DDN) handles one need at a time but does not reflect the complexity of real-world tasks involving multiple needs and personal choices. To bridge this gap, we introduce Task-Preferenced Multi-Demand-Driven Navigation (TP-MDDN), a new benchmark for long-horizon navigation involving multiple sub-demands with explicit task preferences. To solve TP-MDDN, we propose AWMSystem, an autonomous decision-making system composed of three key modules: BreakLLM (instruction decomposition), LocateLLM (goal selection), and StatusMLLM (task monitoring). For spatial memory, we design MASMap, which combines 3D point cloud accumulation with 2D semantic mapping for accurate and efficient environmental understanding. Our Dual-Tempo action generation framework integrates zero-shot planning with policy-based fine control, and is further supported by an Adaptive Error Corrector that handles failure cases in real time. Experiments demonstrate that our approach outperforms state-of-the-art baselines in both perception accuracy and navigation robustness.

