---
layout: default
title: Consistency-Preserving Concept Erasure via Unsafe-Safe Pairing and Directional Fisher-weighted Adaptation
---

# Consistency-Preserving Concept Erasure via Unsafe-Safe Pairing and Directional Fisher-weighted Adaptation
**arXiv**：[2602.05339v1](https://arxiv.org/abs/2602.05339) · [PDF](https://arxiv.org/pdf/2602.05339.pdf)  
**作者**：Yongwoo Kim, Sungmin Cha, Hyunsoo Kim, Jaewon Lee, Donghyun Kim  

**一句话要点**：提出PAIR框架，通过不安全-安全配对和方向性Fisher加权适应，实现一致性保持的概念擦除

**关键词**：概念擦除, 文本到图像扩散模型, 语义一致性, 参数高效微调, 不安全-安全配对

## 3 点简述
- 现有概念擦除方法缺乏安全替代指导，导致结构语义一致性差
- 使用不安全-安全配对进行语义重对齐，并基于Fisher加权初始化DoRA参数
- 实验显示在擦除有害概念时，能保持结构完整性和生成质量

## 摘要（原文）

> With the increasing versatility of text-to-image diffusion models, the ability to selectively erase undesirable concepts (e.g., harmful content) has become indispensable. However, existing concept erasure approaches primarily focus on removing unsafe concepts without providing guidance toward corresponding safe alternatives, which often leads to failure in preserving the structural and semantic consistency between the original and erased generations. In this paper, we propose a novel framework, PAIRed Erasing (PAIR), which reframes concept erasure from simple removal to consistency-preserving semantic realignment using unsafe-safe pairs. We first generate safe counterparts from unsafe inputs while preserving structural and semantic fidelity, forming paired unsafe-safe multimodal data. Leveraging these pairs, we introduce two key components: (1) Paired Semantic Realignment, a guided objective that uses unsafe-safe pairs to explicitly map target concepts to semantically aligned safe anchors; and (2) Fisher-weighted Initialization for DoRA, which initializes parameter-efficient low-rank adaptation matrices using unsafe-safe pairs, encouraging the generation of safe alternatives while selectively suppressing unsafe concepts. Together, these components enable fine-grained erasure that removes only the targeted concepts while maintaining overall semantic consistency. Extensive experiments demonstrate that our approach significantly outperforms state-of-the-art baselines, achieving effective concept erasure while preserving structural integrity, semantic coherence, and generation quality.

