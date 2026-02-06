---
layout: default
title: Robust Inference-Time Steering of Protein Diffusion Models via Embedding Optimization
---

# Robust Inference-Time Steering of Protein Diffusion Models via Embedding Optimization
**arXiv**：[2602.05285v1](https://arxiv.org/abs/2602.05285) · [PDF](https://arxiv.org/pdf/2602.05285.pdf)  
**作者**：Minhuan Li, Jiequn Han, Pilar Cossio, Luhuan Wu  

**一句话要点**：提出EmbedOpt以优化蛋白质扩散模型在推理时的条件嵌入空间，提升实验约束下的构象生成效果。

**关键词**：蛋白质扩散模型, 推理时引导, 条件嵌入优化, 实验约束, 构象生成, 生物物理逆问题

## 3 点简述
- 核心问题：后验采样在目标构象位于先验低密度区域时，需要脆弱的高权重似然引导。
- 方法要点：通过优化条件嵌入空间来调整扩散先验，以对齐实验约束，利用序列和共进化信号。
- 实验或效果：在冷冻电镜图拟合任务中优于坐标后验采样，距离约束任务性能相当，且超参数鲁棒性更强。

## 摘要（原文）

> In many biophysical inverse problems, the goal is to generate biomolecular conformations that are both physically plausible and consistent with experimental measurements. As recent sequence-to-structure diffusion models provide powerful data-driven priors, posterior sampling has emerged as a popular framework by guiding atomic coordinates to target conformations using experimental likelihoods. However, when the target lies in a low-density region of the prior, posterior sampling requires aggressive and brittle weighting of the likelihood guidance. Motivated by this limitation, we propose EmbedOpt, an alternative inference-time approach for steering diffusion models to optimize experimental likelihoods in the conditional embedding space. As this space encodes rich sequence and coevolutionary signals, optimizing over it effectively shifts the diffusion prior to align with experimental constraints. We validate EmbedOpt on two benchmarks simulating cryo-electron microscopy map fitting and experimental distance constraints. We show that EmbedOpt outperforms the coordinate-based posterior sampling method in map fitting tasks, matches performance on distance constraint tasks, and exhibits superior engineering robustness across hyperparameters spanning two orders of magnitude. Moreover, its smooth optimization behavior enables a significant reduction in the number of diffusion steps required for inference, leading to better efficiency.

