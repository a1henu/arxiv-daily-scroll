---
layout: default
title: Emerging from Ground: Addressing Intent Deviation in Tool-Using Agents via Deriving Real Calls into Virtual Trajectories
---

# Emerging from Ground: Addressing Intent Deviation in Tool-Using Agents via Deriving Real Calls into Virtual Trajectories
**arXiv**：[2601.15120v1](https://arxiv.org/abs/2601.15120) · [PDF](https://arxiv.org/pdf/2601.15120.pdf)  
**作者**：Qian Xiong, Yuekai Huang, Yujia Zheng, Tianhao Li, Ziyou Jiang, Zhiyuan Chang, Zhaoyang Li, Huanxiang Feng, Mingyang Li  

**一句话要点**：提出RISE方法，通过真实调用生成虚拟轨迹以解决工具使用代理中的意图偏离问题

**关键词**：工具使用代理, 意图对齐, 虚拟轨迹合成, 负样本生成, 后训练方法

## 3 点简述
- 核心问题：LLM工具使用代理存在意图偏离，影响可靠评估与性能提升
- 方法要点：基于已验证工具原语合成虚拟轨迹，通过参数突变生成多样负样本
- 实验或效果：在八项指标上表现优异，任务完成和意图对齐分别平均提升35.28%和23.27%

## 摘要（原文）

> LLMs have advanced tool-using agents for real-world applications, yet they often lead to unexpected behaviors or results. Beyond obvious failures, the subtle issue of "intent deviation" severely hinders reliable evaluation and performance improvement. Existing post-training methods generally leverage either real system samples or virtual data simulated by LLMs. However, the former is costly due to reliance on hand-crafted user requests, while the latter suffers from distribution shift from the real tools in the wild. Additionally, both methods lack negative samples tailored to intent deviation scenarios, hindering effective guidance on preference learning. We introduce RISE, a "Real-to-Virtual" method designed to mitigate intent deviation. Anchoring on verified tool primitives, RISE synthesizes virtual trajectories and generates diverse negative samples through mutation on critical parameters. With synthetic data, RISE fine-tunes backbone LLMs via the two-stage training for intent alignment. Evaluation results demonstrate that data synthesized by RISE achieve promising results in eight metrics covering user requires, execution trajectories and agent responses. Integrating with training, RISE achieves an average 35.28% improvement in Acctask (task completion) and 23.27% in Accintent (intent alignment), outperforming SOTA baselines by 1.20--42.09% and 1.17--54.93% respectively.

