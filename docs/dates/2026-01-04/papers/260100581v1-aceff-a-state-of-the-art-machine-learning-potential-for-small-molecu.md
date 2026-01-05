---
layout: default
title: AceFF: A State-of-the-Art Machine Learning Potential for Small Molecules
---

# AceFF: A State-of-the-Art Machine Learning Potential for Small Molecules
**arXiv**：[2601.00581v1](https://arxiv.org/abs/2601.00581) · [PDF](https://arxiv.org/pdf/2601.00581.pdf)  
**作者**：Stephen E. Farr, Stefan Doerr, Antonio Mirarchi, Francesc Sabanes Zariquiey, Gianni De Fabritiis  

**一句话要点**：提出AceFF机器学习势函数，以解决小分子药物发现中跨化学空间泛化难题。

**关键词**：机器学习势函数, 小分子药物发现, TensorNet2架构, 有机分子模拟, 高通量推理, DFT级精度

## 3 点简述
- 核心问题：机器学习势函数在多样化化学空间泛化困难，影响小分子药物发现效率。
- 方法要点：基于TensorNet2架构，在类药化合物数据集上训练，支持关键元素和电荷状态。
- 实验或效果：验证显示AceFF在有机分子中达到DFT级精度，实现高通量推理与准确性平衡。

## 摘要（原文）

> We introduce AceFF, a pre-trained machine learning interatomic potential (MLIP) optimized for small molecule drug discovery. While MLIPs have emerged as efficient alternatives to Density Functional Theory (DFT), generalizability across diverse chemical spaces remains difficult. AceFF addresses this via a refined TensorNet2 architecture trained on a comprehensive dataset of drug-like compounds. This approach yields a force field that balances high-throughput inference speed with DFT-level accuracy. AceFF fully supports the essential medicinal chemistry elements (H, B, C, N, O, F, Si, P, S, Cl, Br, I) and is explicitly trained to handle charged states. Validation against rigorous benchmarks, including complex torsional energy scans, molecular dynamics trajectories, batched minimizations, and forces and anergy accuracy demonstrates that AceFF establishes a new state-of-the-art for organic molecules. The AceFF-2 model weights and inference code are available at https://huggingface.co/Acellera/AceFF-2.0.

