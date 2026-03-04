---
layout: default
title: Geometry-Guided Reinforcement Learning for Multi-view Consistent 3D Scene Editing
---

# Geometry-Guided Reinforcement Learning for Multi-view Consistent 3D Scene Editing
**arXiv**：[2603.03143v1](https://arxiv.org/abs/2603.03143) · [PDF](https://arxiv.org/pdf/2603.03143.pdf)  
**作者**：Jiyuan Wang, Chunyu Lin, Lei Sun, Zhi Cao, Yuyang Yin, Lang Nie, Zhenlong Yuan, Xiangxiang Chu, Yunchao Wei, Kang Liao, Guosheng Lin  

**一句话要点**：提出RL3DEdit框架，通过强化学习优化实现多视角一致的3D场景编辑。

**关键词**：3D场景编辑, 多视角一致性, 强化学习, 扩散模型, VGGT模型

## 3 点简述
- 核心问题：利用2D扩散模型先验进行3D编辑时，多视角一致性难以保持，且缺乏配对数据使监督微调不可行。
- 方法要点：基于3D基础模型VGGT设计奖励信号，通过强化学习将2D编辑先验锚定到3D一致流形上。
- 实验或效果：实验显示RL3DEdit在多视角一致性和编辑质量上优于现有方法，效率高。

## 摘要（原文）

> Leveraging the priors of 2D diffusion models for 3D editing has emerged as a promising paradigm. However, maintaining multi-view consistency in edited results remains challenging, and the extreme scarcity of 3D-consistent editing paired data renders supervised fine-tuning (SFT), the most effective training strategy for editing tasks, infeasible. In this paper, we observe that, while generating multi-view consistent 3D content is highly challenging, verifying 3D consistency is tractable, naturally positioning reinforcement learning (RL) as a feasible solution. Motivated by this, we propose \textbf{RL3DEdit}, a single-pass framework driven by RL optimization with novel rewards derived from the 3D foundation model, VGGT. Specifically, we leverage VGGT's robust priors learned from massive real-world data, feed the edited images, and utilize the output confidence maps and pose estimation errors as reward signals, effectively anchoring the 2D editing priors onto a 3D-consistent manifold via RL. Extensive experiments demonstrate that RL3DEdit achieves stable multi-view consistency and outperforms state-of-the-art methods in editing quality with high efficiency. To promote the development of 3D editing, we will release the code and model.

