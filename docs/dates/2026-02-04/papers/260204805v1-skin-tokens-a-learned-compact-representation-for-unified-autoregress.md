---
layout: default
title: Skin Tokens: A Learned Compact Representation for Unified Autoregressive Rigging
---

# Skin Tokens: A Learned Compact Representation for Unified Autoregressive Rigging
**arXiv**：[2602.04805v1](https://arxiv.org/abs/2602.04805) · [PDF](https://arxiv.org/pdf/2602.04805.pdf)  
**作者**：Jia-peng Zhang, Cheng-Feng Pu, Meng-Hao Guo, Yan-Pei Cao, Shi-Min Hu  

**一句话要点**：提出SkinTokens表示与TokenRig框架，以统一自回归方式解决3D模型绑定中的蒙皮与骨骼生成问题。

**关键词**：蒙皮权重表示, 自回归绑定, 强化学习优化, 3D动画生成, 序列预测模型

## 3 点简述
- 核心问题：现有自动绑定方法将蒙皮视为高维回归任务，效率低且与骨骼生成脱节。
- 方法要点：使用FSQ-CVAE学习紧凑离散的SkinTokens表示，将蒙皮重构为序列预测，并整合骨骼参数实现统一自回归建模。
- 实验或效果：SkinTokens提升蒙皮精度98%-133%，TokenRig结合强化学习增强骨骼预测17%-22%，提高泛化能力。

## 摘要（原文）

> The rapid proliferation of generative 3D models has created a critical bottleneck in animation pipelines: rigging. Existing automated methods are fundamentally limited by their approach to skinning, treating it as an ill-posed, high-dimensional regression task that is inefficient to optimize and is typically decoupled from skeleton generation. We posit this is a representation problem and introduce SkinTokens: a learned, compact, and discrete representation for skinning weights. By leveraging an FSQ-CVAE to capture the intrinsic sparsity of skinning, we reframe the task from continuous regression to a more tractable token sequence prediction problem. This representation enables TokenRig, a unified autoregressive framework that models the entire rig as a single sequence of skeletal parameters and SkinTokens, learning the complicated dependencies between skeletons and skin deformations. The unified model is then amenable to a reinforcement learning stage, where tailored geometric and semantic rewards improve generalization to complex, out-of-distribution assets. Quantitatively, the SkinTokens representation leads to a 98%-133% percents improvement in skinning accuracy over state-of-the-art methods, while the full TokenRig framework, refined with RL, enhances bone prediction by 17%-22%. Our work presents a unified, generative approach to rigging that yields higher fidelity and robustness, offering a scalable solution to a long-standing challenge in 3D content creation.

