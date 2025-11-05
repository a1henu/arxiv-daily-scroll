---
layout: default
title: Can Visual Input Be Compressed? A Visual Token Compression Benchmark for Large Multimodal Models
---

# Can Visual Input Be Compressed? A Visual Token Compression Benchmark for Large Multimodal Models
**arXiv**：[2511.02650v1](https://arxiv.org/abs/2511.02650) · [PDF](https://arxiv.org/pdf/2511.02650.pdf)  
**作者**：Tianfan Peng, Yuntao Du, Pengzhou Ji, Shijie Dong, Kailin Jiang, Mingchuan Ma, Yijun Tian, Jinhe Bi, Qian Li, Wei Du, Feng Xiao, Lizhen Cui  

**一句话要点**：提出UniPruneBench基准以评估大型多模态模型中的视觉令牌压缩方法

**关键词**：视觉令牌压缩, 多模态模型基准, 剪枝算法, 推理效率, OCR任务敏感性

## 3 点简述
- 核心问题：大型多模态模型因视觉令牌过多导致推理效率低下，现有压缩方法评估不一致。
- 方法要点：构建统一基准，涵盖六能力维度、十数据集、十压缩算法和三模型家族。
- 实验或效果：发现随机剪枝为强基线，性能受剪枝比主导，任务敏感性差异大。

## 摘要（原文）

> Large multimodal models (LMMs) often suffer from severe inference
> inefficiency due to the large number of visual tokens introduced by image
> encoders. While recent token compression methods, such as pruning and merging,
> have shown promise in reducing redundancy, their evaluation remains fragmented
> and inconsistent. In this work, we present UniPruneBench, a unified and
> extensible benchmark for visual token pruning in multimodal LLMs. UniPruneBench
> provides standardized protocols across six ability dimensions and ten datasets,
> covering ten representative compression algorithms and three families of LMMs
> (LLaVA-v1.5, Intern-VL3, and Qwen2.5-VL). Beyond task accuracy, it incorporates
> system-level metrics such as runtime and prefilling latency to provide a
> holistic view. Our experiments uncover several key findings: (1) random pruning
> is a surprisingly strong baseline, (2) no single method consistently
> outperforms others across scenarios, (3) pruning sensitivity varies
> significantly across tasks, with OCR being most vulnerable, and (4) pruning
> ratio is the dominant factor governing performance degradation. We believe
> UniPruneBench will serve as a reliable foundation for future research on
> efficient multimodal modeling.

