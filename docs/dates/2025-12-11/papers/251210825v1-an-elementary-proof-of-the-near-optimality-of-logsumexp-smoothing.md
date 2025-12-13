---
layout: default
title: An Elementary Proof of the Near Optimality of LogSumExp Smoothing
---

# An Elementary Proof of the Near Optimality of LogSumExp Smoothing
**arXiv**：[2512.10825v1](https://arxiv.org/abs/2512.10825) · [PDF](https://arxiv.org/pdf/2512.10825.pdf)  
**作者**：Thabo Samakhoana, Benjamin Grimmer  

**一句话要点**：提出LogSumExp平滑在无穷范数下近似最优性的初等证明与精确最优平滑构造

**关键词**：函数平滑, LogSumExp, 无穷范数, 近似最优性, 初等证明, 下界构造

## 3 点简述
- 研究在ℝ^d无穷范数下坐标最大函数的平滑设计问题
- 通过初等方法证明LogSumExp平滑与最大函数差值上界为ln(d)，下界约0.8145ln(d)，确立其近似最优性
- 在小维度构造精确最优平滑，显示LogSumExp方法非精确最优

## 摘要（原文）

> We consider the design of smoothings of the (coordinate-wise) max function in $\mathbb{R}^d$ in the infinity norm. The LogSumExp function $f(x)=\ln(\sum^d_i\exp(x_i))$ provides a classical smoothing, differing from the max function in value by at most $\ln(d)$. We provide an elementary construction of a lower bound, establishing that every overestimating smoothing of the max function must differ by at least $\sim 0.8145\ln(d)$. Hence, LogSumExp is optimal up to constant factors. However, in small dimensions, we provide stronger, exactly optimal smoothings attaining our lower bound, showing that the entropy-based LogSumExp approach to smoothing is not exactly optimal.

