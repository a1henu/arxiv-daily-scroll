---
layout: default
title: A Model of Artificial Jagged Intelligence
---

# A Model of Artificial Jagged Intelligence
**arXiv**：[2601.07573v1](https://arxiv.org/abs/2601.07573) · [PDF](https://arxiv.org/pdf/2601.07573.pdf)  
**作者**：Joshua Gans  

**一句话要点**：提出人工锯齿智能的经济模型，以信息问题解释生成式AI在邻近任务中的性能不均现象。

**关键词**：人工锯齿智能, 经济模型, 信息问题, 本地可靠性, 缩放定律, 高斯过程回归

## 3 点简述
- 核心问题：生成式AI在微小变化下性能不均，用户仅观察全局质量信号，导致本地可靠性评估困难。
- 方法要点：基于一维布朗过程构建模型，通过最优插值和后验方差量化本地误差，推导盲用户采用阈值。
- 实验或效果：分析校准用户如何利用本地不确定性获得正期望值，并探讨缩放定律与可发现性的交互作用。

## 摘要（原文）

> Generative AI systems often display highly uneven performance across tasks that appear ``nearby'': they can be excellent on one prompt and confidently wrong on another with only small changes in wording or context. We call this phenomenon Artificial Jagged Intelligence (AJI). This paper develops a tractable economic model of AJI that treats adoption as an information problem: users care about \emph{local} reliability, but typically observe only coarse, global quality signals. In a baseline one-dimensional landscape, truth is a rough Brownian process, and the model ``knows'' scattered points drawn from a Poisson process. The model interpolates optimally, and the local error is measured by posterior variance. We derive an adoption threshold for a blind user, show that experienced errors are amplified by the inspection paradox, and interpret scaling laws as denser coverage that improves average quality without eliminating jaggedness. We then study mastery and calibration: a calibrated user who can condition on local uncertainty enjoys positive expected value even in domains that fail the blind adoption test. Modelling mastery as learning a reliability map via Gaussian process regression yields a learning-rate bound driven by information gain, clarifying when discovering ``where the model works'' is slow. Finally, we study how scaling interacts with discoverability: when calibrated signals and user mastery accelerate the harvesting of scale improvements, and when opacity can make gains from scaling effectively invisible.

