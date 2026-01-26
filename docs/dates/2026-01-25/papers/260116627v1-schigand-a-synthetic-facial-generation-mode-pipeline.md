---
layout: default
title: SCHIGAND: A Synthetic Facial Generation Mode Pipeline
---

# SCHIGAND: A Synthetic Facial Generation Mode Pipeline
**arXiv**：[2601.16627v1](https://arxiv.org/abs/2601.16627) · [PDF](https://arxiv.org/pdf/2601.16627.pdf)  
**作者**：Ananya Kadali, Sunnie Jehan-Morrison, Orasiki Wellington, Barney Evans, Precious Durojaiye, Richard Guest  

**一句话要点**：提出SCHIGAND合成人脸生成管道，以解决隐私合规下高质量多样化人脸数据集需求问题

**关键词**：合成人脸生成, 身份保持, 生物识别测试, 隐私合规数据集, 生成模型集成, 人脸验证评估

## 3 点简述
- 核心问题：隐私法规、数据稀缺和伦理问题限制真实人脸数据集获取，现有生成模型难以平衡真实性、多样性和身份保持
- 方法要点：集成StyleCLIP、HyperStyle、InterfaceGAN和Diffusion模型，增强身份保持并生成可控的类内变化和类间区分
- 实验或效果：使用ArcFace评估，SCHIGAND在图像质量和多样性间取得平衡，适用于生物识别测试，可补充或替代真实数据

## 摘要（原文）

> The growing demand for diverse and high-quality facial datasets for training and testing biometric systems is challenged by privacy regulations, data scarcity, and ethical concerns. Synthetic facial images offer a potential solution, yet existing generative models often struggle to balance realism, diversity, and identity preservation. This paper presents SCHIGAND, a novel synthetic face generation pipeline integrating StyleCLIP, HyperStyle, InterfaceGAN, and Diffusion models to produce highly realistic and controllable facial datasets. SCHIGAND enhances identity preservation while generating realistic intra-class variations and maintaining inter-class distinctiveness, making it suitable for biometric testing. The generated datasets were evaluated using ArcFace, a leading facial verification model, to assess their effectiveness in comparison to real-world facial datasets. Experimental results demonstrate that SCHIGAND achieves a balance between image quality and diversity, addressing key limitations of prior generative models. This research highlights the potential of SCHIGAND to supplement and, in some cases, replace real data for facial biometric applications, paving the way for privacy-compliant and scalable solutions in synthetic dataset generation.

