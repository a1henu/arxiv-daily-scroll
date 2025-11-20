---
layout: default
title: Zero-Shot Open-Vocabulary Human Motion Grounding with Test-Time Training
---

# Zero-Shot Open-Vocabulary Human Motion Grounding with Test-Time Training
**arXiv**：[2511.15379v1](https://arxiv.org/abs/2511.15379) · [PDF](https://arxiv.org/pdf/2511.15379.pdf)  
**作者**：Yunjiao Zhou, Xinyan Chen, Junlang Qian, Lihua Xie, Jianfei Yang  

**一句话要点**：提出ZOMG框架以零样本开放词汇方式实现人类运动序列的语义分割

**关键词**：零样本学习, 开放词汇运动理解, 语义分割, 软掩码优化, 语言模型集成

## 3 点简述
- 核心问题：现有方法依赖预定义动作类的密集监督，难以适应开放词汇真实场景。
- 方法要点：结合语言语义分割和软掩码优化，无需标注或微调即可分解运动序列。
- 实验效果：在HumanML3D基准上mAP提升8.7%，下游检索任务表现显著改进。

## 摘要（原文）

> Understanding complex human activities demands the ability to decompose motion into fine-grained, semantic-aligned sub-actions. This motion grounding process is crucial for behavior analysis, embodied AI and virtual reality. Yet, most existing methods rely on dense supervision with predefined action classes, which are infeasible in open-vocabulary, real-world settings. In this paper, we propose ZOMG, a zero-shot, open-vocabulary framework that segments motion sequences into semantically meaningful sub-actions without requiring any annotations or fine-tuning. Technically, ZOMG integrates (1) language semantic partition, which leverages large language models to decompose instructions into ordered sub-action units, and (2) soft masking optimization, which learns instance-specific temporal masks to focus on frames critical to sub-actions, while maintaining intra-segment continuity and enforcing inter-segment separation, all without altering the pretrained encoder. Experiments on three motion-language datasets demonstrate state-of-the-art effectiveness and efficiency of motion grounding performance, outperforming prior methods by +8.7\% mAP on HumanML3D benchmark. Meanwhile, significant improvements also exist in downstream retrieval, establishing a new paradigm for annotation-free motion understanding.

