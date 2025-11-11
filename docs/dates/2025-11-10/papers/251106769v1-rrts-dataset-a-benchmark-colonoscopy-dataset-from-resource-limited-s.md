---
layout: default
title: RRTS Dataset: A Benchmark Colonoscopy Dataset from Resource-Limited Settings for Computer-Aided Diagnosis Research
---

# RRTS Dataset: A Benchmark Colonoscopy Dataset from Resource-Limited Settings for Computer-Aided Diagnosis Research
**arXiv**：[2511.06769v1](https://arxiv.org/abs/2511.06769) · [PDF](https://arxiv.org/pdf/2511.06769.pdf)  
**作者**：Ridoy Chandra Shil, Ragib Abid, Tasnia Binte Mamun, Samiul Based Shuvo, Masfique Ahmed Bhuiyan, Jahid Ferdous  

**一句话要点**：提出BUET息肉数据集以解决资源受限环境下结肠镜图像诊断的复杂性挑战

**关键词**：结肠镜数据集, 息肉检测, 计算机辅助诊断, 图像分割, 真实世界伪影, 基准测试

## 3 点简述
- 核心问题：现有结肠镜数据集样本小、图像精选，缺乏真实世界伪影，难以支持临床实践。
- 方法要点：收集1,288张息肉图像和1,657张无息肉图像，包含运动模糊等多样伪影，专家标注掩码。
- 实验或效果：基准测试显示分类准确率最高90.8%，分割Dice分数最高0.64，反映真实世界难度。

## 摘要（原文）

> Background and Objective: Colorectal cancer prevention relies on early
> detection of polyps during colonoscopy. Existing public datasets, such as
> CVC-ClinicDB and Kvasir-SEG, provide valuable benchmarks but are limited by
> small sample sizes, curated image selection, or lack of real-world artifacts.
> There remains a need for datasets that capture the complexity of clinical
> practice, particularly in resource-constrained settings. Methods: We introduce
> a dataset, BUET Polyp Dataset (BPD), of colonoscopy images collected using
> Olympus 170 and Pen- tax i-Scan series endoscopes under routine clinical
> conditions. The dataset contains images with corresponding expert-annotated
> binary masks, reflecting diverse challenges such as motion blur, specular
> highlights, stool artifacts, blood, and low-light frames. Annotations were
> manually reviewed by clinical experts to ensure quality. To demonstrate
> baseline performance, we provide bench- mark results for classification using
> VGG16, ResNet50, and InceptionV3, and for segmentation using UNet variants with
> VGG16, ResNet34, and InceptionV4 backbones. Results: The dataset comprises
> 1,288 images with polyps from 164 patients with corresponding ground-truth
> masks and 1,657 polyp-free images from 31 patients. Benchmarking experiments
> achieved up to 90.8% accuracy for binary classification (VGG16) and a maximum
> Dice score of 0.64 with InceptionV4-UNet for segmentation. Performance was
> lower compared to curated datasets, reflecting the real-world difficulty of
> images with artifacts and variable quality.

