---
layout: default
title: R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training
---

# R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training
**arXiv**：[2602.13103v1](https://arxiv.org/abs/2602.13103) · [PDF](https://arxiv.org/pdf/2602.13103.pdf)  
**作者**：Gengsheng Li, Jinghan He, Shijie Wang, Dan Zhang, Ruiqi Liu, Renrui Zhang, Zijun Yao, Junfeng Fang, Haiyun Guo, Jinqiao Wang  

**一句话要点**：提出R-Diverse以缓解自训练LLM中的多样性幻觉问题

**关键词**：自训练LLM, 多样性幻觉, 推理技能评估, 记忆增强惩罚, 技能感知测量, 数学推理

## 3 点简述
- 核心问题：自训练中多样性幻觉导致非持续改进，包括局部和表面多样性幻觉。
- 方法要点：引入记忆增强惩罚和技能感知测量，分别抑制跨迭代模式循环和评估技能多样性。
- 实验或效果：在10个数学和通用推理基准上，R-Diverse实现更持久的增益并优于先前方法。

## 摘要（原文）

> Self-play bootstraps LLM reasoning through an iterative Challenger-Solver loop: the Challenger is trained to generate questions that target the Solver's capabilities, and the Solver is optimized on the generated data to expand its reasoning skills. However, existing frameworks like R-Zero often exhibit non-sustained improvement, where early gains degrade as self-play continues. We identify a key failure mode, Diversity Illusion, where the Solver's training signals appear diverse yet collapse into recurring underlying patterns. It manifests as (1) Local Diversity Illusion, where diversity is enforced only within-batch, inducing cross-iteration mode cycling; and (2) Surface Diversity Illusion, where questions vary superficially but require near-identical reasoning skills. To mitigate them, we propose R-Diverse with two aligned innovations: Memory-Augmented Penalty (MAP), which uses a persistent memory bank to discourage recycling across iterations, and Skill-Aware Measurement (SAM), which evaluates diversity by the reasoning skills exercised rather than surface variation of questions. Across 10 math and general reasoning benchmarks, R-Diverse sustains gains over more iterations and consistently outperforms prior self-play methods. Code is available at https://github.com/Gengsheng-Li/R-Diverse.

