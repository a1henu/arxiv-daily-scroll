---
layout: default
title: Process Over Outcome: Cultivating Forensic Reasoning for Generalizable Multimodal Manipulation Detection
---

# Process Over Outcome: Cultivating Forensic Reasoning for Generalizable Multimodal Manipulation Detection
**arXiv**：[2603.01993v1](https://arxiv.org/abs/2603.01993) · [PDF](https://arxiv.org/pdf/2603.01993.pdf)  
**作者**：Yuchen Zhang, Yaxiong Wang, Kecheng Han, Yujiao Wu, Lianwei Wu, Li Zhu, Zhedong Zheng  

**一句话要点**：提出REFORM框架以通过法证推理提升多模态篡改检测的泛化能力

**关键词**：多模态篡改检测, 法证推理, 泛化学习, 课程学习, 强化学习, 数据集构建

## 3 点简述
- 核心问题：现有篡改检测方法依赖结果导向监督，泛化性差且缺乏可解释性
- 方法要点：采用三阶段课程学习，从诱导法证理据到强化逻辑一致性
- 实验或效果：在ROM等数据集上实现SOTA性能，泛化能力优于现有方法

## 摘要（原文）

> Recent advances in generative AI have significantly enhanced the realism of multimodal media manipulation, thereby posing substantial challenges to manipulation detection. Existing manipulation detection and grounding approaches predominantly focus on manipulation type classification under result-oriented supervision, which not only lacks interpretability but also tends to overfit superficial artifacts. In this paper, we argue that generalizable detection requires incorporating explicit forensic reasoning, rather than merely classifying a limited set of manipulation types, which fails to generalize to unseen manipulation patterns. To this end, we propose REFORM, a reasoning-driven framework that shifts learning from outcome fitting to process modeling. REFORM adopts a three-stage curriculum that first induces forensic rationales, then aligns reasoning with final judgments, and finally refines logical consistency via reinforcement learning. To support this paradigm, we introduce ROM, a large-scale dataset with rich reasoning annotations. Extensive experiments show that REFORM establishes new state-of-the-art performance with superior generalization, achieving 81.52% ACC on ROM, 76.65% ACC on DGM4, and 74.9 F1 on MMFakeBench.

