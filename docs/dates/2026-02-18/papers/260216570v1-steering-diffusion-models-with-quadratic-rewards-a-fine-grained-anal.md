---
layout: default
title: Steering diffusion models with quadratic rewards: a fine-grained analysis
---

# Steering diffusion models with quadratic rewards: a fine-grained analysis
**arXiv**：[2602.16570v1](https://arxiv.org/abs/2602.16570) · [PDF](https://arxiv.org/pdf/2602.16570.pdf)  
**作者**：Ankur Moitra, Andrej Risteski, Dhruv Rohatgi  

**一句话要点**：分析二次奖励下扩散模型采样的计算可处理性，提出高效算法与难解性证明。

**关键词**：扩散模型, 奖励倾斜采样, 计算复杂性, 二次奖励, Hubbard-Stratonovich变换, 推理时算法

## 3 点简述
- 研究从奖励倾斜扩散模型采样的计算问题，聚焦二次奖励函数。
- 证明线性奖励可高效采样，并利用Hubbard-Stratonovich变换处理低秩正定二次奖励。
- 证明负定二次奖励在秩1时难解，即使输入指数级大。

## 摘要（原文）

> Inference-time algorithms are an emerging paradigm in which pre-trained models are used as subroutines to solve downstream tasks. Such algorithms have been proposed for tasks ranging from inverse problems and guided image generation to reasoning. However, the methods currently deployed in practice are heuristics with a variety of failure modes -- and we have very little understanding of when these heuristics can be efficiently improved.
>   In this paper, we consider the task of sampling from a reward-tilted diffusion model -- that is, sampling from $p^{\star}(x) \propto p(x) \exp(r(x))$ -- given a reward function $r$ and pre-trained diffusion oracle for $p$. We provide a fine-grained analysis of the computational tractability of this task for quadratic rewards $r(x) = x^\top A x + b^\top x$. We show that linear-reward tilts are always efficiently sampleable -- a simple result that seems to have gone unnoticed in the literature. We use this as a building block, along with a conceptually new ingredient -- the Hubbard-Stratonovich transform -- to provide an efficient algorithm for sampling from low-rank positive-definite quadratic tilts, i.e. $r(x) = x^\top A x$ where $A$ is positive-definite and of rank $O(1)$. For negative-definite tilts, i.e. $r(x) = - x^\top A x$ where $A$ is positive-definite, we prove that the problem is intractable even if $A$ is of rank 1 (albeit with exponentially-large entries).

