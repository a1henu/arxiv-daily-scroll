---
layout: default
title: Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning
---

# Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning
**arXiv**：[2601.21904v1](https://arxiv.org/abs/2601.21904) · [PDF](https://arxiv.org/pdf/2601.21904.pdf)  
**作者**：Hanmo Chen, Guangtao Lyu, Chenghao Xu, Jiexi Yan, Xu Yang, Cheng Deng  

**一句话要点**：提出金字塔Shapley-Taylor学习框架，通过细粒度对齐解决运动-语言检索中的语义鸿沟问题。

**关键词**：运动-语言检索, 细粒度对齐, 金字塔学习, 跨模态对应, Shapley-Taylor方法

## 3 点简述
- 现有方法聚焦全局对齐，忽略局部运动段与文本令牌的细粒度交互，导致检索性能受限。
- 框架基于人类运动感知的金字塔过程，分解运动为时空单元，渐进学习跨模态对应关系。
- 在多个基准数据集上实验显示，该方法显著优于现有技术，实现精确的细粒度对齐。

## 摘要（原文）

> As a foundational task in human-centric cross-modal intelligence, motion-language retrieval aims to bridge the semantic gap between natural language and human motion, enabling intuitive motion analysis, yet existing approaches predominantly focus on aligning entire motion sequences with global textual representations. This global-centric paradigm overlooks fine-grained interactions between local motion segments and individual body joints and text tokens, inevitably leading to suboptimal retrieval performance. To address this limitation, we draw inspiration from the pyramidal process of human motion perception (from joint dynamics to segment coherence, and finally to holistic comprehension) and propose a novel Pyramidal Shapley-Taylor (PST) learning framework for fine-grained motion-language retrieval. Specifically, the framework decomposes human motion into temporal segments and spatial body joints, and learns cross-modal correspondences through progressive joint-wise and segment-wise alignment in a pyramidal fashion, effectively capturing both local semantic details and hierarchical structural relationships. Extensive experiments on multiple public benchmark datasets demonstrate that our approach significantly outperforms state-of-the-art methods, achieving precise alignment between motion segments and body joints and their corresponding text tokens. The code of this work will be released upon acceptance.

