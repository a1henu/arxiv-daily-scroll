---
layout: default
title: RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation
---

# RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation
**arXiv**：[2602.16444v1](https://arxiv.org/abs/2602.16444) · [PDF](https://arxiv.org/pdf/2602.16444.pdf)  
**作者**：Yixue Zhang, Kun Wu, Zhi Gao, Zhen Zhao, Pei Ren, Zhiyuan Xu, Fei Liao, Xinhua Wang, Shichao Fan, Di Wu, Qiuxuan Feng, Meng Li, Zhengping Che, Chang Liu, Jian Tang  

**一句话要点**：提出RoboGene框架以自动化生成多样且物理可行的机器人操作任务，提升VLA预训练数据质量

**关键词**：机器人操作任务生成, 多样性驱动采样, 物理约束自反思, VLA预训练, 真实世界实验

## 3 点简述
- 核心问题：机器人操作数据稀缺且收集成本高，现有任务生成方法难以扩展或产生物理不可行指令
- 方法要点：集成多样性驱动采样、自反思机制和人在环优化，确保任务覆盖广且物理约束满足
- 实验或效果：在真实世界实验中，RoboGene优于GPT-4o等模型，预训练VLA模型获得更高成功率和泛化能力

## 摘要（原文）

> The pursuit of general-purpose robotic manipulation is hindered by the scarcity of diverse, real-world interaction data. Unlike data collection from web in vision or language, robotic data collection is an active process incurring prohibitive physical costs. Consequently, automated task curation to maximize data value remains a critical yet under-explored challenge. Existing manual methods are unscalable and biased toward common tasks, while off-the-shelf foundation models often hallucinate physically infeasible instructions. To address this, we introduce RoboGene, an agentic framework designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots. RoboGene integrates three core components: diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement for continuous improvement. We conduct extensive quantitative analysis and large-scale real-world experiments, collecting datasets of 18k trajectories and introducing novel metrics to assess task quality, feasibility, and diversity. Results demonstrate that RoboGene significantly outperforms state-of-the-art foundation models (e.g., GPT-4o, Gemini 2.5 Pro). Furthermore, real-world experiments show that VLA models pre-trained with RoboGene achieve higher success rates and superior generalization, underscoring the importance of high-quality task generation. Our project is available at https://robogene-boost-vla.github.io.

