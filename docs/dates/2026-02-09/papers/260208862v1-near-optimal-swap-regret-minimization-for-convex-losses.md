---
layout: default
title: Near-optimal Swap Regret Minimization for Convex Losses
---

# Near-optimal Swap Regret Minimization for Convex Losses
**arXiv**：[2602.08862v1](https://arxiv.org/abs/2602.08862) · [PDF](https://arxiv.org/pdf/2602.08862.pdf)  
**作者**：Lunjia Hu, Jon Schneider, Yifan Wu  

**一句话要点**：提出多尺度分箱随机在线算法，实现凸损失下近最优交换遗憾最小化

**关键词**：在线学习, 交换遗憾最小化, 凸损失, 多尺度分箱, 校准误差, 随机算法

## 3 点简述
- 核心问题：在线学习中对自适应选择的Lipschitz凸损失最小化交换遗憾，改进现有上界
- 方法要点：将单位区间离散化为多粒度分箱，同时使用所有尺度进行随机预测
- 实验或效果：算法运行时间为多项式级，直接应用于一般可引出属性的校准误差最小化

## 摘要（原文）

> We give a randomized online algorithm that guarantees near-optimal $\widetilde O(\sqrt T)$ expected swap regret against any sequence of $T$ adaptively chosen Lipschitz convex losses on the unit interval. This improves the previous best bound of $\widetilde O(T^{2/3})$ and answers an open question of Fishelson et al. [2025b]. In addition, our algorithm is efficient: it runs in $\mathsf{poly}(T)$ time. A key technical idea we develop to obtain this result is to discretize the unit interval into bins at multiple scales of granularity and simultaneously use all scales to make randomized predictions, which we call multi-scale binning and may be of independent interest. A direct corollary of our result is an efficient online algorithm for minimizing the calibration error for general elicitable properties. This result does not require the Lipschitzness assumption of the identification function needed in prior work, making it applicable to median calibration, for which we achieve the first $\widetilde O(\sqrt T)$ calibration error guarantee.

