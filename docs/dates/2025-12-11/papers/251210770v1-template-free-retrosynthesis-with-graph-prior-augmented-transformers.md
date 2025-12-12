---
layout: default
title: Template-Free Retrosynthesis with Graph-Prior Augmented Transformers
---

# Template-Free Retrosynthesis with Graph-Prior Augmented Transformers
**arXiv**：[2512.10770v1](https://arxiv.org/abs/2512.10770) · [PDF](https://arxiv.org/pdf/2512.10770.pdf)  
**作者**：Youjun Zhao  

**一句话要点**：提出基于图先验增强Transformer的无模板逆合成方法，以提升有机合成预测的准确性和鲁棒性。

**关键词**：逆合成预测, 无模板方法, Transformer模型, 图先验增强, 数据增强, 有机合成

## 3 点简述
- 核心问题：逆合成反应预测旨在推断给定产物的可能反应物，是计算机辅助有机合成的关键挑战，现有模型在准确性和鲁棒性上不足。
- 方法要点：采用无模板Transformer框架，通过将分子图信息注入注意力机制，联合利用SMILES序列和结构线索，并应用配对数据增强策略提升训练多样性。
- 实验或效果：在USPTO-50K基准测试中，该方法在无模板方法中达到最优性能，显著优于基础Transformer基线。

## 摘要（原文）

> Retrosynthesis reaction prediction seeks to infer plausible reactant molecules for a given product and is a central problem in computer-aided organic synthesis. Despite recent progress, many existing models still fall short of the accuracy and robustness required for practical deployment. This work studies a template-free, Transformer-based framework that eliminates reliance on handcrafted reaction templates or additional chemical rule engines. The model injects molecular graph information into the attention mechanism to jointly exploit \SMILES\ sequences and structural cues, and further applies a paired data augmentation strategy to enhance training diversity and scale. On the USPTO-50K benchmark, our proposed approach achieves state-of-the-art performance among template-free methods and substantially outperforming a vanilla Transformer baseline.

