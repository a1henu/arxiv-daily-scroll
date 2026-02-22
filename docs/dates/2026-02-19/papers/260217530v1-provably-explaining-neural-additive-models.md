---
layout: default
title: Provably Explaining Neural Additive Models
---

# Provably Explaining Neural Additive Models
**arXiv**：[2602.17530v1](https://arxiv.org/abs/2602.17530) · [PDF](https://arxiv.org/pdf/2602.17530.pdf)  
**作者**：Shahaf Bassan, Yizhak Yisrael Elboher, Tobias Ladner, Volkan Şahin, Jan Kretinsky, Matthias Althoff, Guy Katz  

**一句话要点**：提出高效算法为神经加法模型生成可证明最小基数解释，解决解释性神经网络缺乏可证明保证的问题。

**关键词**：神经加法模型, 可证明解释, 最小基数子集, 后验解释方法, 计算效率

## 3 点简述
- 核心问题：现有神经网络后验解释方法多为启发式，缺乏可证明保证，且标准神经网络中寻找最小特征子集计算不可行。
- 方法要点：针对神经加法模型，设计新算法，通过并行预处理和验证查询，高效生成可证明最小基数解释。
- 实验或效果：实验显示，相比现有算法，本方法提供更小解释并大幅减少计算时间，优于采样技术。

## 摘要（原文）

> Despite significant progress in post-hoc explanation methods for neural networks, many remain heuristic and lack provable guarantees. A key approach for obtaining explanations with provable guarantees is by identifying a cardinally-minimal subset of input features which by itself is provably sufficient to determine the prediction. However, for standard neural networks, this task is often computationally infeasible, as it demands a worst-case exponential number of verification queries in the number of input features, each of which is NP-hard.
>   In this work, we show that for Neural Additive Models (NAMs), a recent and more interpretable neural network family, we can efficiently generate explanations with such guarantees. We present a new model-specific algorithm for NAMs that generates provably cardinally-minimal explanations using only a logarithmic number of verification queries
>   in the number of input features, after a parallelized preprocessing step with logarithmic runtime in the required precision is applied to each small univariate NAM component.
>   Our algorithm not only makes the task of obtaining cardinally-minimal explanations feasible, but even outperforms existing algorithms designed to find the relaxed variant of subset-minimal explanations - which may be larger and less informative but easier to compute - despite our algorithm solving a much more difficult task.
>   Our experiments demonstrate that, compared to previous algorithms, our approach provides provably smaller explanations than existing works and substantially reduces the computation time. Moreover, we show that our generated provable explanations offer benefits that are unattainable by standard sampling-based techniques typically used to interpret NAMs.

