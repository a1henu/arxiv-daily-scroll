---
layout: default
title: SynPlanResearch-R1: Encouraging Tool Exploration for Deep Research with Synthetic Plans
---

# SynPlanResearch-R1: Encouraging Tool Exploration for Deep Research with Synthetic Plans
**arXiv**：[2603.07853v1](https://arxiv.org/abs/2603.07853) · [PDF](https://arxiv.org/pdf/2603.07853.pdf)  
**作者**：Hansi Zeng, Zoey Li, Yifan Gao, Chenwei Zhang, Xiaoman Pan, Tao Yang, Fengran Mo, Jiacheng Lin, Xian Li, Jingbo Shang  

**一句话要点**：提出SynPlanResearch-R1框架，通过合成轨迹增强研究代理的探索能力以提升多跳和开放网络查询性能。

**关键词**：研究代理, 工具探索, 合成轨迹, 监督微调, 强化学习, 多跳查询

## 3 点简述
- 研究代理在工具使用中常出现探索不足问题，如过早终止和工具使用偏差，限制强化学习改进。
- 框架合成工具使用轨迹，在监督微调阶段引导深度探索，为后续强化学习提供强初始化。
- 在七个基准测试中，相比SOTA基线，Qwen3-8B和Qwen3-4B模型性能提升最高达6.0%和5.8%。

## 摘要（原文）

> Research Agents enable models to gather information from the web using tools to answer user queries, requiring them to dynamically interleave internal reasoning with tool use. While such capabilities can in principle be learned via reinforcement learning with verifiable rewards (RLVR), we observe that agents often exhibit poor exploration behaviors, including premature termination and biased tool usage. As a result, RLVR alone yields limited improvements. We propose SynPlanResearch-R1, a framework that synthesizes tool-use trajectories that encourage deeper exploration to shape exploration during cold-start supervised fine-tuning, providing a strong initialization for subsequent RL. Across seven multi-hop and open-web benchmarks, \framework improves performance by up to 6.0% on Qwen3-8B and 5.8% on Qwen3-4B backbones respectively compared to SOTA baselines. Further analyses of tool-use patterns and training dynamics compared to baselines shed light on the factors underlying these gains. Our code is publicly available at https://github.com/HansiZeng/syn-plan-research.

