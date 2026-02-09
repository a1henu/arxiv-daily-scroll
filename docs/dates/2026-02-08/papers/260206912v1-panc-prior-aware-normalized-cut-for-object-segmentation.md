---
layout: default
title: PANC: Prior-Aware Normalized Cut for Object Segmentation
---

# PANC: Prior-Aware Normalized Cut for Object Segmentation
**arXiv**：[2602.06912v1](https://arxiv.org/abs/2602.06912) · [PDF](https://arxiv.org/pdf/2602.06912.pdf)  
**作者**：Juan Gutiérrez, Victor Gutiérrez-Garcia, José Luis Blanco-Murillo  

**一句话要点**：提出PANC弱监督谱分割框架，利用少量标注视觉标记提升对象分割的稳定性和可控性。

**关键词**：弱监督分割, 谱分割, 图拓扑优化, 视觉标记, 对象分割, 先验引导

## 3 点简述
- 核心问题：无监督分割方法对初始化敏感，产生非确定性分割结果。
- 方法要点：通过标注先验增强图拓扑，引导谱特征空间生成与标注一致的分割。
- 实验或效果：在多个基准数据集上实现SotA性能，尤其在细粒度或纹理有限领域表现优异。

## 摘要（原文）

> Fully unsupervised segmentation pipelines naively seek the most salient object, should this be present. As a result, most of the methods reported in the literature deliver non-deterministic partitions that are sensitive to initialization, seed order, and threshold heuristics.
>   We propose PANC, a weakly supervised spectral segmentation framework that uses a minimal set of annotated visual tokens to produce stable, controllable, and reproducible object masks. From the TokenCut approach, we augment the token-token affinity graph with a handful of priors coupled to anchor nodes. By manipulating the graph topology, we bias the spectral eigenspace toward partitions that are consistent with the annotations. Our approach preserves the global grouping enforced by dense self-supervised visual features, trading annotated tokens for significant gains in reproducibility, user control, and segmentation quality.
>   Using 5 to 30 annotations per dataset, our training-free method achieves state-of-the-art performance among weakly and unsupervised approaches on standard benchmarks (e.g., DUTS-TE, ECSSD, MS COCO). Contrarily, it excels in domains where dense labels are costly or intra-class differences are subtle. We report strong and reliable results on homogeneous, fine-grained, and texture-limited domains, achieving 96.8% (+14.43% over SotA), 78.0% (+0.2%), and 78.8% (+0.37%) average mean intersection-over-union (mIoU) on CrackForest (CFD), CUB-200-2011, and HAM10000 datasets, respectively. For multi-object benchmarks, the framework showcases explicit, user-controllable semantic segmentation.

