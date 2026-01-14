---
layout: default
title: RMBRec: Robust Multi-Behavior Recommendation towards Target Behaviors
---

# RMBRec: Robust Multi-Behavior Recommendation towards Target Behaviors
**arXiv**：[2601.08705v1](https://arxiv.org/abs/2601.08705) · [PDF](https://arxiv.org/pdf/2601.08705.pdf)  
**作者**：Miaomiao Cai, Zhijie Zhang, Junfeng Fang, Zhiyong Cheng, Xiang Wang, Meng Wang  

**一句话要点**：提出RMBRec框架，通过信息论原则增强多行为推荐对目标行为的鲁棒性。

**关键词**：多行为推荐, 鲁棒性学习, 信息论优化, 表示学习, 风险最小化

## 3 点简述
- 核心问题：辅助行为（如点击）与目标行为（如购买）不一致导致推荐偏差。
- 方法要点：结合局部语义一致性与全局风险方差最小化，提升鲁棒性。
- 实验或效果：在三个真实数据集上优于现有方法，且对噪声扰动保持稳定。

## 摘要（原文）

> Multi-behavior recommendation faces a critical challenge in practice: auxiliary behaviors (e.g., clicks, carts) are often noisy, weakly correlated, or semantically misaligned with the target behavior (e.g., purchase), which leads to biased preference learning and suboptimal performance. While existing methods attempt to fuse these heterogeneous signals, they inherently lack a principled mechanism to ensure robustness against such behavioral inconsistency.
>   In this work, we propose Robust Multi-Behavior Recommendation towards Target Behaviors (RMBRec), a robust multi-behavior recommendation framework grounded in an information-theoretic robustness principle. We interpret robustness as a joint process of maximizing predictive information while minimizing its variance across heterogeneous behavioral environments. Under this perspective, the Representation Robustness Module (RRM) enhances local semantic consistency by maximizing the mutual information between users' auxiliary and target representations, whereas the Optimization Robustness Module (ORM) enforces global stability by minimizing the variance of predictive risks across behaviors, which is an efficient approximation to invariant risk minimization. This local-global collaboration bridges representation purification and optimization invariance in a theoretically coherent way. Extensive experiments on three real-world datasets demonstrate that RMBRec not only outperforms state-of-the-art methods in accuracy but also maintains remarkable stability under various noise perturbations. For reproducibility, our code is available at https://github.com/miaomiao-cai2/RMBRec/.

