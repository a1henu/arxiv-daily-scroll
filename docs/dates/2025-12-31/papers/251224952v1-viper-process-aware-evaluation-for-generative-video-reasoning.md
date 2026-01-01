---
layout: default
title: VIPER: Process-aware Evaluation for Generative Video Reasoning
---

# VIPER: Process-aware Evaluation for Generative Video Reasoning
**arXiv**：[2512.24952v1](https://arxiv.org/abs/2512.24952) · [PDF](https://arxiv.org/pdf/2512.24952.pdf)  
**作者**：Yifan Li, Yukai Gu, Yingqian Min, Zikang Liu, Yifan Du, Kun Zhou, Min Yang, Wayne Xin Zhao, Minghui Qiu  

**一句话要点**：提出VIPER基准和POC@r指标以解决生成视频推理中的过程评估问题

**关键词**：生成视频推理, 过程评估, 基准测试, 结果作弊, 视觉语言模型, 推理一致性

## 3 点简述
- 现有视频生成评估依赖单帧分析，易导致结果作弊，忽略推理过程有效性
- 引入VIPER基准覆盖16个任务，并提出POC@r指标使用VLM-as-Judge评估步骤和结果一致性
- 实验显示当前模型POC@1.0仅约20%，存在显著结果作弊，揭示与真实视觉推理的差距

## 摘要（原文）

> Recent breakthroughs in video generation have demonstrated an emerging capability termed Chain-of-Frames (CoF) reasoning, where models resolve complex tasks through the generation of continuous frames. While these models show promise for Generative Video Reasoning (GVR), existing evaluation frameworks often rely on single-frame assessments, which can lead to outcome-hacking, where a model reaches a correct conclusion through an erroneous process. To address this, we propose a process-aware evaluation paradigm. We introduce VIPER, a comprehensive benchmark spanning 16 tasks across temporal, structural, symbolic, spatial, physics, and planning reasoning. Furthermore, we propose Process-outcome Consistency (POC@r), a new metric that utilizes VLM-as-Judge with a hierarchical rubric to evaluate both the validity of the intermediate steps and the final result. Our experiments reveal that state-of-the-art video models achieve only about 20% POC@1.0 and exhibit a significant outcome-hacking. We further explore the impact of test-time scaling and sampling robustness, highlighting a substantial gap between current video generation and true generalized visual reasoning. Our benchmark will be publicly released.

