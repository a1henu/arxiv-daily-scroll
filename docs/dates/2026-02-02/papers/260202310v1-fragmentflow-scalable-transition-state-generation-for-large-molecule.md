---
layout: default
title: FragmentFlow: Scalable Transition State Generation for Large Molecules
---

# FragmentFlow: Scalable Transition State Generation for Large Molecules
**arXiv**：[2602.02310v1](https://arxiv.org/abs/2602.02310) · [PDF](https://arxiv.org/pdf/2602.02310.pdf)  
**作者**：Ron Shprints, Peter Holderrieth, Juno Nam, Rafael Gómez-Bombarelli, Tommi Jaakkola  

**一句话要点**：提出FragmentFlow以解决大分子过渡态生成中的分布偏移问题

**关键词**：过渡态生成, 生成模型, 大分子反应, 分布偏移, 分治策略, 反应核心

## 3 点简述
- 核心问题：传统方法计算成本高，现有生成模型因分子尺寸增大导致分布偏移，无法泛化到大分子。
- 方法要点：采用分治策略，训练生成模型预测反应核心原子的过渡态几何结构，再重新连接取代基片段。
- 实验或效果：在含多达33个重原子的反应数据集上，正确识别90%过渡态，比经典初始化方案减少30%鞍点优化步骤。

## 摘要（原文）

> Transition states (TSs) are central to understanding and quantitatively predicting chemical reactivity and reaction mechanisms. Although traditional TS generation methods are computationally expensive, recent generative modeling approaches have enabled chemically meaningful TS prediction for relatively small molecules. However, these methods fail to generalize to practically relevant reaction substrates because of distribution shifts induced by increasing molecular sizes. Furthermore, TS geometries for larger molecules are not available at scale, making it infeasible to train generative models from scratch on such molecules. To address these challenges, we introduce FragmentFlow: a divide-and-conquer approach that trains a generative model to predict TS geometries for the reactive core atoms, which define the reaction mechanism. The full TS structure is then reconstructed by re-attaching substituent fragments to the predicted core. By operating on reactive cores, whose size and composition remain relatively invariant across molecular contexts, FragmentFlow mitigates distribution shifts in generative modeling. Evaluated on a new curated dataset of reactions involving reactants with up to 33 heavy atoms, FragmentFlow correctly identifies 90% of TSs while requiring 30% fewer saddle-point optimization steps than classical initialization schemes. These results point toward scalable TS generation for high-throughput reactivity studies.

