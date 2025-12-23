---
layout: default
title: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
---

# Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement
**arXiv**：[2512.18950v1](https://arxiv.org/abs/2512.18950) · [PDF](https://arxiv.org/pdf/2512.18950.pdf)  
**作者**：Saman Forouzandeh, Wei Peng, Parham Moradi, Xinghuo Yu, Mahdi Jalili  

**一句话要点**：提出MACLA框架，通过外部分层程序记忆实现LLM代理的样本高效适应，无需更新模型参数。

**关键词**：LLM代理, 程序记忆, 贝叶斯选择, 对比学习, 样本效率, 外部记忆

## 3 点简述
- 核心问题：LLM代理适应新任务时依赖参数微调，效率低且缺乏可解释性。
- 方法要点：在冻结LLM外构建分层程序记忆，通过贝叶斯选择与对比精炼提取可靠过程。
- 实验效果：在四个基准测试中平均性能达78.1%，构建记忆速度比参数训练基线快2800倍。

## 摘要（原文）

> We present MACLA, a framework that decouples reasoning from learning by maintaining a frozen large language model while performing all adaptation in an external hierarchical procedural memory. MACLA extracts reusable procedures from trajectories, tracks reliability via Bayesian posteriors, selects actions through expected-utility scoring, and refines procedures by contrasting successes and failures. Across four benchmarks (ALFWorld, WebShop, TravelPlanner, InterCodeSQL), MACLA achieves 78.1 percent average performance, outperforming all baselines. On ALFWorld unseen tasks, MACLA reaches 90.3 percent with 3.1 percent positive generalization. The system constructs memory in 56 seconds, 2800 times faster than the state-of-the-art LLM parameter-training baseline, compressing 2851 trajectories into 187 procedures. Experimental results demonstrate that structured external memory with Bayesian selection and contrastive refinement enables sample-efficient, interpretable, and continually improving agents without LLM parameter updates.

