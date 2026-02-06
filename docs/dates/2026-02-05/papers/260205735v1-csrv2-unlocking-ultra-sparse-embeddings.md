---
layout: default
title: CSRv2: Unlocking Ultra-Sparse Embeddings
---

# CSRv2: Unlocking Ultra-Sparse Embeddings
**arXiv**：[2602.05735v1](https://arxiv.org/abs/2602.05735) · [PDF](https://arxiv.org/pdf/2602.05735.pdf)  
**作者**：Lixuan Guo, Yifei Wang, Tiansheng Wen, Yifan Wang, Aosong Feng, Bo Chen, Stefanie Jegelka, Chenyu You  

**一句话要点**：提出CSRv2训练方法，通过渐进稀疏化和监督对比学习，实现超稀疏嵌入的高效与高性能，适用于实时和边缘AI系统。

**关键词**：超稀疏嵌入, 对比稀疏表示, 渐进稀疏化, 监督对比学习, 边缘AI部署, 嵌入效率优化

## 3 点简述
- 核心问题：CSR在超稀疏（如k=2）时性能严重下降，死神经元达80%，效率潜力未发挥。
- 方法要点：采用渐进k-退火稳定稀疏学习，结合监督对比目标提升表示质量，支持全骨干微调确保端到端适应性。
- 实验或效果：将死神经元降至20%，在k=2时准确率提升14%，性能媲美CSR（k=8）和MRL（32维），计算和内存效率相比密集嵌入提升高达300倍。

## 摘要（原文）

> In the era of large foundation models, the quality of embeddings has become a central determinant of downstream task performance and overall system capability. Yet widely used dense embeddings are often extremely high-dimensional, incurring substantial costs in storage, memory, and inference latency. To address these, Contrastive Sparse Representation (CSR) is recently proposed as a promising direction, mapping dense embeddings into high-dimensional but k-sparse vectors, in contrast to compact dense embeddings such as Matryoshka Representation Learning (MRL). Despite its promise, CSR suffers severe degradation in the ultra-sparse regime, where over 80% of neurons remain inactive, leaving much of its efficiency potential unrealized. In this paper, we introduce CSRv2, a principled training approach designed to make ultra-sparse embeddings viable. CSRv2 stabilizes sparsity learning through progressive k-annealing, enhances representational quality via supervised contrastive objectives, and ensures end-to-end adaptability with full backbone finetuning. CSRv2 reduces dead neurons from 80% to 20% and delivers a 14% accuracy gain at k=2, bringing ultra-sparse embeddings on par with CSR at k=8 and MRL at 32 dimensions, all with only two active features. While maintaining comparable performance, CSRv2 delivers a 7x speedup over MRL, and yields up to 300x improvements in compute and memory efficiency relative to dense embeddings in text representation. Extensive experiments across text and vision demonstrate that CSRv2 makes ultra-sparse embeddings practical without compromising performance, where CSRv2 achieves 7%/4% improvement over CSR when k=4 and further increases this gap to 14%/6% when k=2 in text/vision representation. By making extreme sparsity viable, CSRv2 broadens the design space for real-time and edge-deployable AI systems where both embedding quality and efficiency are critical.

