---
layout: default
title: No Generation without Representation: Efficient Causal Protein Language Models Enable Zero-Shot Fitness Estimation
---

# No Generation without Representation: Efficient Causal Protein Language Models Enable Zero-Shot Fitness Estimation
**arXiv**：[2602.01845v1](https://arxiv.org/abs/2602.01845) · [PDF](https://arxiv.org/pdf/2602.01845.pdf)  
**作者**：Furkan Eris  

**一句话要点**：提出Proust因果蛋白质语言模型，通过架构创新实现零样本适应度估计与生成能力统一。

**关键词**：蛋白质语言模型, 因果模型, 零样本适应度估计, 架构创新, 计算效率

## 3 点简述
- 核心问题：蛋白质语言模型中掩码模型擅长适应度预测而因果模型支持生成，需分离架构。
- 方法要点：采用分组查询注意力、跨层值残差和深度因果卷积等创新，构建高效因果模型。
- 实验或效果：在ProteinGym和EVEREST基准上表现优异，计算效率高，并保留生成能力。

## 摘要（原文）

> Protein language models (PLMs) face a fundamental divide: masked language models (MLMs) excel at fitness prediction while causal models enable generation, forcing practitioners to maintain separate architectures. We introduce \textbf{Proust}, a 309M-parameter causal PLM that bridges this gap through architectural innovations adapted from recent LLM research, including grouped-query attention with shared K/V projections, cross-layer value residuals, and depthwise causal convolutions. Trained on 33B tokens in 40 B200 GPU-hours, Proust achieves Spearman $ρ= 0.390$ on ProteinGym substitutions, competitive with MLMs requiring 50--200$\times$ the compute. On indels, Proust sets a new state-of-the-art, outperforming models up to 20$\times$ larger. On EVEREST viral fitness benchmarks, it approaches structure-aware methods using sequence alone. These powerful representations position Proust in a sweet spot as it also retains native generative capabilities that MLMs lack by design. Interpretability analysis reveals that per-position entropy variance predicts, to an extent, when retrieval augmentation helps and hurts. Such insights can grow in both quantity and quality at scale and inform capabilities such as test-time scaling. Code and weights are available at https://github.com/Furkan9015/proust-inference

