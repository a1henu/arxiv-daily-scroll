---
layout: default
title: Crowdsourcing the Frontier: Advancing Hybrid Physics-ML Climate Simulation via $50,000 Kaggle Competition
---

# Crowdsourcing the Frontier: Advancing Hybrid Physics-ML Climate Simulation via $50,000 Kaggle Competition
**arXiv**：[2511.20963v1](https://arxiv.org/abs/2511.20963) · [PDF](https://arxiv.org/pdf/2511.20963.pdf)  
**作者**：Jerry Lin, Zeyuan Hu, Tom Beucler, Katherine Frields, Hannah Christensen, Walter Hannah, Helge Heuer, Peter Ukkonnen, Laura A. Mansfield, Tian Zheng, Liran Peng, Ritwik Gupta, Pierre Gentine, Yusef Al-Naher, Mingjiang Duan, Kyo Hattori, Weiliang Ji, Chunhan Li, Kippei Matsuda, Naoki Murakami, Shlomo Ron, Marec Serlin, Hongjian Song, Yuma Tanabe, Daisuke Yamamoto, Jianyao Zhou, Mike Pritchard  

**一句话要点**：通过Kaggle竞赛推进混合物理-ML气候模拟，实现在线稳定性与SOTA性能

**关键词**：气候模拟, 机器学习参数化, 在线稳定性, Kaggle竞赛, 子网格建模, 混合物理-AI模型

## 3 点简述
- 核心问题：子网格ML参数化存在在线不稳定性和性能不一致，阻碍长期气候预测应用。
- 方法要点：发布ClimSim数据集并举办Kaggle竞赛，耦合获胜架构到交互式气候模型进行测试。
- 实验或效果：多架构实现在线稳定性，部分在特定指标上达到SOTA，显示众包可提升在线性能。

## 摘要（原文）

> Subgrid machine-learning (ML) parameterizations have the potential to introduce a new generation of climate models that incorporate the effects of higher-resolution physics without incurring the prohibitive computational cost associated with more explicit physics-based simulations. However, important issues, ranging from online instability to inconsistent online performance, have limited their operational use for long-term climate projections. To more rapidly drive progress in solving these issues, domain scientists and machine learning researchers opened up the offline aspect of this problem to the broader machine learning and data science community with the release of ClimSim, a NeurIPS Datasets and Benchmarks publication, and an associated Kaggle competition. This paper reports on the downstream results of the Kaggle competition by coupling emulators inspired by the winning teams' architectures to an interactive climate model (including full cloud microphysics, a regime historically prone to online instability) and systematically evaluating their online performance. Our results demonstrate that online stability in the low-resolution, real-geography setting is reproducible across multiple diverse architectures, which we consider a key milestone. All tested architectures exhibit strikingly similar offline and online biases, though their responses to architecture-agnostic design choices (e.g., expanding the list of input variables) can differ significantly. Multiple Kaggle-inspired architectures achieve state-of-the-art (SOTA) results on certain metrics such as zonal mean bias patterns and global RMSE, indicating that crowdsourcing the essence of the offline problem is one path to improving online performance in hybrid physics-AI climate simulation.

