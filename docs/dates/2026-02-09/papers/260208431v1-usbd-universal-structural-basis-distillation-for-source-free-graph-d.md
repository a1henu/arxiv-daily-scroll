---
layout: default
title: USBD: Universal Structural Basis Distillation for Source-Free Graph Domain Adaptation
---

# USBD: Universal Structural Basis Distillation for Source-Free Graph Domain Adaptation
**arXiv**：[2602.08431v1](https://arxiv.org/abs/2602.08431) · [PDF](https://arxiv.org/pdf/2602.08431.pdf)  
**作者**：Yingxu Wang, Kunyu Zhang, Mengzhu Wang, Siyang Gao, Nan Yin  

**一句话要点**：提出通用结构基蒸馏框架，以解决源自由图域适应中结构偏移导致的泛化瓶颈。

**关键词**：源自由图域适应, 结构基蒸馏, 拓扑模式覆盖, 谱感知集成, 双层优化, 计算效率

## 3 点简述
- 核心问题：源自由图域适应中，源模型对结构平滑性先验的依赖限制了在拓扑显著变化目标上的泛化能力。
- 方法要点：通过双层优化蒸馏源数据集为紧凑结构基，覆盖全谱拓扑模式，并基于目标图谱指纹动态激活原型组合。
- 实验或效果：在基准测试中显著优于现有方法，尤其在结构偏移严重场景下，同时实现计算高效性。

## 摘要（原文）

> SF-GDA is pivotal for privacy-preserving knowledge transfer across graph datasets. Although recent works incorporate structural information, they implicitly condition adaptation on the smoothness priors of sourcetrained GNNs, thereby limiting their generalization to structurally distinct targets. This dependency becomes a critical bottleneck under significant topological shifts, where the source model misinterprets distinct topological patterns unseen in the source domain as noise, rendering pseudo-label-based adaptation unreliable. To overcome this limitation, we propose the Universal Structural Basis Distillation, a framework that shifts the paradigm from adapting a biased model to learning a universal structural basis for SF-GDA. Instead of adapting a biased source model to a specific target, our core idea is to construct a structure-agnostic basis that proactively covers the full spectrum of potential topological patterns. Specifically, USBD employs a bi-level optimization framework to distill the source dataset into a compact structural basis. By enforcing the prototypes to span the full Dirichlet energy spectrum, the learned basis explicitly captures diverse topological motifs, ranging from low-frequency clusters to high-frequency chains, beyond those present in the source. This ensures that the learned basis creates a comprehensive structural covering capable of handling targets with disparate structures. For inference, we introduce a spectral-aware ensemble mechanism that dynamically activates the optimal prototype combination based on the spectral fingerprint of the target graph. Extensive experiments on benchmarks demonstrate that USBD significantly outperforms state-of-the-art methods, particularly in scenarios with severe structural shifts, while achieving superior computational efficiency by decoupling the adaptation cost from the target data scale.

