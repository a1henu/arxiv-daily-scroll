---
layout: default
title: RedSage: A Cybersecurity Generalist LLM
---

# RedSage: A Cybersecurity Generalist LLM
**arXiv**：[2601.22159v1](https://arxiv.org/abs/2601.22159) · [PDF](https://arxiv.org/pdf/2601.22159.pdf)  
**作者**：Naufal Suryanto, Muzammal Naseer, Pengfei Li, Syed Talal Wasim, Jinhui Yi, Juergen Gall, Paolo Ceravolo, Ernesto Damiani  

**一句话要点**：提出RedSage：基于领域感知预训练与代理增强的开源网络安全LLM，以支持本地部署的多样化工作流。

**关键词**：网络安全大语言模型, 领域感知预训练, 代理增强, 开源本地部署, 网络安全基准评估

## 3 点简述
- 核心问题：现有网络安全LLM依赖隐私风险的专有API或缺乏领域适应的开源模型，难以兼顾数据安全与专业能力。
- 方法要点：通过大规模网络过滤和手动收集，构建11.8B令牌的网络安全持续预训练数据，并设计代理增强管道生成266K多轮样本进行监督微调。
- 实验或效果：在8B规模下，RedSage在网络安全基准上超越基线模型达+5.59点，在通用LLM任务上提升+5.05点，验证了领域增强对专业与通用能力的提升。

## 摘要（原文）

> Cybersecurity operations demand assistant LLMs that support diverse workflows without exposing sensitive data. Existing solutions either rely on proprietary APIs with privacy risks or on open models lacking domain adaptation. To bridge this gap, we curate 11.8B tokens of cybersecurity-focused continual pretraining data via large-scale web filtering and manual collection of high-quality resources, spanning 28.6K documents across frameworks, offensive techniques, and security tools. Building on this, we design an agentic augmentation pipeline that simulates expert workflows to generate 266K multi-turn cybersecurity samples for supervised fine-tuning. Combined with general open-source LLM data, these resources enable the training of RedSage, an open-source, locally deployable cybersecurity assistant with domain-aware pretraining and post-training. To rigorously evaluate the models, we introduce RedSage-Bench, a benchmark with 30K multiple-choice and 240 open-ended Q&A items covering cybersecurity knowledge, skills, and tool expertise. RedSage is further evaluated on established cybersecurity benchmarks (e.g., CTI-Bench, CyberMetric, SECURE) and general LLM benchmarks to assess broader generalization. At the 8B scale, RedSage achieves consistently better results, surpassing the baseline models by up to +5.59 points on cybersecurity benchmarks and +5.05 points on Open LLM Leaderboard tasks. These findings demonstrate that domain-aware agentic augmentation and pre/post-training can not only enhance cybersecurity-specific expertise but also help to improve general reasoning and instruction-following. All models, datasets, and code are publicly available.

