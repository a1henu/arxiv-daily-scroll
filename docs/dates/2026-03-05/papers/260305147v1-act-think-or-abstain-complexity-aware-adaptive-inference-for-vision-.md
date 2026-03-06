---
layout: default
title: Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models
---

# Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models
**arXiv**：[2603.05147v1](https://arxiv.org/abs/2603.05147) · [PDF](https://arxiv.org/pdf/2603.05147.pdf)  
**作者**：Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci  

**一句话要点**：提出自适应推理框架以解决视觉-语言-动作模型的计算效率与不确定性估计问题

**关键词**：视觉-语言-动作模型, 自适应推理, 计算复杂度, 不确定性估计, 任务复杂度检测, 机器人控制

## 3 点简述
- 当前VLA模型普遍采用推理技术提升泛化，但增加计算复杂度和延迟，且缺乏不确定性估计
- 提出基于状态复杂度的动态路由框架，通过嵌入投影实现Act、Think、Abstain三种执行模式
- 在LIBERO等基准测试中，仅视觉配置以5%训练数据达到80% F1-Score，验证高效性

## 摘要（原文）

> Current research on Vision-Language-Action (VLA) models predominantly focuses on enhancing generalization through established reasoning techniques. While effective, these improvements invariably increase computational complexity and inference latency. Furthermore, these mechanisms are typically applied indiscriminately, resulting in the inefficient allocation of resources for trivial tasks while simultaneously failing to provide the uncertainty estimation necessary to prevent catastrophic failure on out-of-distribution tasks. Inspired by human cognition, we propose an adaptive framework that dynamically routes VLA execution based on the complexity of the perceived state. Our approach transforms the VLA's vision-language backbone into an active detection tool by projecting latent embeddings into an ensemble of parametric and non-parametric estimators. This allows the system to execute known tasks immediately (Act), reason about ambiguous scenarios (Think), and preemptively halt execution when encountering significant physical or semantic anomalies (Abstain). In our empirical analysis, we observe a phenomenon where visual embeddings alone are superior for inferring task complexity due to the semantic invariance of language. Evaluated on the LIBERO and LIBERO-PRO benchmarks as well as on a real robot, our vision-only configuration achieves 80% F1-Score using as little as 5% of training data, establishing itself as a reliable and efficient task complexity detector.

