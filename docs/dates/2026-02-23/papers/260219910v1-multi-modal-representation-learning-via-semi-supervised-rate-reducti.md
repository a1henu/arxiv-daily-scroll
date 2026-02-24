---
layout: default
title: Multi-Modal Representation Learning via Semi-Supervised Rate Reduction for Generalized Category Discovery
---

# Multi-Modal Representation Learning via Semi-Supervised Rate Reduction for Generalized Category Discovery
**arXiv**：[2602.19910v1](https://arxiv.org/abs/2602.19910) · [PDF](https://arxiv.org/pdf/2602.19910.pdf)  
**作者**：Wei He, Xianghan Meng, Zhiyuan Huang, Xianbiao Qi, Rong Xiao, Chun-Guang Li  

**一句话要点**：提出SSR²-GCD框架，通过半监督率降低学习多模态表示，解决广义类别发现中的开放集识别问题。

**关键词**：广义类别发现, 多模态表示学习, 半监督率降低, 模态内对齐, 开放集识别, 视觉语言模型

## 3 点简述
- 核心问题：广义类别发现（GCD）需识别已知和未知类别，仅部分已知类别有标签，是开放集识别挑战。
- 方法要点：基于半监督率降低，强调模态内对齐以学习具有理想结构的多模态表示，并集成视觉语言模型的提示候选以促进知识迁移。
- 实验或效果：在通用和细粒度基准数据集上进行了广泛实验，展示了方法的优越性能。

## 摘要（原文）

> Generalized Category Discovery (GCD) aims to identify both known and unknown categories, with only partial labels given for the known categories, posing a challenging open-set recognition problem. State-of-the-art approaches for GCD task are usually built on multi-modality representation learning, which is heavily dependent upon inter-modality alignment. However, few of them cast a proper intra-modality alignment to generate a desired underlying structure of representation distributions. In this paper, we propose a novel and effective multi-modal representation learning framework for GCD via Semi-Supervised Rate Reduction, called SSR$^2$-GCD, to learn cross-modality representations with desired structural properties based on emphasizing to properly align intra-modality relationships. Moreover, to boost knowledge transfer, we integrate prompt candidates by leveraging the inter-modal alignment offered by Vision Language Models. We conduct extensive experiments on generic and fine-grained benchmark datasets demonstrating superior performance of our approach.

