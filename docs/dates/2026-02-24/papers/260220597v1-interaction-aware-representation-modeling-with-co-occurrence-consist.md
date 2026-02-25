---
layout: default
title: Interaction-aware Representation Modeling with Co-occurrence Consistency for Egocentric Hand-Object Parsing
---

# Interaction-aware Representation Modeling with Co-occurrence Consistency for Egocentric Hand-Object Parsing
**arXiv**：[2602.20597v1](https://arxiv.org/abs/2602.20597) · [PDF](https://arxiv.org/pdf/2602.20597.pdf)  
**作者**：Yuejiao Su, Yi Wang, Lei Yao, Yawen Cui, Lap-Pui Chau  

**一句话要点**：提出Interaction-aware Transformer以解决第一人称视角手-物解析中的交互幻觉与查询初始化问题

**关键词**：第一人称视角解析, 手-物交互, Transformer架构, 动态查询生成, 条件共现损失, 泛化能力

## 3 点简述
- 核心问题：现有方法在查询初始化、特征选择与物理一致性方面存在局限，导致交互幻觉。
- 方法要点：集成动态查询生成器、双上下文特征选择器和条件共现损失，增强交互感知与一致性。
- 实验或效果：在EgoHOS和mini-HOI4D数据集上实现最先进性能，展示强泛化能力。

## 摘要（原文）

> A fine-grained understanding of egocentric human-environment interactions is crucial for developing next-generation embodied agents. One fundamental challenge in this area involves accurately parsing hands and active objects. While transformer-based architectures have demonstrated considerable potential for such tasks, several key limitations remain unaddressed: 1) existing query initialization mechanisms rely primarily on semantic cues or learnable parameters, demonstrating limited adaptability to changing active objects across varying input scenes; 2) previous transformer-based methods utilize pixel-level semantic features to iteratively refine queries during mask generation, which may introduce interaction-irrelevant content into the final embeddings; and 3) prevailing models are susceptible to "interaction illusion", producing physically inconsistent predictions. To address these issues, we propose an end-to-end Interaction-aware Transformer (InterFormer), which integrates three key components, i.e., a Dynamic Query Generator (DQG), a Dual-context Feature Selector (DFS), and the Conditional Co-occurrence (CoCo) loss. The DQG explicitly grounds query initialization in the spatial dynamics of hand-object contact, enabling targeted generation of interaction-aware queries for hands and various active objects. The DFS fuses coarse interactive cues with semantic features, thereby suppressing interaction-irrelevant noise and emphasizing the learning of interactive relationships. The CoCo loss incorporates hand-object relationship constraints to enhance physical consistency in prediction. Our model achieves state-of-the-art performance on both the EgoHOS and the challenging out-of-distribution mini-HOI4D datasets, demonstrating its effectiveness and strong generalization ability. Code and models are publicly available at https://github.com/yuggiehk/InterFormer.

