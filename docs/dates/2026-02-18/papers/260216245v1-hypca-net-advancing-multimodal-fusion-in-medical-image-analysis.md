---
layout: default
title: HyPCA-Net: Advancing Multimodal Fusion in Medical Image Analysis
---

# HyPCA-Net: Advancing Multimodal Fusion in Medical Image Analysis
**arXiv**：[2602.16245v1](https://arxiv.org/abs/2602.16245) · [PDF](https://arxiv.org/pdf/2602.16245.pdf)  
**作者**：J. Dhar, M. K. Pandey, D. Chakladar, M. Haghighat, A. Alavi, S. Mistry, N. Zaidi  

**一句话要点**：提出HyPCA-Net以解决医学图像多模态融合中的计算成本高和信息损失问题。

**关键词**：多模态融合, 医学图像分析, 注意力机制, 计算效率, 泛化能力

## 3 点简述
- 现有方法计算成本高且易在级联注意力模块中丢失信息，限制泛化能力。
- HyPCA-Net包含残差自适应学习注意力块和双视角级联注意力块，提升效率和鲁棒性。
- 在十个公开数据集上，性能提升达5.2%，计算成本降低达73.1%。

## 摘要（原文）

> Multimodal fusion frameworks, which integrate diverse medical imaging modalities (e.g., MRI, CT), have shown great potential in applications such as skin cancer detection, dementia diagnosis, and brain tumor prediction. However, existing multimodal fusion methods face significant challenges. First, they often rely on computationally expensive models, limiting their applicability in low-resource environments. Second, they often employ cascaded attention modules, which potentially increase risk of information loss during inter-module transitions and hinder their capacity to effectively capture robust shared representations across modalities. This restricts their generalization in multi-disease analysis tasks. To address these limitations, we propose a Hybrid Parallel-Fusion Cascaded Attention Network (HyPCA-Net), composed of two core novel blocks: (a) a computationally efficient residual adaptive learning attention block for capturing refined modality-specific representations, and (b) a dual-view cascaded attention block aimed at learning robust shared representations across diverse modalities. Extensive experiments on ten publicly available datasets exhibit that HyPCA-Net significantly outperforms existing leading methods, with improvements of up to 5.2% in performance and reductions of up to 73.1% in computational cost. Code: https://github.com/misti1203/HyPCA-Net.

