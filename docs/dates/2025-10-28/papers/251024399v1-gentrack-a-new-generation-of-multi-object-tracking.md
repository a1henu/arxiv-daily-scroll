---
layout: default
title: GenTrack: A New Generation of Multi-Object Tracking
---

# GenTrack: A New Generation of Multi-Object Tracking
**arXiv**：[2510.24399v1](https://arxiv.org/abs/2510.24399) · [PDF](https://arxiv.org/pdf/2510.24399.pdf)  
**作者**：Toan Van Nguyen, Rasmus G. K. Christiansen, Dirk Kraft, Leon Bodenhagen  

**一句话要点**：提出GenTrack多目标跟踪方法，结合随机与确定性方式处理动态目标数。

**关键词**：多目标跟踪, 粒子群优化, 社交交互, ID一致性, 非线性动态

## 3 点简述
- 核心问题：处理未知和时变目标数，维持ID一致性和非线性动态。
- 方法要点：使用粒子群优化和社交交互，增强跟踪鲁棒性。
- 实验效果：在标准基准和真实场景中优于先进跟踪器。

## 摘要（原文）

> This paper introduces a novel multi-object tracking (MOT) method, dubbed
> GenTrack, whose main contributions include: a hybrid tracking approach
> employing both stochastic and deterministic manners to robustly handle unknown
> and time-varying numbers of targets, particularly in maintaining target
> identity (ID) consistency and managing nonlinear dynamics, leveraging particle
> swarm optimization (PSO) with some proposed fitness measures to guide
> stochastic particles toward their target distribution modes, enabling effective
> tracking even with weak and noisy object detectors, integration of social
> interactions among targets to enhance PSO-guided particles as well as improve
> continuous updates of both strong (matched) and weak (unmatched) tracks,
> thereby reducing ID switches and track loss, especially during occlusions, a
> GenTrack-based redefined visual MOT baseline incorporating a comprehensive
> state and observation model based on space consistency, appearance, detection
> confidence, track penalties, and social scores for systematic and efficient
> target updates, and the first-ever publicly available source-code reference
> implementation with minimal dependencies, featuring three variants, including
> GenTrack Basic, PSO, and PSO-Social, facilitating flexible reimplementation.
> Experimental results have shown that GenTrack provides superior performance on
> standard benchmarks and real-world scenarios compared to state-of-the-art
> trackers, with integrated implementations of baselines for fair comparison.
> Potential directions for future work are also discussed. The source-code
> reference implementations of both the proposed method and compared-trackers are
> provided on GitHub: https://github.com/SDU-VelKoTek/GenTrack

