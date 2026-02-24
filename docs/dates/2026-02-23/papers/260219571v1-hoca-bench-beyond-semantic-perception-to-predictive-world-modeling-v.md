---
layout: default
title: HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies
---

# HOCA-Bench: Beyond Semantic Perception to Predictive World Modeling via Hegelian Ontological-Causal Anomalies
**arXiv**：[2602.19571v1](https://arxiv.org/abs/2602.19571) · [PDF](https://arxiv.org/pdf/2602.19571.pdf)  
**作者**：Chang Liu, Yunfan Ye, Qingyang Zhou, Xichen Tan, Mengxuan Luo, Zhenyu Qiu, Wei Peng, Zhiping Cai  

**一句话要点**：提出HOCA-Bench基准，通过黑格尔式本体-因果异常评估视频-LLMs的预测世界建模能力。

**关键词**：视频-LLMs, 预测世界建模, 异常检测, 基准测试, 物理推理

## 3 点简述
- 视频-LLMs在语义感知上进步，但预测世界建模能力不足，影响物理基础智能。
- 基于黑格尔哲学，将异常分为本体异常和因果异常，利用生成视频模型构建测试集。
- 评估17个模型显示，因果任务性能下降超20%，系统-2推理模式未弥补差距。

## 摘要（原文）

> Video-LLMs have improved steadily on semantic perception, but they still fall short on predictive world modeling, which is central to physically grounded intelligence. We introduce HOCA-Bench, a benchmark that frames physical anomalies through a Hegelian lens. HOCA-Bench separates anomalies into two types: ontological anomalies, where an entity violates its own definition or persistence, and causal anomalies, where interactions violate physical relations. Using state-of-the-art generative video models as adversarial simulators, we build a testbed of 1,439 videos (3,470 QA pairs). Evaluations on 17 Video-LLMs show a clear cognitive lag: models often identify static ontological violations (e.g., shape mutations) but struggle with causal mechanisms (e.g., gravity or friction), with performance dropping by more than 20% on causal tasks. System-2 "Thinking" modes improve reasoning, but they do not close the gap, suggesting that current architectures recognize visual patterns more readily than they apply basic physical laws.

