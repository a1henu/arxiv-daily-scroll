---
layout: default
title: GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation
---

# GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation
**arXiv**：[2512.17495v1](https://arxiv.org/abs/2512.17495) · [PDF](https://arxiv.org/pdf/2512.17495.pdf)  
**作者**：Rang Li, Lei Li, Shuhuai Ren, Hao Tian, Shuhao Gu, Shicheng Li, Zihao Yue, Yudong Wang, Wenhan Ma, Zhe Yang, Jingyuan Ma, Zhifang Sui, Fuli Luo  

**一句话要点**：提出GroundingME基准以评估多模态大语言模型在真实复杂场景下的视觉定位能力

**关键词**：视觉定位, 多模态大语言模型, 基准评估, 拒绝能力, 复杂场景, 安全部署

## 3 点简述
- 核心问题：现有基准无法捕捉真实世界复杂性，MLLMs在视觉定位上可能仅依赖简化数据集模式匹配
- 方法要点：通过自动生成与人工验证创建包含1,005个挑战性示例的基准，涵盖判别、空间、限制和拒绝四个维度
- 实验或效果：评估25个MLLMs揭示显著能力差距，最佳模型准确率仅45.1%，拒绝任务多数得0%，提出改进策略提升性能

## 摘要（原文）

> Visual grounding, localizing objects from natural language descriptions, represents a critical bridge between language and vision understanding. While multimodal large language models (MLLMs) achieve impressive scores on existing benchmarks, a fundamental question remains: can MLLMs truly ground language in vision with human-like sophistication, or are they merely pattern-matching on simplified datasets? Current benchmarks fail to capture real-world complexity where humans effortlessly navigate ambiguous references and recognize when grounding is impossible. To rigorously assess MLLMs' true capabilities, we introduce GroundingME, a benchmark that systematically challenges models across four critical dimensions: (1) Discriminative, distinguishing highly similar objects, (2) Spatial, understanding complex relational descriptions, (3) Limited, handling occlusions or tiny objects, and (4) Rejection, recognizing ungroundable queries. Through careful curation combining automated generation with human verification, we create 1,005 challenging examples mirroring real-world complexity. Evaluating 25 state-of-the-art MLLMs reveals a profound capability gap: the best model achieves only 45.1% accuracy, while most score 0% on rejection tasks, reflexively hallucinating objects rather than acknowledging their absence, raising critical safety concerns for deployment. We explore two strategies for improvements: (1) test-time scaling selects optimal response by thinking trajectory to improve complex grounding by up to 2.9%, and (2) data-mixture training teaches models to recognize ungroundable queries, boosting rejection accuracy from 0% to 27.9%. GroundingME thus serves as both a diagnostic tool revealing current limitations in MLLMs and a roadmap toward human-level visual grounding.

