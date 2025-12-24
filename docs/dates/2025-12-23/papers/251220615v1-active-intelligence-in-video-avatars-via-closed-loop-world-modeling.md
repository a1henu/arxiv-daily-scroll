---
layout: default
title: Active Intelligence in Video Avatars via Closed-loop World Modeling
---

# Active Intelligence in Video Avatars via Closed-loop World Modeling
**arXiv**：[2512.20615v1](https://arxiv.org/abs/2512.20615) · [PDF](https://arxiv.org/pdf/2512.20615.pdf)  
**作者**：Xuanhua He, Tianyu Yang, Ke Cao, Ruiqi Wu, Cheng Meng, Yong Zhang, Zhuoliang Kang, Xiaoming Wei, Qifeng Chen  

**一句话要点**：提出ORCA框架以解决视频化身在随机生成环境中缺乏自主目标导向规划能力的问题。

**关键词**：视频化身生成, 主动智能, 内部世界建模, 目标导向规划, 随机生成环境, 闭环控制

## 3 点简述
- 核心问题：现有视频化身生成方法缺乏主动智能，无法通过自适应环境交互实现长期目标。
- 方法要点：引入L-IVA基准和ORCA框架，通过闭环OTAR循环和分层双系统架构实现内部世界建模。
- 实验或效果：ORCA在任务成功率和行为一致性上显著优于开环和非反思基线，验证了主动智能设计。

## 摘要（原文）

> Current video avatar generation methods excel at identity preservation and motion alignment but lack genuine agency, they cannot autonomously pursue long-term goals through adaptive environmental interaction. We address this by introducing L-IVA (Long-horizon Interactive Visual Avatar), a task and benchmark for evaluating goal-directed planning in stochastic generative environments, and ORCA (Online Reasoning and Cognitive Architecture), the first framework enabling active intelligence in video avatars. ORCA embodies Internal World Model (IWM) capabilities through two key innovations: (1) a closed-loop OTAR cycle (Observe-Think-Act-Reflect) that maintains robust state tracking under generative uncertainty by continuously verifying predicted outcomes against actual generations, and (2) a hierarchical dual-system architecture where System 2 performs strategic reasoning with state prediction while System 1 translates abstract plans into precise, model-specific action captions. By formulating avatar control as a POMDP and implementing continuous belief updating with outcome verification, ORCA enables autonomous multi-step task completion in open-domain scenarios. Extensive experiments demonstrate that ORCA significantly outperforms open-loop and non-reflective baselines in task success rate and behavioral coherence, validating our IWM-inspired design for advancing video avatar intelligence from passive animation to active, goal-oriented behavior.

