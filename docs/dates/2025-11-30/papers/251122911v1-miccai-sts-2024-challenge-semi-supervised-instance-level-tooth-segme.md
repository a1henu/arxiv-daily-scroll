---
layout: default
title: MICCAI STS 2024 Challenge: Semi-Supervised Instance-Level Tooth Segmentation in Panoramic X-ray and CBCT Images
---

# MICCAI STS 2024 Challenge: Semi-Supervised Instance-Level Tooth Segmentation in Panoramic X-ray and CBCT Images
**arXiv**：[2511.22911v1](https://arxiv.org/abs/2511.22911) · [PDF](https://arxiv.org/pdf/2511.22911.pdf)  
**作者**：Yaqi Wang, Zhi Li, Chengyu Wu, Jun Liu, Yifan Zhang, Jiaxue Ni, Qian Luo, Jialuo Chen, Hongyuan Zhang, Jin Liu, Can Han, Kaiwen Fu, Changkai Ji, Xinxu Cai, Jing Hao, Zhihao Zheng, Shi Xu, Junqiang Chen, Qianni Zhang, Dahong Qian, Shuai Wang, Huiyu Zhou  

**一句话要点**：组织MICCAI STS 2024挑战赛，推动半监督学习在牙科影像实例分割中的应用以解决标注数据稀缺问题。

**关键词**：半监督学习, 牙科影像分割, 实例分割, 全景X光, CBCT, MICCAI挑战赛

## 3 点简述
- 核心问题：牙科全景X光和CBCT影像的实例级分割标注成本高，导致训练数据稀缺。
- 方法要点：基于大规模数据集，采用半监督学习框架，结合基础模型和多阶段细化流程。
- 实验或效果：半监督方法显著优于全监督基线，在2D和3D任务中分别提升44和61个百分点。

## 摘要（原文）

> Orthopantomogram (OPGs) and Cone-Beam Computed Tomography (CBCT) are vital for dentistry, but creating large datasets for automated tooth segmentation is hindered by the labor-intensive process of manual instance-level annotation. This research aimed to benchmark and advance semi-supervised learning (SSL) as a solution for this data scarcity problem. We organized the 2nd Semi-supervised Teeth Segmentation (STS 2024) Challenge at MICCAI 2024. We provided a large-scale dataset comprising over 90,000 2D images and 3D axial slices, which includes 2,380 OPG images and 330 CBCT scans, all featuring detailed instance-level FDI annotations on part of the data. The challenge attracted 114 (OPG) and 106 (CBCT) registered teams. To ensure algorithmic excellence and full transparency, we rigorously evaluated the valid, open-source submissions from the top 10 (OPG) and top 5 (CBCT) teams, respectively. All successful submissions were deep learning-based SSL methods. The winning semi-supervised models demonstrated impressive performance gains over a fully-supervised nnU-Net baseline trained only on the labeled data. For the 2D OPG track, the top method improved the Instance Affinity (IA) score by over 44 percentage points. For the 3D CBCT track, the winning approach boosted the Instance Dice score by 61 percentage points. This challenge confirms the substantial benefit of SSL for complex, instance-level medical image segmentation tasks where labeled data is scarce. The most effective approaches consistently leveraged hybrid semi-supervised frameworks that combined knowledge from foundational models like SAM with multi-stage, coarse-to-fine refinement pipelines. Both the challenge dataset and the participants' submitted code have been made publicly available on GitHub (https://github.com/ricoleehduu/STS-Challenge-2024), ensuring transparency and reproducibility.

