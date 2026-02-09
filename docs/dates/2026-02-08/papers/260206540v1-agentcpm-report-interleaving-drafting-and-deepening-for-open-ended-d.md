---
layout: default
title: AgentCPM-Report: Interleaving Drafting and Deepening for Open-Ended Deep Research
---

# AgentCPM-Report: Interleaving Drafting and Deepening for Open-Ended Deep Research
**arXiv**：[2602.06540v1](https://arxiv.org/abs/2602.06540) · [PDF](https://arxiv.org/pdf/2602.06540.pdf)  
**作者**：Yishan Li, Wentong Chen, Yukun Yan, Mingwei Li, Sen Mei, Xiaorong Wang, Kunpeng Liu, Xin Cong, Shuo Wang, Zhong Zhang, Yaxi Lu, Zhenghao Liu, Yankai Lin, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出AgentCPM-Report框架，通过动态修订大纲解决开放域深度研究报告生成问题。

**关键词**：深度研究报告生成, 动态大纲修订, 多阶段代理训练, 本地轻量解决方案, 推理驱动深化

## 3 点简述
- 核心问题：现有方法依赖初始大纲质量，导致系统需闭源大模型，引发部署与隐私问题。
- 方法要点：采用Writing As Reasoning Policy，交替证据起草与推理深化，支持迭代大纲演化。
- 实验或效果：在多个基准测试中超越闭源系统，尤其在Insight指标上表现显著提升。

## 摘要（原文）

> Generating deep research reports requires large-scale information acquisition and the synthesis of insight-driven analysis, posing a significant challenge for current language models. Most existing approaches follow a plan-then-write paradigm, whose performance heavily depends on the quality of the initial outline. However, constructing a comprehensive outline itself demands strong reasoning ability, causing current deep research systems to rely almost exclusively on closed-source or online large models. This reliance raises practical barriers to deployment and introduces safety and privacy concerns for user-authored data. In this work, we present AgentCPM-Report, a lightweight yet high-performing local solution composed of a framework that mirrors the human writing process and an 8B-parameter deep research agent. Our framework uses a Writing As Reasoning Policy (WARP), which enables models to dynamically revise outlines during report generation. Under this policy, the agent alternates between Evidence-Based Drafting and Reasoning-Driven Deepening, jointly supporting information acquisition, knowledge refinement, and iterative outline evolution. To effectively equip small models with this capability, we introduce a Multi-Stage Agentic Training strategy, consisting of cold-start, atomic skill RL, and holistic pipeline RL. Experiments on DeepResearch Bench, DeepConsult, and DeepResearch Gym demonstrate that AgentCPM-Report outperforms leading closed-source systems, with substantial gains in Insight.

