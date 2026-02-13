---
layout: default
title: Vascular anatomy-aware self-supervised pre-training for X-ray angiogram analysis
---

# Vascular anatomy-aware self-supervised pre-training for X-ray angiogram analysis
**arXiv**：[2602.11536v1](https://arxiv.org/abs/2602.11536) · [PDF](https://arxiv.org/pdf/2602.11536.pdf)  
**作者**：De-Xing Huang, Chaohui Yu, Xiao-Hu Zhou, Tian-Yu Xiang, Qin-Yi Zhang, Mei-Jiang Gui, Rui-Ze Ma, Chen-Yu Wang, Nu-Fang Xiao, Fan Wang, Zeng-Guang Hou  

**一句话要点**：提出血管解剖感知的自监督预训练框架VasoMIM，以解决X射线血管造影分析中标注数据稀缺问题。

**关键词**：自监督学习, X射线血管造影, 掩蔽图像建模, 解剖感知, 预训练数据集, 心血管疾病分析

## 3 点简述
- 核心问题：X射线血管造影分析因标注数据稀缺，限制了深度学习应用。
- 方法要点：VasoMIM集成解剖知识，包括血管引导掩蔽策略和解剖一致性损失。
- 实验或效果：在四个下游任务上验证，VasoMIM表现出优越迁移性和先进性能。

## 摘要（原文）

> X-ray angiography is the gold standard imaging modality for cardiovascular diseases. However, current deep learning approaches for X-ray angiogram analysis are severely constrained by the scarcity of annotated data. While large-scale self-supervised learning (SSL) has emerged as a promising solution, its potential in this domain remains largely unexplored, primarily due to the lack of effective SSL frameworks and large-scale datasets. To bridge this gap, we introduce a vascular anatomy-aware masked image modeling (VasoMIM) framework that explicitly integrates domain-specific anatomical knowledge. Specifically, VasoMIM comprises two key designs: an anatomy-guided masking strategy and an anatomical consistency loss. The former strategically masks vessel-containing patches to compel the model to learn robust vascular semantics, while the latter preserves structural consistency of vessels between original and reconstructed images, enhancing the discriminability of the learned representations. In conjunction with VasoMIM, we curate XA-170K, the largest X-ray angiogram pre-training dataset to date. We validate VasoMIM on four downstream tasks across six datasets, where it demonstrates superior transferability and achieves state-of-the-art performance compared to existing methods. These findings highlight the significant potential of VasoMIM as a foundation model for advancing a wide range of X-ray angiogram analysis tasks. VasoMIM and XA-170K will be available at https://github.com/Dxhuang-CASIA/XA-SSL.

