---
layout: default
title: The Effect of Architecture During Continual Learning
---

# The Effect of Architecture During Continual Learning
**arXiv**：[2601.19766v1](https://arxiv.org/abs/2601.19766) · [PDF](https://arxiv.org/pdf/2601.19766.pdf)  
**作者**：Allyson Hahn, Krishnan Raghavan  

**一句话要点**：提出联合优化架构与权重的双层优化框架，以缓解持续学习中的灾难性遗忘。

**关键词**：持续学习, 架构优化, 灾难性遗忘, 双层优化, 低秩转移

## 3 点简述
- 核心问题：静态架构模型在数据分布变化时难以适应，导致灾难性遗忘。
- 方法要点：在Sobolev空间中建模架构与权重，通过双层优化和低秩转移机制实现联合学习。
- 实验或效果：在回归和分类任务中，性能提升达两个数量级，遗忘减少且鲁棒性增强。

## 摘要（原文）

> Continual learning is a challenge for models with static architecture, as they fail to adapt to when data distributions evolve across tasks. We introduce a mathematical framework that jointly models architecture and weights in a Sobolev space, enabling a rigorous investigation into the role of neural network architecture in continual learning and its effect on the forgetting loss. We derive necessary conditions for the continual learning solution and prove that learning only model weights is insufficient to mitigate catastrophic forgetting under distribution shifts. Consequently, we prove that by learning the architecture and weights simultaneously at each task, we can reduce catastrophic forgetting.
>   To learn weights and architecture simultaneously, we formulate continual learning as a bilevel optimization problem: the upper level selects an optimal architecture for a given task, while the lower level computes optimal weights via dynamic programming over all tasks. To solve the upper level problem, we introduce a derivative-free direct search algorithm to determine the optimal architecture. Once found, we must transfer knowledge from the current architecture to the optimal one. However, the optimal architecture will result in a weights parameter space different from the current architecture (i.e., dimensions of weights matrices will not match). To bridge the dimensionality gap, we develop a low-rank transfer mechanism to map knowledge across architectures of mismatched dimensions. Empirical studies across regression and classification problems, including feedforward, convolutional, and graph neural networks, demonstrate that learning the optimal architecture and weights simultaneously yields substantially improved performance (up to two orders of magnitude), reduced forgetting, and enhanced robustness to noise compared with static architecture approaches.

