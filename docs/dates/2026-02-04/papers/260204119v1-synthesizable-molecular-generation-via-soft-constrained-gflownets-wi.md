---
layout: default
title: Synthesizable Molecular Generation via Soft-constrained GFlowNets with Rich Chemical Priors
---

# Synthesizable Molecular Generation via Soft-constrained GFlowNets with Rich Chemical Priors
**arXiv**：[2602.04119v1](https://arxiv.org/abs/2602.04119) · [PDF](https://arxiv.org/pdf/2602.04119.pdf)  
**作者**：Hyeonah Kim, Minsu Kim, Celine Roget, Dionessa Biton, Louis Vaillancourt, Yves V. Brun, Yoshua Bengio, Alex Hernandez-Garcia  

**一句话要点**：提出S3-GFN，通过软约束GFlowNets结合化学先验生成可合成分子，以解决实验药物发现中分子合成性不足的问题。

**关键词**：分子生成, 可合成性约束, GFlowNets, 软正则化, 对比学习, 药物发现

## 3 点简述
- 核心问题：生成模型在实验药物发现中因分子合成性差而受限，现有硬约束方法缺乏灵活性和可扩展性。
- 方法要点：基于序列的GFlowNet，通过软正则化和对比学习信号，利用大规模SMILES语料库的先验引导生成高奖励可合成分子。
- 实验或效果：S3-GFN生成可合成分子比例≥95%，在多样任务中实现更高奖励，提升合成性和性能。

## 摘要（原文）

> The application of generative models for experimental drug discovery campaigns is severely limited by the difficulty of designing molecules de novo that can be synthesized in practice. Previous works have leveraged Generative Flow Networks (GFlowNets) to impose hard synthesizability constraints through the design of state and action spaces based on predefined reaction templates and building blocks. Despite the promising prospects of this approach, it currently lacks flexibility and scalability. As an alternative, we propose S3-GFN, which generates synthesizable SMILES molecules via simple soft regularization of a sequence-based GFlowNet. Our approach leverages rich molecular priors learned from large-scale SMILES corpora to steer molecular generation towards high-reward, synthesizable chemical spaces. The model induces constraints through off-policy replay training with a contrastive learning signal based on separate buffers of synthesizable and unsynthesizable samples. Our experiments show that S3-GFN learns to generate synthesizable molecules ($\geq 95\%$) with higher rewards in diverse tasks.

