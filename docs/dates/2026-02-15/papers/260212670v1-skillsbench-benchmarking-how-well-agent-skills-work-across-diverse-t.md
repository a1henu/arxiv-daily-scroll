---
layout: default
title: SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks
---

# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks
**arXiv**：[2602.12670v1](https://arxiv.org/abs/2602.12670) · [PDF](https://arxiv.org/pdf/2602.12670.pdf)  
**作者**：Xiangyi Li, Wenbo Chen, Yimin Liu, Shenghan Zheng, Xiaokun Chen, Yifeng He, Yubo Li, Bingran You, Haotian Shen, Jiankai Sun, Shuyi Wang, Qunhong Zeng, Di Wang, Xuandong Zhao, Yuanli Wang, Roey Ben Chaim, Zonglin Di, Yipeng Gao, Junwei He, Yizhuo He, Liqiang Jing, Luyang Kong, Xin Lan, Jiachen Li, Songlin Li, Yijiang Li, Yueqian Lin, Xinyi Liu, Xuanqing Liu, Haoran Lyu, Ze Ma, Bowei Wang, Runhui Wang, Tianyu Wang, Wengao Ye, Yue Zhang, Hanwen Xing, Yiqi Xue, Steven Dillmann, Han-chung Lee  

**一句话要点**：提出SkillsBench基准，评估Agent Skills在多样化任务中的实际效果。

**关键词**：Agent Skills, 基准测试, LLM代理, 任务评估, 程序知识

## 3 点简述
- 核心问题：缺乏标准方法衡量Agent Skills对LLM代理推理的帮助程度。
- 方法要点：构建包含86个任务、11个领域的基准，提供策划Skills和确定性验证器。
- 实验或效果：策划Skills平均提升通过率16.2个百分点，但效果因领域和任务而异。

## 摘要（原文）

> Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations over 7,308 trajectories. Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2--3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.

