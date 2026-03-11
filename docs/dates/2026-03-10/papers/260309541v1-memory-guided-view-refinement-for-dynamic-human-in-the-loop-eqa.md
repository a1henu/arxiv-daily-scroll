---
layout: default
title: Memory-Guided View Refinement for Dynamic Human-in-the-loop EQA
---

# Memory-Guided View Refinement for Dynamic Human-in-the-loop EQA
**arXiv**：[2603.09541v1](https://arxiv.org/abs/2603.09541) · [PDF](https://arxiv.org/pdf/2603.09541.pdf)  
**作者**：Xin Lu, Rui Li, Xun Huang, Weixin Li, Chuanqing Zhuang, Jiayuan Li, Zhengda Lu, Jun Xiao, Yunhong Wang  

**一句话要点**：提出DIVRR框架以解决动态人机交互EQA中的视角依赖遮挡和证据冗余问题

**关键词**：具身问答, 动态场景理解, 视角细化, 选择性记忆, 人机交互, 推理效率

## 3 点简述
- 核心问题：动态人机交互场景中，人类活动和遮挡导致视觉证据瞬变，传统方法积累冗余证据且推理成本高。
- 方法要点：DIVRR框架结合相关性引导的视角细化和选择性记忆准入，无需训练，验证模糊观察并保留信息性证据。
- 实验或效果：在DynHiL-EQA和HM-EQA数据集上，DIVRR在动态和静态设置中均优于基线，同时保持高推理效率。

## 摘要（原文）

> Embodied Question Answering (EQA) has traditionally been evaluated in temporally stable environments where visual evidence can be accumulated reliably. However, in dynamic, human-populated scenes, human activities and occlusions introduce significant perceptual non-stationarity: task-relevant cues are transient and view-dependent, while a store-then-retrieve strategy over-accumulates redundant evidence and increases inference cost. This setting exposes two practical challenges for EQA agents: resolving ambiguity caused by viewpoint-dependent occlusions, and maintaining compact yet up-to-date evidence for efficient inference. To enable systematic study of this setting, we introduce DynHiL-EQA, a human-in-the-loop EQA dataset with two subsets: a Dynamic subset featuring human activities and temporal changes, and a Static subset with temporally stable observations. To address the above challenges, we present DIVRR (Dynamic-Informed View Refinement and Relevance-guided Adaptive Memory Selection), a training-free framework that couples relevance-guided view refinement with selective memory admission. By verifying ambiguous observations before committing them and retaining only informative evidence, DIVRR improves robustness under occlusions while preserving fast inference with compact memory. Extensive experiments on DynHiL-EQA and the established HM-EQA dataset demonstrate that DIVRR consistently improves over existing baselines in both dynamic and static settings while maintaining high inference efficiency.

