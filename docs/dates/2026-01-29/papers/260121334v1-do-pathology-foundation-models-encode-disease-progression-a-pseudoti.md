---
layout: default
title: Do Pathology Foundation Models Encode Disease Progression? A Pseudotime Analysis of Visual Representations
---

# Do Pathology Foundation Models Encode Disease Progression? A Pseudotime Analysis of Visual Representations
**arXiv**：[2601.21334v1](https://arxiv.org/abs/2601.21334) · [PDF](https://arxiv.org/pdf/2601.21334.pdf)  
**作者**：Pritika Vig, Ren-Chin Wu, William Lotter  

**一句话要点**：提出基于扩散伪时间分析视觉表示的方法，以评估病理基础模型是否编码疾病进展

**关键词**：病理基础模型, 疾病进展表示, 扩散伪时间分析, 视觉表示学习, 轨迹保真度

## 3 点简述
- 核心问题：视觉基础模型是否从离散图像中学习到连续疾病进展的表示
- 方法要点：利用扩散伪时间方法分析模型表示空间中的疾病轨迹排序
- 实验或效果：在四种癌症进展和六个模型上验证轨迹保真度，并与少样本分类性能相关

## 摘要（原文）

> Vision foundation models trained on discretely sampled images achieve strong performance on classification benchmarks, yet whether their representations encode the continuous processes underlying their training data remains unclear. This question is especially pertinent in computational pathology, where we posit that models whose latent representations implicitly capture continuous disease progression may better reflect underlying biology, support more robust generalization, and enable quantitative analyses of features associated with disease transitions. Using diffusion pseudotime, a method developed to infer developmental trajectories from single-cell transcriptomics, we probe whether foundation models organize disease states along coherent progression directions in representation space. Across four cancer progressions and six models, we find that all pathology-specific models recover trajectory orderings significantly exceeding null baselines, with vision-only models achieving the highest fidelities $(τ> 0.78$ on CRC-Serrated). Model rankings by trajectory fidelity on reference diseases strongly predict few-shot classification performance on held-out diseases ($ρ= 0.92$), and exploratory analysis shows cell-type composition varies smoothly along inferred trajectories in patterns consistent with known stromal remodeling. Together, these results demonstrate that vision foundation models can implicitly learn to represent continuous processes from independent static observations, and that trajectory fidelity provides a complementary measure of representation quality beyond downstream performance. While demonstrated in pathology, this framework could be applied to other domains where continuous processes are observed through static snapshots.

