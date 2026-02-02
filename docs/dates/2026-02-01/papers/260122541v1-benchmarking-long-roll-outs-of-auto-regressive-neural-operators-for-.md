---
layout: default
title: Benchmarking Long Roll-outs of Auto-regressive Neural Operators for the Compressible Navier-Stokes Equations with Conserved Quantity Correction
---

# Benchmarking Long Roll-outs of Auto-regressive Neural Operators for the Compressible Navier-Stokes Equations with Conserved Quantity Correction
**arXiv**：[2601.22541v1](https://arxiv.org/abs/2601.22541) · [PDF](https://arxiv.org/pdf/2601.22541.pdf)  
**作者**：Sean Current, Chandan Kumar, Datta Gaitonde, Srinivasan Parthasarathy  

**一句话要点**：提出守恒量校正技术以提升自回归神经算子在可压缩Navier-Stokes方程长期预测中的稳定性

**关键词**：守恒量校正, 自回归神经算子, 可压缩Navier-Stokes方程, 长期预测稳定性, 谱域分析, 湍流建模

## 3 点简述
- 自回归神经算子在长期预测中因误差累积和物理量不守恒而性能下降
- 引入模型无关的守恒量校正技术，强制模型满足物理守恒准则
- 实验显示该技术能一致提升长期稳定性，并揭示现有架构在高频分量上的局限性

## 摘要（原文）

> Deep learning has been proposed as an efficient alternative for the numerical approximation of PDE solutions, offering fast, iterative simulation of PDEs through the approximation of solution operators. However, deep learning solutions have struggle to perform well over long prediction durations due to the accumulation of auto-regressive error, which is compounded by the inability of models to conserve physical quantities. In this work, we present conserved quantity correction, a model-agnostic technique for incorporation physical conservation criteria within deep learning models. Our results demonstrate consistent improvement in the long-term stability of auto-regressive neural operator models, regardless of the model architecture. Furthermore, we analyze the performance of neural operators from the spectral domain, highlighting significant limitations of present architectures. These results highlight the need for future work to consider architectures that place specific emphasis on high frequency components, which are integral to the understanding and modeling of turbulent flows.

