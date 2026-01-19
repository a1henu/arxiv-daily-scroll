---
layout: default
title: Wetland mapping from sparse annotations with satellite image time series and temporal-aware segment anything model
---

# Wetland mapping from sparse annotations with satellite image time series and temporal-aware segment anything model
**arXiv**：[2601.11400v1](https://arxiv.org/abs/2601.11400) · [PDF](https://arxiv.org/pdf/2601.11400.pdf)  
**作者**：Shuai Yuan, Tianwu Lin, Shuang Chen, Yu Xia, Peng Qin, Xiangyu Liu, Xiaoqing Xu, Nan Xu, Hongsheng Zhang, Jie Wang, Peng Gong  

**一句话要点**：提出WetSAM框架，利用卫星图像时间序列和时序感知SAM从稀疏点标注实现湿地映射

**关键词**：湿地映射, 卫星图像时间序列, 时序感知模型, 稀疏标注, 伪标签生成, 一致性正则

## 3 点简述
- 核心问题：稀疏点标注下湿地映射困难，单时相图像无法处理湿地动态变化，现有模型性能不佳。
- 方法要点：设计双分支框架，时序提示分支扩展SAM以建模时间信息，空间分支生成伪标签，通过一致性正则联合优化。
- 实验或效果：在八个全球区域验证，平均F1分数达85.58%，优于现有方法，实现高精度湿地分割。

## 摘要（原文）

> Accurate wetland mapping is essential for ecosystem monitoring, yet dense pixel-level annotation is prohibitively expensive and practical applications usually rely on sparse point labels, under which existing deep learning models perform poorly, while strong seasonal and inter-annual wetland dynamics further render single-date imagery inadequate and lead to significant mapping errors; although foundation models such as SAM show promising generalization from point prompts, they are inherently designed for static images and fail to model temporal information, resulting in fragmented masks in heterogeneous wetlands. To overcome these limitations, we propose WetSAM, a SAM-based framework that integrates satellite image time series for wetland mapping from sparse point supervision through a dual-branch design, where a temporally prompted branch extends SAM with hierarchical adapters and dynamic temporal aggregation to disentangle wetland characteristics from phenological variability, and a spatial branch employs a temporally constrained region-growing strategy to generate reliable dense pseudo-labels, while a bidirectional consistency regularization jointly optimizes both branches. Extensive experiments across eight global regions of approximately 5,000 km2 each demonstrate that WetSAM substantially outperforms state-of-the-art methods, achieving an average F1-score of 85.58%, and delivering accurate and structurally consistent wetland segmentation with minimal labeling effort, highlighting its strong generalization capability and potential for scalable, low-cost, high-resolution wetland mapping.

