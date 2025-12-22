---
layout: default
title: CheXPO-v2: Preference Optimization for Chest X-ray VLMs with Knowledge Graph Consistency
---

# CheXPO-v2: Preference Optimization for Chest X-ray VLMs with Knowledge Graph Consistency
**arXiv**：[2512.17213v1](https://arxiv.org/abs/2512.17213) · [PDF](https://arxiv.org/pdf/2512.17213.pdf)  
**作者**：Xiao Liang, Yuxuan An, Di Wang, Jiawei Hu, Zhicheng Jiao, Bin Jing, Quan Wang  

**一句话要点**：提出CheXPO-v2框架，通过知识图谱一致性奖励解决胸部X光视觉语言模型幻觉问题。

**关键词**：医学视觉语言模型, 知识图谱一致性, 实体关系匹配, 过程监督, 胸部X光分析, 低样本学习

## 3 点简述
- 核心问题：医学视觉语言模型易产生幻觉，传统强化学习方法导致推理冗长且不可验证。
- 方法要点：引入知识图谱一致性奖励，基于实体关系匹配对推理步骤进行细粒度监督。
- 实验或效果：在MIMIC-CXR-VQA基准上超越现有方法，仅用5k样本实现高精度和临床可验证性。

## 摘要（原文）

> Medical Vision-Language Models (VLMs) are prone to hallucinations, compromising clinical reliability. While reinforcement learning methods like Group Relative Policy Optimization (GRPO) offer a low-cost alignment solution, their reliance on sparse, outcome-based rewards inadvertently encourages models to "overthink" -- generating verbose, convoluted, and unverifiable Chain-of-Thought reasoning to justify answers. This focus on outcomes obscures factual errors and poses significant safety risks. To address this, we propose CheXPO-v2, a novel alignment framework that shifts from outcome to process supervision. Our core innovation is a Knowledge Graph Consistency Reward mechanism driven by Entity-Relation Matching. By explicitly parsing reasoning steps into structured "Disease, Relation, Anatomy" triplets, we provide fine-grained supervision that penalizes incoherent logic and hallucinations at the atomic level. Integrating this with a hard-example mining strategy, our approach significantly outperforms GRPO and state-of-the-art models on benchmarks like MIMIC-CXR-VQA. Crucially, CheXPO-v2 achieves new state-of-the-art accuracy using only 5k samples, demonstrating exceptional data efficiency while producing clinically sound and verifiable reasoning. The project source code is publicly available at: https://github.com/ecoxial2007/CheX-Phi4MM.

