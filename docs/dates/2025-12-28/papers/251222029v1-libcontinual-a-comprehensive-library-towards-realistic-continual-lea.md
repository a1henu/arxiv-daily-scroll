---
layout: default
title: LibContinual: A Comprehensive Library towards Realistic Continual Learning
---

# LibContinual: A Comprehensive Library towards Realistic Continual Learning
**arXiv**：[2512.22029v1](https://arxiv.org/abs/2512.22029) · [PDF](https://arxiv.org/pdf/2512.22029.pdf)  
**作者**：Wenbin Li, Shangge Liu, Borui Kang, Yiyang Chen, KaXuan Lew, Yang Chen, Yinghuan Shi, Lei Wang, Yang Gao, Jiebo Luo  

**一句话要点**：提出LibContinual库以解决持续学习中评估不一致和现实适用性问题

**关键词**：持续学习, 灾难性遗忘, 开源库, 评估协议, 内存预算, 在线学习

## 3 点简述
- 核心问题：持续学习领域方法多样但缺乏统一框架，导致公平比较和可复现研究困难
- 方法要点：构建高内聚低耦合的模块化库，集成19种代表性算法，提供标准化执行环境
- 实验或效果：通过严格在线设置、统一内存预算和类别随机化，揭示主流方法在现实约束下性能显著下降

## 摘要（原文）

> A fundamental challenge in Continual Learning (CL) is catastrophic forgetting, where adapting to new tasks degrades the performance on previous ones. While the field has evolved with diverse methods, this rapid surge in diverse methodologies has culminated in a fragmented research landscape. The lack of a unified framework, including inconsistent implementations, conflicting dependencies, and varying evaluation protocols, makes fair comparison and reproducible research increasingly difficult. To address this challenge, we propose LibContinual, a comprehensive and reproducible library designed to serve as a foundational platform for realistic CL. Built upon a high-cohesion, low-coupling modular architecture, LibContinual integrates 19 representative algorithms across five major methodological categories, providing a standardized execution environment. Meanwhile, leveraging this unified framework, we systematically identify and investigate three implicit assumptions prevalent in mainstream evaluation: (1) offline data accessibility, (2) unregulated memory resources, and (3) intra-task semantic homogeneity. We argue that these assumptions often overestimate the real-world applicability of CL methods. Through our comprehensive analysis using strict online CL settings, a novel unified memory budget protocol, and a proposed category-randomized setting, we reveal significant performance drops in many representative CL methods when subjected to these real-world constraints. Our study underscores the necessity of resource-aware and semantically robust CL strategies, and offers LibContinual as a foundational toolkit for future research in realistic continual learning. The source code is available from \href{https://github.com/RL-VIG/LibContinual}{https://github.com/RL-VIG/LibContinual}.

