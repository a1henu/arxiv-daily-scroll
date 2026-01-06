---
layout: default
title: PsychEval: A Multi-Session and Multi-Therapy Benchmark for High-Realism and Comprehensive AI Psychological Counselor
---

# PsychEval: A Multi-Session and Multi-Therapy Benchmark for High-Realism and Comprehensive AI Psychological Counselor
**arXiv**：[2601.01802v1](https://arxiv.org/abs/2601.01802) · [PDF](https://arxiv.org/pdf/2601.01802.pdf)  
**作者**：Qianjun Pan, Junyi Wang, Jie Zhou, Yutao Yang, Junsong Li, Kaiyin Xu, Yougen Zhou, Yihan Li, Jingyuan Zhao, Qin Chen, Ningning Zhou, Kai Chen, Liang He  

**一句话要点**：提出PsychEval基准以解决高真实感、多会话和多疗法AI心理咨询师的训练与评估问题

**关键词**：AI心理咨询, 多会话基准, 多疗法数据集, 技能标注, 强化学习环境, 临床评估

## 3 点简述
- 核心问题：现有AI心理咨询师在真实感、多会话记忆和多疗法灵活性方面存在不足，缺乏系统性评估框架。
- 方法要点：构建多会话（6-10次）、多疗法（五种疗法加整合疗法）数据集，标注677元技能和4577原子技能，支持强化学习环境。
- 实验或效果：通过18个指标和2000多样本评估，验证数据集质量和临床保真度，促进AI咨询师自进化训练。

## 摘要（原文）

> To develop a reliable AI for psychological assessment, we introduce \texttt{PsychEval}, a multi-session, multi-therapy, and highly realistic benchmark designed to address three key challenges: \textbf{1) Can we train a highly realistic AI counselor?} Realistic counseling is a longitudinal task requiring sustained memory and dynamic goal tracking. We propose a multi-session benchmark (spanning 6-10 sessions across three distinct stages) that demands critical capabilities such as memory continuity, adaptive reasoning, and longitudinal planning. The dataset is annotated with extensive professional skills, comprising over 677 meta-skills and 4577 atomic skills. \textbf{2) How to train a multi-therapy AI counselor?} While existing models often focus on a single therapy, complex cases frequently require flexible strategies among various therapies. We construct a diverse dataset covering five therapeutic modalities (Psychodynamic, Behaviorism, CBT, Humanistic Existentialist, and Postmodernist) alongside an integrative therapy with a unified three-stage clinical framework across six core psychological topics. \textbf{3) How to systematically evaluate an AI counselor?} We establish a holistic evaluation framework with 18 therapy-specific and therapy-shared metrics across Client-Level and Counselor-Level dimensions. To support this, we also construct over 2,000 diverse client profiles. Extensive experimental analysis fully validates the superior quality and clinical fidelity of our dataset. Crucially, \texttt{PsychEval} transcends static benchmarking to serve as a high-fidelity reinforcement learning environment that enables the self-evolutionary training of clinically responsible and adaptive AI counselors.

