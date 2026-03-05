---
layout: default
title: MOO: A Multi-view Oriented Observations Dataset for Viewpoint Analysis in Cattle Re-Identification
---

# MOO: A Multi-view Oriented Observations Dataset for Viewpoint Analysis in Cattle Re-Identification
**arXiv**：[2603.04314v1](https://arxiv.org/abs/2603.04314) · [PDF](https://arxiv.org/pdf/2603.04314.pdf)  
**作者**：William Grolleau, Achraf Chaouch, Astrid Sabourin, Guillaume Lapouge, Catherine Achard  

**一句话要点**：提出MOO数据集以解决动物重识别中视角变化问题，通过合成数据量化几何影响。

**关键词**：动物重识别, 视角分析, 合成数据集, 空对地重识别, 几何先验, 迁移学习

## 3 点简述
- 动物重识别面临视角变化挑战，尤其在空对地场景中缺乏精确角度标注。
- 引入大规模合成数据集MOO，包含1000头牛从128个视角的128,000张图像。
- 量化海拔影响，识别关键阈值，并在真实数据集上验证迁移性能提升。

## 摘要（原文）

> Animal re-identification (ReID) faces critical challenges due to viewpoint variations, particularly in Aerial-Ground (AG-ReID) settings where models must match individuals across drastic elevation changes. However, existing datasets lack the precise angular annotations required to systematically analyze these geometric variations. To address this, we introduce the Multi-view Oriented Observation (MOO) dataset, a large-scale synthetic AG-ReID dataset of $1,000$ cattle individuals captured from $128$ uniformly sampled viewpoints ($128,000$ annotated images). Using this controlled dataset, we quantify the influence of elevation and identify a critical elevation threshold, above which models generalize significantly better to unseen views. Finally, we validate the transferability to real-world applications in both zero-shot and supervised settings, demonstrating performance gains across four real-world cattle datasets and confirming that synthetic geometric priors effectively bridge the domain gap. Collectively, this dataset and analysis lay the foundation for future model development in cross-view animal ReID. MOO is publicly available at https://github.com/TurtleSmoke/MOO.

