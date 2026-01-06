---
layout: default
title: Forget Less by Learning Together through Concept Consolidation
---

# Forget Less by Learning Together through Concept Consolidation
**arXiv**：[2601.01963v1](https://arxiv.org/abs/2601.01963) · [PDF](https://arxiv.org/pdf/2601.01963.pdf)  
**作者**：Arjun Ramesh Kaushik, Naresh Kumar Devulapally, Vishnu Suresh Lokhande, Nalini Ratha, Venu Govindaraju  

**一句话要点**：提出FL2T框架以解决定制扩散模型在连续学习中的灾难性遗忘问题

**关键词**：定制扩散模型, 灾难性遗忘, 连续学习, 概念间学习, 集合不变模块, CLIP对齐

## 3 点简述
- 核心问题：定制扩散模型在连续学习新概念时易发生灾难性遗忘，现有方法忽略概念间交互
- 方法要点：引入集合不变的概念间学习模块，通过代理指导特征选择，促进知识保留与迁移
- 实验或效果：在三个数据集上验证，显著提升概念保留，平均CLIP图像对齐分数至少提高2%

## 摘要（原文）

> Custom Diffusion Models (CDMs) have gained significant attention due to their remarkable ability to personalize generative processes. However, existing CDMs suffer from catastrophic forgetting when continuously learning new concepts. Most prior works attempt to mitigate this issue under the sequential learning setting with a fixed order of concept inflow and neglect inter-concept interactions. In this paper, we propose a novel framework - Forget Less by Learning Together (FL2T) - that enables concurrent and order-agnostic concept learning while addressing catastrophic forgetting. Specifically, we introduce a set-invariant inter-concept learning module where proxies guide feature selection across concepts, facilitating improved knowledge retention and transfer. By leveraging inter-concept guidance, our approach preserves old concepts while efficiently incorporating new ones. Extensive experiments, across three datasets, demonstrates that our method significantly improves concept retention and mitigates catastrophic forgetting, highlighting the effectiveness of inter-concept catalytic behavior in incremental concept learning of ten tasks with at least 2% gain on average CLIP Image Alignment scores.

