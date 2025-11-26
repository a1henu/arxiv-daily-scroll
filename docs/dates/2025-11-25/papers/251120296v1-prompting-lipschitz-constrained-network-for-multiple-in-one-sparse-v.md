---
layout: default
title: Prompting Lipschitz-constrained network for multiple-in-one sparse-view CT reconstruction
---

# Prompting Lipschitz-constrained network for multiple-in-one sparse-view CT reconstruction
**arXiv**：[2511.20296v1](https://arxiv.org/abs/2511.20296) · [PDF](https://arxiv.org/pdf/2511.20296.pdf)  
**作者**：Baoshun Shi, Ke Jiang, Qiusheng Lian, Xinran Yu, Huazhu Fu  

**一句话要点**：提出PromptCT框架以解决稀疏视图CT重建中的Lipschitz约束和存储成本问题

**关键词**：稀疏视图CT重建, Lipschitz约束网络, 深度展开框架, 提示学习, 多配置模型, 存储优化

## 3 点简述
- 核心问题：深度学习稀疏视图CT方法难以证明Lipschitz约束且多视图模型存储成本高
- 方法要点：集成LipNet网络确保Lipschitz连续性，并添加提示模块处理多配置
- 实验或效果：在模拟和真实数据中优于基准算法，实现高质量重建并降低存储

## 摘要（原文）

> Despite significant advancements in deep learning-based sparse-view computed tomography (SVCT) reconstruction algorithms, these methods still encounter two primary limitations: (i) It is challenging to explicitly prove that the prior networks of deep unfolding algorithms satisfy Lipschitz constraints due to their empirically designed nature. (ii) The substantial storage costs of training a separate model for each setting in the case of multiple views hinder practical clinical applications. To address these issues, we elaborate an explicitly provable Lipschitz-constrained network, dubbed LipNet, and integrate an explicit prompt module to provide discriminative knowledge of different sparse sampling settings, enabling the treatment of multiple sparse view configurations within a single model. Furthermore, we develop a storage-saving deep unfolding framework for multiple-in-one SVCT reconstruction, termed PromptCT, which embeds LipNet as its prior network to ensure the convergence of its corresponding iterative algorithm. In simulated and real data experiments, PromptCT outperforms benchmark reconstruction algorithms in multiple-in-one SVCT reconstruction, achieving higher-quality reconstructions with lower storage costs. On the theoretical side, we explicitly demonstrate that LipNet satisfies boundary property, further proving its Lipschitz continuity and subsequently analyzing the convergence of the proposed iterative algorithms. The data and code are publicly available at https://github.com/shibaoshun/PromptCT.

