---
layout: default
title: FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents
---

# FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents
**arXiv**：[2603.01712v1](https://arxiv.org/abs/2603.01712) · [PDF](https://arxiv.org/pdf/2603.01712.pdf)  
**作者**：Qizheng Li, Yifei Zhang, Xiao Yang, Xu Yang, Zhuo Wang, Weiqing Liu, Jiang Bian  

**一句话要点**：提出FT-Dojo环境与FT-Agent系统，以语言代理自动化LLM垂直领域微调过程。

**关键词**：语言代理, LLM微调自动化, 评估驱动反馈, 垂直领域适应, 交互式环境

## 3 点简述
- 核心问题：LLM垂直领域微调依赖专家，缺乏端到端自动化代理方法。
- 方法要点：FT-Agent利用评估反馈迭代诊断失败并优化微调策略。
- 实验效果：FT-Agent在13个任务中10个表现最佳，验证代理泛化性与局限性。

## 摘要（原文）

> Fine-tuning large language models for vertical domains remains a labor-intensive and expensive process, requiring domain experts to curate data, configure training, and iteratively diagnose model behavior. Despite growing interest in autonomous machine learning, no prior work has tackled end-to-end LLM fine-tuning with agents. Can LLM-based agents automate this complete process? We frame this as a substantially open problem: agents must navigate an open-ended search space spanning data curation from diverse data sources, processing with complex tools, building a training pipeline, and iteratively refining their approach based on evaluation outcomes in rapidly growing logs--an overall scenario far more intricate than existing benchmarks. To study this question, we introduce FT-Dojo, an interactive environment comprising 13 tasks across 5 domains. We further develop FT-Agent, an autonomous system that mirrors human experts by leveraging evaluation-driven feedback to iteratively diagnose failures and refine fine-tuning strategies. Experiments on FT-Dojo demonstrate that purpose-built fine-tuning agents significantly outperform general-purpose alternatives, with FT-Agent achieving the best performance on 10 out of 13 tasks across all five domains. Ablations show that the approach generalizes effectively to 3B models, with additional insights on data scaling trade-offs and backbone sensitivity. Case analyses reveal that agents can recover from failures through cumulative learning from historical experience, while also exposing fundamental limitations in causal reasoning--highlighting both the promise and current boundaries of autonomous LLM fine-tuning.

