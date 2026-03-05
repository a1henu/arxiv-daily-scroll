---
layout: default
title: ProFound: A moderate-sized vision foundation model for multi-task prostate imaging
---

# ProFound: A moderate-sized vision foundation model for multi-task prostate imaging
**arXiv**：[2603.03961v1](https://arxiv.org/abs/2603.03961) · [PDF](https://arxiv.org/pdf/2603.03961.pdf)  
**作者**：Yipei Wang, Yinsong Xu, Weixi Yi, Shaheer Ullah Saeed, Natasha Thorley, Alexander Ng, Yukun Zhou, Wen Yan, Dean Barratt, Shonit Punwani, Veeru Kasivisvanathan, Mark Emberton, Daniel C. Alexander, Yipeng Hu  

**一句话要点**：提出ProFound视觉基础模型，用于多任务前列腺MRI分析，以解决临床任务自动化中标注数据稀缺问题。

**关键词**：前列腺MRI, 视觉基础模型, 自监督学习, 多任务学习, 医学图像分析, 三维图像处理

## 3 点简述
- 核心问题：前列腺癌多参数MRI临床任务自动化依赖专家标注，难以扩展深度学习应用。
- 方法要点：基于自监督预训练，在5000患者数据集上构建领域专用三维MRI视觉基础模型。
- 实验或效果：在11项下游任务中，微调后模型优于或媲美现有专业模型和医学视觉基础模型。

## 摘要（原文）

> Many diagnostic and therapeutic clinical tasks for prostate cancer increasingly rely on multi-parametric MRI. Automating these tasks is challenging because they necessitate expert interpretations, which are difficult to scale to capitalise on modern deep learning. Although modern automated systems achieve expert-level performance in isolated tasks, their general clinical utility remains limited by the requirement of large task-specific labelled datasets. In this paper, we present ProFound, a domain-specialised vision foundation model for volumetric prostate mpMRI. ProFound is pre-trained using several variants of self-supervised approaches on a diverse, multi-institutional collection of 5,000 patients, with a total of over 22,000 unique 3D MRI volumes (over 1,800,000 2D image slices). We conducted a systematic evaluation of ProFound across a broad spectrum of $11$ downstream clinical tasks on over 3,000 independent patients, including prostate cancer detection, Gleason grading, lesion localisation, gland volume estimation, zonal and surrounding structure segmentation. Experimental results demonstrate that finetuned ProFound consistently outperforms or remains competitive with state-of-the-art specialised models and existing medical vision foundation models trained/finetuned on the same data.

