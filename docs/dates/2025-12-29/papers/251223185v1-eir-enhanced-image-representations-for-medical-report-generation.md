---
layout: default
title: EIR: Enhanced Image Representations for Medical Report Generation
---

# EIR: Enhanced Image Representations for Medical Report Generation
**arXiv**：[2512.23185v1](https://arxiv.org/abs/2512.23185) · [PDF](https://arxiv.org/pdf/2512.23185.pdf)  
**作者**：Qiang Sun, Zongcheng Ji, Yinlong Xiao, Peng Chang, Jun Yu  

**一句话要点**：提出EIR方法，通过跨模态融合和医学域预训练解决胸部X光报告生成中的信息不对称和领域差距问题。

**关键词**：医学报告生成, 胸部X光图像, 跨模态融合, 医学域预训练, 信息不对称, 领域差距

## 3 点简述
- 核心问题：现有方法在融合医学元数据和视觉表示时存在信息不对称，且图像表示存在领域差距。
- 方法要点：使用跨模态Transformer融合元数据与图像表示，并采用医学域预训练模型编码图像。
- 实验或效果：在MIMIC和Open-I数据集上验证了方法的有效性。

## 摘要（原文）

> Generating medical reports from chest X-ray images is a critical and time-consuming task for radiologists, especially in emergencies. To alleviate the stress on radiologists and reduce the risk of misdiagnosis, numerous research efforts have been dedicated to automatic medical report generation in recent years. Most recent studies have developed methods that represent images by utilizing various medical metadata, such as the clinical document history of the current patient and the medical graphs constructed from retrieved reports of other similar patients. However, all existing methods integrate additional metadata representations with visual representations through a simple "Add and LayerNorm" operation, which suffers from the information asymmetry problem due to the distinct distributions between them. In addition, chest X-ray images are usually represented using pre-trained models based on natural domain images, which exhibit an obvious domain gap between general and medical domain images. To this end, we propose a novel approach called Enhanced Image Representations (EIR) for generating accurate chest X-ray reports. We utilize cross-modal transformers to fuse metadata representations with image representations, thereby effectively addressing the information asymmetry problem between them, and we leverage medical domain pre-trained models to encode medical images, effectively bridging the domain gap for image representation. Experimental results on the widely used MIMIC and Open-I datasets demonstrate the effectiveness of our proposed method.

