---
layout: default
title: Exact Recovery of Non-Random Missing Multidimensional Time Series via Temporal Isometric Delay-Embedding Transform
---

# Exact Recovery of Non-Random Missing Multidimensional Time Series via Temporal Isometric Delay-Embedding Transform
**arXiv**：[2512.10191v1](https://arxiv.org/abs/2512.10191) · [PDF](https://arxiv.org/pdf/2512.10191.pdf)  
**作者**：Hao Shu, Jicheng Li, Yu Jin, Ling Zhou  

**一句话要点**：提出基于时间等距延迟嵌入变换的低秩张量补全模型，以解决多维时间序列非随机缺失数据的精确恢复问题。

**关键词**：多维时间序列, 非随机缺失数据, Hankel张量补全, 时间等距延迟嵌入变换, 低秩张量恢复, 精确恢复理论

## 3 点简述
- 核心问题：非随机缺失数据威胁多维时间序列分析的可靠性，现有方法在理论和实践上存在不足。
- 方法要点：引入时间等距延迟嵌入变换，构建Hankel张量，其低秩性源于时间序列的平滑性和周期性，结合t-SVD框架实现精确恢复。
- 实验或效果：在模拟和真实任务（如网络流量重建、交通估计）中验证了精确恢复，并优于现有张量方法。

## 摘要（原文）

> Non-random missing data is a ubiquitous yet undertreated flaw in multidimensional time series, fundamentally threatening the reliability of data-driven analysis and decision-making. Pure low-rank tensor completion, as a classical data recovery method, falls short in handling non-random missingness, both methodologically and theoretically. Hankel-structured tensor completion models provide a feasible approach for recovering multidimensional time series with non-random missing patterns. However, most Hankel-based multidimensional data recovery methods both suffer from unclear sources of Hankel tensor low-rankness and lack an exact recovery theory for non-random missing data. To address these issues, we propose the temporal isometric delay-embedding transform, which constructs a Hankel tensor whose low-rankness is naturally induced by the smoothness and periodicity of the underlying time series. Leveraging this property, we develop the \textit{Low-Rank Tensor Completion with Temporal Isometric Delay-embedding Transform} (LRTC-TIDT) model, which characterizes the low-rank structure under the \textit{Tensor Singular Value Decomposition} (t-SVD) framework. Once the prescribed non-random sampling conditions and mild incoherence assumptions are satisfied, the proposed LRTC-TIDT model achieves exact recovery, as confirmed by simulation experiments under various non-random missing patterns. Furthermore, LRTC-TIDT consistently outperforms existing tensor-based methods across multiple real-world tasks, including network flow reconstruction, urban traffic estimation, and temperature field prediction. Our implementation is publicly available at https://github.com/HaoShu2000/LRTC-TIDT.

