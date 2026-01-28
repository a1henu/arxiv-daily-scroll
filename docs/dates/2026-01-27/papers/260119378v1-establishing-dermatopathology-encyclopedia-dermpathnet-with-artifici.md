---
layout: default
title: Establishing dermatopathology encyclopedia DermpathNet with Artificial Intelligence-Based Workflow
---

# Establishing dermatopathology encyclopedia DermpathNet with Artificial Intelligence-Based Workflow
**arXiv**：[2601.19378v1](https://arxiv.org/abs/2601.19378) · [PDF](https://arxiv.org/pdf/2601.19378.pdf)  
**作者**：Ziyang Xu, Mingquan Lin, Yiliang Zhou, Zihan Xu, Seth J. Orlow, Zihan Xu, Shane A. Meehan, Alexandra Flamm, Ata S. Moshiri, Yifan Peng  

**一句话要点**：提出基于人工智能工作流的皮肤病病理学百科全书DermpathNet，以解决高质量开放数据集获取难题。

**关键词**：皮肤病病理学, 图像数据集, 深度学习分类, 混合工作流, 开放访问, 医学教育

## 3 点简述
- 核心问题：临床医生和学员缺乏高质量、开放访问的皮肤病病理学图像数据集用于学习和交叉参考。
- 方法要点：采用混合工作流，结合深度学习图像模态分类和图文分析，从PubMed Central库中筛选和分类图像。
- 实验或效果：在651张手动标注图像上验证，混合方法F-score达90.4%，构建了包含7,772张图像、166种诊断的开放数据集。

## 摘要（原文）

> Accessing high-quality, open-access dermatopathology image datasets for learning and cross-referencing is a common challenge for clinicians and dermatopathology trainees. To establish a comprehensive open-access dermatopathology dataset for educational, cross-referencing, and machine-learning purposes, we employed a hybrid workflow to curate and categorize images from the PubMed Central (PMC) repository. We used specific keywords to extract relevant images, and classified them using a novel hybrid method that combined deep learning-based image modality classification with figure caption analyses. Validation on 651 manually annotated images demonstrated the robustness of our workflow, with an F-score of 89.6\% for the deep learning approach, 61.0\% for the keyword-based retrieval method, and 90.4\% for the hybrid approach. We retrieved over 7,772 images across 166 diagnoses and released this fully annotated dataset, reviewed by board-certified dermatopathologists. Using our dataset as a challenging task, we found the current image analysis algorithm from OpenAI inadequate for analyzing dermatopathology images. In conclusion, we have developed a large, peer-reviewed, open-access dermatopathology image dataset, DermpathNet, which features a semi-automated curation workflow.

