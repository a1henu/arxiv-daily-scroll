---
layout: default
title: MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models
---

# MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusion Models
**arXiv**：[2602.17602v1](https://arxiv.org/abs/2602.17602) · [PDF](https://arxiv.org/pdf/2602.17602.pdf)  
**作者**：Hojung Jung, Rodrigo Hormazabal, Jaehyeong Jo, Youngrok Park, Kyunggeun Roh, Se-Young Yun, Sehui Han, Dae-Woong Jeong  

**一句话要点**：提出MolHIT框架，基于分层离散扩散模型提升分子图生成性能，用于药物发现与材料科学。

**关键词**：分子图生成, 离散扩散模型, 药物发现, 化学有效性, 多属性引导生成, 支架扩展

## 3 点简述
- 现有图扩散模型在分子生成中化学有效性低且难以满足属性需求。
- MolHIT采用分层离散扩散模型，引入化学先验编码和解耦原子编码。
- 在MOSES数据集上实现新SOTA，首次在图扩散中达到近完美有效性，并在下游任务中表现优异。

## 摘要（原文）

> Molecular generation with diffusion models has emerged as a promising direction for AI-driven drug discovery and materials science. While graph diffusion models have been widely adopted due to the discrete nature of 2D molecular graphs, existing models suffer from low chemical validity and struggle to meet the desired properties compared to 1D modeling. In this work, we introduce MolHIT, a powerful molecular graph generation framework that overcomes long-standing performance limitations in existing methods. MolHIT is based on the Hierarchical Discrete Diffusion Model, which generalizes discrete diffusion to additional categories that encode chemical priors, and decoupled atom encoding that splits the atom types according to their chemical roles. Overall, MolHIT achieves new state-of-the-art performance on the MOSES dataset with near-perfect validity for the first time in graph diffusion, surpassing strong 1D baselines across multiple metrics. We further demonstrate strong performance in downstream tasks, including multi-property guided generation and scaffold extension.

