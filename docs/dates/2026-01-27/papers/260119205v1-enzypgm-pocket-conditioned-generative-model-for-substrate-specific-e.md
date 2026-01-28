---
layout: default
title: EnzyPGM: Pocket-conditioned Generative Model for Substrate-specific Enzyme Design
---

# EnzyPGM: Pocket-conditioned Generative Model for Substrate-specific Enzyme Design
**arXiv**：[2601.19205v1](https://arxiv.org/abs/2601.19205) · [PDF](https://arxiv.org/pdf/2601.19205.pdf)  
**作者**：Zefeng Lin, Zhihang Zhang, Weirong Zhu, Tongchang Han, Xianyong Fang, Tianfan Fu, Xiaohua Xu  

**一句话要点**：提出EnzyPGM以解决酶设计中口袋-底物交互建模的挑战

**关键词**：酶设计, 口袋-底物交互, 生成模型, 蛋白质工程, 数据集构建

## 3 点简述
- 核心问题：现有生成模型无法建模口袋-底物交互，限制酶催化环境设计。
- 方法要点：引入RBA模块联合建模口袋残基与底物原子交互，RFF模块融合功能先验。
- 实验或效果：在EnzyPock数据集上实现SOTA，平均结合能降低0.47 kcal/mol。

## 摘要（原文）

> Designing enzymes with substrate-binding pockets is a critical challenge in protein engineering, as catalytic activity depends on the precise interaction between pockets and substrates. Currently, generative models dominate functional protein design but cannot model pocket-substrate interactions, which limits the generation of enzymes with precise catalytic environments. To address this issue, we propose EnzyPGM, a unified framework that jointly generates enzymes and substrate-binding pockets conditioned on functional priors and substrates, with a particular focus on learning accurate pocket-substrate interactions. At its core, EnzyPGM includes two main modules: a Residue-atom Bi-scale Attention (RBA) that jointly models intra-residue dependencies and fine-grained interactions between pocket residues and substrate atoms, and a Residue Function Fusion (RFF) that incorporates enzyme function priors into residue representations. Also, we curate EnzyPock, an enzyme-pocket dataset comprising 83,062 enzyme-substrate pairs across 1,036 four-level enzyme families. Extensive experiments demonstrate that EnzyPGM achieves state-of-the-art performance on EnzyPock. Notably, EnzyPGM reduces the average binding energy of 0.47 kcal/mol over EnzyGen, showing its superior performance on substrate-specific enzyme design. The code and dataset will be released later.

