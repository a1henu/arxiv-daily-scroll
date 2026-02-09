---
layout: default
title: ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training
---

# ScaleEnv: Scaling Environment Synthesis from Scratch for Generalist Interactive Tool-Use Agent Training
**arXiv**：[2602.06820v1](https://arxiv.org/abs/2602.06820) · [PDF](https://arxiv.org/pdf/2602.06820.pdf)  
**作者**：Dunwei Tu, Hongyan Hao, Hansi Yang, Yihao Chen, Yi-Kai Zhang, Zhikang Xia, Yu Yang, Yueqing Sun, Xingchen Liu, Furao Shen, Qi Gu, Hui Su, Xunliang Cai  

**一句话要点**：提出ScaleEnv框架，从零构建交互环境以训练通用工具使用智能体

**关键词**：交互环境合成, 通用智能体训练, 工具使用, 程序化测试, 任务验证, 泛化能力

## 3 点简述
- 核心问题：交互环境稀缺，现有合成方法在多样性和可扩展性上受限
- 方法要点：通过程序化测试确保环境可靠性，依赖图扩展和动作验证保证任务完整可解
- 实验或效果：在未见多轮工具使用基准上表现提升，实证环境多样性扩展对泛化关键

## 摘要（原文）

> Training generalist agents capable of adapting to diverse scenarios requires interactive environments for self-exploration. However, interactive environments remain critically scarce, and existing synthesis methods suffer from significant limitations regarding environmental diversity and scalability. To address these challenges, we introduce ScaleEnv, a framework that constructs fully interactive environments and verifiable tasks entirely from scratch. Specifically, ScaleEnv ensures environment reliability through procedural testing, and guarantees task completeness and solvability via tool dependency graph expansion and executable action verification. By enabling agents to learn through exploration within ScaleEnv, we demonstrate significant performance improvements on unseen, multi-turn tool-use benchmarks such as $τ^2$-Bench and VitaBench, highlighting strong generalization capabilities. Furthermore, we investigate the relationship between increasing number of domains and model generalization performance, providing empirical evidence that scaling environmental diversity is critical for robust agent learning.

