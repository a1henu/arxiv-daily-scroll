---
layout: default
title: TrueCity: Real and Simulated Urban Data for Cross-Domain 3D Scene Understanding
---

# TrueCity: Real and Simulated Urban Data for Cross-Domain 3D Scene Understanding
**arXiv**：[2511.07007v1](https://arxiv.org/abs/2511.07007) · [PDF](https://arxiv.org/pdf/2511.07007.pdf)  
**作者**：Duc Nguyen, Yan-Ling Lai, Qilin Zhang, Prabin Gyawali, Benedikt Schwab, Olaf Wysocki, Thomas H. Kolbe  

**一句话要点**：提出TrueCity数据集以解决3D语义分割中合成到真实域差距问题

**关键词**：3D语义分割, 合成到真实域差距, 点云数据, 城市场景理解, 跨域基准

## 3 点简述
- 核心问题：3D语义场景理解缺乏真实标注数据，合成数据存在域差距。
- 方法要点：提供同步真实与模拟点云，支持跨域分割分析。
- 实验或效果：量化域差距，展示合成数据提升真实世界理解策略。

## 摘要（原文）

> 3D semantic scene understanding remains a long-standing challenge in the 3D
> computer vision community. One of the key issues pertains to limited real-world
> annotated data to facilitate generalizable models. The common practice to
> tackle this issue is to simulate new data. Although synthetic datasets offer
> scalability and perfect labels, their designer-crafted scenes fail to capture
> real-world complexity and sensor noise, resulting in a synthetic-to-real domain
> gap. Moreover, no benchmark provides synchronized real and simulated point
> clouds for segmentation-oriented domain shift analysis. We introduce TrueCity,
> the first urban semantic segmentation benchmark with cm-accurate annotated
> real-world point clouds, semantic 3D city models, and annotated simulated point
> clouds representing the same city. TrueCity proposes segmentation classes
> aligned with international 3D city modeling standards, enabling consistent
> evaluation of synthetic-to-real gap. Our extensive experiments on common
> baselines quantify domain shift and highlight strategies for exploiting
> synthetic data to enhance real-world 3D scene understanding. We are convinced
> that the TrueCity dataset will foster further development of sim-to-real gap
> quantification and enable generalizable data-driven models. The data, code, and
> 3D models are available online: https://tum-gis.github.io/TrueCity/

