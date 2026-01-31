---
layout: default
title: DSCD-Nav: Dual-Stance Cooperative Debate for Object Navigation
---

# DSCD-Nav: Dual-Stance Cooperative Debate for Object Navigation
**arXiv**：[2601.21409v1](https://arxiv.org/abs/2601.21409) · [PDF](https://arxiv.org/pdf/2601.21409.pdf)  
**作者**：Weitao An, Qi Liu, Chenghao Xu, Jiayi Chai, Xu Yang, Kun Wei, Cheng Deng  

**一句话要点**：提出双立场协同辩论导航以解决室内物体导航中的决策可靠性问题

**关键词**：物体导航, 决策机制, 视觉语言模型, 室内环境, 辩论系统

## 3 点简述
- 核心问题：现有导航系统依赖单次评分，导致长时程错误和冗余探索。
- 方法要点：构建任务场景理解与安全信息平衡双立场，通过辩论和证据仲裁提升决策可靠性。
- 实验或效果：在HM3D和MP3D数据集上验证了成功率和路径效率的改进。

## 摘要（原文）

> Adaptive navigation in unfamiliar indoor environments is crucial for household service robots. Despite advances in zero-shot perception and reasoning from vision-language models, existing navigation systems still rely on single-pass scoring at the decision layer, leading to overconfident long-horizon errors and redundant exploration. To tackle these problems, we propose Dual-Stance Cooperative Debate Navigation (DSCD-Nav), a decision mechanism that replaces one-shot scoring with stance-based cross-checking and evidence-aware arbitration to improve action reliability under partial observability. Specifically, given the same observation and candidate action set, we explicitly construct two stances by conditioning the evaluation on diverse and complementary objectives: a Task-Scene Understanding (TSU) stance that prioritizes goal progress from scene-layout cues, and a Safety-Information Balancing (SIB) stance that emphasizes risk and information value. The stances conduct a cooperative debate and make policy by cross-checking their top candidates with cue-grounded arguments. Then, a Navigation Consensus Arbitration (NCA) agent is employed to consolidate both sides' reasons and evidence, optionally triggering lightweight micro-probing to verify uncertain choices, preserving NCA's primary intent while disambiguating. Experiments on HM3Dv1, HM3Dv2, and MP3D demonstrate consistent improvements in success and path efficiency while reducing exploration redundancy.

