---
layout: default
title: ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design
---

# ReACT-Drug: Reaction-Template Guided Reinforcement Learning for de novo Drug Design
**arXiv**：[2512.20958v1](https://arxiv.org/abs/2512.20958) · [PDF](https://arxiv.org/pdf/2512.20958.pdf)  
**作者**：R Yadunandan, Nimisha Ghosh  

**一句话要点**：提出ReACT-Drug框架，基于强化学习与反应模板指导，用于从头药物设计以优化合成可及性与结合亲和力。

**关键词**：从头药物设计, 强化学习, 反应模板, 蛋白嵌入, 分子生成, 合成可及性

## 3 点简述
- 核心问题：从头药物设计需在广阔化学空间中寻找合成可及、高亲和力候选分子，传统方法难以实现多目标优化。
- 方法要点：利用ESM-2蛋白嵌入识别相似蛋白，分解已知配体初始化片段空间，结合PPO代理与ChemBERTa编码进行反应模板引导的分子变换。
- 实验或效果：生成候选分子在MOSES基准测试中确保100%化学有效性和新颖性，具有竞争性结合亲和力与高合成可及性。

## 摘要（原文）

> De novo drug design is a crucial component of modern drug development, yet navigating the vast chemical space to find synthetically accessible, high-affinity candidates remains a significant challenge. Reinforcement Learning (RL) enhances this process by enabling multi-objective optimization and exploration of novel chemical space - capabilities that traditional supervised learning methods lack. In this work, we introduce \textbf{ReACT-Drug}, a fully integrated, target-agnostic molecular design framework based on Reinforcement Learning. Unlike models requiring target-specific fine-tuning, ReACT-Drug utilizes a generalist approach by leveraging ESM-2 protein embeddings to identify similar proteins for a given target from a knowledge base such as Protein Data Base (PDB). Thereafter, the known drug ligands corresponding to such proteins are decomposed to initialize a fragment-based search space, biasing the agent towards biologically relevant subspaces. For each such fragment, the pipeline employs a Proximal Policy Optimization (PPO) agent guiding a ChemBERTa-encoded molecule through a dynamic action space of chemically valid, reaction-template-based transformations. This results in the generation of \textit{de novo} drug candidates with competitive binding affinities and high synthetic accessibility, while ensuring 100\% chemical validity and novelty as per MOSES benchmarking. This architecture highlights the potential of integrating structural biology, deep representation learning, and chemical synthesis rules to automate and accelerate rational drug design. The dataset and code are available at https://github.com/YadunandanRaman/ReACT-Drug/.

