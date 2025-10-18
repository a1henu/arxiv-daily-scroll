---
layout: default
title: Scaling Tumor Segmentation: Best Lessons from Real and Synthetic Data
---

# Scaling Tumor Segmentation: Best Lessons from Real and Synthetic Data
**arXiv**：[2510.14831v1](https://arxiv.org/abs/2510.14831) · [PDF](https://arxiv.org/pdf/2510.14831.pdf)  
**作者**：Qi Chen, Xinze Zhou, Chen Liu, Hao Chen, Wenxuan Li, Zekun Jiang, Ziyan Huang, Yuxuan Zhao, Dexin Yu, Junjun He, Yefeng Zheng, Ling Shao, Alan Yuille, Zongwei Zhou  

**一句话要点**：提出AbdomenAtlas 2.0数据集，结合合成数据提升肿瘤分割效率与泛化能力

**关键词**：肿瘤分割, 合成数据, 医学影像, CT扫描, 数据增强, 泛化性能

## 3 点简述
- 核心问题：肿瘤分割AI受限于大规模体素标注数据稀缺，标注成本高且依赖专家
- 方法要点：利用合成数据增强真实数据，在JHH数据集上验证合成数据可减少真实数据需求
- 实验或效果：AbdomenAtlas 2.0在分布内测试DSC提升7%，分布外测试提升16%

## 摘要（原文）

> AI for tumor segmentation is limited by the lack of large, voxel-wise
> annotated datasets, which are hard to create and require medical experts. In
> our proprietary JHH dataset of 3,000 annotated pancreatic tumor scans, we found
> that AI performance stopped improving after 1,500 scans. With synthetic data,
> we reached the same performance using only 500 real scans. This finding
> suggests that synthetic data can steepen data scaling laws, enabling more
> efficient model training than real data alone. Motivated by these lessons, we
> created AbdomenAtlas 2.0--a dataset of 10,135 CT scans with a total of 15,130
> tumor instances per-voxel manually annotated in six organs (pancreas, liver,
> kidney, colon, esophagus, and uterus) and 5,893 control scans. Annotated by 23
> expert radiologists, it is several orders of magnitude larger than existing
> public tumor datasets. While we continue expanding the dataset, the current
> version of AbdomenAtlas 2.0 already provides a strong foundation--based on
> lessons from the JHH dataset--for training AI to segment tumors in six organs.
> It achieves notable improvements over public datasets, with a +7% DSC gain on
> in-distribution tests and +16% on out-of-distribution tests.

