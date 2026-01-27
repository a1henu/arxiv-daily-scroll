---
layout: default
title: LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts
---

# LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts
**arXiv**：[2601.18089v1](https://arxiv.org/abs/2601.18089) · [PDF](https://arxiv.org/pdf/2601.18089.pdf)  
**作者**：Venmugil Elango, Nidhi Bhatia, Roger Waleffe, Rasoul Shafipour, Tomer Asida, Abhinav Khattar, Nave Assaf, Maximilian Golub, Joey Guman, Tiyasa Mitra, Ritchie Zhao, Ritika Borkar, Ran Zilberstein, Mostofa Patwary, Mohammad Shoeybi, Bita Rouhani  

**一句话要点**：提出LatentMoE架构以优化混合专家模型的每FLOP和每参数准确率

**关键词**：混合专家模型, 软硬件协同设计, 推理优化, 大规模训练, 模型架构探索, 计算效率

## 3 点简述
- 核心问题：现有MoE架构在推理成本（每FLOP和每参数准确率）方面是否接近最优未知
- 方法要点：从软硬件协同设计角度，通过经验与理论分析，系统探索设计空间并引入LatentMoE
- 实验或效果：在高达950亿参数和超1万亿令牌训练规模下，LatentMoE在每FLOP和每参数准确率上优于标准MoE

## 摘要（原文）

> Mixture of Experts (MoEs) have become a central component of many state-of-the-art open-source and proprietary large language models. Despite their widespread adoption, it remains unclear how close existing MoE architectures are to optimal with respect to inference cost, as measured by accuracy per floating-point operation and per parameter. In this work, we revisit MoE design from a hardware-software co-design perspective, grounded in empirical and theoretical considerations. We characterize key performance bottlenecks across diverse deployment regimes, spanning offline high-throughput execution and online, latency-critical inference. Guided by these insights, we introduce LatentMoE, a new model architecture resulting from systematic design exploration and optimized for maximal accuracy per unit of compute. Empirical design space exploration at scales of up to 95B parameters and over a 1T-token training horizon, together with supporting theoretical analysis, shows that LatentMoE consistently outperforms standard MoE architectures in terms of accuracy per FLOP and per parameter. Given its strong performance, the LatentMoE architecture has been adopted by the flagship Nemotron-3 Super and Ultra models and scaled to substantially larger regimes, including longer token horizons and larger model sizes, as reported in Nvidia et al. (arXiv:2512.20856).

