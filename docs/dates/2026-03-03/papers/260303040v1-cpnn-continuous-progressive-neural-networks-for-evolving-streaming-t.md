---
layout: default
title: cPNN: Continuous Progressive Neural Networks for Evolving Streaming Time Series
---

# cPNN: Continuous Progressive Neural Networks for Evolving Streaming Time Series
**arXiv**：[2603.03040v1](https://arxiv.org/abs/2603.03040) · [PDF](https://arxiv.org/pdf/2603.03040.pdf)  
**作者**：Federico Giannini, Giacomo Ziffer, Emanuele Della Valle  

**一句话要点**：提出连续渐进神经网络以处理演化流式时间序列中的概念漂移、时间依赖和灾难性遗忘问题。

**关键词**：流式时间序列, 概念漂移, 渐进神经网络, 灾难性遗忘, 循环神经网络, 随机梯度下降

## 3 点简述
- 核心问题：流式数据存在时间依赖和概念漂移，现有方法缺乏联合解决方案，且需避免灾难性遗忘。
- 方法要点：基于循环神经网络和随机梯度下降，扩展渐进神经网络为连续版本，实现知识迁移和快速适应新概念。
- 实验或效果：消融研究显示cPNN能快速适应新概念，对漂移具有鲁棒性，有效处理时间依赖。

## 摘要（原文）

> Dealing with an unbounded data stream involves overcoming the assumption that data is identically distributed and independent. A data stream can, in fact, exhibit temporal dependencies (i.e., be a time series), and data can change distribution over time (concept drift). The two problems are deeply discussed, and existing solutions address them separately: a joint solution is absent. In addition, learning multiple concepts implies remembering the past (a.k.a. avoiding catastrophic forgetting in Neural Networks' terminology). This work proposes Continuous Progressive Neural Networks (cPNN), a solution that tames concept drifts, handles temporal dependencies, and bypasses catastrophic forgetting. cPNN is a continuous version of Progressive Neural Networks, a methodology for remembering old concepts and transferring past knowledge to fit the new concepts quickly. We base our method on Recurrent Neural Networks and exploit the Stochastic Gradient Descent applied to data streams with temporal dependencies. Results of an ablation study show a quick adaptation of cPNN to new concepts and robustness to drifts.

