---
layout: default
title: Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation
---

# Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation
**arXiv**：[2601.21751v1](https://arxiv.org/abs/2601.21751) · [PDF](https://arxiv.org/pdf/2601.21751.pdf)  
**作者**：Jiankun Peng, Jianyuan Guo, Ying Xu, Yue Liu, Jiashuang Yan, Xuanwei Ye, Houhua Li, Xiaoming Wang  

**一句话要点**：提出DGNav框架以解决视觉语言导航中拓扑图粒度刚性问题

**关键词**：视觉语言导航, 拓扑图构建, 动态规划, 多模态融合, 连续环境导航, 自适应采样

## 3 点简述
- 核心问题：现有拓扑规划方法依赖固定阈值采样节点，导致在简单区域过采样、复杂区域欠采样，影响导航效率与安全。
- 方法要点：引入场景感知自适应策略动态调整图构建阈值，并设计动态图变换器融合多模态信息重构图连接性。
- 实验或效果：在R2R-CE和RxR-CE基准测试中表现优异，实现导航效率与安全探索的平衡，代码已开源。

## 摘要（原文）

> Vision-Language Navigation in Continuous Environments (VLN-CE) presents a core challenge: grounding high-level linguistic instructions into precise, safe, and long-horizon spatial actions. Explicit topological maps have proven to be a vital solution for providing robust spatial memory in such tasks. However, existing topological planning methods suffer from a "Granularity Rigidity" problem. Specifically, these methods typically rely on fixed geometric thresholds to sample nodes, which fails to adapt to varying environmental complexities. This rigidity leads to a critical mismatch: the model tends to over-sample in simple areas, causing computational redundancy, while under-sampling in high-uncertainty regions, increasing collision risks and compromising precision. To address this, we propose DGNav, a framework for Dynamic Topological Navigation, introducing a context-aware mechanism to modulate map density and connectivity on-the-fly. Our approach comprises two core innovations: (1) A Scene-Aware Adaptive Strategy that dynamically modulates graph construction thresholds based on the dispersion of predicted waypoints, enabling "densification on demand" in challenging environments; (2) A Dynamic Graph Transformer that reconstructs graph connectivity by fusing visual, linguistic, and geometric cues into dynamic edge weights, enabling the agent to filter out topological noise and enhancing instruction adherence. Extensive experiments on the R2R-CE and RxR-CE benchmarks demonstrate DGNav exhibits superior navigation performance and strong generalization capabilities. Furthermore, ablation studies confirm that our framework achieves an optimal trade-off between navigation efficiency and safe exploration. The code is available at https://github.com/shannanshouyin/DGNav.

