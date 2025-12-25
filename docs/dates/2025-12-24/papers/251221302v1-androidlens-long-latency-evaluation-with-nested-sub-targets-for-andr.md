---
layout: default
title: AndroidLens: Long-latency Evaluation with Nested Sub-targets for Android GUI Agents
---

# AndroidLens: Long-latency Evaluation with Nested Sub-targets for Android GUI Agents
**arXiv**：[2512.21302v1](https://arxiv.org/abs/2512.21302) · [PDF](https://arxiv.org/pdf/2512.21302.pdf)  
**作者**：Yue Cao, Yingyao Wang, Pi Bu, Jingxuan Xing, Wei Jiang, Zekun Zhu, Junpeng Ma, Sashuai Zhou, Tong Lu, Jun Song, Yu Cheng, Yuning Jiang, Bo Zheng  

**一句话要点**：提出AndroidLens评估框架以解决移动GUI代理在长延迟任务中的评测挑战

**关键词**：移动GUI代理, 长延迟任务评估, 静态动态评测, 多领域任务, 里程碑进度测量, 真实场景异常

## 3 点简述
- 现有移动GUI代理评测基准应用有限、任务简单、指标粗糙，难以反映真实场景复杂性
- AndroidLens包含571个长延迟任务，覆盖38个领域，支持静态和动态评估以减少偏差并精细测量进度
- 实验显示最佳模型任务成功率仅12.7%，平均任务进度50.47%，突显环境异常、自适应探索和长期记忆等挑战

## 摘要（原文）

> Graphical user interface (GUI) agents can substantially improve productivity by automating frequently executed long-latency tasks on mobile devices. However, existing evaluation benchmarks are still constrained to limited applications, simple tasks, and coarse-grained metrics. To address this, we introduce AndroidLens, a challenging evaluation framework for mobile GUI agents, comprising 571 long-latency tasks in both Chinese and English environments, each requiring an average of more than 26 steps to complete. The framework features: (1) tasks derived from real-world user scenarios across 38 domains, covering complex types such as multi-constraint, multi-goal, and domain-specific tasks; (2) static evaluation that preserves real-world anomalies and allows multiple valid paths to reduce bias; and (3) dynamic evaluation that employs a milestone-based scheme for fine-grained progress measurement via Average Task Progress (ATP). Our evaluation indicates that even the best models reach only a 12.7% task success rate and 50.47% ATP. We also underscore key challenges in real-world environments, including environmental anomalies, adaptive exploration, and long-term memory retention.

