---
layout: default
title: Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation
---

# Rethinking Diffusion Models with Symmetries through Canonicalization with Applications to Molecular Graph Generation
**arXiv**：[2602.15022v1](https://arxiv.org/abs/2602.15022) · [PDF](https://arxiv.org/pdf/2602.15022.pdf)  
**作者**：Cai Zhou, Zijie Chen, Zian Li, Jike Wang, Kaiyi Jiang, Pan Li, Rose Yu, Muhan Zhang, Stephen Bates, Tommi Jaakkola  

**一句话要点**：提出基于规范化的扩散模型框架，用于分子图生成等对称不变分布任务。

**关键词**：扩散模型, 分子图生成, 对称不变性, 规范化方法, 几何光谱, 最优传输

## 3 点简述
- 核心问题：化学和科学中生成任务常涉及群对称不变分布，传统方法通过架构约束实现不变性。
- 方法要点：采用规范化视角，先映射样本到规范表示，训练无约束扩散模型，再通过随机对称变换恢复分布。
- 实验或效果：在3D分子生成任务中显著优于等变基线，并在GEOM-DRUG数据集上达到先进性能。

## 摘要（原文）

> Many generative tasks in chemistry and science involve distributions invariant to group symmetries (e.g., permutation and rotation). A common strategy enforces invariance and equivariance through architectural constraints such as equivariant denoisers and invariant priors. In this paper, we challenge this tradition through the alternative canonicalization perspective: first map each sample to an orbit representative with a canonical pose or order, train an unconstrained (non-equivariant) diffusion or flow model on the canonical slice, and finally recover the invariant distribution by sampling a random symmetry transform at generation time. Building on a formal quotient-space perspective, our work provides a comprehensive theory of canonical diffusion by proving: (i) the correctness, universality and superior expressivity of canonical generative models over invariant targets; (ii) canonicalization accelerates training by removing diffusion score complexity induced by group mixtures and reducing conditional variance in flow matching. We then show that aligned priors and optimal transport act complementarily with canonicalization and further improves training efficiency. We instantiate the framework for molecular graph generation under $S_n \times SE(3)$ symmetries. By leveraging geometric spectra-based canonicalization and mild positional encodings, canonical diffusion significantly outperforms equivariant baselines in 3D molecule generation tasks, with similar or even less computation. Moreover, with a novel architecture Canon, CanonFlow achieves state-of-the-art performance on the challenging GEOM-DRUG dataset, and the advantage remains large in few-step generation.

