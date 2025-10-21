---
layout: default
title: CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference
---

# CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference
**arXiv**：[2510.17318v1](https://arxiv.org/abs/2510.17318) · [PDF](https://arxiv.org/pdf/2510.17318.pdf)  
**作者**：Sangyoon Bae, Jiook Cha  

**一句话要点**：提出CausalMamba框架以解决fMRI因果推断中的病态逆问题和计算难题

**关键词**：因果推断, 状态空间模型, fMRI分析, BOLD去卷积, 神经网络动态

## 3 点简述
- 核心问题：从血氧水平依赖信号推断神经因果性存在病态逆问题和计算不可行性
- 方法要点：将问题分解为BOLD去卷积和因果图推断，采用条件Mamba架构
- 实验或效果：在模拟数据上准确率比DCM高37%，真实数据中恢复已知神经通路达88%

## 摘要（原文）

> We introduce CausalMamba, a scalable framework that addresses fundamental
> limitations in fMRI-based causal inference: the ill-posed nature of inferring
> neural causality from hemodynamically distorted BOLD signals and the
> computational intractability of existing methods like Dynamic Causal Modeling
> (DCM). Our approach decomposes this complex inverse problem into two tractable
> stages: BOLD deconvolution to recover latent neural activity, followed by
> causal graph inference using a novel Conditional Mamba architecture. On
> simulated data, CausalMamba achieves 37% higher accuracy than DCM. Critically,
> when applied to real task fMRI data, our method recovers well-established
> neural pathways with 88% fidelity, whereas conventional approaches fail to
> identify these canonical circuits in over 99% of subjects. Furthermore, our
> network analysis of working memory data reveals that the brain strategically
> shifts its primary causal hub-recruiting executive or salience networks
> depending on the stimulus-a sophisticated reconfiguration that remains
> undetected by traditional methods. This work provides neuroscientists with a
> practical tool for large-scale causal inference that captures both fundamental
> circuit motifs and flexible network dynamics underlying cognitive function.

