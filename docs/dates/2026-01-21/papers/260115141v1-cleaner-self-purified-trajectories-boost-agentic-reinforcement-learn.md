---
layout: default
title: CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning
---

# CLEANER: Self-Purified Trajectories Boost Agentic Reinforcement Learning
**arXiv**：[2601.15141v1](https://arxiv.org/abs/2601.15141) · [PDF](https://arxiv.org/pdf/2601.15141.pdf)  
**作者**：Tianshi Xu, Yuteng Chen, Meng Li  

**一句话要点**：提出CLEANER方法，通过自净化轨迹解决参数受限模型的智能体强化学习噪声问题。

**关键词**：智能体强化学习, 轨迹净化, 自校正机制, 参数受限模型, 信用分配问题, 相似性感知回滚

## 3 点简述
- 核心问题：参数受限模型在探索阶段因执行失败产生噪声轨迹，导致信用分配问题，阻碍策略优化。
- 方法要点：利用模型内在自校正能力，通过相似性感知自适应回滚机制，在数据收集时替换失败为成功自校正，构建净化轨迹。
- 实验或效果：在AIME24/25、GPQA和LiveCodeBench基准上，平均准确率提升6%、3%和5%，训练步骤仅需三分之一达到最优性能。

## 摘要（原文）

> Agentic Reinforcement Learning (RL) has empowered Large Language Models (LLMs) to utilize tools like Python interpreters for complex problem-solving. However, for parameter-constrained models (e.g., 4B--7B), the exploration phase is often plagued by frequent execution failures, creating noisy trajectories that hinder policy optimization. Under standard outcome-based reward settings, this noise leads to a critical credit assignment issue, where erroneous actions are inadvertently reinforced alongside successful outcomes. Existing mitigations face a dilemma: dense rewards often trigger reward hacking, while supersampling incurs prohibitive computational costs. To address these challenges, we propose CLEANER. Distinct from external filtering methods, CLEANER exploits the model's intrinsic self-correction capabilities to eliminate error-contaminated context directly during data collection. At its core, the Similarity-Aware Adaptive Rollback (SAAR) mechanism autonomously constructs clean, purified trajectories by retrospectively replacing failures with successful self-corrections. Based on semantic similarity, SAAR adaptively regulates replacement granularity from shallow execution repairs to deep reasoning substitutions. By training on these self-purified paths, the model internalizes correct reasoning patterns rather than error-recovery loops. Empirical results on AIME24/25, GPQA, and LiveCodeBench show average accuracy gains of 6%, 3%, and 5% over baselines. Notably, CLEANER matches state-of-the-art performance using only one-third of the training steps, highlighting trajectory purification as a scalable solution for efficient agentic RL. Our models and code are available at GitHub

