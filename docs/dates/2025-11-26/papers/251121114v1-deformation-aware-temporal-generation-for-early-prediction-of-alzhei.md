---
layout: default
title: Deformation-aware Temporal Generation for Early Prediction of Alzheimers Disease
---

# Deformation-aware Temporal Generation for Early Prediction of Alzheimers Disease
**arXiv**：[2511.21114v1](https://arxiv.org/abs/2511.21114) · [PDF](https://arxiv.org/pdf/2511.21114.pdf)  
**作者**：Xin Honga, Jie Lin, Minghui Wang  

**一句话要点**：提出变形感知时序生成网络以自动化学习脑图像形态变化，用于阿尔茨海默病早期预测

**关键词**：阿尔茨海默病预测, 时序图像生成, 变形感知网络, 脑图像分析, 数据插补, 分类准确率提升

## 3 点简述
- 核心问题：阿尔茨海默病早期预测依赖脑图像形态变化分析，但现有方法多需手动特征提取。
- 方法要点：DATGN先插补缺失MRI序列，再通过双向时序变形感知模块生成符合疾病进展的未来图像。
- 实验或效果：在ADNI数据集上，生成图像质量竞争性，集成合成数据显著提升分类准确率6.21%至21.25%。

## 摘要（原文）

> Alzheimer's disease (AD), a degenerative brain condition, can benefit from early prediction to slow its progression. As the disease progresses, patients typically undergo brain atrophy. Current prediction methods for Alzheimers disease largely involve analyzing morphological changes in brain images through manual feature extraction. This paper proposes a novel method, the Deformation-Aware Temporal Generative Network (DATGN), to automate the learning of morphological changes in brain images about disease progression for early prediction. Given the common occurrence of missing data in the temporal sequences of MRI images, DATGN initially interpolates incomplete sequences. Subsequently, a bidirectional temporal deformation-aware module guides the network in generating future MRI images that adhere to the disease's progression, facilitating early prediction of Alzheimer's disease. DATGN was tested for the generation of temporal sequences of future MRI images using the ADNI dataset, and the experimental results are competitive in terms of PSNR and MMSE image quality metrics. Furthermore, when DATGN-generated synthetic data was integrated into the SVM vs. CNN vs. 3DCNN-based classification methods, significant improvements were achieved from 6. 21\% to 16\% in AD vs. NC classification accuracy and from 7. 34\% to 21. 25\% in AD vs. MCI vs. NC classification accuracy. The qualitative visualization results indicate that DATGN produces MRI images consistent with the brain atrophy trend in Alzheimer's disease, enabling early disease prediction.

